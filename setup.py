#! /usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="openshift-python-wrapper",
    license="apache-2.0",
    download_url="https://github.com/RedHatQE/openshift-python-wrapper/archive/refs/tags/v1.0.tar.gz",
    keywords=["Openshift", "Kubevirt", "CNV"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "kubernetes",
        "openshift",
        "xmltodict",
        "urllib3",
        "netaddr",
        "paramiko",
        "pbr",
    ],
    python_requires=">=3.6",
)
