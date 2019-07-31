#!/usr/bin/env python3
from setuptools import find_packages, setup

deps = {
    "raiden": [
        "requests>=2.22.0,<2.23.0",
        "jsonschema>=3.0.1,<3.1.0",
        "eth-utils>=1.6.1,<1.7.0",
        "mypy-extensions>=0.4.1,<0.5.0",
        "eth-hash[pycryptodome]>=0.2.0,<0.3.0",
    ],
    "dev": [
        # Strict raiden (stable) version
        "raiden==0.100.3",
        "pytest-mypy>=0.3.3,<0.4.0",
        "pytest>=4.6.3,<4.7.0",
        "black>=19.3b0,<19.4",
    ],
}

install_requires = deps["raiden"]

setup(
    name="raiden-client",
    author="Aleksandr Sobolev",
    author_email="thesobolev@gmail.com",
    description="Python client library Raiden API",
    license="MIT",
    extras_require=deps,
    install_requires=install_requires,
    include_package_data=True,
    keywords="raiden",
    packages=find_packages(exclude=["tests", "tests.*"]),
    url="https://github.com/s0b0lev/raiden-python",
    version="0.0.2",
    entry_points={"console_scripts": ["raiden-cli=raiden_client.interfaces.cli:main"]},
)
