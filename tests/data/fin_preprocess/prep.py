""" Preprocess the financial data for the tsmixer model """
# in ../train.csv we have a yahoo finance data set with the columns:
# Date,Open,High,Low,Close,Adj Close,Volume

# In order to use this data in the tsmixer model, I would like
#  to preprocess the data in the following ways:
# - detrended price
# - log returns

# the steps to do this are:
# 1. read the data from disk
# 2. calculate the detrended price
# 3. calculate the log returns
# 4. save the data to disk

from tsmixer.data_load import load_data

# 1. read the data from hf
data = load_data()

print(data.head())

# 2. calculate the detrended price


# 3. calculate the log returns


# 4. save the data to disk
# the first will be the labels
data[
    [
        "date",
        "detrended_price",
        "detrended_high",
        "detrended_low",
        "detrended_open",
        "detrended_adj_close",
        "log_returns",
        "log_returns_high",
        "log_returns_low",
        "log_returns_open",
        "log_returns_adj_close",
        "volume",
    ]
].to_csv("../train_preprocessed.csv", index=False)
