# 🧬 CRISPR-AI: Web3-Enhanced gRNA Optimizer

A futuristic cyberpunk DApp that combines **AI**, **synthetic biology**, and **blockchain** to design and store **high-efficiency CRISPR guide RNAs (gRNAs)** with **zero off-target risks**.

> Powered by: Deep Learning + GNNs | Streamlit | Solidity | Metamask | Anime.js

![Deploy to Streamlit](https://img.shields.io/badge/Deploy-Streamlit-blueviolet?logo=streamlit)
![Polygon Mumbai](https://img.shields.io/badge/Blockchain-Polygon_Mumbai-purple?logo=ethereum)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python)

---

## 🚀 Features

- 🔍 **Input a DNA sequence and gene** — receive AI-predicted top 3 gRNAs.
- 📈 **Visualize** off-target risk and efficiency scores.
- 🔗 **Record gRNA results on-chain** via Metamask (Polygon Mumbai).
- 🧾 **Real-time dashboard** for gene frequency, top scorers, and submission analytics.
- 🧬 Streamlined interface with **cyberpunk-themed animation** (anime.js).

---

## 🧠 Tech Stack

| Layer       | Tech                                |
|------------|-------------------------------------|
| Frontend    | Streamlit, HTML, CSS, JS, Anime.js |
| Backend     | PyTorch, Biopython, GNN inference  |
| Blockchain  | Solidity, Web3.py, Metamask        |
| Hosting     | GitHub Pages / Vercel + Streamlit  |

---

## 🎥 Walkthrough

<img src="static/images/demo.gif" width="100%" alt="App Demo"/>

---

## 🧪 Sample Input

```text
DNA Sequence: ACGTAGCTAGCATGCTACGTAGC
Target Gene:   BRCA1
```

Returns:

```
1. gRNA: TAGCATGCTACG — Score: 0.921
2. gRNA: GTAGCTAGCATA — Score: 0.879
3. gRNA: CGTAGCTAGCAT — Score: 0.861
```

---

## 📦 Install & Run Locally

```bash
git clone https://github.com/your-username/crispr-ai-dapp.git
cd crispr-ai-dapp
bash run.sh
```

Make sure you have:
- Python 3.9+
- Metamask (browser extension)
- Node.js (for contract deployments if needed)

---

## 📊 Dashboard View

<img src="static/images/dashboard-preview.png" width="100%" />

---

## 🔗 Blockchain

- Chain: Polygon Mumbai
- Contract: `0xYourDeployedContractAddress`
- ABI: stored in `blockchain/abi.json`

---

## 🔐 Metamask Integration

- Auto-signs transaction with gRNA data
- Shows "Transaction Complete ✅" message
- Full login/auth + wallet address shown

---

## 🧠 Model Training

```bash
# Training from CRISPR open dataset
python model/train.py
```

---

## ✅ Deployment Checklist

| Step | Description |
|------|-------------|
| ✅   | Train GNN model + export inference script |
| ✅   | Deploy Solidity smart contract to Mumbai |
| ✅   | Store contract address + ABI |
| ✅   | Create Streamlit UI (Metamask-ready) |
| ✅   | Add anime.js animations + CSS |
| ✅   | Build dashboard page |
| ✅   | Push to GitHub |
| 💜   | Deploy Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud) |
| 💜   | Deploy frontend (metamask component + HTML) on [Vercel](https://vercel.com/) |
| 💜   | Announce 🚀 on Twitter / DevPost / BioHackathon |

---

## 🤝 Contributing

Pull requests are welcome! Here's how to get involved:

1. Fork the repo
2. Create a new branch: `git checkout -b feature-new`  
3. Commit your changes: `git commit -m 'add cool feature'`  
4. Push to the branch: `git push origin feature-new`  
5. Open a Pull Request

For major changes, open an issue first to discuss what you want to change. Contributions welcome from biohackers, devs, and designers!

---

## 🙌 Credits

- Open gRNA Efficiency Data: [CRISPR Knockout Consortium](https://github.com/CRISPR)
- Animation Engine: [anime.js](https://animejs.com)
- Blockchain Infra: [Polygon Mumbai](https://mumbai.polygonscan.com/)
- Made with ❤️ in Python + Web3

---

## 📜 License

MIT License — use it, remix it, extend it for your own research!

