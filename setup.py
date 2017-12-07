from setuptools import setup

setup(
    name='DrawingProgram',
    version='0.1.dev0',
    packages=['drawing'],
    url='',
    license='MIT',
    author='Kunal Chowdhury',
    author_email='kunal.chowdhury@gmail.com',
    description='console based drawing tool',
    scripts=['bin/draw.py'],
    install_requires=['pyparsing == 2.2.0'],
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
)
