
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



def AlexNet(**kwargs):
    '''AlexNet
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _alexnet.AlexNet(**kwargs)
    if pretrained:
        assert 'AlexNet' in _checkpoints, 'Not provide `AlexNet` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['AlexNet'])
        model.set_state_dict(paddle.load(path))

    return model



def VGG11(**kwargs):
    '''VGG11
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG11(**kwargs)
    if pretrained:
        assert 'VGG11' in _checkpoints, 'Not provide `VGG11` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG11'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG13(**kwargs):
    '''VGG13
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG13(**kwargs)
    if pretrained:
        assert 'VGG13' in _checkpoints, 'Not provide `VGG13` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG13'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG16(**kwargs):
    '''VGG16
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG16(**kwargs)
    if pretrained:
        assert 'VGG16' in _checkpoints, 'Not provide `VGG16` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG16'])
        model.set_state_dict(paddle.load(path))

    return model


def VGG19(**kwargs):
    '''VGG19
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _vgg.VGG19(**kwargs)
    if pretrained:
        assert 'VGG19' in _checkpoints, 'Not provide `VGG19` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['VGG19'])
        model.set_state_dict(paddle.load(path))

    return model




def ResNet18(**kwargs):
    '''ResNet18
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet18(**kwargs)
    if pretrained:
        assert 'ResNet18' in _checkpoints, 'Not provide `ResNet18` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet18'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet34(**kwargs):
    '''ResNet34
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet34(**kwargs)
    if pretrained:
        assert 'ResNet34' in _checkpoints, 'Not provide `ResNet34` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet34'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet50(**kwargs):
    '''ResNet50
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet50(**kwargs)
    if pretrained:
        assert 'ResNet50' in _checkpoints, 'Not provide `ResNet50` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet50'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet101(**kwargs):
    '''ResNet101
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet101(**kwargs)
    if pretrained:
        assert 'ResNet101' in _checkpoints, 'Not provide `ResNet101` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet101'])
        model.set_state_dict(paddle.load(path))

    return model


def ResNet152(**kwargs):
    '''ResNet152
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _resnet.ResNet152(**kwargs)
    if pretrained:
        assert 'ResNet152' in _checkpoints, 'Not provide `ResNet152` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['ResNet152'])
        model.set_state_dict(paddle.load(path))

    return model



def SqueezeNet1_0(**kwargs):
    '''SqueezeNet1_0
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _squeezenet.SqueezeNet1_0(**kwargs)
    if pretrained:
        assert 'SqueezeNet1_0' in _checkpoints, 'Not provide `SqueezeNet1_0` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['SqueezeNet1_0'])
        model.set_state_dict(paddle.load(path))

    return model


def SqueezeNet1_1(**kwargs):
    '''SqueezeNet1_1
    '''
    pretrained = kwargs.pop('pretrained', False)

    model = _squeezenet.SqueezeNet1_1(**kwargs)
    if pretrained:
        assert 'SqueezeNet1_1' in _checkpoints, 'Not provide `SqueezeNet1_1` pretrained model.'
        path = paddle.utils.download.get_weights_path_from_url(_checkpoints['SqueezeNet1_1'])
        model.set_state_dict(paddle.load(path))

    return model


    