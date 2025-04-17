# import streamlit as st
# import streamlit.components.v1 as components
# import json
# import torch
# import os
# import sys
# from pathlib import Path
# from Bio.Seq import Seq
# from torch_geometric.data import Data

# # --- Path Configuration ---
# current_dir = Path(__file__).parent
# project_root = current_dir.parent
# ai_model_dir = project_root / "ai_model"
# blockchain_dir = project_root / "blockchain"
# webapp_dir = project_root / "webapp"

# sys.path.append(str(ai_model_dir))
# sys.path.append(str(blockchain_dir))

# # --- Load Blockchain ABI and Address ---
# def load_blockchain_config():
#     try:
#         abi_path = blockchain_dir / "abi.json"
#         contract_path = blockchain_dir / "contract_address.txt"
        
#         with open(abi_path) as f:
#             abi = json.load(f)
        
#         with open(contract_path) as f:
#             address = f.read().strip()
            
#         return abi, address
#     except FileNotFoundError as e:
#         st.error(f"Blockchain configuration missing: {e}")
#         return None, None

# # --- HTML Header with Anime.js ---
# st.markdown("""
#     <html>
#     <head>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
#     <style>
#         .log-card {
#             background: rgba(0, 243, 255, 0.1);
#             padding: 15px;
#             border-radius: 8px;
#             margin: 10px 0;
#             border-left: 4px solid #00f3ff;
#         }
#         .card-0 { border-color: #00f3ff; }
#         .card-1 { border-color: #0066ff; }
#         .card-2 { border-color: #ff00aa; }
#     </style>
#     <script>
#       document.addEventListener('DOMContentLoaded', function() {
#         anime({
#           targets: 'h1',
#           translateY: [-20, 0],
#           opacity: [0, 1],
#           duration: 1500,
#           easing: 'easeOutExpo'
#         });
#       });
#     </script>
#     </head>
#     <body>
#     <h1>🧬 CRISPR gRNA Optimizer 🔐</h1>
#     </body>
#     </html>
# """, unsafe_allow_html=True)

# # --- Load Model ---
# @st.cache_resource
# def load_model():
#     try:
#         model_path = ai_model_dir / "model_weights.pt"
#         model = gRNA_GNN()
#         model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
#         model.eval()
#         return model
#     except Exception as e:
#         st.error(f"Failed to load model: {e}")
#         return None

# try:
#     from gnn_model import gRNA_GNN
#     model = load_model()
# except ImportError as e:
#     st.error(f"Model import error: {e}")
#     model = None

# # --- Sequence Encoding ---
# def one_hot_encode(seq):
#     mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'G': [0,0,1,0], 'C': [0,0,0,1]}
#     return [mapping.get(nuc, [0,0,0,0]) for nuc in seq]

# def make_graph(seq):
#     x = torch.tensor(one_hot_encode(seq), dtype=torch.float)
#     edge_index = [[i, i+1] for i in range(len(seq)-1)]
#     edge_index += [[i+1, i] for i in range(len(seq)-1)]
#     edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
#     return Data(x=x, edge_index=edge_index)

# # --- UI Inputs ---
# st.subheader("🧫 Input DNA Sequence & Target Gene")
# dna_input = st.text_input("Enter DNA sequence:", max_chars=100)
# gene_target = st.text_input("Target gene name:")

# # --- Metamask Component ---
# def show_metamask_component(seq, gene, score):
#     abi, address = load_blockchain_config()
#     if abi is None or address is None:
#         return

#     try:
#         component_path = webapp_dir / "metamask_component.html"
#         with open(component_path) as f:
#             html_str = f.read()
            
#         html_str = html_str.replace("{{contract_address}}", address)
#         html_str = html_str.replace("{{abi}}", json.dumps(abi))
#         html_str = html_str.replace("{{sequence}}", seq)
#         html_str = html_str.replace("{{gene}}", gene)
#         html_str = html_str.replace("{{score}}", str(int(score * 1000)))

#         components.html(html_str, height=300)
#     except Exception as e:
#         st.error(f"Failed to load MetaMask component: {e}")

# # --- Prediction Logic ---
# if st.button("Predict Optimal gRNAs") and model is not None:
#     if len(dna_input) < 20:
#         st.warning("Please enter at least 20 base pairs.")
#     else:
#         subseqs = [dna_input[i:i+20] for i in range(len(dna_input)-19)]
#         scored = []
#         for seq in subseqs:
#             graph = make_graph(seq)
#             with torch.no_grad():
#                 score = model(graph.unsqueeze(0)).item()
#             scored.append((seq, score))
#         top3 = sorted(scored, key=lambda x: x[1], reverse=True)[:3]

#         st.success("Top 3 Predicted gRNAs:")
#         for i, (g, s) in enumerate(top3, 1):
#             st.markdown(f"**{i}. {g}** — Score: {s:.3f}")
#             show_metamask_component(g, gene_target, s)
            
#             # Log to blockchain if available
#             try:
#                 from blockchain.log_results import log_to_chain
#                 log_to_chain(g, gene_target, round(s, 3))
#             except Exception as e:
#                 st.warning(f"Couldn't log to blockchain: {e}")

# # --- Blockchain Log Viewer ---
# st.markdown("---")
# st.subheader("📦 Blockchain Log Viewer")

# if st.button("View Stored gRNA Logs"):
#     try:
#         from blockchain.log_results import contract
#         total = contract.functions.getTotalEntries().call()
        
