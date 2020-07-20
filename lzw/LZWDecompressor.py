#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of the LZW descompressor

@author: gabrielrodriguezj
"""

from util.Alphabet import Alphabet
import copy

class LZWDecompressor:

    def __init__(self, alphabet, numBitsForCharacter):
        self._alphabet = copy.deepcopy(alphabet)
        self._inverseAlphabet = self._alphabet.getInverseAlphabet()
        self._numBitsForCharacter = numBitsForCharacter

    """
    Decompression of a String compressed with LZW algorithm
    """
    def decompress(self, binaryString): 
        strCode = ""
        codes = []
        for bite in binaryString:
            strCode = strCode + bite
            if len(strCode) == self._numBitsForCharacter:
                codes.append(self._binaryToInt(strCode))
                strCode = ""
        
        strDecompressed = ""
        
        """
        Here is the core of the LZW decompression algorithm. The 
        dictorionary(alphabet) in the compression step will be rebuilded,
        just having the initial alphanet(dictionary)
        """
        i = 0
        old_code = codes[i]
        character = self._translate(old_code)
        #print(old_code, " - ", character)
        strDecompressed = strDecompressed + character
        while i < len(codes) - 1:
            i = i + 1
            new_code = codes[i]
            
            if not self._isInDictionary(new_code):
                string = self._translate(old_code) + character
            else:
                string = self._translate(new_code)
            
            
            if string == Alphabet.END_STRING_CHARACTER:
                break
                
            #print(new_code, " - ", string)
            strDecompressed = strDecompressed + string 
            #Assign to character the first character of the variable string
            character = string[0]
            
            #Agregar Traducir(cód_viejo)+carácter al diccionario
            strAux = self._translate(old_code) + character
            intIndex = self._alphabet.insertElement(strAux)
            #self._inverseAlphabet = self._alphabet.getInverseAlphabet()
            self._inverseAlphabet[intIndex] = strAux #A faster
            
            old_code = new_code            
        return strDecompressed
            
        
    
    def _binaryToInt(self, strBinary):
        return int('0b' + strBinary, 2)
    
    def _translate(self, intCharacter):
        return self._inverseAlphabet[intCharacter]
    
    def _isInDictionary(self, intCharacter):
        return True if intCharacter in self._inverseAlphabet else False