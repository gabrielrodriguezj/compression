#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for execute the compress and decompress strings using Huffman algorithm.
@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet
from lzw.LZWCompressor import LZWCompressor
from lzw.LZWDecompressor import LZWDecompressor

#forAlphabet = "compadre no compro coco"
forAlphabet = "BBBBBBNBBBBNBBBBNNNBBBBBB"

alphabet = Alphabet(forAlphabet, algorithm = "LZW")

compressor = LZWCompressor(alphabet)
(binaryString, numBitsForCharacter) = compressor.compress(forAlphabet)

#print(binaryString)
#print(numBitsForCharacter)

decompressor = LZWDecompressor(alphabet, numBitsForCharacter)
strDecompressed = decompressor.decompress(binaryString)
print(strDecompressed)
if strDecompressed == forAlphabet:
    print("Ok")
else:
    print("BAD")

