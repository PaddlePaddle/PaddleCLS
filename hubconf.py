# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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


dependencies = ['paddle', 'numpy']

import paddle

from ppcls.modeling.architectures import alexnet as _alexnet
from ppcls.modeling.architectures import vgg as _vgg 
from ppcls.modeling.architectures import resnet as _resnet 
from ppcls.modeling.architectures import squeezenet as _squeezenet
from ppcls.modeling.architectures import densenet as _densenet
from ppcls.modeling.architectures import inception_v3 as _inception_v3
from ppcls.modeling.architectures import inception_v4 as _inception_v4
from ppcls.modeling.architectures import googlenet as _googlenet
from ppcls.modeling.architectures import shufflenet_v2 as _shufflenet_v2
from ppcls.modeling.architectures import mobilenet_v1 as _mobilenet_v1
from ppcls.modeling.architectures import mobilenet_v2 as _mobilenet_v2
from ppcls.modeling.architectures import mobilenet_v3 as _mobilenet_v3
from ppcls.modeling.architectures import resnext as _resnext


# _checkpoints = {
#     'ResNet18': 'https://paddle-imagenet-models-name.bj.bcebos.com/dygraph/ResNet18_pretrained.pdparams',
#     'ResNet34': 'https://paddle-imagenet-models-name.bj.bcebos.com/dygraph/ResNet34_pretrained.pdparams',
# }


def _load_pretrained_urls():
    '''Load pretrained model parameters url from README.md
    '''
    import re
    import os
    from collections import OrderedDict

    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')

    with open(readme_path, 'r') as f:
        lines = f.readlines()
        lines = [lin for lin in lines if lin.strip().startswith('|') and 'Download link' in lin]
    
    urls = OrderedDict()
    for lin in lines:
        try:
            name = re.findall(r'\|(.*?)\|', lin)[0].strip().replace('<br>', '')
            url = re.findall(r'\((.*?)\)', lin)[-1].strip()
            if name in url:
                urls[name] = url
        except:
            pass

    return urls


_checkpoints = _load_pretrained_urls()


def _load_pretrained_parameters(model, name):
    assert name in _checkpoints, 'Not provide {} pretrained model.'.format(name)
    path = paddle.utils.download.get_weights_path_from_url(_checkpoints[name])
    model.set_state_dict(paddle.load(path))
    return model
    

def AlexNet(pretrained=False, **kwargs):
    '''AlexNet
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _alexnet.AlexNet(**kwargs)
    if pretrained:
        assert 'AlexNet' in _checkpoints, 'Not provide `AlexNet` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['AlexNet'])
        model.set_state_dict(paddle.load(path))

    return model



def VGG11(pretrained=False, **kwargs):
    '''VGG11
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG11(**kwargs)
    if pretrained:
        assert 'VGG11' in _checkpoints, 'Not provide `VGG11` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG11'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG13(pretrained=False, **kwargs):
    '''VGG13
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG13(**kwargs)
    if pretrained:
        assert 'VGG13' in _checkpoints, 'Not provide `VGG13` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG13'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG16(pretrained=False, **kwargs):
    '''VGG16
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG16(**kwargs)
    if pretrained:
        assert 'VGG16' in _checkpoints, 'Not provide `VGG16` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG16'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG19(pretrained=False, **kwargs):
    '''VGG19
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG19(**kwargs)
    if pretrained:
        assert 'VGG19' in _checkpoints, 'Not provide `VGG19` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG19'])
        model.set_state_dict(paddle.load(path))

    return model




def ResNet18(pretrained=False, **kwargs):
    '''ResNet18
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet18(**kwargs)
    if pretrained:
        assert 'ResNet18' in _checkpoints, 'Not provide `ResNet18` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet18'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet34(pretrained=False, **kwargs):
    '''ResNet34
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet34(**kwargs)
    if pretrained:
        assert 'ResNet34' in _checkpoints, 'Not provide `ResNet34` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet34'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet50(pretrained=False, **kwargs):
    '''ResNet50
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet50(**kwargs)
    if pretrained:
        assert 'ResNet50' in _checkpoints, 'Not provide `ResNet50` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet50'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet101(pretrained=False, **kwargs):
    '''ResNet101
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet101(**kwargs)
    if pretrained:
        assert 'ResNet101' in _checkpoints, 'Not provide `ResNet101` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet101'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet152(pretrained=False, **kwargs):
    '''ResNet152
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet152(**kwargs)
    if pretrained:
        assert 'ResNet152' in _checkpoints, 'Not provide `ResNet152` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet152'])
        model.set_state_dict(paddle.load(path))

    return model



