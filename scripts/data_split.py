# To create a smoke test dataset for the model

# Path: scripts/data_split.py

# The data is in reverse chronological order
# Read  the last 1000 rows from data/SPX.csv
# Save the prior 800 rows to data/train.csv
# Save the prior 100 rows to data/test.csv
# Save the prior 100 rows to data/validation.csv

from data_load import load_data


def split_data(data):
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
