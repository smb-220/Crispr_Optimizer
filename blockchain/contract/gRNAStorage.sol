// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract gRNAStorage {
    struct gRNAEntry {
        string sequence;
        string gene;
        uint timestamp;
        uint8 score;
    }

    gRNAEntry[] public entries;

    function storeEntry(string memory _seq, string memory _gene, uint8 _score) public {
        entries.push(gRNAEntry(_seq, _gene, block.timestamp, _score));
    }

    function getCount() public view returns (uint) {
        return entries.length;
    }
}
