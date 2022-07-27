from setuptools import setup

package_name = 'rosbridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rk',
    maintainer_email='rk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rosbridge_listener  = rosbridge.rosbridge_listener:main',
            'room_directing  = rosbridge.room_directing:main',
        ],
    },
)
