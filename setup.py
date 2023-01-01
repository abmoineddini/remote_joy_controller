import os
from glob import glob
from setuptools import setup

package_name = 'remote_joy_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amirbahador',
    maintainer_email='abmoineddini@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "joy_topic = remote_joy_controller.joy_publisher:main",
            "twist_topic = remote_joy_controller.cmd_vel_publisher:main"
        ],
    },
)
