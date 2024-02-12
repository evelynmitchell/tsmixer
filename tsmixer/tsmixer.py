#Hi. Thanks for helping me today. I would like to write a model which implements the paper I will upload. The input is a matrix, where the rows are observations in time, and the columns are the observed features. The model architecture image looks like the attached image. The model used has N Mixer layers, where N is a configuration quantity. A  mixer layer takes in the matrix of time rows and feature columns. The first section is the time mixer. The data is copied to use as the residuals from the layer, and creates a 2D batch norm which is applied to the features. Then the matrix is rotated clockwise so time is columns and features are rows. Then it is passed to the MLP_time module, which consists of a Fully connected layer, a ReLU, and a dropout, the output of the MLP_time module is a matrix which is the same shape as the imput to the MLP_time module. This output is then counterclockwise  rotated so  time is again rows, and features columns. The final output is combined with the original input as  a residual. This ends the time mixer segment. The output of the time mixer is fed into the feature mixer segment. The first step of the feature mixer segment is to copy the original input data for the residual. Next, the 2D batch norm is created, which is used as input to the MLP_feature module. The MLP_feature module includes a fully connected layer, ReLU, dropout, another fully connected layer and then another dropout. The output of the MLP_feature module is combined with the residual  to create the output of the feature mixer segment. These two segments, the time mixer and the feature mixer make up the Mixer segment. There are N mixer segments. The output of the Mixer segments are the input to the Temporal Projection module. The Temporal Projection module is made up of the time row, feature column input matrix, which is rotated clockwise to have time as columns and features as rows, which is the passed into a fully connected layer, which creates the forecast matrix which is rotated counterclockwise to again have time as rows and featured as columns. The temporal projection segement does not include a skip residual. The output from the Temporal projection is the forecast for  the multivariate time series.

import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, dropout_rate):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)
        self.fc2 = nn.Linear(hidden_dim, input_dim)
        self.dropout2 = nn.Dropout(dropout_rate)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.dropout2(x)
        return x

class MixerLayer(nn.Module):
    def __init__(self, num_features, num_time_steps, hidden_dim, dropout_rate):
        super(MixerLayer, self).__init__()
        self.norm_features = nn.BatchNorm2d(num_features)
        self.norm_time = nn.BatchNorm2d(num_time_steps)
        self.mlp_time = MLP(num_time_steps, hidden_dim, dropout_rate)
        self.mlp_feature = MLP(num_features, hidden_dim, dropout_rate)

    def forward(self, x):
        # Time Mixing
        x_residual = x
        x = self.norm_features(x)
        x = x.permute(0, 2, 1, 3)  # Transpose to (batch, time, features, channels)
        x = self.mlp_time(x)
        x = x.permute(0, 2, 1, 3)  # Transpose back to (batch, features, time, channels)
        x = x + x_residual

        # Feature Mixing
        x_residual = x
        x = self.norm_time(x)
        x = self.mlp_feature(x)
        x = x + x_residual

        return x

class TemporalProjection(nn.Module):
    def __init__(self, num_features, num_time_steps):
        super(TemporalProjection, self).__init__()
        self.norm_time = nn.BatchNorm2d(num_time_steps)
        self.fc = nn.Linear(num_features, num_features)

    def forward(self, x):
        x = self.norm_time(x)
        x = x.permute(0, 2, 1, 3)  # Transpose to (batch, time, features, channels)
        x = self.fc(x)
        x = x.permute(0, 2, 1, 3)  # Transpose back to (batch, features, time, channels)
        return x

class TSMixer(nn.Module):
    def __init__(self, num_features, num_time_steps, hidden_dim, dropout_rate, num_layers):
        super(TSMixer, self).__init__()
        self.mixer_layers = nn.ModuleList([MixerLayer(num_features, num_time_steps, hidden_dim, dropout_rate) for _ in range(num_layers)])
        self.temporal_projection = TemporalProjection(num_features, num_time_steps)

    def forward(self, x):
        for mixer_layer in self.mixer_layers:
            x = mixer_layer(x)
        x = self.temporal_projection(x)
        return x
