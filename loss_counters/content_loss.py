import torch.nn as nn
import torch.nn.functional as F


class ContentLoss(nn.Module):
    def __init__(self, target_img):
        super(ContentLoss, self).__init__()
        self.target = target_img.detach()
        self.loss = F.mse_loss(self.target, self.target)

    def forward(self, input_img):
        self.loss = F.mse_loss(input_img, self.target_img)
        return input
