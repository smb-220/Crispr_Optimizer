import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class gRNA_GNN(torch.nn.Module):
    def __init__(self, input_dim=4, hidden_dim=32, output_dim=1):
        super().__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.linear = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.3, training=self.training)
        x = self.conv2(x, edge_index)
        return torch.sigmoid(self.linear(x)).mean(dim=0)
