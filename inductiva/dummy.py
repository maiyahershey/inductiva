"""
Functions that call `dummy` endpoints.
"""
from .api import invoke_api


def sum(a: float, b: float) -> float:
    return invoke_api(locals(), sum)


# Still WIP: this one creates a file. How to specify it as output?
#def gen_file(size: int, sleep_s: int) -> float:
#   return invoke_api(locals(), gen_file)
