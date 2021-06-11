# LeViT

## 概述
LeViT是一种快速推理的、用于图像分类任务的混合神经网络。其设计之初考虑了网络模型在不同的硬件平台上的性能，因此能够更好地反映普遍应用的真实场景。通过大量实验，作者找到了卷积神经网络与Transformer体系更好的结合方式，并且提出了attention-based方法，用于整合Transformer中的位置信息编码。[论文地址](https://arxiv.org/abs/2104.01136)。

## 精度、FLOPS和参数量

| Models           | Top1 | Top5 | Reference<br>top1 | Reference<br>top5 | FLOPS<br>(G) | Params<br>(M) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| LeViT-128S | 0.7621 | 0.9277 | 0.766 | 0.929 | 305  | 7.8 |
| LeViT-128  | 0.7833 | 0.9378 | 0.786 | 0.940 | 406  | 9.2 |
| LeViT-192  | 0.7963 | 0.9460 | 0.800 | 0.947 | 658  | 11 |
| LeViT-256  | 0.8085 | 0.9497 | 0.816 | 0.954 | 1120 | 19 |
| LeViT-384  | 0.8234 | 0.9587 | 0.826 | 0.960 | 2353 | 39 |


**注**：与Reference的精度差异源于数据预处理不同。