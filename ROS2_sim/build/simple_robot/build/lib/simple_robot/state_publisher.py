from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

class StatePublisher(Node):
	
	def __init__(self):

		super().__init__('State_publisher')
		qos_profile = QoSProfile(depth=10)
		self.joint_pub = self.create_publisher(JointState, 'joint_states',qos_profile)
		self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
		self.nodeName = self.get_name()

		self.get_logger().info("{0} started".format(self.nodeName))

		#Estado inicial del robot
		self.J1 = 0.0
		self.J2 = 0.0
		self.J3 = 0.0

		self.base_trans = TransformStamped()
		self.base_trans.header.frame_id = 'base_link'
		self.base_trans.child_frame_id = 'link1_2'
		self.joint_state = JointState()

		self.Ts = 0.1
		self.timer = self.create_timer(self.Ts, self.timer_callback)
		

	def timer_callback(self):
        
		self.get_logger().info('Publishing: ')
		now = self.get_clock().now()
		
		self.joint_state.name = ['J1', 'J2', 'J3']
		self.joint_state.position = [self.J1, self.J2, self.J3]

		self.base_trans.header.stamp = now.to_msg()
		self.base_trans.transform.translation.x = 0.0
		self.base_trans.transform.translation.y = 0.0
		self.base_trans.transform.translation.x = 0.0
		print('aqui voy 1')
		# Quaternion methods
		quat_tf = [0.0, 0.0, 0.0, 1.0]
		quat = Quaternion(x=quat_tf[0], y=quat_tf[1], z=quat_tf[2], w=quat_tf[3])
		
		self.base_trans.transform.rotation = quat#Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
		
		self.joint_pub.publish(self.joint_state)
		print('aqui voy 2')
		self.broadcaster.sendTransform(self.base_trans)
		print('aqui voy 3')
		

		# self.J1 = self.J1 + 0.1 * self.Ts
		# self.J2 = self.J2 + 0.25 * self.Ts
		# self.J3 = self.J3 + 0.3 * self.Ts

		#self.i += 1

def main(args=None):
	rclpy.init(args=args)
	
	state_publisher = StatePublisher()
	rclpy.spin(state_publisher)
	
	state_publisher.destroy_node()
	rclpy.shutdown()		
		
if __name__ == '__main__':
    main()