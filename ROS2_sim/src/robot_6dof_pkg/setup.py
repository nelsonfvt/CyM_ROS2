import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_6dof_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share/' + package_name, 'launch'), glob(os.path.join('launch', '*launch.py'))),
        (os.path.join('share/' + package_name, 'urdf'), glob(os.path.join('urdf', '*.*'))),
        (os.path.join('share/' + package_name, 'rviz'), glob(os.path.join('rviz', '*.*'))),
        (os.path.join('share/' + package_name, 'meshes'), glob(os.path.join('meshes', '*.*'))),
        (os.path.join('share/' + package_name, 'worlds'), glob(os.path.join('worlds', '*.*'))),
        (os.path.join('share/' + package_name, 'config'), glob(os.path.join('config', '*.*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nelsonvt',
    maintainer_email='nelsonfvt@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_6dof_control = robot_6dof_pkg.robot_6dof_control:main'
        ],
    },
)
