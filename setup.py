from setuptools import find_packages, setup
from typing import List

def get_requiremnts() -> List[str]:
    """
    This function will return the list of string
    """
    requirements_list:List[str] =[]
    try:
        with open("requirements.txt") as f:
            list = f.read()
            requirements_list = list.splitlines()
            requirements_list.remove("-e .")
    except FileNotFoundError as e:
        raise e
    return requirements_list

AUTHOR_NAME = "Atiqur Rahman"
AUTHOR_EMAIL = "Atikurrahman209@gmail.com"
PROJECT_NAME = "sensor"

setup(
    name=PROJECT_NAME,
    version="0.0.1",
    author= AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages= find_packages(),
    install_requires=get_requiremnts(),

)