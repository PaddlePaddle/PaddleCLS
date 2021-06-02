# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import sys
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(__dir__, '../')))

import paddle
import paddle.nn as nn

from ppcls.utils import config
from ppcls.engine.trainer import Trainer
from ppcls.arch import build_model
from ppcls.utils.save_load import load_dygraph_pretrain


class ClasModel(nn.Layer):
    """
    ClasModel: add softmax onto the model
    """

    def __init__(self, config):
        super().__init__()
        self.base_model = build_model(config)
        self.softmax = nn.Softmax(axis=-1)

    def eval(self):
        self.training = False
        for layer in self.sublayers():
            layer.training = False
            layer.eval()

    def forward(self, x):
        x = self.base_model(x)
        x = self.softmax(x)
        return x


if __name__ == "__main__":
    args = config.parse_args()
    config = config.get_config(args.config, overrides=args.override, show=True)
    # set device
    assert config["Global"]["device"] in ["cpu", "gpu", "xpu"]
    device = paddle.set_device(config["Global"]["device"])

    model = ClasModel(config["Arch"])

    if config["Global"]["pretrained_model"] is not None:
        load_dygraph_pretrain(model.base_model,
                              config["Global"]["pretrained_model"])

    model.eval()

    model = paddle.jit.to_static(
        model,
        input_spec=[
            paddle.static.InputSpec(
                shape=[None] + config["Global"]["image_shape"],
                dtype='float32')
        ])
    paddle.jit.save(model,
                    os.path.join(config["Global"]["save_inference_dir"],
                                 "inference"))
