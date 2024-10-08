


# class MultiAttention(nn.Moudle):
#     def __init__(self,embedding_dim, head_num):
#         self.embedding_dim = embedding_dim
#         self.head_num = head_num
#         self.head_dim = embedding_dim // head_num
#         self.q = nn.Linear(embedding_dim, embedding_dim)
#         self.k = nn.Linear(embedding_dim, embedding_dim)
#         self.v = nn.Linear(embedding_dim, embedding_dim)


#     def forward(self,x):
#         batch_size = x.size(0)
#         q = self.q(x).view(batch_size, -1, self.head_num, self.head_dim).transpose(1,2)
#         k = self.k(x).view(batch_size, -1, self.head_num, self.head_dim).transpose(1,2)
#         v = self.v(x).view(batch_size, -1, self.head_num, self.head_dim).transpose(1,2)
#         attn = torch.matmul(q,k.transpose(-2,-1))/torch.sqrt(self.head_dim)
#         attn = F.softmax(attn,dim=-1)
#         score = torch.matmul(v,attn).transpose(1,2).view(batch_size,-1,self.embedding_dim)


def quick_sort(nums,l,r):
        value = nums[l]
        while l<r:
            while l<r and nums[r]<=value:
                r-=1
            nums[l] = nums[r]
            while l<r and nums[l]>=value:
                l+=1
            nums[r] = nums[l]
        nums[l] = value
        return l

if __name__ == "__main__":
    s = [9,7,4,6]
    print(quick_sort(s,0,3))