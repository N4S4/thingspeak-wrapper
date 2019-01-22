from setuptools import setup, find_packages

setup(
    name='thingspeak_wrapper',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A thingspeak.com wrapper',
    long_description=open('README.md').read(),
    install_requires=['pandas'],
    url='https://github.com/N4S4/thingspeak_wrapper',
    author='Renato Visaggio',
    author_email='renatovisaggio@gmail.com'
)
