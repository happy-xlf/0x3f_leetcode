import torch
import torch.nn as nn
input = torch.randint(0,256,(2,3,4,5)).float()

# bn = nn.BatchNorm2d(num_features=3)
# out = bn(input)#注输入需为float类型
# print(out)

# mean_channel1 = torch.mean(input[:,0,:,:])
# var_channel1 = torch.var(input[:,0,:,:], unbiased=False)
# normed_res_channel1 = (input[:,0,:,:] - mean_channel1) / ((var_channel1 + 1e-5)**0.5)
# print(normed_res_channel1)  

ln = nn.LayerNorm(normalized_shape=(3,4,5))
out = ln(input)
print(out)

mean = input.reshape(input.shape[0], -1).mean(axis=1).reshape(-1,1,1,1)
var = input.reshape(input.shape[0], -1).var(axis=1, unbiased=False).reshape(-1,1,1,1)
normed_res = (input - mean) / ((var + 1e-5)**0.5)
print(normed_res)