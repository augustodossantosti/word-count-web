import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:/Python36x64/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Python36x64/tcl/tk8.6"

include_files = ['resources/autorun.inf',
                 'resources/favicon.ico',
                 'C:/Python36x64/DLLs/tcl86t.dll',
                 'C:/Python36x64/DLLs/tk86t.dll']

build_exe_options = {'include_files': include_files}

base = 'Win32GUI' if sys.platform == 'win32' else None
executables = [Executable('wordcountweb/word-count-app.py', base=base, icon='resources/favicon.ico')]

setup(
    name='word-count-web',
    version='1.0',
    url='https://github.com/augustodossantosti/word-count-web',
    license='MIT License',
    author='Augusto Santos',
    author_email='augustodossantos.ti@gmail.com',
    description='A simple word count application for web pages with Python and TkInter.',
    options={'build_exe': build_exe_options},
    executables=executables
)
