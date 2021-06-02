import copy
import paddle
import paddle.nn as nn

from .celoss import CELoss

from .triplet import TripletLoss, TripletLossV2
from .msmloss import MSMLoss
from .emlloss import EmlLoss
from .npairsloss  import NpairsLoss
from .trihardloss import TriHardLoss
from .centerloss  import CenterLoss

class CombinedLoss(nn.Layer):
    def __init__(self, config_list):
        super().__init__()
        self.loss_func = []
        self.loss_weight = []
        assert isinstance(config_list, list), (
            'operator config should be a list')
        for config in config_list:
            print(config)
            assert isinstance(config,
                              dict) and len(config) == 1, "yaml format error"
            name = list(config)[0]
            param = config[name]
            assert "weight" in param, "weight must be in param, but param just contains {}".format(
                param.keys())
            self.loss_weight.append(param.pop("weight"))
            self.loss_func.append(eval(name)(**param))

    def __call__(self, input, batch):
        loss_dict = {}
        for idx, loss_func in enumerate(self.loss_func):
            loss = loss_func(input, batch)
            weight = self.loss_weight[idx]
            loss = {key: loss[key] * weight for key in loss}
            loss_dict.update(loss)
        loss_dict["loss"] = paddle.add_n(list(loss_dict.values()))
        return loss_dict

def build_loss(config):
    module_class = CombinedLoss(config)
    return module_class
