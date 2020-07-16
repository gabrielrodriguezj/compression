#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet

class HuffmanDecoder:
    LENGTH_CHARACTER_BITS = 8; #8 bits for encoding and decoding.
    
    def __init__(self, huffmanTree):
            self._mapInverseCodeHuffman = huffmanTree.getInverseHuffmanCode()
            self._intMaxSizeCode = huffmanTree.getMaxSizeCode()
            
            
    def decompress(self, strBinaryToDecompress):
        strDecodified = ""
        strCode = ""
        for bite in strBinaryToDecompress:
            strCode = strCode + bite
            character = self._mapInverseCodeHuffman.get(strCode, "")
            
            #If found end of string
            if character == Alphabet.END_STRING_CHARACTER:
                break
            if not character == "":
                strCode = ""
                strDecodified = strDecodified + character
        
        return strDecodified
    
    """
    Receive a list of bytes
    """
    def decompressBytes(self, lstBytesCompress):
        strBytes = ""
        size = len(lstBytesCompress)
        for i in range(size):
            byte = lstBytesCompress[i]
            
            #strBytes = strBytes + bin(byte[0])[2:]
            strBytes = strBytes + '{0:08b}'.format(byte[0])
            """
            In previous line is needed implement the constant LENGTH_CHARACTER_BITS,
            also implement that constant just in one class, not in two as is now
            """
        return self.decompress(strBytes)
    
    


