from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file_path = os.path.join(
        get_package_share_directory('kit_sensor_fusion'), 'config', 'ekf_config.yaml'
    )
    
    imu_launch_file = os.path.join(
        get_package_share_directory('kit_imu_driver'), 'launch', 'imu_launch.py'
    )
    
    wheel_odometry_launch_file = os.path.join(
        get_package_share_directory('kit_encoder_driver'), 'launch', 'wheel_odometry_launch.py'
    )

    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[config_file_path],
            remappings=[
                ('/odometry/filtered', '/kit/odometry/filtered'),
                ('/set_pose', '/kit/set_pose')
            ],
        ),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(imu_launch_file)
        ),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(wheel_odometry_launch_file)
        )
    ])
