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


with open('README.md', 'r')as f:
    readme_content = f.read()


setup(
    name="raiden-client",
    author="Aleksandr Sobolev",
    author_email="thesobolev@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Client library for Raiden Rest API",
    license="MIT license",
    extras_require=deps,
    long_description=readme_content,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    include_package_data=True,
    keywords="raiden",
    packages=find_packages(exclude=["tests", "tests.*"]),
    url="https://github.com/maddevsio/raiden-python-client",
    version="0.0.8",
    entry_points={"console_scripts": ["raiden-cli=raiden_client.interfaces.cli:main"]},
)
