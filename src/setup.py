#!/usr/bin/env python

import os
from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "spinebreaker",
    version = "0.1",
    author = "Choonho Son",
    author_email = "choonho.son@gmail.com",
    description = ("Failure Testing Framework"),
    license = "BSD",
    keywords = "failure aws framework",
    url = "https://github.com/choonho/spine-breaker",
    packages=['spinebreaker','spinebreaker.api', 'spinebreaker.db', 'spinebreaker.provider',
                'spinebreaker.scheduler'],
    long_description=read('../README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe=True,
)

