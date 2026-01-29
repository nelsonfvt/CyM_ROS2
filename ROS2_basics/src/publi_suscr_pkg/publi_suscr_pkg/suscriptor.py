import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class my_suscriptor(Node):
    def __init__(self):
        super().__init__('Nodo_suscriptor')
        self.nodo_suscriptor = self.create_subscription(String, 'topic_tmp', self.suscrip_llamado, 10)
        self.nodo_suscriptor

    def suscrip_llamado(self, msg):
        self.get_logger().info('Llegó: "%s"' % msg.data)



def main(args=None):

    try:
        rclpy.init(args=args)
        mini_suscriber = my_suscriptor()
        rclpy.spin(mini_suscriber)


    except KeyboardInterrupt:
        print(' ...Exit Node')
        mini_suscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()