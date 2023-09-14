#! /usr/bin/env python

from setuptools import setup, find_packages

setup(name="nginx_log_bot_statistic",
      version="0.1",
      author="HectorTwist",
      py_modules=['nginx_log_bot_statistic'],
      summary="Library for parse NGINX access.log files and grep info about bot requests",
      description="Library for parse NGINX access.log files and grep info about bot requests",
      url="https://github.com/SergeyFrancev/nginx-log-bot-statistic",
      license="GPLv3+",
      test_suite='tests',
      install_requires = [
          "six",
      ],
      classifiers=[
            'Development Status :: 1 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
            'Topic :: Internet :: WWW/HTTP :: Site Management',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
)
