#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for execute the compress and decompress strings using Huffman algorithm.
@author: gabrielrodriguezj
"""

from lzw.LZWCompressor import LZWCompressor

forAlphabet = "compadre no compro coco"
compressor = LZWCompressor(forAlphabet)

(compressedString, alphabet, numBitsForCharacter) = compressor.compress()

print(compressedString)
print(alphabet.getAlphabetTable())
print(numBitsForCharacter)



