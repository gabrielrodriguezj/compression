#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of the LZW descompressor

@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet

class LZWDecompressor:

    def __init__(self, binaryString, alphabet, numBitsForCharacter):
        self._binaryString = binaryString
        self._inverseAlphabet = alphabet.getInverseAlphabet()
        self._numBitsForCharacter = numBitsForCharacter

    """
    Decompression of a String compressed with LZW algorithm
    """
    def decompress(self): 
        strDecompressed = ""
        strCode = ""
        for bite in self._binaryString:
            strCode = strCode + bite
            if len(strCode) == self._numBitsForCharacter:
                character = self._inverseAlphabet.get(self._binaryToInt(strCode), "")
                
                if character == Alphabet.END_STRING_CHARACTER:
                    break
                
                strDecompressed = strDecompressed + character
                strCode = ""
                
        return strDecompressed
            
        
    
    def _binaryToInt(self, strBinary):
        return int('0b' + strBinary, 2)