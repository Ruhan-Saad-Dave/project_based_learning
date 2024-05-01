"""
This file is used for automatic installing of required python libraries in order to run the program.

importlib - tries to import a library just for testing to see if it exists
subprocess - it uses command promt to install required python libraries.

This file will be used by main.py
"""


import importlib
import subprocess

required_modules = ['kivy', 'requests', 'pymongo']    #Libraries that will be used in the project

def check_installation(module_name):
    '''
    Checks if a specific module exists.

    module_name - The module that we are checking whether it is installed or not
    '''
    try:
        importlib.import_module(module_name)
        return True    #Module exists
    except ImportError:
        return False    #Module doesnt exist
    
def install_module(module_name):
    '''
    Installs the module is it doesnt exist.

    module_name - The module to be installed.
    '''
    print(f"Installing {module_name}...")
    subprocess.check_call(['pip','install',module_name])
    print(f"{module_name} has been installed successfully!")

def check_and_install_module():
    '''
    Calls the check_installation and install_module function, check and installs all the required modules for the project to work.
    '''
    for module_name in required_modules:
        if not check_installation(module_name):
            install_module(module_name)    #Module doesnt exist, so installs it
        else:
            print(f"module {module_name} exists")    #Module exists.


#The end of file