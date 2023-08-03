"""DualSPHysics module of the API."""
from typing import Optional
from uuid import UUID

from inductiva import types, tasks
from inductiva.simulation import Simulator


class XBeach(Simulator):
    """Class to invoke a generic XBeach simulation on the API."""

    @property
    def api_method_name(self) -> str:
        return "sw.xbeach.run_simulation"

    def run(
        self,
        input_dir: types.Path,
        sim_config_filename: Optional[str] = "params.txt",
        resource_pool_id: Optional[UUID] = None,
        n_cores: int = 1,
        run_async: bool = False,
    ) -> tasks.Task:
        """Run the simulation.

        Args:
            sim_config_filename: Name of the simulation configuration file.
            n_cores: Number of MPI cores to use for the simulation.
            other arguments: See the documentation of the base class.
        """
        return super().run(
            input_dir,
            input_filename=sim_config_filename,
            n_cores=n_cores,
            resource_pool_id=resource_pool_id,
            run_async=run_async,
        )
