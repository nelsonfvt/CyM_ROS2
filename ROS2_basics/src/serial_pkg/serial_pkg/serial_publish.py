import rclpy
from rclpy.node import Node
from my_interfaces.msg import Myimudata
from my_interfaces.srv import Imuserv
import serial
import threading
import struct

class SerialPublisher(Node):

    def __init__(self):
        super().__init__('serial_publisher')
        self.declare_parameter('serial_port', '/dev/ttyUSB0') #revisar puerto del micro
        self.declare_parameter('baud_rate', 115200)

        self.sens_arr = [0.0] * 6

        # Obtener parámetros
        serial_port = self.get_parameter('serial_port').get_parameter_value().string_value
        baud_rate = self.get_parameter('baud_rate').get_parameter_value().integer_value

        # Crear el publicador
        self.publisher = self.create_publisher(Myimudata, 'sensores', 10)
        # Crear el servidor
        self.serv = self.create_service(Imuserv, 'sens_serv', self.imu_data_callback)

        # Inicializar comunicación serial
        self.serial_connection = serial.Serial(serial_port, baud_rate, timeout=1)

        # Iniciar el hilo de lectura
        self.lock = threading.Lock()
        self.read_thread = threading.Thread(target=self.read_serial_data, daemon=True)
        self.read_thread.daemon = True
        self.read_thread.start()

    def read_serial_data(self):
        
        while rclpy.ok():

            # Leer datos de la comunicación serial
            band = self.serial_connection.read() # leer un byte
            
            if band[0] == 97: # llego 'a'
                msg = Myimudata() # crea tipo de mensaje

                with self.lock:

                    buff = self.serial_connection.read(4)
                    self.sens_arr[0] = struct.unpack('f', buff[0:4])[0] # bytes a float
                    buff = self.serial_connection.read(4)
                    self.sens_arr[1] = struct.unpack('f', buff[0:4])[0] # bytes a float
                    buff = self.serial_connection.read(4)
                    self.sens_arr[2] = struct.unpack('f', buff[0:4])[0] # bytes a float

                    buff = self.serial_connection.read(4)
                    self.sens_arr[3] = struct.unpack('f', buff[0:4])[0] # bytes a float
                    buff = self.serial_connection.read(4)
                    self.sens_arr[4] = struct.unpack('f', buff[0:4])[0] # bytes a float
                    buff = self.serial_connection.read(4)
                    self.sens_arr[5] = struct.unpack('f', buff[0:4])[0] # bytes a float

                    msg.ax = self.sens_arr[0]
                    msg.ay = self.sens_arr[1]
                    msg.az = self.sens_arr[2]
                    msg.gx = self.sens_arr[3]
                    msg.gy = self.sens_arr[4]
                    msg.gz = self.sens_arr[5]

                self.publisher.publish(msg)
                self.get_logger().info('Publicando sensores IMU 6dof')

    def imu_data_callback(self, request, response):
        if -1 < request.canal < 6:
            with self.lock:
                response.variable = self.sens_arr[request.canal]
        else:
            response.variable = 0.0

        return response

    def destroy_node(self):
        # Cerrar la conexión serial antes de destruir el nodo
        self.serial_connection.close()
        super().destroy_node()


def main(args=None):

    print('Hola desde serial_pkg')
    rclpy.init(args=args)
    node = SerialPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()