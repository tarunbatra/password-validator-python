#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="password_validator",
      version="0.1",
      description="Validates password according to flexible and intuitive specifications",
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="MIT",
      author="Tarun Batra",
      author_email="tarun.batra00@gmail.com",
      url="https://github.com/tarunbatra/password-validator-python",
      packages=find_packages("src"),
      package_dir={"": "src"},
      classifiers=[
          "Development Status :: 1 - Planning",
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
      )
