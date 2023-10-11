"""Base class for scenarios."""

from abc import ABC, abstractmethod
import io
import tempfile
from typing import Optional, Union

from inductiva import resources, types
from inductiva.simulators import Simulator
import json


class Scenario(ABC):
    """Base class for scenarios."""
    valid_simulators = []

    @abstractmethod
    def create_input_files(self, simulator: Simulator, input_dir: types.Path):
        """To be implemented in subclasses."""
        pass

    def read_commands_from_file(self, commands_file: Union[str, io.StringIO]):
        "Read list of commands from commands.json file"
        if isinstance(commands_file, str):
            with open(commands_file, "r", encoding="utf-8") as f:
                return json.load(f)

        # Make sure already opened file is read from the beginning
        commands_file.seek(0)
        return json.load(commands_file)

    def validate_simulator(self, simulator: Simulator):
        """Checks if the scenario can be simulated with the given simulator."""
        if type(simulator) not in self.valid_simulators:
            raise ValueError(
                f"Simulator not supported for `{self.__class__.__name__}` "
                "scenario.")

    def simulate(
        self,
        simulator: Simulator,
        machine_group: Optional[resources.MachineGroup] = None,
        run_async: bool = False,
        storage_parent_dir: Optional[types.Path] = None,
        **kwargs,
    ):
        """Simulates the scenario synchronously."""
        self.validate_simulator(simulator)

        with tempfile.TemporaryDirectory() as input_dir:
            self.create_input_files(simulator, input_dir)

            return simulator.run(
                input_dir,
                machine_group=machine_group,
                run_async=run_async,
                storage_parent_dir=storage_parent_dir,
                **kwargs,
            )
