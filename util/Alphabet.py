#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Take a text and convert this text in a table (represented in a list) with
symbols and probabilitie of every symbols

@author: gabrielrodriguezj
"""


class Alphabet:
    
    END_STRING_CHARACTER = chr(36)
    
    def __init__(self, source, algorithm = "HUFFMAN"):
        
        #If the source is text
        if type(source) == type(""):
            
            if algorithm == "HUFFMAN":
                source = source + self.END_STRING_CHARACTER
                """
                Determite how often each character appears.
                """
                strtext = source
                frecuencyTable = {}
                for char in strtext:
                    intCount = frecuencyTable.get(char, 0) #If char does not exist return 0
                    frecuencyTable[char] = intCount + 1
            
                """
                Sort the frecuency table by the frecuency
                """
                lstSorted = sorted(frecuencyTable.items(), key=lambda x: x[1])
                
                """
                Calculate the probability of every element
                Pending, is not strictly neccesary
                """
                self._alphabetTable = lstSorted
            
            elif algorithm == "LZW":
                i = 0
                self._alphabetTable = {}
                for char in source:                    
                    if char not in self._alphabetTable:
                        self._alphabetTable[char] = i  
                        i = i + 1
                        
    """
    Return a sorted list with the symbols and their probability
    """
    def getAlphabetTable(self):
        return self._alphabetTable