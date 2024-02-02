from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='ML_project',
    version='0.1',
    author='Gani',
    author_email='mdgani.buhari@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('ML_project\requirements.txt')
)