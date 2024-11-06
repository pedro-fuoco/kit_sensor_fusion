from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file_path = os.path.join(
        get_package_share_directory('kit_sensor_fusion'), 'config', 'ekf_config.yaml'
    )

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[config_file_path],
        remappings=[
            ('/odometry/filtered', '/kit/odometry/filtered'),
            ('/set_pose', '/kit/set_pose')
        ],
    )

    return LaunchDescription([ekf_node])
