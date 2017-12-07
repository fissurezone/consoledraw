==============
DrawingProgram
==============

DrawingProgram provides a handy console based 2D shape drawing tool.

DrawingProgram has been written in Python 2.7. You need to install Python 2.7 on your system for it to work.

    *It is recommended that you install Python through the miniconda distribution.*
    Please visit `miniconda install guide <https://conda.io/docs/user-guide/install/>`.`

Once you have Python 2 installed, you need to build and install DrawingProgram using::

    * ``unzip DrawingProgram-0.1.dev0.zip`` OR ``tar -xvzf DrawingProgram-0.1.dev0.tar.gz``
    * ``cd DrawingProgram-0.1.dev0``
    * ``pip2 install -r requirements.txt``
    * ``python2 setup.py build install``

(Note: you may need elevated privileges to make these commands work.)

For example:

    ``sudo pip2 install -r requirements.txt``

Once Python 2 is installed, you can run DrawingProgram using::

    * ``python2 bin/draw.py``

(Note: you may need elevated privileges to make these commands work.)

How to build from source
========================

To build the tar.gz source distribution, use::

    * ``rm -rf DrawingProgram.egg-info build dist``
    * ``python2 setup.py clean``
    * ``python2 setup.py nosetests``
    * ``python2 setup.py sdist --formats=gztar,zip``

(Note: you may need elevated privileges to make these commands work.)

Design Assumptions
==================


