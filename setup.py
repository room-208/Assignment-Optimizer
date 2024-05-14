from pathlib import Path

from setuptools import find_packages, setup


def parse_requirements(filename):
    return Path(filename).read_text().splitlines()


setup(
    name="assignment_optimizer",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=parse_requirements("requirements.txt"),
)
