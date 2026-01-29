import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class my_publicador(Node):
    def __init__(self):
        super().__init__('Nodo_publicador')
        self.nodo_publicador = self.create_publisher(String, 'topic_tmp', 10)
        self.timer = self.create_timer(1.0, self.timer_llamado)
        self.contador = 0

    def timer_llamado(self):
        msg = String()
        msg.data = 'Mensaje: %d' % self.contador
        self.nodo_publicador.publish(msg)
        print("Publicando...")
        self.contador += 1



def main(args=None):

    try:
        rclpy.init(args=args)
        mini_publisher = my_publicador()
        rclpy.spin(mini_publisher)


    except KeyboardInterrupt:
        print(' ...Exit Node')
        mini_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()