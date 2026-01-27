# Robot_3dof

Este ejemplo toma un modelo realizado en FreeCAD. El urdf se obtuvo mediante el workbench RobotCAD para ser visualizado en Rviz.

Una vez que compile y ejecute el ejemplo el brazo robot tendra movimiento automático.

Notará que el robot no está ubicado en el origen del entorno. ¿Como solucionar esto?

## Compilación del paquete

En una terminal ubicada en el direcorio ROS2_sim ejecute

`colcon build --packages-select robot_3dof`

`source install/setup.bash`

## Ejecución del ejemplo

`ros2 launch robot_3dof display.launch.py`

