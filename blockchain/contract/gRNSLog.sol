// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract gRNALog {
    struct Entry {
        string sequence;
        string gene;
        uint256 score; // Store scaled score (e.g., 95 for 0.95)
        uint256 timestamp;
    }

    Entry[] public entries;

    function storeEntry(string memory _seq, string memory _gene, uint256 _score) public {
        entries.push(Entry(_seq, _gene, _score, block.timestamp));
    }

    function getEntry(uint256 index) public view returns (string memory, string memory, uint256, uint256) {
        Entry storage e = entries[index];
        return (e.sequence, e.gene, e.score, e.timestamp);
    }

    function getTotalEntries() public view returns (uint256) {
        return entries.length;
    }
}
