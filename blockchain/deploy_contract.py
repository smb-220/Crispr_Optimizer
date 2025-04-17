from solcx import compile_standard, install_solc
from web3 import Web3
import json
import os

install_solc("0.8.0")

# --- Solidity Contract ---
contract_source_code = '''
pragma solidity ^0.8.0;

contract gRNALog {
    struct Entry {
        string sequence;
        string gene;
        float score;
    }

    Entry[] public entries;

    function storeEntry(string memory _seq, string memory _gene, float _score) public {
        entries.push(Entry(_seq, _gene, _score));
    }

    function getEntry(uint i) public view returns (string memory, string memory, float) {
        Entry storage e = entries[i];
        return (e.sequence, e.gene, e.score);
    }

    function totalEntries() public view returns (uint) {
        return entries.length;
    }
}
'''

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"gRNALog.sol": {"content": contract_source_code}},
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    }
}, solc_version="0.8.0")

# --- Save ABI ---
abi = compiled_sol['contracts']['gRNALog.sol']['gRNALog']['abi']
bytecode = compiled_sol['contracts']['gRNALog.sol']['gRNALog']['evm']['bytecode']['object']

with open("abi.json", "w") as f:
    json.dump(abi, f)

# --- Connect to Ganache ---
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]

# --- Deploy Contract ---
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("✅ Contract deployed at:", tx_receipt.contractAddress)

# Save address to file
with open("contract_address.txt", "w") as f:
    f.write(tx_receipt.contractAddress)

# Ensure the appropriate Solidity compiler version is installed
install_solc('0.8.17')

# Connect to Polygon Mumbai (or your preferred network)
w3 = Web3(Web3.HTTPProvider("https://rpc-mumbai.maticvigil.com"))
w3.eth.defaultAccount = w3.eth.accounts[0]

# Load the contract code (replace with your contract path)
with open('blockchain/contracts/gRNALog.sol', 'r') as file:
    contract_source_code = file.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "gRNALog.sol": {
            "content": contract_source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode"]
            }
        }
    }
})

# Get ABI and Bytecode
abi = compiled_sol['contracts']['gRNALog.sol']['gRNALog']['abi']
bytecode = compiled_sol['contracts']['gRNALog.sol']['gRNALog']['evm']['bytecode']['object']

# Set up the contract
gRNA_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy the contract
tx_hash = gRNA_contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Get the contract address
contract_address = tx_receipt['contractAddress']

# Save the contract address to the contract_address.txt file
with open('blockchain/contract_address.txt', 'w') as f:
    f.write(contract_address)

print(f"Contract deployed successfully at address: {contract_address}")