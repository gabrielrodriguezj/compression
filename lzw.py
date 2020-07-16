#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for execute the compress and decompress strings using Huffman algorithm.
@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet

forAlphabet = "compadre no compro coco"

alphabet = Alphabet(forAlphabet, algorithm = "LZW")
print(alphabet.getAlphabetTable())


