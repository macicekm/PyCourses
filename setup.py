#https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python
from cx_Freeze import setup, Executable

base = None

executables = [Executable("helloWorld.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)