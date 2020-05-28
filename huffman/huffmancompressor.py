#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gabrielrodriguezj
"""

class HuffmanCompressor:
    LENGTH_CHARACTER_BITS = 8; #8 bits for encoding and decoding.
    
    def __init__(self, huffmanTree):
            self._mapCodeHuffman = huffmanTree.getHuffmanCode()
    
        
    def compress(self, strToCompress):
        strToCompress = strToCompress
        self._lstBytesCompress = []
        
        self._strBinary = ""
        for symbol in strToCompress:
            self._strBinary = self._strBinary + self._mapCodeHuffman[symbol]
        
        """
        Convert the 1 and 0 of self._strBinary to a valid string, this means
        take LENGTH_CHARACTER_BITS elements and turn them it from to a binary 
        code to a decimal code.
        """
        #intBits = math.ceil(len(self._strBinary) / self.LENGTH_CHARACTER_BITS)
        strBits = ""
        for bit in self._strBinary:
            strBits = strBits + bit
            if len(strBits) == self.LENGTH_CHARACTER_BITS:
                self._lstBytesCompress.append(self._bitstring_to_bytes(strBits))
                strBits = ""
        
        #If Some part of the self._strBinary was not processed       
        if not strBits == "":
            self._lstBytesCompress.append(self._bitstring_to_bytes(strBits.zfill(self.LENGTH_CHARACTER_BITS)))
        
    def getBinaryString(self):
        return self._strBinary
    
    def getBytesRepresentation(self):
        return self._lstBytesCompress
        
    def _bitstring_to_bytes(self, strBinary):
        return int(strBinary, 2).to_bytes(len(strBinary) // self.LENGTH_CHARACTER_BITS, byteorder='big')
    
