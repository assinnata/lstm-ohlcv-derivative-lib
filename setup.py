#!/usr/bin/env python
import codecs
import os.path
import re

from setuptools import find_packages, setup


def find_version(*file_paths):
    version_file = codecs.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), *file_paths), "r"
    ).read()
    version_match = re.search(r"^VERSION = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().split("\n")

setup(
    name="lstm_ohlcv_derivative_lib",
    version=find_version("lstm_ohlcv_derivative_lib", "settings.py"),
    author="Matteo Assinnata",
    author_email="matteo@assinnata.com",
    description="amazon keyword",
    scripts=["bin/lstm_test"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/assinnata/lstm-ohlcv-derivative-lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements,
    include_package_data=True,
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
    license="GPL-3.0 License",
    python_requires=">= 3.6",
)