#         if total == 0:
#             st.info("No entries stored on-chain yet.")
#         else:
#             for i in reversed(range(total)):
#                 seq, gene, score, ts = contract.functions.getEntry(i).call()
#                 st.markdown(f"""
#                 <div class='log-card card-{i%3}'>
#                     <b>🔗 Entry #{i+1}</b><br>
#                     🧬 Sequence: <code>{seq}</code><br>
#                     🎯 Gene: <i>{gene}</i><br>
#                     📊 Score: {score/1000:.3f}<br>
#                     🕒 Timestamp: {ts}
#                 </div><br>
#                 """, unsafe_allow_html=True)
#     except Exception as e:
#         st.error(f"Failed to load blockchain logs: {e}")

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import json
from Bio.Seq import Seq
import torch
from torch_geometric.data import Data
import sys, os

# --- Fix import path ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from ai_model.gnn_model import gRNA_GNN
from blockchain.log_results import log_to_chain, contract

# --- Paths to static files ---
STATIC_DIR = os.path.join(os.path.dirname(__file__), "..", "webapp")
BLOCKCHAIN_DIR = os.path.join(os.path.dirname(__file__), "..", "blockchain")
ABI_PATH = os.path.join(BLOCKCHAIN_DIR, "abi.json")
ADDRESS_PATH = os.path.join(BLOCKCHAIN_DIR, "contract_address.txt")
METAMASK_HTML_PATH = os.path.join(STATIC_DIR, "metamask_component.html")

# --- HTML Header with Anime.js and Cyberpunk Styling ---
st.markdown(f"""
    <html>
    <head>
    <link rel="stylesheet" href="static/style.css">
    <script src="static/anime.min.js"></script>
    <script>
      window.onload = function() {{
        anime({{
          targets: 'h1',
          translateY: [-20, 0],
          opacity: [0, 1],
          duration: 1500,
          easing: 'easeOutExpo'
        }});
      }};
    </script>
    </head>
    <body>
    <h1>🧬 CRISPR gRNA Optimizer 🔐</h1>
    </body>
    </html>
""", unsafe_allow_html=True)

# --- Load Model ---
@st.cache_resource
def load_model():
    model = gRNA_GNN()
    model.load_state_dict(torch.load(os.path.join(BASE_DIR, "ai_model", "model_weights.pt"), map_location=torch.device("cpu")))
    model.eval()
    return model

model = load_model()

# --- Helpers ---
def one_hot_encode(seq):
    mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'G': [0,0,1,0], 'C': [0,0,0,1]}
    return [mapping.get(nuc, [0,0,0,0]) for nuc in seq]

def make_graph(seq):
    x = torch.tensor(one_hot_encode(seq), dtype=torch.float)
    edge_index = [[i, i+1] for i in range(len(seq)-1)]
    edge_index += [[i+1, i] for i in range(len(seq)-1)]
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
    return Data(x=x, edge_index=edge_index)

def show_metamask_component(seq, gene, score):
    with open(ABI_PATH) as f:
        abi = json.load(f)
    with open(ADDRESS_PATH) as f:
        address = f.read().strip()

    html_str = open(METAMASK_HTML_PATH).read()
    html_str = html_str.replace("{{contract_address}}", address)
    html_str = html_str.replace("{{abi}}", json.dumps(abi))
    html_str = html_str.replace("{{sequence}}", seq)
    html_str = html_str.replace("{{gene}}", gene)
    html_str = html_str.replace("{{score}}", str(int(score * 1000)))

    components.html(html_str, height=300)

# --- UI ---
st.subheader("🧫 Input DNA Sequence & Target Gene")
dna_input = st.text_input("Enter DNA sequence:", max_chars=100)
gene_target = st.text_input("Target gene name:")

if st.button("Predict Optimal gRNAs"):
    if len(dna_input) < 20:
        st.warning("Please enter at least 20 base pairs.")
    else:
        subseqs = [dna_input[i:i+20] for i in range(len(dna_input)-19)]
        scored = []
        for seq in subseqs:
            graph = make_graph(seq)
            with torch.no_grad():
                score = model(graph).item()
            scored.append((seq, score))
        top3 = sorted(scored, key=lambda x: x[1], reverse=True)[:3]
        st.success("Top 3 Predicted gRNAs:")
        for i, (g, s) in enumerate(top3, 1):
            st.markdown(f"**{i}. {g}** — Score: `{s:.3f}`")
            show_metamask_component(g, gene_target, s)
            log_to_chain(g, gene_target, round(s, 3))

# --- View Blockchain Logs ---
st.markdown("---")
st.subheader("📦 Blockchain Log Viewer")

if st.button("View Stored gRNA Logs"):
    total = contract.functions.getTotalEntries().call()
    if total == 0:
        st.info("No entries stored on-chain yet.")
    else:
        for i in reversed(range(total)):
            seq, gene, score, ts = contract.functions.getEntry(i).call()
            st.markdown(f"""
            <div class='log-card card-{i}'>
                <b>🔗 Entry #{i+1}</b><br>
                🧬 Sequence: <code>{seq}</code><br>
                🎯 Gene: <i>{gene}</i><br>
                📊 Score: {score/1000:.3f}<br>
                🕒 Timestamp: {ts}
            </div><br>
            """, unsafe_allow_html=True)

        st.markdown("""
        <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
        <script>
        document.addEventListener("DOMContentLoaded", function() {
            anime({
                targets: '.log-card',
                translateX: [-20, 0],
                opacity: [0, 1],
                delay: anime.stagger(150),
                easing: 'easeOutExpo'
            });
        });
        </script>
        """, unsafe_allow_html=True)
