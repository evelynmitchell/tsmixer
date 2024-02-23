""" This is a test module for the data_gen.py file. """

# Generated by CodiumAI

import pytest
from tsmixer import data_gen
import numpy as np

class TestDataGeneration:

    def test_generate_data(self):
        """ The code generates random time series data with specified mean 
            and standard deviation."""
        mu = 0
        sigma = 1
        n = 365
        data = data_gen.generate_data(n, mu, sigma)
        assert len(data) == n
        assert np.mean(data) == pytest.approx(mu, abs=0.1)
        assert np.std(data) == pytest.approx(sigma, abs=0.1)


    def test_generate_data_with_trend(self):
        """ The code generates time series data with a specified trend."""
        mu = 0
        sigma = 1
        n = 365
        data = data_gen.generate_data_with_trend(n, mu, sigma)
        assert len(data) == n
        #assert np.mean(data) == pytest.approx(mu, abs=0.1)
        # assert np.std(data) == pytest.approx(sigma, abs=0.1)
        # assert np.allclose(data, np.arange(n) * 0.1, atol=0.1)


    def test_generate_data_with_seasonality(self):
        """The code generates time series data with a specified seasonality."""
        mu = 0
        sigma = 1
        n = 365
        data = data_gen.generate_data_with_seasonality(n, mu, sigma)
        assert len(data) == n
        assert np.mean(data) == pytest.approx(mu, abs=0.1)
        # assert np.std(data) == pytest.approx(sigma, abs=0.1)
        # assert np.allclose(data, np.sin(np.arange(n) * 2 * np.pi / 365), atol=0.1)


    def test_generate_data_with_missing_values(self):
        """ The code generates time series data with missing values at regular intervals."""
        mu = 0
        sigma = 1
        n = 365
        data = data_gen.generate_data_with_missing_values(n, mu, sigma)
        assert len(data) == n
        assert np.mean(data) == pytest.approx(mu, abs=0.1)
        assert np.std(data) == pytest.approx(sigma, abs=0.1)
        assert np.isnan(data[::5]).all()


    def test_generate_data_with_outliers(self):
        """ The code generates time series data with outliers at regular intervals."""
        mu = 0
        sigma = 1
        n = 365
        data = data_gen.generate_data_with_outliers(n, mu, sigma)
        assert len(data) == n
        # assert np.mean(data) == pytest.approx(mu, abs=0.1)
        # assert np.std(data) == pytest.approx(sigma, abs=0.1)
        # assert np.allclose(data[::5], data[::5] + 3 * sigma, atol=0.1)
