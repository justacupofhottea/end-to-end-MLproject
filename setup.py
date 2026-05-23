from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        #requirements = [req.replace("\n", "")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name ='end-to-end-MLproject', 
    version ='0.0.1',
    author = 'Anna',
    author_email = 'aabrahamyan2000@gmail.com',
    packages = find_packages(),
    #install_requires = ['pandas', 'numpy', 'seaborn']
    install_requires = get_requirements('requirements.txt')
) 


# how  find_packages() works:
# checks how many folders have __init__.py and considers them as source


#when we have a lot of packages we create 
# function instead if install_requires = ['pandas', 'numpy', 'seaborn']