def SqueezeNet1_0(pretrained=False, **kwargs):
    '''SqueezeNet1_0
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _squeezenet.SqueezeNet1_0(**kwargs)
    if pretrained:
        assert 'SqueezeNet1_0' in _checkpoints, 'Not provide `SqueezeNet1_0` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['SqueezeNet1_0'])
        model.set_state_dict(paddle.load(path))

    return model


def SqueezeNet1_1(pretrained=False, **kwargs):
    '''SqueezeNet1_1
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _squeezenet.SqueezeNet1_1(**kwargs)
    if pretrained:
        assert 'SqueezeNet1_1' in _checkpoints, 'Not provide `SqueezeNet1_1` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['SqueezeNet1_1'])
        model.set_state_dict(paddle.load(path))

    return model




def DenseNet121(pretrained=False, **kwargs):
    '''DenseNet121
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _densenet.DenseNet121(**kwargs)
    if pretrained:
        assert 'DenseNet121' in _checkpoints, 'Not provide `DenseNet121` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['DenseNet121'])
        model.set_state_dict(paddle.load(path))

    return model


def DenseNet161(pretrained=False, **kwargs):
    '''DenseNet161
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _densenet.DenseNet161(**kwargs)
    if pretrained:
        assert 'DenseNet161' in _checkpoints, 'Not provide `DenseNet161` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['DenseNet161'])
        model.set_state_dict(paddle.load(path))

    return model


def DenseNet169(pretrained=False, **kwargs):
    '''DenseNet169
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _densenet.DenseNet169(**kwargs)
    if pretrained:
        assert 'DenseNet169' in _checkpoints, 'Not provide `DenseNet169` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['DenseNet169'])
        model.set_state_dict(paddle.load(path))

    return model


def DenseNet201(pretrained=False, **kwargs):
    '''DenseNet201
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _densenet.DenseNet201(**kwargs)
    if pretrained:
        assert 'DenseNet201' in _checkpoints, 'Not provide `DenseNet201` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['DenseNet201'])
        model.set_state_dict(paddle.load(path))

    return model


def DenseNet264(pretrained=False, **kwargs):
    '''DenseNet264
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _densenet.DenseNet264(**kwargs)
    if pretrained:
        assert 'DenseNet264' in _checkpoints, 'Not provide `DenseNet264` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['DenseNet264'])
        model.set_state_dict(paddle.load(path))

    return model



def InceptionV3(pretrained=False, **kwargs):
    '''InceptionV3
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _inception_v3.InceptionV3(**kwargs)
    if pretrained:
        assert 'InceptionV3' in _checkpoints, 'Not provide `InceptionV3` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['InceptionV3'])
        model.set_state_dict(paddle.load(path))

    return model


def InceptionV4(pretrained=False, **kwargs):
    '''InceptionV4
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _inception_v4.InceptionV4(**kwargs)
    if pretrained:
        assert 'InceptionV4' in _checkpoints, 'Not provide `InceptionV4` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['InceptionV4'])
        model.set_state_dict(paddle.load(path))

    return model



def GoogLeNet(pretrained=False, **kwargs):
    '''GoogLeNet
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _googlenet.GoogLeNet(**kwargs)
    if pretrained:
        assert 'GoogLeNet' in _checkpoints, 'Not provide `GoogLeNet` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['GoogLeNet'])
        model.set_state_dict(paddle.load(path))

    return model



