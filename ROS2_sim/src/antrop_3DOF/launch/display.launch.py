import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    urdf_file_name = 'antrop_3DOF.urdf'
    urdf = os.path.join(
        get_package_share_directory('antrop_3DOF'),
        'urdf',
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    static_transform_publiser_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=[
                '--x', '0', '--y', '0', '--z', '0',
                '--yaw', '0', '--pitch', '0', '--roll',
                '0', '--frame-id', 'world', '--child-frame-id', 'base_link']
        )


    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}],
        arguments=[urdf]
    )

    # Nodo de control del robot
    antrop_control_node = Node(
        package = 'antrop_3DOF',
        executable = 'antrop_control',
        name = 'antrop_contol' 
    )

    # Create a node for rviz2
    rviz2_node = Node(
        package='rviz2',
        namespace='',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', [os.path.join(os.path.join(
            get_package_share_directory('antrop_3DOF'),
            'urdf',
            'my_config.rviz'), )]]

    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                             description='Flag to enable joint_state_publisher_gui'),
        
        #static_transform_publiser_node,
        robot_state_publisher_node,
        antrop_control_node,
        rviz2_node,


    ])