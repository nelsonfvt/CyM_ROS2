import rclpy
from rclpy.node import Node

import random

from my_interfaces.msg import Mypoint3d



class envia_node(Node):
    def __init__(self):
        super().__init__('Nodo_envia')
        self.nodo_publicador = self.create_publisher(Mypoint3d, 'topic_tmp', 10)

        self.timer = self.create_timer(1.0, self.timer_llamado)

    def timer_llamado(self):
        msg = Mypoint3d()
        msg.x = random.uniform(-1.0, 1.0)
        msg.y = random.random()
        msg.z = random.uniform(0.0, 2.0)

        print('Publicando...')
        print(msg.x)
        print(msg.y)
        print(msg.z)
        self.nodo_publicador.publish(msg)


def main(args=None):

    print("En el main...")
    try:
        rclpy.init(args=args)
        mini_publisher = envia_node()
        rclpy.spin(mini_publisher)


    except KeyboardInterrupt:
        print(' ...Exit Node')
        mini_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()