#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gabrielrodriguezj
"""

class HuffmanDecompressor:
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
            
            #The last byte could not be of size 8, and this avoid the left pad
            #with unnecesarys 0's
            if i == size - 1:
                strBytes = strBytes + bin(byte[0])[2:]
            else:
                strBytes = strBytes + '{0:08b}'.format(byte[0])
            """
            In previous line is needed implement the constant LENGTH_CHARACTER_BITS,
            also implement that constant just in one class, not in two as is now
            """
        return self.decompress(strBytes)
    
    


