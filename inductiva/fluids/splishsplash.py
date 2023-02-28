"""SplishSplash module of the API."""
import os
import pathlib

import inductiva
from inductiva.types import Path


class SPlisHSPlasH:
    """Class to invoke a generic SplishSplash simulation on the API.

    Attributes:
        sim_dir: Path to the directory with all the simulation input files.
        input_file_name: Name of the SplishSplash input file. The file should
            be present in `sim_dir`, and the name is relative to that
            directory.
    """

    def __init__(self, sim_dir: Path, input_file_name: str):
        self.input_file_name = input_file_name
        self.sim_dir = pathlib.Path(sim_dir)

        if not os.path.isdir(sim_dir):
            raise ValueError("The provided path is not a directory.")

    def simulate(self, output_dir=None) -> Path:
        """Run the simulation.

        Args:
            output_dir: Directory where the generated files will be stored.
        """
        return inductiva.sph.splishsplash.run_simulation(self.sim_dir,
                                                         self.input_file_name,
                                                         output_dir=output_dir)
