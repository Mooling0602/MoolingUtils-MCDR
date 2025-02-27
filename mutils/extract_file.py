## This module need MCDR plugin env.
from . import psi


def extract_file(file_path, target_path):
    with psi.open_bundled_file(file_path) as file_handler:
        with open(target_path, 'wb') as target_file:
            target_file.write(file_handler.read())

__all__ = ["extract_file"]
import sys
sys.modules[__name__] = extract_file