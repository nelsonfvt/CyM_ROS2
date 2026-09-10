# Rviz - ejemplo con robot sumo

En este ejemplo se tiene un modelo sencillo de un robot mobil tipo minisumo. Previamente debe tener instalados los siguientes paquetes:

`ros-jazzy-joint-state-publisher`

`ros-jazzy-joint-state-publisher-gui`

Para compilar el ejemplo en una terminal ubidaca en el directorio ROS2_sim ejecute:

`colcon build --packages-select rvix_ex`

`source install/setup.bash`

Para correr el ejemplo en una terminal ejecutar el siguiente comando:

`ros2 launch rviz_ex display.launch.py`

en otra terminal:

`source install/setup.bash`

`ros2 run rviz_ex sumo_comando`
