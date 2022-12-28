from setuptools import find_packages, setup

setup(
    name="Lu's Website",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "secret",
        "mysql-connector-python"
    ]
)