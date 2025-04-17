import torch
import os
from ai_model.gnn_model import gRNA_GNN

model = gRNA_GNN()

dummy_input = [torch.randn(20, 4)]  # Corrected shape: 20 rows × 4 features

output_path = os.path.join("ai_model", "model_weights.pt")
torch.save(model.state_dict(), output_path)

print(f"✅ Model weights saved to {output_path}")
