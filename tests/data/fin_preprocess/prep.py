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

# I will use the following libraries:
import pandas as pd
import numpy as np

# 1. read the data from disk
data = pd.read_csv("../train.csv")

# 2. calculate the detrended price
data["detrended_price"] = data["Close"] - data["Close"].shift(1)
data["detrended_high"] = data["High"] - data["High"].shift(1)
data["detrended_low"] = data["Low"] - data["Low"].shift(1)
data["detrended_open"] = data["Open"] - data["Open"].shift(1)
data["detrended_adj_close"] = data["Adj Close"] - data[
    "Adj Close"
].shift(1)

# 3. calculate the log returns
data["log_returns"] = np.log(data["Close"]) - np.log(
    data["Close"].shift(1)
)
data["log_returns_high"] = np.log(data["High"]) - np.log(
    data["High"].shift(1)
)
data["log_returns_low"] = np.log(data["Low"]) - np.log(
    data["Low"].shift(1)
)
data["log_returns_open"] = np.log(data["Open"]) - np.log(
    data["Open"].shift(1)
)
data["log_returns_adj_close"] = np.log(data["Adj Close"]) - np.log(
    data["Adj Close"].shift(1)
)

data["date"] = pd.to_datetime(data["Date"])
data["volume"] = data["Volume"]


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
