import rclpy
from rclpy.node import Node
from my_interfaces.msg import Myimudata

class IMU_Receiver(Node):
    def __init__(self):
        super().__init__('IMU_receiver')

        #Crear sucriptor
        self.suscriber = self.create_subscription(Myimudata, 'sensores', self.receiver_callback, 10)

    def receiver_callback(self, msg):
        print('Recibiendo:')
        print('Aceleracion X: ' + str(msg.ax))
        print('Aceleracion Y: ' + str(msg.ay))
        print('Aceleracion Z: ' + str(msg.az))
        print('Vel angular X: ' + str(msg.gx))
        print('Vel angular Y: ' + str(msg.gy))
        print('Vel angular Z: ' + str(msg.gz))

def main(args=None):
    print('Hi from serial_pkg.receiver')
    rclpy.init(args=args)
    node = IMU_Receiver()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
