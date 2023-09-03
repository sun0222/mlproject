from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    It is return the list of requirements
    """
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
    return requirements


setup(
    name="Sunilkumar",
    version="0.0.1",
    author="Sunil",
    author_email="sunilkumart461@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)