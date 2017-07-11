#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import materializecssform

setup(
        name='django-materializecss-form',
        version=materializecssform.__version__,
        packages=find_packages()
        author="Daniel Grimshaw"
        author_email="danielgrimshaw42@gmail.com"
        description="Simple Django form template tag to work with the Materialize CSS library",
        long_description="A simple Django form template tag to work with the Materialize CSS library, compatible with Django 1.11.3"
        include_package_data=True,
        url='https://github.com/danielgrimshaw/django-materializecss-form',
        classifiers=[
            'Programming Language :: Python',
            'Development Status :: 4 - Beta',
            'Framework :: Django :: 1.11',
            'Intended Audience :: Developers'
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Topic :: Documentation :: Sphinx',
        ],
        license="GPLv3",
        zip_safe=False
)
