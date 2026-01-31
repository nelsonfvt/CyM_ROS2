import rclpy
from rclpy.node import Node

from my_interfaces.msg import Mypoint3d

class receive_node(Node):
    def __init__(self):
        super().__init__('Nodo_receptor')
        self.nodo_suscriptor = self.create_subscription(Mypoint3d, 'topic_tmp', self.reci_llamado, 10)
        self.nodo_suscriptor

    def reci_llamado(self, r_point):
        print('Llegó un mensaje:')
        self.get_logger().info('Coord x: "%f"' % r_point.x)
        self.get_logger().info('Coord y: "%f"' % r_point.y)
        self.get_logger().info('Coord z: "%f"' % r_point.z)

def main(args=None):

    try:
        rclpy.init(args=args)
        receptor = receive_node()
        rclpy.spin(receptor)


    except KeyboardInterrupt:
        print(' ...Exit Node')
        receptor.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()