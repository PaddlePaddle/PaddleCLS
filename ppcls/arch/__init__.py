#copyright (c) 2021 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import copy
import importlib

import paddle.nn as nn

from . import backbone, gears
from .backbone import *
from .gears import build_gear
from .utils import *

__all__ = ["build_model", "RecModel", "DistillationModel"]


def build_model(config):
    config = copy.deepcopy(config)
    model_type = config.pop("name")
    mod = importlib.import_module(__name__)
    arch = getattr(mod, model_type)(**config)
    return arch


class RecModel(nn.Layer):
    def __init__(self, **config):
        super().__init__()
        backbone_config = config["Backbone"]
        backbone_name = backbone_config.pop("name")
        self.backbone = eval(backbone_name)(**backbone_config)
        if "BackboneStopLayer" in config:
            backbone_stop_layer = config["BackboneStopLayer"]["name"]
            self.backbone.stop_after(backbone_stop_layer)

        if "Neck" in config:
            self.neck = build_gear(config["Neck"])
        else:
            self.neck = None

        if "Head" in config:
            self.head = build_gear(config["Head"])
        else:
            self.head = None

    def forward(self, x, label=None):
        x = self.backbone(x)
        if self.neck is not None:
            x = self.neck(x)
        if self.head is not None:
            y = self.head(x, label)
        else:
            y = None
        return {"features": x, "logits": y}


class DistillationModel(nn.Layer):
    def __init__(self, models=None):
        super().__init__()
        assert isinstance(models, dict)
        self.model_list = []
        self.model_name_list = []
        for key in models:
            model_config = models[key]
            freeze_params = False
            pretrained = None
            if "freeze_params" in model_config:
                freeze_params = model_config.pop("freeze_params")
            if "pretrained" in model_config:
                pretrained = model_config.pop("pretrained")
            model_name = models.pop(model_name)
            model = eval(model_name)(model_config)
            if pretrained is not None:
                init_model(model, path=pretrained)
            if freeze_params:
                for param in model.parameters():
                    param.trainable = False
            self.model_list.append(self.add_sublayer(key, model))
            self.model_name_list.append(key)

    def forward(self, x, label=None):
        return None