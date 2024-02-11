""" The main file for the TSMixer application. """

import sys
import os
import logging
import argparse
import json
import time

from tsmixer import __version__

from tsmixer import config

from tsmixer import mixer
from tsmixer import server
from tsmixer import client

from tsmixer import utils

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the argument parser
parser = argparse.ArgumentParser(description="TSMixer - A multivariate time series forecasting tool.")

parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s " + __version__
)

parser.add_argument(
    "-c",
    "--config",
    type=str,
    help="Path to the configuration file."
)

parser.add_argument(
    "-s",
    "--server",
    action="store_true",
    help="Run the TSMixer server."
)

parser.add_argument(
    "-p",
    "--port",
    type=int,
    help="The port to run the server on."
)

parser.add_argument(
    "-d",
    "--data",
    type=str,
    help="Path to the data file."
)

parser.add_argument(
    "-m",
    "--model",
    type=str,
    help="Path to the model file."
)

parser.add_argument(
    "-o",
    "--output",
    type=str,
    help="Path to the output file."
)


def main():
    """ The main function for the TSMixer application. """

    # Parse the arguments
    args = parser.parse_args()

    # Load the configuration
    if args.config:
        config.load(args.config)

    # Run the server
    if args.server:
        server.run(port=args.port)

    # Run the client
    else:
        # Load the data
        data = utils.load_data(args.data)

        # Load the model
        model = utils.load_model(args.model)

        # Make the forecast
        forecast = model.forecast(data)

        # Save the forecast
        utils.save_forecast(forecast, args.output)

