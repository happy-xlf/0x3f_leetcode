# Transformer 前向计算
class TransformerEncoder(nn.Moudle):
    
    def FeedForward(self, d_model, d_ff, dropout):
        super(FeedForward, self).__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc3 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(d_model)
    

    
    def init(self, vocab_size, d_model, N, heads, dropout):
        super(TransformerEncoder, self).__init__()
        self.N = N
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)

        self.q = nn.Linear(d_model, d_model)
        self.k = nn.Linear(d_model, d_model)
        self.v = nn.Linear(d_model, d_model)
        self.fc = nn.Linear(d_model, d_model)
        self.layer_norm = nn.LayerNorm(d_model)
        self.feed_forward = FeedForward(d_model, d_model, dropout)
        
        self.dropout = nn.Dropout(dropout)