"Postprocessing steps for the MDWaterBox scenario."
import os
import MDAnalysis as mda
from MDAnalysis import transformations
import nglview as nv
from pathlib import Path


class MDWaterBoxOutput:
    """Post process the simulation output of a MDWaterBox scenario."""

    def __init__(self, sim_output_path: Path = None):
        """Initializes a `MDWaterBoxOutput` object.

        Given a simulation output directory that contains the standard files
        generated by a MDWaterBox simulation run, this class provides methods to
        visualize the simulation outputs in a notebook interactively.

        Args:
            sim_output_path: Path to the simulation output directory."""

        self.sim_output_dir = sim_output_path

    def render_interactive(self):
        """Render the simulation outputs in an interactive visualization."""

        topology = os.path.join(self.sim_output_dir, "eql.tpr")
        trajectory = os.path.join(self.sim_output_dir, "eql.xtc")
        universe = mda.Universe(topology, trajectory, all_coordinates=True)
        atoms = universe.atoms
        transformation = transformations.unwrap(atoms)
        universe.trajectory.add_transformations(transformation)

        view = nv.show_mdanalysis(universe)
        view.add_ball_and_stick("all")
        view.center()
        view.parameters = {
            "backgroundColor": "white"
        }  # Set the background color
        return view
