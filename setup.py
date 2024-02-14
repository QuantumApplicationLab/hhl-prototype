from setuptools import find_packages, setup

name = "hhl_prototype"
version = "0.0.1"
description = "HHL linear solver package"

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    install_requires = f.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    install_requires=install_requires,
    packages=find_packages(),
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    include_package_data=True,
)
