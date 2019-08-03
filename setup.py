#!/usr/bin/env python3
from setuptools import find_packages, setup

deps = {
    "raiden": [
        "requests>=2.22.0,<2.23.0",
        "mypy-extensions>=0.4.1,<0.5.0",
        "eth-hash[pycryptodome]>=0.2.0,<0.3.0",
        "argcomplete>=1.10.0,<2",
        # Replace web3 later
        "web3==4.9.1",
    ],
    "dev": [
        "black>=19.3b0,<19.4",
        "codecov>=2.0.15,<2.1.0",
        "pytest>=4.6.3,<4.7.0",
        "pytest-cov>=2.7.1,<2.8.0",
        "pytest-mypy>=0.3.3,<0.4.0",
    ],
    "docs": [
        "sphinx-argparse>=0.2.5,<0.3.0",
        "sphinx-autodoc-typehints>=1.7.0,<1.8.0"
    ],
}

deps["docs"] = (deps["raiden"], deps["docs"])

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
    url="https://github.com/maddevsio/raiden-python-client",
    version="0.0.3",
    entry_points={"console_scripts": ["raiden-cli=raiden_client.interfaces.cli:main"]},
)
