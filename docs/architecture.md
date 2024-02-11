# Architecture 

[tsmixer](./assets/img/TSMixer.png)

The data is a matrix where the rows are time steps and the columns are features. The model uses two MLP layers, one for time and one for features, which are combined using fully connected layers to create forecasts for all features.
