#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name = 'piston-api-auth',
    version = '0.1.2',
    url = 'https://github.com/pbs/piston-api-auth',
    license = 'BSD',
    description = "Piston authentication extension that adds per request signing (similar with 2 legged OAuth).",
    author = 'Sever Banesiu',
    author_email = 'banesiu.sever@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
