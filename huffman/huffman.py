#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gabriel
"""

class HuffmanCompressor:
    def __init__(self, huffmanTree):  
            self._length_character_bits = 8; #8 bits for encoding and decoding.
            self._end_string = int(36); #Character for end of the string to compress
            self._mapCodeHuffman = huffmanTree.
    
        
    def compress(self, strToCompress):
        string = strToCompress + self._end_string
        
        
        """
        Step one: Determite how often each character appears.
        """
        frecuencyTable = {}
        for char in string:
            intCount = frecuencyTable.get7(char, 0) #If char does not exist retunr 0
            frecuencyTable[char, intCount + 1]
        
        """
        Step two: Sort the frecuency table by the frecuency
        """
        lstSorted = sorted(frecuencyTable.items(), key=lambda x: x[1])
        
        """
        Step three: Cpnvert each character and 
            """