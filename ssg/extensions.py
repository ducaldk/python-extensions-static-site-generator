import sys
import importlib
from pathlib import Path

def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    # so this is how one would do 'shift'
    sys.path.pop(0)

def load_directory(directory):
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)

def load_bundled():
    # this __file__ is a new weird one - does it refer to the current module (file)?
    directory = Path(__file__).parent / "extensions"
    load_directory(directory)