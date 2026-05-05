from math import sin, cos, pi
from geometry_msgs.msg import Quaternion

def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)

def mod_cinemat_inv(vx, vr):
    d = 0.29
    r = 0.16

    # aplica cinemática inversa -> velocidad ruedas
    wl = (vx - (d)*vr)/r # w rueda izq
    wr = (vx + (d)*vr)/r # w rueda der

    ws = [wl, wr]
    return ws