#!/usr/bin/env python
from setuptools import setup

#from setuptools import setup, find_packages

setup (
     name = "autonetkit-v3",
     version = "0.0.1",
     description = 'Automated configuration generator for cBGP, Netkit and Junosphere',
     long_description = 'Automated configuration generator for cBGP, Netkit and Junosphere',

     # simple to run 
     entry_points = {
         'console_scripts': [
             'autonetkit = autonetkit.console_script:main',
         ],
     },

     author = 'Simon Knight',
     author_email = "simon.knight@gmail.com",
     url = "http://www.autonetkit.org",
     packages = ['autonetkit'],

     package_data = {'': ['settings.cfg', 
                          ]},
     download_url = ("http://pypi.python.org/pypi/AutoNetkit"),

     install_requires = ['netaddr', 'mako', 'networkx>=1.7', 
         'configobj',  'textfsm', 'pika',
         ],

     classifiers = [
         "Programming Language :: Python",
         "Development Status :: 3 - Alpha",
         "Intended Audience :: Science/Research",
         "Intended Audience :: System Administrators",
         "Intended Audience :: Telecommunications Industry",
         "License :: OSI Approved :: BSD License",
         "Operating System :: MacOS :: MacOS X",
         "Operating System :: POSIX :: Linux",
         "Topic :: System :: Networking",
         "Topic :: System :: Software Distribution",
         "Topic :: Scientific/Engineering :: Mathematics",
         ],     
 
)