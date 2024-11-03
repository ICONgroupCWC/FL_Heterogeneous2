import torch
from torch.utils.data import Dataset
from torchvision import transforms
from preprocessUtil import get_transformations
import numpy as np

class ImageDataset(Dataset):

    def __init__(self, dataset, labels, transformations):
        super().__init__()
        self.dataset = dataset
        self.labels = labels
        # self.transform = transforms.Compose(get_transformations(transformations))
        # self.target_transform = transforms.Compose([transforms.ToTensor()])

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        image = self.dataset[index].astype(np.float32)
        label = self.labels[index]
        return image, label