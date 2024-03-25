"""
This file is for automatic installation of modules if you dont have it.
currently under testing
"""

import importlib
import subprocess

required_modules = ['kivy', 'requests']

def check_installation(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False
    
def install_module(module_name):
    print(f"Installing {module_name}...")
    subprocess.check_call(['pip','install',module_name])

def check_and_install_modules():
    for module_name in required_modules:
        if not check_installation(module_name):
            install_module(module_name)
        else:
            print(f"module {module_name} exists")

#using import on this point in other file