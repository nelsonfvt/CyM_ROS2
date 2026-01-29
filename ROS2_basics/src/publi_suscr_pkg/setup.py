from setuptools import find_packages, setup

package_name = 'publi_suscr_pkg'

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
    description='Ejemplo simple con nodos publicador y suscriptor',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publi_suscr = publi_suscr_pkg.publi_suscr:main',
            'publicador = publi_suscr_pkg.publicador:main',
            'suscriptor = publi_suscr_pkg.suscriptor:main',
        ],
    },
)
