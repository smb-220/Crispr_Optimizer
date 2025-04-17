from torch_geometric.data import Data
from ai_model.gnn_model import gRNA_GNN
import torch

def predict_efficiency(graph_data):
    model = gRNA_GNN()
    model.load_state_dict(torch.load("model_weights.pt"))
    model.eval()
    with torch.no_grad():
        return model(graph_data).item()
