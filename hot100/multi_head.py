import torch


class MultiHead(torch.nn.Module):
    def __init__(self,embed_dim,num_heads):
        super.()
        self.num_heads = num_heads
        self.embed_dim = embed_dim
        self.head_dim = embed_dim // num_heads

        self.q=tor.nn.Linear(embed_dim,embed_dim)
        self.k=torch.nn.Linear(embed_dim,embed_dim)
        self.v=torch.nn.Linear(embed_dim,embed_dim)
    
    def forward(self,x):
        batch_size, seq_len, embed_dim = x.size()
        q=self.q(x).view(batch_size,seq_len,self.num_heads,self.head_dim).transpose(1,2)
        k=self.k(x).view(batch_size,seq_len,self.num_heads,self.head_dim).transpose(1,2)
        v=self.v(x).view(batch_size,seq_len,self.num_heads,self.head_dim).transpose(1,2)

        att_weight = torch.matmul(q,k.transpose(-1,-2))/torch.sqrt(torch.tensor(self.num_heads))
        att_weight = F.softmax(att_weight,dim=-1)

        score = torch.matmul(att_weight,v).transpose(1,2).view(batch_size,seq_len,embed_dim)

        return score