""" This module contains the tests for the main module of tsmixer. """
# Generated by CodiumAI

import pytest
import sys
from unittest.mock import patch
from safetensors import safe_open

from tsmixer import tsmixer

class TestTSMixerMain:
    """ This class contains the tests for the main module. """

    def test_load_configuration_file(self):
        """ The program should load the configuration file if the --config i
            flag is set."""

        sys.argv = ['main.py', '--config', 'config.json']

        # Act
        with patch.object(config, 'load') as mock_load:
            tsmixer.main()

        # Assert
        mock_load.assert_called_once_with('config.json')


    def test_load_data_and_model_files_and_make_forecast(self):
        """ The program should load the data and model files and make a i
            forecast if the --data and --model flags are set."""


        sys.argv = ['main.py', '--data', 'data.csv', '--model', 'model.safetensors']
        # tensors = {}
        # with safe_open("model.safetensors", framework="pt", device=0) as f:
        #     for k in f.keys():
        #         tensors[k] = f.get_tensor(k)
        
        # Act
        with patch.object(utils, 'load_data') as mock_load_data, \
             patch.object(utils, 'load_model') as mock_load_model, \
             patch.object(utils, 'save_forecast') as mock_save_forecast:
            tsmixer.main()

        # Assert
        mock_load_data.assert_called_once_with('data.csv')
        mock_save_forecast.assert_called_once()


    def test_handle_missing_arguments_gracefully(self):
        """ The program should handle missing arguments gracefully."""
        # Arrange
        import sys

        sys.argv = ['main.py']

        # Act
        with pytest.raises(SystemExit):
            tsmixer.main()


    def test_handle_invalid_arguments_gracefully(self):
        """The program should handle invalid arguments gracefully."""
        # Arrange
        import sys

        sys.argv = ['main.py', '--invalid']

        # Act
        with pytest.raises(SystemExit):
            tsmixer.main()


    def test_handle_missing_configuration_file_gracefully(self):
        """The program should handle missing configuration file gracefully."""
        # Arrange
        import sys

        sys.argv = ['main.py', '--config']

        # Act
        with pytest.raises(SystemExit):
            tsmixer.main()
