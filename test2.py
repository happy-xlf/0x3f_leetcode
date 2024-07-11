#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test2.py
@Time    :   2024/05/23 11:50:06
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

nums = [1,3,4,7,2]

def dc(nums):
    tmp = [False]*len(nums)
    tmp[0] = True

    for i in range(len(nums)):
        if tmp[i] == True:
            ed = i + nums[i]
            ed = min(len(nums)-1, ed)
            if ed == len(nums)-1:
                return True
            for j in range(i+1,ed+1):
                tmp[j] = True
        

    return False

print(dc(nums))

class Self_attention(nn.Moudle):
    def __init__(self,emb_dim, num_head):
        self.emb_dim = emb_dim
        self.num_head = num_head
        self.head_dim = emb_dim // num_head
        self.q = nn.Linear(emb_dim, emb_dim)
        self.k = nn.Linear(emb_dim, emb_dim)
        self.v = nn.Linear(emb_dim, emb_dim)

    def forward(self,x):
        batch_size = x.size(0)
        q = self.q(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1,2)
        k = self.q(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1,2)
        v = self.q(x).view(batch_size, -1, self.num_head, self.head_dim).transpose(1,2)

        score = q.dot(k.transpose(-2,-1)) // sqrt(self.head_dim)
        score = F.softmax(score, dim=-1)

        atten = score.dot(v).view(batch_size, -1, self.emb_dim)

        return atten











