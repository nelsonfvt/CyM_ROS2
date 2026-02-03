from setuptools import find_packages, setup

package_name = 'area_triangulo_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'area_cliente = area_triangulo_pkg.area_cliente:main',
            'area_server = area_triangulo_pkg.area_server:main',
        ],
    },
)
