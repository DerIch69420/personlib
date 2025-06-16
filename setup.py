from setuptools import setup, find_packages

setup(
    name="personlib",
    version="0.1",
    packages=find_packages(include=['personlib']),
    author="Morten Barthel",
    description="Simple JSON-based person handler",
    python_requires=">=3.13",
)

