# Mobile robot - RViz

Ejemplo de un robot diferencial sencillo.

## Ejecución del ejemplo

### Lanzando simulación

En una terminal dentro del workspace ejecute:
ro2 launch mobile_robot view.launch.py

En otra terminal ejecute:

ros2 topic pub --rate 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.1}}"
