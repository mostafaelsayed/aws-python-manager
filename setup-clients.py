from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Clients Package'
# Setting up
setup(
       # the name must match the folder name 'utils'
        name="clients",
        version=VERSION,
        packages=find_packages()
)