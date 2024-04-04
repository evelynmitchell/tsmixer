# Architecture 

[tsmixer](./assets/img/TSMixer.png)

The data is a matrix where the rows are time steps and the columns are features. The model uses two MLP layers, one for time and one for features, which are combined using fully connected layers to create forecasts for all features.

## Architecture Analysis and Design Language

### Input

Data will be read from disk as a csv file. The data will be a matrix where the rows are time steps and the columns are features.

Feature columns will include:
    - detrended price
    - log returns
    - volume
    - volatility
    - momentum indicators
    - moving averages
    - regression studies
    - trend studies
    - volatility studies
    - volume studies

Missing value policy is to fill with the last value carried forward.

Feature engineering will be done using the following techniques:
    - detrending
    - differencing
    - log returns
    - moving averages
    - momentum indicators
    - regression studies
    - trend studies
    - volatility studies
    - volume studies

The cleaned data will be split into training and testing sets.

The training set will be no more than 80% of the data.

The testing set will be no less than 20% of the data.

Open questions:
    Which of the features can be calculated on detrended data? 
    Which of the features can be calculated on log returns?
    Which of the features can be calculated on volume?
    Which of the features can be calculated on volatility?

Tiny training to sort out the code will be done on the first 1000 rows of the data.


