# EJEMPLO Comunicación puerto serial

En este ejemplo se tiene una demostración básica para comunicar ROS con un microcontrolador (sin usar micro-ros). Previamente debe tener:

`instalar pyserial`

`permisos de lectura y escritura sobre el puerto serial`

Para ejecutar el ejemplo, en una terminal ejecute los siguientes comandos:

`colcon build`

`source install/setup.bash`

`ros2 run serial_pkg serial_publish`

En otra terminal, para recibir datos a travez de un topic ejecute:

`source install/setup.bash`

`ros2 run serial_pkg serial_receive`

En otra terminal, para recibir datos desde un servicio ejecute:

`source install/setup.bash`

`ros2 run serial_pkg serial_client #`

donde # corresponde aun número entero ente 0 y 5
