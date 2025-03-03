from .conv_mixer import *
from .mlp_mixer import *
from .mpvit import *
from .patchconvnet import *
from .poolformer import *
from .segformer import *
from .convnext import *


model_dict = {
    "mpvit-tiny": MPViT_Tiny,
    "mpvit-xsmall": MPViT_XSmall,
    "mpvit-small": MPViT_Small,
    "mpvit-base": MPViT_Base,
    "patchconvnet-s60": PatchConvNet_S60,
    "patchconvnet-s120": PatchConvNet_S120,
    "patchconvnet-b60": PatchConvNet_B60,
    "patchconvnet-b120": PatchConvNet_B120,
    "patchconvnet-l60": PatchConvNet_L60,
    "patchconvnet-l120": PatchConvNet_L120,
    "poolformer-s12": PoolFormer_S12,
    "poolformer-s24": PoolFormer_S24,
    "poolformer-s36": PoolFormer_S36,
    "poolformer-m36": PoolFormer_M36,
    "poolformer-m48": PoolFormer_M48,
    "mlpmixer-s16": MLPMixer_S16,
    "mlpmixer-s32": MLPMixer_S32,
    "mlpmixer-b32": MLPMixer_B32,
    "mlpmixer-l16": MLPMixer_L16,
    "mlpmixer-l32": MLPMixer_L32,
    "mlpmixer-h14": MLPMixer_H14,
    "convmixer-1536-20": ConvMixer_1536_20,
    "convmixer-1024-20": ConvMixer_1024_20,
    "convmixer-768-32": ConvMixer_768_32,
    "convmixer-512-12": ConvMixer_512_12,
    "segformer-b0": SegFormer_B0,
    "segformer-b1": SegFormer_B1,
    "segformer-b2": SegFormer_B2,
    "segformer-b3": SegFormer_B3,
    "segformer-b4": SegFormer_B4,
    "segformer-b5": SegFormer_B5,
    "convnext-tiny": ConvNeXt_Tiny,
    "convnext-small": ConvNeXt_Small,
    "convnext-base": ConvNeXt_Base,
    "convnext-large": ConvNeXt_Large,
    "convnext-xlarge": ConvNeXt_XLarge,
}


def list_models():
    return sorted(list(model_dict.keys()))


def load_model(
    model_str="", attach_head=False, num_classes=1000, dropout=0.1, **kwargs
):
    return model_dict[model_str](attach_head, num_classes, dropout=dropout, **kwargs)
