from setuptools import find_packages
from setuptools import setup

requirements = [
    "numpy>=1.19.4",
    "scipy>=1.5.4",
    "Pillow>=8.0.1",
    "PyYAML>=5.3.1",
]

setup(
    name="panoptic_parts",
    version="0.1",
    author="pmeletis",
    url="https://github.com/pmeletis/panoptic_parts",
    description="Panoptic-Parts dataset tools",
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
)
