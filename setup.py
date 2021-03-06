#!/usr/bin/env python
#
# Copyright (C) 2013 Itzik Kotler
#
# This file is part of Hackersh.
#
# Hackersh is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# Hackersh is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hackersh; see the file COPYING.  If not,
# see <http://www.gnu.org/licenses/>.

try:

    import setuptools

except ImportError:

    from distribute_setup import use_setuptools

    use_setuptools()

    import setuptools


import sys
import distutils.core
import distutils.command.build


# Local imports

import hackersh


# Functions

def _mk_versiondotpy():

    with open('hackersh/_version.py', 'wt') as f:

        f.write('# DO NOT EDIT THIS FILE! It is automatically generated by setup.py\n__version__ = \'' + hackersh.__version__ + '\'\n')


# Classes

class Build(distutils.command.build.build):

    def run(self):

        # Generate `_version.py`

        _mk_versiondotpy()

        return distutils.command.build.build.run(self)


# Entry Point

if __name__ == "__main__":

    dependencies = ['pythonect>=0.4.2', 'prettytable>=0.6.1', 'netaddr>=0.7.10']

    major, minor = sys.version_info[:2]

    python_27 = (major > 2 or (major == 2 and minor >= 7))

    # < Python 2.7 ?

    if not python_27:

        # Python 2.6

        dependencies = dependencies + ['argparse>=1.2.1', 'ordereddict>=1.1']

    setupconf = dict(
        name='Hackersh',
        version=hackersh.__version__,
        author='Itzik Kotler',
        author_email='xorninja@gmail.com',
        url='http://www.hackersh.org/',
        license='GPLv2+',
        description='Hacker Shell, a shell (command interpreter) written in Python with Pythonect-like syntax, built-in security commands, and out of the box wrappers for various security tools.',

        long_description=open('README.rst').read(),

        scripts=['bin/hackersh'],

        packages=setuptools.find_packages(),

        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
        ],

        install_requires=dependencies,

        cmdclass={'build': Build},

        zip_safe=False,

    )

    setuptools.setup(**setupconf)
