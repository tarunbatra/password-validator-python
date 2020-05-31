#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

name = "password_validator"
version = "1.0"

setup(name=name,
    version=version,
    description="Validates password according to flexible and intuitive specifications",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license="MIT",
    author="Tarun Batra",
    author_email="tarun.batra00@gmail.com",
    url="https://github.com/tarunbatra/password-validator-python",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/build')}},
      )
