from torch import nn


model = nn.Sequential(
    nn.Linear(9, 9),
    nn.ReLU(),
    nn.Linear(9, 9),
    nn.ReLU(),
    nn.Linear(9, 9),
)
