# To create a smoke test dataset for the model

# This uses a hard-coded path to the data file
# TODO: Refactor the code to use the data_load module

# Path: scripts/data_split.py

# Read  the first 1000 rows from data/SPX.csv
# Save the first 800 rows to data/train.csv
# Save the next 100 rows to data/test.csv
# Save the last 100 rows to data/validation.csv

import pandas as pd

data = pd.read_csv("tests/data/original/SPX.csv")
train = data.iloc[:799]
test = data.iloc[800:899]
validation = data.iloc[900:1000]

train.to_csv("tests/data/train.csv", index=False)
test.to_csv("tests/data/test.csv", index=False)
validation.to_csv("tests/data/validation.csv", index=False)

# test the script
