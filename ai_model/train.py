from dataset import load_dataset
from gnn_model import gRNA_GNN
from torch_geometric.loader import DataLoader
import torch
import random

# Dummy training sequences
sequences = ["ATGCGTACGTAGCTAGCTAG", "TGCATGCATGCATGCACTGA", "CGTAGCTAGCTAGCTAGCTA"] * 100
dataset = load_dataset(sequences)
loader = DataLoader(dataset, batch_size=8, shuffle=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = gRNA_GNN().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.MSELoss()

for epoch in range(10):
    total_loss = 0
    model.train()
    for data in loader:
        data = data.to(device)
        out = model(data)
        loss = loss_fn(out, data.y.mean())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

torch.save(model.state_dict(), "model_weights.pt")
print("✅ Model saved as model_weights.pt")
