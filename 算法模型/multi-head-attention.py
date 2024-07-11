#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   multi-head-attention.py
@Time    :   2024/03/27 18:58:25
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
"""

import torch
import numpy as np
from transformers import BertModel, BertTokenizer


class MultiHead(torch.nn.Module):
    def __init__(self, embed_dim, num_head) -> None:
        super().__init__()
        self.num_head = num_head
        self.embed_dim = embed_dim
        self.head_dim = self.embed_dim // num_head

        self.q = torch.nn.Linear(embed_dim, embed_dim)
        self.k = torch.nn.Linear(embed_dim, embed_dim)
        self.v = torch.nn.Linear(embed_dim, embed_dim)

    def forward(self, x, mask=None):
        batch_size = x.size(0)
        q = self.q(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1, 2)
        k = self.k(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1, 2)
        v = self.v(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1, 2)

        attn = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(
            torch.tensor(self.head_dim, dtype=torch.float32)
        )
        print(attn.shape)
        if mask != None:
            mask = mask.unsqueeze(1)
            attn = attn.masked_fill(mask == 0, float("-inf"))
            # attn = attn.masked_fill(mask == 0, -1e9)
        score = torch.nn.functional.softmax(attn, dim=-1)

        score = torch.matmul(score, v).transpose(1, 2).contiguous()
        score = score.reshape(batch_size, -1, self.embed_dim)

        return score


def subsequent_mask(size):
    """生成向后遮掩的掩码张量, 参数size是掩码张量最后两个维度的大小, 它的最后两维形成一个方阵"""
    # 在函数中, 首先定义掩码张量的形状
    attn_shape = (1, size, size)

    # 然后使用np.ones方法向这个形状中添加1元素,形成上三角阵, 最后为了节约空间,
    # 再使其中的数据类型变为无符号8位整形unit8
    subsequent_mask = np.triu(np.ones(attn_shape), k=1).astype("uint8")

    # 最后将numpy类型转化为torch中的tensor, 内部做一个1 - 的操作,
    # 在这个其实是做了一个三角阵的反转, subsequent_mask中的每个元素都会被1减,
    # 如果是0, subsequent_mask中的该位置由0变成1
    # 如果是1, subsequent_mask中的该位置由1变成0
    return torch.from_numpy(1 - subsequent_mask)


if __name__ == "__main__":
    x = torch.randn(2, 10, 40)
    mask = subsequent_mask(10)
    # mask = torch.zeros(2, n_q, n_k).bool()
    model = MultiHead(40, 4)
    out = model(x, mask)
    print(out.shape)
