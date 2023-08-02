"""Sample usage of SPlisHSPlasH simulation via the API."""
from absl import logging
from absl import flags
from absl import app

import inductiva

FLAGS = flags.FLAGS

flags.DEFINE_string("api_url", "http://api.inductiva.ai",
                    "Base URL of the Inductiva API.")
flags.DEFINE_string("sim_dir",
                    None,
                    "Directory with the simulation inputs.",
                    required=True)
flags.DEFINE_string("sim_config_filename",
                    None,
                    "Name of the input file.",
                    required=True)
flags.DEFINE_string("output_dir",
                    None,
                    "Directory where the outputs will be stored.",
                    required=True)


def main(_):
    """Run a SPlisHSPlasH simulation using user-provided input files."""

    inductiva.api_url = FLAGS.api_url

    sph_sim = inductiva.fluids.simulators.SPlisHSPlasH()

    task = sph_sim.run(input_dir=FLAGS.sim_dir,
                       sim_config_filename=FLAGS.sim_config_filename)

    logging.info("Task ID %s", task.id)


if __name__ == "__main__":
    app.run(main)
