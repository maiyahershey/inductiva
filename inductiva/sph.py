"""Low-level method that interact with the API for SPH computation.

These functions are to be used inside the higher level constructs of the
Inductiva client. For instance, `scenario.simulate()` uses the `run_simulation`
function.
"""
import os
import pathlib
from .api import invoke_api
from .types import Path

from typing import Optional

# pylint: disable=unused-argument


def run_simulation(sim_dir: Path,
                   output_dir: Optional[Path] = None) -> pathlib.Path:
    """Run SplishSplash in the API.

    Args:
        sim_dir: Path to the directory containing the simulation inputs.

    Returns:
        TODO: once we have a class for holding the outputs of the simulation,
        it should be used here
    """
    sim_dir = pathlib.Path(sim_dir)
    if not os.path.isdir(sim_dir):
        raise ValueError("The provided path is not a directory.")

    params = locals()
    del params["output_dir"]

    return invoke_api(params, run_simulation, output_dir=output_dir)


# pylint: enable=unused-argument
