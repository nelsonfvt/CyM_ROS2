import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nelsonvt/workspace/Repos/CyM_ROS2/ROS2_sim/install/simple_robot'
