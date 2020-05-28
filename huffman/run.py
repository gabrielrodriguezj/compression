#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for execute the compressing and decompressing using Huffman algorithm.
@author: gabrielrodriguezj
"""

from alphabet import Alphabet
from huffmantree import  HuffmanTree
from huffmancompressor import HuffmanCompressor
from huffmandecompressor import HuffmanDecompressor


forAlphabet = "what you see is what you get"
strText = "who is that"
strText = "what you see is what you ghetatttt"

alphabet = Alphabet(forAlphabet)
#print(alphabet.getAlphabetTable())

tree = HuffmanTree(alphabet)
#print(tree.getHuffmanCode())

huffman = HuffmanCompressor(tree)
huffman.compress(strText)
#print(huffman.getBinaryString())

huffman2 = HuffmanDecompressor(tree)
strDec = huffman2.decompress(huffman.getBinaryString())
print(strDec)
print(huffman.getBinaryString())

lst = huffman.getBytesRepresentation()
#for i in lst:
    #print(i)
    #print(i[0])

strDec2 = huffman2.decompressBytes(huffman.getBytesRepresentation())
print(strDec2)

print(strText)
          