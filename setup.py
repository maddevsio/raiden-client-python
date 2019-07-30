#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    author="Aleksandr Sobolev",
    author_email="thesobolev@gmail.com",
    description="Python client library Raiden API",
    install_requires=[
        "requests>=2.22.0,<2.23.0",
        "pytest-mypy>=0.3.3,<0.3.4",
        "pytest>=4.6.3,<4.7.0"
    ],
    include_package_data=True,
    keywords="raiden",
    name="raiden",
    packages=find_packages(),
    url="https://github.com/s0b0lev/raiden-python",
    version="0.0.1",
)
