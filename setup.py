from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT= '-e .'
def get_requirements(filepath:str)-> List[str]:
    """ This function will return the requirements """
    requirements= []
    with open(filepath) as fileobj:
        requirements= fileobj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name= 'MLProject',
    version= '0.0.1',
    author= 'Shakti',
    author_email= 'spm.datascientist7@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)