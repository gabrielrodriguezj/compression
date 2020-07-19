#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for execute the compress and decompress strings using Huffman algorithm.
@author: gabrielrodriguezj
"""

from lzw.LZWCompressor import LZWCompressor
from lzw.LZWDecompressor import LZWDecompressor

forAlphabet = "compadre no compro coco"
compressor = LZWCompressor(forAlphabet)

(binaryString, alphabet, numBitsForCharacter) = compressor.compress()

#print(binaryString)
#print(alphabet.getAlphabetTable())
#print(numBitsForCharacter)

decompressor = LZWDecompressor(binaryString, alphabet, numBitsForCharacter)
strDecompressed = decompressor.decompress()
print(strDecompressed)


