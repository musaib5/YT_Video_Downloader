import sys
import subprocess #Subprocess in Python is used to run new programs and scripts by spawning new processes and enables the user to launch new programs right from the current Python program.
import pkg_resources #pkg_resources is a module used to find and manage Python package/version dependencies and access bundled files and resources.
from pprint import pprint #pprint is a Python module made to print data structures in a pretty way.

required  = {'pytube', 'pyinstaller'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
# pprint(installed)
missing   = required - installed


if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
else:
    exit()