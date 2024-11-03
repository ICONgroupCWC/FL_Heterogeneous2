import torch.nn as nn
import torch.nn.functional as F


class GlobalModel(nn.Module):
    def __init__(self):
        super(GlobalModel, self).__init__()
        self.fc1 = nn.Linear(400, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 2)

    def forward(self, x):
        x = F.tanh(self.fc1(x))
        x = F.tanh(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

    def l2_regularization(self):
        l2_norm = sum(p.pow(2.0).sum() for p in self.parameters())
        return self.l2_lambda * l2_norm