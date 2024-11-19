"""
Module for creating a smoke test dataset for the TSMixer model.

This module reads data from SPX.csv, splits it into train, test,
and validation sets, and saves each set to separate CSV files.

Usage:
    - Reads the last 1000 rows from data/SPX.csv
    - Saves the first 800 rows as training data
    - Saves the next 100 rows as test data
    - Saves the final 100 rows as validation data

The data is split in reverse chronological order.
"""

# Path: scripts/data_split.py

from tsmixer.data_load import load_data


def split_data(data):
    """Split the data into train, test, and validation sets."""
    last_1000 = data.tail(1000)
    train = last_1000.head(800)
    test = last_1000[800:900]
    validation = last_1000[900:1000]

    return train, test, validation


def save_to_csv(df, filename):
    df.to_csv(filename, index=False)


# Load the data using the data_load module
data = load_data()

# Split the data
train, test, validation = split_data(data)

# Save the split data
save_to_csv(train, "tests/data/train.csv")
save_to_csv(test, "tests/data/test.csv")
save_to_csv(validation, "tests/data/validation.csv")

print("Data splitting completed successfully.")

# test the script
