import rclpy
from rclpy.node import Node

from my_interfaces.srv import TriangArea

class server_area(Node):

    def __init__(self):
        super().__init__('servidor')
        self.srv = self.create_service(TriangArea, 'Area_triangulo', self.serv_callback)

    def serv_callback(self, request, response):
        response.area = (request.altura * request.base) / 2.0
        self.get_logger().info('Incoming request\naltura: %f base: %f' % (request.altura, request.base))

        return response

def main(args=None):

    try:
        rclpy.init(args=args)
        my_server = server_area()
        rclpy.spin(my_server)


    except KeyboardInterrupt:
        print(' ...Exit Node')
        my_server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()