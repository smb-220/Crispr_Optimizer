import torch
from torch_geometric.data import Data
import random

# Encode nucleotides: A, T, G, C as one-hot
def one_hot_encode(seq):
    mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'G': [0,0,1,0], 'C': [0,0,0,1]}
    return [mapping.get(nuc, [0,0,0,0]) for nuc in seq]

def generate_dummy_graph(sequence):
    x = torch.tensor(one_hot_encode(sequence), dtype=torch.float)
    edge_index = []
    for i in range(len(sequence)-1):
        edge_index.append([i, i+1])
        edge_index.append([i+1, i])
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
    y = torch.tensor([random.random()], dtype=torch.float)
    return Data(x=x, edge_index=edge_index, y=y)

def load_dataset(sequences):
    return [generate_dummy_graph(seq) for seq in sequences]
