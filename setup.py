#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata-django",
      version='0.9.0',
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="python opencivicdata library",
      long_description="",
      url="",
      py_modules=['opencivicdata.apps',
                  'opencivicdata.common'
                  'opencivicdata.divisions',
                  ],
      packages=['opencivicdata.admin',
                'opencivicdata.management',
                'opencivicdata.management.commands',
                'opencivicdata.migrations',
                'opencivicdata.models',
                'opencivicdata.tests',
                'opencivicdata.templates',
                ],
      include_package_data=True,
      install_requires=[
          'Django>=1.9',
          'psycopg2',
      ],
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   ],
      )
