import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'rviz_ex'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share/', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share/', package_name, 'urdf'), glob(os.path.join('urdf', '*.*')) ),
        (os.path.join('share/', package_name, 'meshes'), glob(os.path.join('meshes', '*.*')) ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='nelsonfvt@gmail.com',
    description='Ejemplo simple con Rviz',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sumo_control = rviz_ex.sumo_control:main',
            'sumo_comando = rviz_ex.sumo_comando:main'
        ],
    },
)
