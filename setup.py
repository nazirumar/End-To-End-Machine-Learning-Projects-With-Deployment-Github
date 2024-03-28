from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    this function will the list of requirements
    """
    requirements =[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements =[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="MLprojects",
    version='0.0.1',
    author='Nazbeen Ai',
    author_email='nazirumar888@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt'),
)