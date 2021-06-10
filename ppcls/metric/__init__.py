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

from paddle import nn
import copy
from collections import OrderedDict

from .metrics import TopkAcc, mAP, mINP, Recallk, RetriMetric
from .metrics import DistillationTopkAcc


class CombinedMetrics(nn.Layer):
    def __init__(self, config_list):
        super().__init__()
        self.metric_func_list = []
        assert isinstance(config_list, list), (
            'operator config should be a list')

        self.retri_config = dict()  # retrieval metrics config
        for config in config_list:
            assert isinstance(config,
                              dict) and len(config) == 1, "yaml format error"
            metric_name = list(config)[0]
            if metric_name in ["Recallk", "mAP", "mINP"]:
                self.retri_config[metric_name] = config[metric_name]
                continue
            metric_params = config[metric_name]
            self.metric_func_list.append(eval(metric_name)(**metric_params))

        if self.retri_config:
            self.metric_func_list.append(RetriMetric(self.retri_config))

    def __call__(self, *args, **kwargs):
        metric_dict = OrderedDict()
        for idx, metric_func in enumerate(self.metric_func_list):
            metric_dict.update(metric_func(*args, **kwargs))

        return metric_dict


def build_metrics(config):
    metrics_list = CombinedMetrics(copy.deepcopy(config))
    return metrics_list
