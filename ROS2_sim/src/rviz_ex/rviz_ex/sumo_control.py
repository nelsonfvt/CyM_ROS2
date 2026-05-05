from math import sin, cos
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped
from rviz_ex.my_libs import euler_to_quaternion, mod_cinemat_inv

class Sumo_Controller(Node):
    def __init__(self):
        super().__init__('state_publisher')
        qos_profile = QoSProfile(depth=10)

        #self.get_logger().info("{0} iniciado".format(self.nodeName))
        # inicializa variables ruedas
        self.ejes_pos = {'izq':0.0, 'der':0.0}
        self.ejes_vel = {'izq':0.0, 'der':0.0}
        
        # variables chasis
        self.pos_ch = {'x': 0.0, 'y': 0.0, 'a':0.0}
        self.vel_ch = {'v': 0.0, 'w':0.0}
        self.dt = 0.1

        # initializa publicadores y suscriptores
        self.cmd_vel = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, qos_profile)
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)

        # inicia estados de ruedas
        now = self.get_clock().now() #nanoseconds
        self.joint_state = JointState()
        self.joint_state.header.stamp = now.to_msg()
        self.joint_state.name = ['eje_i', 'eje_d']
        self.joint_state.position = [self.ejes_pos['izq'], self.ejes_pos['der']]

        # inicia posición robot
        self.base_trans = TransformStamped()
        self.base_trans.header.stamp = now.to_msg()
        self.base_trans.header.frame_id = 'map'
        self.base_trans.child_frame_id = 'chasis'
        self.base_trans.transform.translation.x = 0.0
        self.base_trans.transform.translation.y = 0.0
        self.base_trans.transform.translation.z = 0.0
        self.base_trans.transform.rotation = euler_to_quaternion(0, 0, 0)

        # publicando valores iniciales
        self.joint_pub.publish(self.joint_state)
        self.broadcaster.sendTransform(self.base_trans)

        # timer para mover robot
        self.timer = self.create_timer(self.dt, self.timer_callback)

    def cmd_vel_callback(self, msg):
        # lee el mensaje
        lin = msg.linear.x # Vel lineal chasis
        ang = msg.angular.z # Vel angular chasis

        self.vel_ch['v'] = lin
        self.vel_ch['w'] = ang

        ws = mod_cinemat_inv(lin, ang)

        self.ejes_vel['izq'] = -ws[0]
        self.ejes_vel['der'] = ws[1]
    
    def timer_callback(self):

        now = self.get_clock().now()

        # calcula nueva pos ruedas
        self.ejes_pos['izq'] += self.ejes_vel['izq'] *self.dt
        self.ejes_pos['der'] += self.ejes_vel['der'] *self.dt

        # calcula nueva pos chasis
        d_th = self.vel_ch['w'] * self.dt
        d_x = ( self.vel_ch['v']*cos(d_th) ) * self.dt
        d_y = ( self.vel_ch['v']*sin(d_th) ) * self.dt

        self.pos_ch['x'] += d_x*cos(self.pos_ch['a']) - d_y*sin(self.pos_ch['a'])
        self.pos_ch['y'] += d_x*sin(self.pos_ch['a']) + d_y*cos(self.pos_ch['a'])
        self.pos_ch['a'] += d_th

        # prepara el mensaje de posición de ruedas
        self.joint_state.header.stamp = now.to_msg()
        self.joint_state.position = [self.ejes_pos['izq'], self.ejes_pos['der']]

        # prepara mensaje de posicion del chasis
        self.base_trans.header.stamp = now.to_msg()
        self.base_trans.transform.translation.x = self.pos_ch['x']
        self.base_trans.transform.translation.y = self.pos_ch['y']
        self.base_trans.transform.rotation = euler_to_quaternion(0, 0, self.pos_ch['a'])

        # publicando valores iniciales
        self.joint_pub.publish(self.joint_state)
        self.broadcaster.sendTransform(self.base_trans)



def main(args=None):
    
    try:
        rclpy.init(args=args)
        my_robot_controller = Sumo_Controller()
        rclpy.spin(my_robot_controller)
    except KeyboardInterrupt: 
        print(' ... exit node')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()