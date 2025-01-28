'''
the setup.py file is an essential part of packaging an distributing python projects.
It is used by setup tools to define the configuration of projects such as its metadata dependencies and more

'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements != '-e .':
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("Error: requirements.txt file not found.")
    
    return requirement_lst

print(get_requirements())

setup(
    name="sensor",
    version="0.0.1",
    author="BhavithShetty",
    author_email="nkrbhavith@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)