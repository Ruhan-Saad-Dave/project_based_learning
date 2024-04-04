import importlib
import subprocess

required_modules = ['kivy', 'requests', 'pymongo']

def check_installation(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False
def install_module(module_name):
    print(f"Installing {module_name}...")
    subprocess.check_call(['pip','install',module_name])
def cim():
    for module_name in required_modules:
        if not check_installation(module_name):
            install_module(module_name)
        else:
            print(f"module {module_name} exists")