def ShuffleNet(pretrained=False, **kwargs):
    '''ShuffleNet
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _shufflenet_v2.ShuffleNet(**kwargs)
    if pretrained:
        assert 'ShuffleNet' in _checkpoints, 'Not provide `ShuffleNet` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ShuffleNet'])
        model.set_state_dict(paddle.load(path))

    return model



def MobileNetV1(pretrained=False, **kwargs):
    '''MobileNetV1
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v1.MobileNetV1(**kwargs)
    if pretrained:
        assert 'MobileNetV1' in _checkpoints, 'Not provide `MobileNetV1` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV1'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV1_x0_25(pretrained=False, **kwargs):
    '''MobileNetV1_x0_25
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v1.MobileNetV1_x0_25(**kwargs)
    if pretrained:
        assert 'MobileNetV1_x0_25' in _checkpoints, 'Not provide `MobileNetV1_x0_25` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV1_x0_25'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV1_x0_5(pretrained=False, **kwargs):
    '''MobileNetV1_x0_5
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v1.MobileNetV1_x0_5(**kwargs)
    if pretrained:
        assert 'MobileNetV1_x0_5' in _checkpoints, 'Not provide `MobileNetV1_x0_5` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV1_x0_5'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV1_x0_75(pretrained=False, **kwargs):
    '''MobileNetV1_x0_75
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v1.MobileNetV1_x0_75(**kwargs)
    if pretrained:
        assert 'MobileNetV1_x0_75' in _checkpoints, 'Not provide `MobileNetV1_x0_75` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV1_x0_75'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV2_x0_25(pretrained=False, **kwargs):
    '''MobileNetV2_x0_25
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v2.MobileNetV2_x0_25(**kwargs)
    if pretrained:
        assert 'MobileNetV2_x0_25' in _checkpoints, 'Not provide `MobileNetV2_x0_25` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV2_x0_25'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV2_x0_5(pretrained=False, **kwargs):
    '''MobileNetV2_x0_5
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v2.MobileNetV2_x0_5(**kwargs)
    if pretrained:
        assert 'MobileNetV2_x0_5' in _checkpoints, 'Not provide `MobileNetV2_x0_5` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV2_x0_5'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV2_x0_75(pretrained=False, **kwargs):
    '''MobileNetV2_x0_75
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v2.MobileNetV2_x0_75(**kwargs)
    if pretrained:
        assert 'MobileNetV2_x0_75' in _checkpoints, 'Not provide `MobileNetV2_x0_75` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV2_x0_75'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV2_x1_5(pretrained=False, **kwargs):
    '''MobileNetV2_x1_5
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v2.MobileNetV2_x1_5(**kwargs)
    if pretrained:
        assert 'MobileNetV2_x1_5' in _checkpoints, 'Not provide `MobileNetV2_x1_5` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV2_x1_5'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV2_x2_0(pretrained=False, **kwargs):
    '''MobileNetV2_x2_0
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v2.MobileNetV2_x2_0(**kwargs)
    if pretrained:
        assert 'MobileNetV2_x2_0' in _checkpoints, 'Not provide `MobileNetV2_x2_0` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV2_x2_0'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_large_x0_35(pretrained=False, **kwargs):
    '''MobileNetV3_large_x0_35
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_large_x0_35(**kwargs)
    if pretrained:
        assert 'MobileNetV3_large_x0_35' in _checkpoints, 'Not provide `MobileNetV3_large_x0_35` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_large_x0_35'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_large_x0_5(pretrained=False, **kwargs):
    '''MobileNetV3_large_x0_5
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_large_x0_5(**kwargs)
    if pretrained:
        assert 'MobileNetV3_large_x0_5' in _checkpoints, 'Not provide `MobileNetV3_large_x0_5` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_large_x0_5'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_large_x0_75(pretrained=False, **kwargs):
    '''MobileNetV3_large_x0_75
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_large_x0_75(**kwargs)
    if pretrained:
        assert 'MobileNetV3_large_x0_75' in _checkpoints, 'Not provide `MobileNetV3_large_x0_75` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_large_x0_75'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_large_x1_0(pretrained=False, **kwargs):
    '''MobileNetV3_large_x1_0
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_large_x1_0(**kwargs)
    if pretrained:
        assert 'MobileNetV3_large_x1_0' in _checkpoints, 'Not provide `MobileNetV3_large_x1_0` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_large_x1_0'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_large_x1_25(pretrained=False, **kwargs):
    '''MobileNetV3_large_x1_25
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_large_x1_25(**kwargs)
    if pretrained:
        assert 'MobileNetV3_large_x1_25' in _checkpoints, 'Not provide `MobileNetV3_large_x1_25` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_large_x1_25'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_small_x0_35(pretrained=False, **kwargs):
    '''MobileNetV3_small_x0_35
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_small_x0_35(**kwargs)
    if pretrained:
        assert 'MobileNetV3_small_x0_35' in _checkpoints, 'Not provide `MobileNetV3_small_x0_35` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_small_x0_35'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_small_x0_5(pretrained=False, **kwargs):
    '''MobileNetV3_small_x0_5
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_small_x0_5(**kwargs)
    if pretrained:
        assert 'MobileNetV3_small_x0_5' in _checkpoints, 'Not provide `MobileNetV3_small_x0_5` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_small_x0_5'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_small_x0_75(pretrained=False, **kwargs):
    '''MobileNetV3_small_x0_75
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_small_x0_75(**kwargs)
    if pretrained:
        assert 'MobileNetV3_small_x0_75' in _checkpoints, 'Not provide `MobileNetV3_small_x0_75` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_small_x0_75'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_small_x1_0(pretrained=False, **kwargs):
    '''MobileNetV3_small_x1_0
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_small_x1_0(**kwargs)
    if pretrained:
        assert 'MobileNetV3_small_x1_0' in _checkpoints, 'Not provide `MobileNetV3_small_x1_0` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_small_x1_0'])
        model.set_state_dict(paddle.load(path))

    return model


def MobileNetV3_small_x1_25(pretrained=False, **kwargs):
    '''MobileNetV3_small_x1_25
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _mobilenet_v3.MobileNetV3_small_x1_25(**kwargs)
    if pretrained:
        assert 'MobileNetV3_small_x1_25' in _checkpoints, 'Not provide `MobileNetV3_small_x1_25` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['MobileNetV3_small_x1_25'])
        model.set_state_dict(paddle.load(path))

    return model



