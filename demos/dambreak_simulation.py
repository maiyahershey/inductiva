"""Sample usage of SPlisHSPlasH simulation via API."""
from absl import logging
from absl import flags
from absl import app
import time

import inductiva
import inductiva_utils

FLAGS = flags.FLAGS

flags.DEFINE_string("api_url", "http://api.inductiva.ai",
                    "Base URL of the Inductiva API.")
flags.DEFINE_list("fluid_dimensions", [0.2, 1, 1],
                  "Dimensions of the fluid column.")
flags.DEFINE_list("fluid_position", [0.0, 0.0, 0.0],
                  "Position of the fluid column in the tank.")
flags.DEFINE_enum("resolution", "medium", ["high", "medium", "low"],
                  "Sets the fluid resolution to simulate..")
flags.DEFINE_string(
    "color_quantity", None, " Quantity to represent in the color scale of the"
    "scatter plot.")


def main(_):
    inductiva.api_url = FLAGS.api_url

    time_start = time.perf_counter()

    scenario = inductiva.fluids.DamBreak(
        fluid=inductiva.fluids.WATER,
        fluid_dimensions=inductiva_utils.flags.cast_list_to_float(
            FLAGS.fluid_dimensions),
        fluid_position=inductiva_utils.flags.cast_list_to_float(
            FLAGS.fluid_position),
        resolution=FLAGS.resolution)

    simulation_output = scenario.simulate()
    simulation_output.render(color_quantity=FLAGS.color_quantity)

    logging.info("Local time: %s", time.perf_counter() - time_start)


if __name__ == "__main__":
    logging.set_verbosity(logging.DEBUG)
    app.run(main)
