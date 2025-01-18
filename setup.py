# by using this file, i am installing this local package in my current venv.

from setuptools import find_packages,setup

setup(
    name='mcqgenerator',  # Name of the package
    version='0.0.1',      # Version of the package
    author='Rishu Kumar', # Author's name
    author_email='kumar05.rishu@gmail.com', # Author's email
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"], 
    # Dependencies required to run the project
    packages=find_packages()  # Automatically includes all sub-packages
)

'''
- setuptools: A library for packaging Python projects.
- find_packages(): Automatically finds all packages (folders with an __init__.py file).

The setup.py file is used to package and distribute a Python project. It contains metadata and configuration for your project, allowing it to be installed or shared with others easily. Here's a breakdown of the code you shared:

Uses of setup.py:
- Package Creation: Converts your project into a distributable Python package.
- Dependency Management: Lists external libraries (install_requires) needed for your project.
- Metadata: Provides information like the project's name, version, author, and contact details.
- Distribution: Enables uploading the package to repositories like PyPI for others to use.

Why Use This?
- Makes your project easy to share and install using pip install . or from PyPI.
- Automatically handles dependencies and project structure.

In Short: This file is a blueprint for creating and distributing a Python package, ensuring it works seamlessly when others use it.
'''