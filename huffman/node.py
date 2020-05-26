#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: gabrielrodriguezj
"""


class Node:        
    def __init__(self, param1, param2):
        if type(param1) == type(""):
            self._symbol = param1
            self._probability = param2
            self._left = None
            self._right = None
        
        if type(param1) == type(param2) == type(self):
            self._symbol = None
            self._probability = param1.getProbability() + param2.getProbability()
            self._left = param1
            self._right = param2
    
    def setLeftNode(self, node):
        self._left = node
    
    def setRightNode(self, node):
        self._right = node
        
    def getLeftNode(self):
        return self._left
    
    def getRightNode(self):
        return self._right
    
    def getSymbol(self):
        return self._symbol
    
    def getProbability(self):
        return self._probability
    
    def __lt__(self, other):
        return self._probability < other._probability
    
    """
    __lt__(self, other):
    __le__(self, other):
    __eq__(self, other):
    __ne__(self, other):
    __ge__(self, other):
    __gt__(self, other):
    """
        