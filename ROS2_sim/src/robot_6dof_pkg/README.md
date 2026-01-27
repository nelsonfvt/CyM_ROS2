# Robot_6dof_pkg

En este ejemplo se tiene un modelo sencillo con un manipulador antropomórfico con muñeca esférica.

Para compilar el ejemplo en una terminal ubidaca en el directorio ROS2_sim ejecute:

`colcon build --packages-select robot_6dof_pkg`

`source install/setup.bash`

Para ejecutar la simulación:

`ros2 launch robot_6dof_pkg gazebo.launch.py`

en otra terminal:

`source install/setup.bash`

`ros2 run robot_6dof_pkg robot_6dof_control.py`

El último nodo ejecutado lanza un algoritmo para mover el robot manipulador sin intervención del usuario.
Este nodo hace uso del módulo ro2_control.

Para la implementación se usaron partes que puede consultar en el listado de recursos.


## Recursos

### RobotCAD - FreeCAD

https://github.com/drfenixion/freecad.robotcad

### Controlling a 6DOF Robot Arm with ros2_control

https://mikelikesrobots.github.io/blog/6dof-arm-ros2-control/

### How to Simulate a Robotic Arm in Gazebo – ROS 2 Jazzy

https://automaticaddison.com/how-to-simulate-a-robotic-arm-in-gazebo-ros-2-jazzy/#Create_a_YAML_Configuration_File_for_the_Controller_Manager

### MOGI-ROS_Week-9-10-Simple-arm

https://github.com/MOGI-ROS/Week-9-10-Simple-arm
