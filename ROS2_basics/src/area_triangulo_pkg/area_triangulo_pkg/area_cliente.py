import sys
import rclpy
from rclpy.node import Node

from my_interfaces.srv import TriangArea

class cliente_area(Node):

    def __init__(self):
        super().__init__('cliente')
        self.cli = self.create_client(TriangArea, 'Area_triangulo')
        while not self.cli.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TriangArea.Request()

    def send_request(self, alt, bas):
        self.req.base = bas
        self.req.altura = alt
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    cliente = cliente_area()
    resp = cliente.send_request(float(sys.argv[1]), float(sys.argv[2]))
    rclpy.spin_until_future_complete(cliente, resp)
    response = resp.result()
    cliente.get_logger().info(
        'Result of triangle area: %f' %
        (response.area))


if __name__ == '__main__':
    main()