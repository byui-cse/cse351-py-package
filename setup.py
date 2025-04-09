from setuptools import setup

setup(
    name='cse351',
    version='1.0.0',
    description='This package contains common classes and helper methods for the CSE 351 course at BYU-I.',
    url='https://github.com/byui-cse/cse351-py-package',
    author='Luc Comeau, Hunter Wilhelm, and Christopher Keers',
    license='MIT',
    packages=['cse351'],
    install_requires=['matplotlib', 'numpy', 'pillow', 'opencv-python', 'requests'],
    zip_safe=False
)