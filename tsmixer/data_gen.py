""" Time series data generation for testing purposes. """

import numpy as np
import pandas as pd
from scipy.stats import norm


def generate_data(n, mu, sigma, seed=42):
    """ Generate time series data. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    return pd.Series(data)


def generate_data_with_index(n, mu, sigma, seed=42):
    """ Generate time series data with index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_missing_values(n, mu, sigma, seed=42):
    """ Generate time series data with missing values. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data[::5] = np.nan
    return pd.Series(data)


def generate_data_with_missing_values_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with missing values and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data[::5] = np.nan
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_outliers(n, mu, sigma, seed=42):
    """ Generate time series data with outliers. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data[::5] = data[::5] + 3 * sigma
    return pd.Series(data)


def generate_data_with_outliers_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with outliers and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data[::5] = data[::5] + 3 * sigma
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend(n, mu, sigma, seed=42):
    """ Generate time series data with trend. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1
    return pd.Series(data)


def generate_data_with_trend_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_seasonality(n, mu, sigma, seed=42):
    """ Generate time series data with seasonality. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.sin(np.arange(n) * 2 * np.pi / 365)
    return pd.Series(data)


def generate_data_with_seasonality_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with seasonality and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.sin(np.arange(n) * 2 * np.pi / 365)
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality(n, mu, sigma, seed=42):
    """ Generate time series data with trend and seasonality. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality_and_noise(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality and noise. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + \
        np.sin(np.arange(n) * 2 * np.pi / 365) + \
        norm.rvs(loc=0, scale=0.1, size=n)
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_noise_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, noise and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + \
        np.sin(np.arange(n) * 2 * np.pi / 365) + \
        norm.rvs(loc=0, scale=0.1, size=n)
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality_and_outliers(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality and outliers. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_outliers_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, outliers and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality_and_missing_values(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality and missing values. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = np.nan
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_missing_values_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, missing values and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = np.nan
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality_and_outliers_and_missing_values(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, outliers and missing values. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    data[::10] = np.nan
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, outliers, missing values and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    data[::10] = np.nan
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)


def generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, outliers, missing values and noise. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    data[::10] = np.nan
    data = data + norm.rvs(loc=0, scale=0.1, size=n)
    return pd.Series(data)


def generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise_and_index(n, mu, sigma, seed=42):
    """ Generate time series data with trend, seasonality, outliers, missing values, noise and index. """
    np.random.seed(seed)
    data = norm.rvs(loc=mu, scale=sigma, size=n)
    data = data + np.arange(n) * 0.1 + np.sin(np.arange(n) * 2 * np.pi / 365)
    data[::5] = data[::5] + 3 * sigma
    data[::10] = np.nan
    data = data + norm.rvs(loc=0, scale=0.1, size=n)
    index = pd.date_range(start='2020-01-01', periods=n, freq='D')
    return pd.Series(data, index=index)

# using a common time index of 365 days, combine the above functions to generate a dataset with a specific pattern
# where the time is the row and the features are the columns.
# The dataset will have 365 rows and a variable number of columns (at least one).
# The columns will be named "feature_1", "feature_2", etc.


def generate_dataset(pattern, mu, sigma, seed=42):
    """ Generate a dataset with a specific pattern. """
    n = 365
    np.random.seed(seed)
    data = []
    if pattern == 'random':
        for i in range(1, 6):
            data.append(generate_data(n, mu, sigma))
    elif pattern == 'random_with_index':
        for i in range(1, 6):
            data.append(generate_data_with_index(n, mu, sigma))
    elif pattern == 'random_with_missing_values':
        for i in range(1, 6):
            data.append(generate_data_with_missing_values(n, mu, sigma))
    elif pattern == 'random_with_missing_values_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_missing_values_and_index(n, mu, sigma))
    elif pattern == 'random_with_outliers':
        for i in range(1, 6):
            data.append(generate_data_with_outliers(n, mu, sigma))
    elif pattern == 'random_with_outliers_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_outliers_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend':
        for i in range(1, 6):
            data.append(generate_data_with_trend(n, mu, sigma))
    elif pattern == 'random_with_trend_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_index(n, mu, sigma))
    elif pattern == 'random_with_seasonality':
        for i in range(1, 6):
            data.append(generate_data_with_seasonality(n, mu, sigma))
    elif pattern == 'random_with_seasonality_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_seasonality_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_noise':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_noise(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_noise_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_noise_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_missing_values':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_missing_values(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_missing_values_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_missing_values_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers_and_missing_values':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers_and_missing_values(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers_and_missing_values_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_index(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise(n, mu, sigma))
    elif pattern == 'random_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise_and_index':
        for i in range(1, 6):
            data.append(generate_data_with_trend_and_seasonality_and_outliers_and_missing_values_and_noise_and_index(n, mu, sigma))
    else:
        raise ValueError('Invalid pattern')
    return pd.concat(data, axis=1)

# generate a dataset with a specific pattern and save it to a CSV file


def generate_dataset_to_csv(pattern, mu, sigma, filename, seed=42):
    """ Generate a dataset with a specific pattern and save it to a CSV file. """
    dataset = generate_dataset(pattern, mu, sigma, seed)
    dataset.to_csv(filename)

# generate a dataset with a specific pattern and save it to a CSV file


def generate_dataset_to_csv_with_index(pattern, mu, sigma, filename, seed=42):
    """ Generate a dataset with a specific pattern and save it to a CSV file. """
    dataset = generate_dataset(pattern, mu, sigma, seed)
    dataset.to_csv(filename, index_label='date')

# generate a dataset with a specific pattern and save it to a CSV file


def generate_dataset_to_csv_with_header(pattern, mu, sigma, filename, seed=42):
    """ Generate a dataset with a specific pattern and save it to a CSV file. """
    dataset = generate_dataset(pattern, mu, sigma, seed)
    dataset.to_csv(filename, header=True)

# generate a dataset with a specific pattern and save it to a CSV file


def generate_dataset_to_csv_with_index_and_header(pattern, mu, sigma, filename, seed=42):
    """ Generate a dataset with a specific pattern and save it to a CSV file. """
    dataset = generate_dataset(pattern, mu, sigma, seed)
    dataset.to_csv(filename, index_label='date', header=True)
