import sys

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Imuserv

class IMU_cliente(Node):

    def __init__(self):
        super().__init__('IMU_cliente')

        #crea cliente
        self.cli = self.create_client(Imuserv, 'sens_serv')

        # Hacer peticion
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Imuserv.Request()

    def send_req(self, a):
        self.req.canal = a
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    cliente = IMU_cliente()
    print('Canal solicitado:')
    print(sys.argv[1])
    future = cliente.send_req(int(sys.argv[1]))
    rclpy.spin_until_future_complete(cliente, future)
    resp = future.result()
    cliente.get_logger().info(
        'El valor es: %f' %(resp.variable))
    
    cliente.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()