from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

class ScaraControl(Node):

    def __init__(self):
        super().__init__('Scara_Control')
        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, 'joint_states',qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
        self.nodeName = self.get_name()



def main(args=None):

    try:
	    rclpy.init(args=args)
	
	    scara_control = ScaraControl()
	    rclpy.spin(scara_control)
	
    except KeyboardInterrupt:
        print(' ...Exit Node')
        scara_control.destroy_node()
        rclpy.shutdown()

    except Exception as e:
        print(e)

	#scara_control.destroy_node()
	#rclpy.shutdown()		
		
if __name__ == '__main__':
    main()