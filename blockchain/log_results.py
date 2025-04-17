# import json
# from web3 import Web3

# # --- Auto-load ABI and Contract Address ---
# with open("blockchain/abi.json", "r") as f:
#     abi = json.load(f)

# with open("blockchain/contract_address.txt", "r") as f:
#     contract_address = f.read().strip()

# # --- Connect to Ganache / Custom Network ---
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# w3.eth.default_account = w3.eth.accounts[0]

# contract = w3.eth.contract(address=contract_address, abi=abi)

# # --- Function to log results ---
# def log_to_chain(sequence, gene, score):
#     scaled_score = int(score * 1000)
#     tx = contract.functions.storeEntry(sequence, gene, scaled_score).transact()
#     receipt = w3.eth.wait_for_transaction_receipt(tx)
#     print(f"✅ Logged on-chain: {sequence} ({gene}) → {score:.3f}")
#     return receipt

import json
from web3 import Web3
import os

# --- Paths relative to this file's directory ---
base_dir = os.path.dirname(__file__)
abi_path = os.path.join(base_dir, "abi.json")
address_path = os.path.join(base_dir, "contract_address.txt")

# --- Load ABI ---
with open(abi_path, "r") as f:
    abi = json.load(f)

# --- Load contract address ---
with open(address_path, "r") as f:
    contract_address = f.read().strip() 

# --- Connect to Ganache or Local Ethereum Node ---
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]

# --- Create Contract Instance ---
contract = w3.eth.contract(address=contract_address, abi=abi)

# --- Function to log results to blockchain ---
def log_to_chain(sequence, gene, score):
    scaled_score = int(score * 1000)  # scale to int if Solidity expects uint
    tx = contract.functions.recordEntry(sequence, gene, scaled_score).transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    print(f"✅ Logged on-chain: {sequence} ({gene}) → {score:.3f}")
    return receipt
