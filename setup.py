from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(filename: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirments = []
    with open(filename) as f:
        requirments = f.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)

    return requirments


setup(
    name="mlproject",
    version='0.0.1',
    author="Sanjith Kumar V",
    author_email="sanjithk50201@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
