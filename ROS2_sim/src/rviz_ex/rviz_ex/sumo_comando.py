import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist

class Sumo_Commander(Node):
    def __init__(self):
        super().__init__('command_publisher')
        qos_profile = QoSProfile(depth=10)

        self.cmd_vel = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.get_logger().info('Nodo cmd_vel_publisher iniciado')

    def publish_velocity(self, linear_vel, angular_vel):
        msg = Twist()
        msg.linear.x = linear_vel
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = angular_vel

        self.cmd_vel.publish(msg)
        self.get_logger().info(f'Publicado -> linear: {linear_vel}, angular: {angular_vel}')


def main(args=None):
    rclpy.init(args=args)
    my_robot_commander = Sumo_Commander()
    
    
    try:
        while rclpy.ok():
            try:
                linear = float(input("Ingrese velocidad lineal (m/s): "))
                angular = float(input("Ingrese velocidad angular (rad/s): "))
                my_robot_commander.publish_velocity(linear, angular)
            except ValueError:
                print("Entrada inválida. Por favor ingrese números.")
        
    except KeyboardInterrupt: 
        print(' ... exit node')
    except Exception as e:
        print(e)

    my_robot_commander.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()