#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:12:18 2020

@author: gabriel
"""

from alphabet import Alphabet
from huffmantree import  HuffmanTree
from huffmancompressor import HuffmanCompressor
from huffmandecompressor import HuffmanDecompressor


#strText = "what you see is what you get"
strText = "who is that"

alphabet = Alphabet(strText)
#print(alphabet.getAlphabetTable())

tree = HuffmanTree(alphabet)
#print(tree.getHuffmanCode())

huffman = HuffmanCompressor(tree)
huffman.compress(strText)
#print(huffman.getBinaryString())

huffman2 = HuffmanDecompressor(tree)
strDec = huffman2.decompress(huffman.getBinaryString())
print(strDec)

#print(huffman.getBytesRepresentation())

strDec2 = huffman2.decompressBytes(huffman.getBytesRepresentation())
print(strDec2)



"""huffman.compress("who is that")
strDec3 = huffman2.decompress(huffman.getBinaryString())
print(strDec3)
"""
          