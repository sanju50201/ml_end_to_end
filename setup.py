from setuptools import find_packages, setup
from typing import List
import os


def get_requirements(filename: str) -> List[str]:
    '''
    This function will return the list of requirements.

    Args:
    - filename: str -> Path to Requirements file.

    Returns:
    - List[str]

    '''
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")

    with open(filename, 'r', encoding="utf-8") as f:
        requirements = [line.strip()
                        for line in f if line.strip() and line.strip() != "-e ."]

        return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author="Sanjith Kumar V",
    author_email="sanjithk50201@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