def ResNeXt101_32x4d(pretrained=False, **kwargs):
    '''ResNeXt101_32x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt101_32x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt101_32x4d' in _checkpoints, 'Not provide `ResNeXt101_32x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt101_32x4d'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNeXt101_64x4d(pretrained=False, **kwargs):
    '''ResNeXt101_64x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt101_64x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt101_64x4d' in _checkpoints, 'Not provide `ResNeXt101_64x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt101_64x4d'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNeXt152_32x4d(pretrained=False, **kwargs):
    '''ResNeXt152_32x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt152_32x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt152_32x4d' in _checkpoints, 'Not provide `ResNeXt152_32x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt152_32x4d'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNeXt152_64x4d(pretrained=False, **kwargs):
    '''ResNeXt152_64x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt152_64x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt152_64x4d' in _checkpoints, 'Not provide `ResNeXt152_64x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt152_64x4d'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNeXt50_32x4d(pretrained=False, **kwargs):
    '''ResNeXt50_32x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt50_32x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt50_32x4d' in _checkpoints, 'Not provide `ResNeXt50_32x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt50_32x4d'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNeXt50_64x4d(pretrained=False, **kwargs):
    '''ResNeXt50_64x4d
    '''
    # pretrained = kwargs.pop('pretrained', False)

    model = _resnext.ResNeXt50_64x4d(**kwargs)
    if pretrained:
        assert 'ResNeXt50_64x4d' in _checkpoints, 'Not provide `ResNeXt50_64x4d` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNeXt50_64x4d'])
        model.set_state_dict(paddle.load(path))

    return model