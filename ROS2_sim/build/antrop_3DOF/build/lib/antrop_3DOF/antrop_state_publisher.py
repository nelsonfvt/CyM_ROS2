from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

class AntropStatePublisher(Node):

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
        self.base_trans.header.frame_id = 'world'
        self.base_trans.child_frame_id = 'base_link'
        self.joint_state = JointState()



def main(args=None):
	rclpy.init(args=args)
	
	state_publisher = AntropStatePublisher()
	rclpy.spin(state_publisher)
	
	state_publisher.destroy_node()
	rclpy.shutdown()		
		
if __name__ == '__main__':
    main()