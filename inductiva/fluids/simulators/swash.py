"""SWASH module of the API."""
import inductiva
from inductiva.fluids.simulators._base_simulator import BaseSimulator
from inductiva.types import Path


class SWASH(BaseSimulator):
    """Class to invoke a generic SWASH simulation on the API."""

    def simulate(self, n_cores=1, output_dir=None) -> Path:
        """Run the simulation.

        Args:
            output_dir: Directory where the generated files will be stored.
        """
        return inductiva.sw.swash.run_simulation(self.sim_dir,
                                                 self.input_filename,
                                                 n_cores=n_cores,
                                                 output_dir=output_dir)
