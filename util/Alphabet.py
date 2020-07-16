#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Take a text and convert this text in a table (represented in a list) with
symbols and probabilitie of every symbols

@author: gabrielrodriguezj
"""


class Alphabet:
    
    END_STRING_CHARACTER = chr(36)
    
    def __init__(self, source):
        
        source = source + self.END_STRING_CHARACTER
        """
        Determite how often each character appears.
        """
        
        #If the source is text
        if type(source) == type(""):
            strtext = source
            frecuencyTable = {}
            for char in strtext:
                intCount = frecuencyTable.get(char, 0) #If char does not exist retunr 0
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
    
    """
    Return a sorted list with the symbols and their probability
    """
    def getAlphabetTable(self):
        return self._alphabetTable