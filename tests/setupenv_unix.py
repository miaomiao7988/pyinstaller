#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from __future__ import print_function

# Install necessary 3rd party Python modules to run all tests.
# This script is supposed to be used in a continuous integration system:
# https://jenkins.shiningpanda.com/pyinstaller/
# Python there is mostly 64bit.


import os
import sys


# Expand PYTHONPATH with PyInstaller package to support running without
# installation -- only if not running in a virtualenv.
if not hasattr(sys, 'real_prefix'):
    pyi_home = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    sys.path.insert(0, pyi_home)


import PyInstaller.compat as compat


# Pick a PyCrypto version to use to test bytecode encryption. This is typically
# used in conjunction with continuous integration.
if 'PYCRYPTO_VERSION' in os.environ:
    pycrypto = 'PyCrypto==%s' % os.environ['PYCRYPTO_VERSION']
else:
    pycrypto = 'PyCrypto'


_PACKAGES = [
    'docutils',
    'jinja2',
    'MySQL-python',
    'numpy ',
    'PIL',
    #'pyenchant',
    'pyodbc',
    'pytz',
    'sphinx',
    'simplejson',
    'SQLAlchemy',
    #'wxPython',
    'IPython',
    'zope.interface',
    pycrypto,
]


# TODO remove this block when we support Python 2.6+ only.
# Python 2.4 and 2.5 does not have ssl module. But we need
# it.
if sys.version_info[0:2] < (2,6):
    _PACKAGES.append('ssl')


def main():
    for pkg in _PACKAGES:
        print('Installing module...', pkg)
        retcode = compat.exec_command_rc('pip', 'install', pkg)
        if retcode:
            print(' ', pkg, 'installation failed')


if __name__ == '__main__':
    main()
