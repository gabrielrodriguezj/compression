#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of the LZW compression algorithm

@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet
import math

class LZWCompressor:
    
    LENGTH_CHARACTER_BITS = 8; #8 bits for encoding and decoding.
    
    def __init__(self, source):
        self._source = source
        
        
    def compress(self):
        
        self._alphabet = Alphabet(self._source, algorithm = "LZW")
        self._source =  self._source + Alphabet.END_STRING_CHARACTER
        
        lstOutput = []        
        w = ""
        for k in  self._source:
            wk = w + k
            if wk in self._alphabet.getAlphabetTable():
                w = wk
            else:
                self._alphabet.insertElement(wk)
                #print(w, "-", self._alphabet.getAlphabetTable()[w])
                lstOutput.append(self._alphabet.getAlphabetTable()[w])
                w = k
        #print(w, "-", self._alphabet.getAlphabetTable()[w])
        #print(self._alphabet.getAlphabetTable())
        lstOutput.append(self._alphabet.getAlphabetTable()[w])
        
        """
        Calculate the number of bits needed for representing every character
        from the alphabet
        """
        self._numBits = math.ceil(math.log(self._alphabet.getAlphabetLength(), 2))
        
        """
        Convert the output of the lzw algorithm in a string with 1 and 0s
        """
        self._strBinary = ""
        for char in lstOutput:
            #left padding witj 0
            self._strBinary = self._strBinary + self._decimalToBinary(char, self._numBits)
        #print(strBits)
        
        """
        Process strBits: take 8 bits and convert it in a byte. This step and 
        the previous one could be together in a single step.
        """
        self._lstBytesCompress = []
        strBits = ""
        for bit in self._strBinary:
            strBits = strBits + bit
            if len(strBits) == self.LENGTH_CHARACTER_BITS:
                self._lstBytesCompress.append(self._bitstring_to_bytes(strBits))
                strBits = ""
        
        #If Some part of the self._strBinary was not processed       
        if not strBits == "":
            #Complete with LENGTH_CHARACTER_BITS adding 0 to the right 
            self._lstBytesCompress.append(self._bitstring_to_bytes(strBits.ljust(self.LENGTH_CHARACTER_BITS, '0')))
        
        return (self.getBinaryString(), self.getAlphabet(), self.getNumBitsRepresentsCharacter())
        #return (self.getBytesRepresentation(), self.getAlphabet(), self.getNumBitsRepresentsCharacter())
    
    """
    Convert a string with 1 and 0 in the decimal representation
    """
    def _bitstring_to_bytes(self, strBinary):
        return int(strBinary, 2).to_bytes(len(strBinary) // self.LENGTH_CHARACTER_BITS, byteorder='big')
    
    """
    Convert a decimal to binary and the applies a padding left
    """
    def _decimalToBinary(self, intDecimal, padLeft = 0):
        if padLeft == 0:
            return "{0:b}".format(intDecimal)
        else:
            strBinary = "{0:b}".format(intDecimal)
            strBinary = strBinary.rjust(padLeft, '0')
            return strBinary
    
    def getNumBitsRepresentsCharacter(self):
        return self._numBits
    
    def getBinaryString(self):
        return self._strBinary
    
    def getBytesRepresentation(self):
        return self._lstBytesCompress
    
    def getAlphabet(self):
        return self._alphabet
    