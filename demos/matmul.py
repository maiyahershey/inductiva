"""
Sample usage of the inductiva package.
"""
import inductiva
import numpy as np

from absl import logging

if __name__ == "__main__":
    logging.set_verbosity(logging.DEBUG)

    inductiva.init(address="http://192.168.1.50:8000", output_dir="output")

    m = np.random.randint(10, size=(10, 10))
    n = np.identity(10)

    result = inductiva.math.matmul(m=m, n=n)

    logging.debug("Operation successful" if np.allclose(m, result) else \
        "Operation unsuccessful")
