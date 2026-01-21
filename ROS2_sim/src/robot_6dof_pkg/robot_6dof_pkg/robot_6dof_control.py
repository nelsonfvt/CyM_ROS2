from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rclpy.qos import QoSProfile

class JointAnglePublisher(Node):
    def __init__(self):
        super().__init__('robot6dof_control')
        qos_profile = QoSProfile(depth=10)
        # publicador para topic /arm_controller...
        self.joint_publisher = self.create_publisher(JointTrajectory,
                                '/arm_controller/joint_trajectory',
                                qos_profile)
        
        # Creando Mensaje
        self.trajectory_command = JointTrajectory()
        self.trajectory_command.joint_names = ['Base__to__link_1',
                                               'link_1__to__link_2',
                                               'link_2__to__link_3',
                                               'link_3__to__link_4',
                                               'link_4__to__link_5',
                                               'link_5__to__link_6']

        self.s_rot = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        # Punto inicial
        self.point = JointTrajectoryPoint()
        self.point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.point.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.point.time_from_start.sec = 1

        self.trajectory_command.points = [self.point]

        self.joint_publisher.publish(self.trajectory_command)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"Publishing...")

        pos_list = list(self.point.positions)
        
        if pos_list[0] > 3.14:
            self.s_rot[0] = -1.0
        if pos_list[0] < -3.14:
            self.s_rot[0] = 1.0

        if pos_list[1] > 0.0:
            self.s_rot[1] = -1.0
        if pos_list[1] < -1.57:
            self.s_rot[1] = 1.0

        if pos_list[2] > 0.0:
            self.s_rot[2] = -1.0
        if pos_list[2] < -1.57:
            self.s_rot[2] = 1.0

        if pos_list[3] > 3.14:
            self.s_rot[3] = -1.0
        if pos_list[3] < -3.14:
            self.s_rot[3] = 1.0

        if pos_list[4] > 1.57:
            self.s_rot[4] = -1.0
        if pos_list[4] < 0.0:
            self.s_rot[4] = 1.0

        if pos_list[5] > 3.14:
            self.s_rot[5] = -1.0
        if pos_list[5] < -3.14:
            self.s_rot[5] = 1.0
        

        vels = [0.1, 0.08, 0.07, 0.12, 0.1, 0.13]
        t_rot = self.s_rot.copy()

        deltas = [vels * t_rot for vels, t_rot in zip(vels, t_rot)]

        pos_list1 = [pos_list + deltas for pos_list, deltas in zip(pos_list, deltas)]

        self.point.positions = pos_list1
        self.trajectory_command.points = [self.point]
        self.joint_publisher.publish(self.trajectory_command)


def main():
    
    try:
        rclpy.init()
        robot_control = JointAnglePublisher()
        rclpy.spin(robot_control)

    except KeyboardInterrupt:
        print(' ...Exit Node')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
