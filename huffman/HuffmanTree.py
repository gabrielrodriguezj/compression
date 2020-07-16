#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gabriel
"""
from huffman.Node import Node
from queue import PriorityQueue

class HuffmanTree:
    
    def __init__(self, alphabet):
        self._intMaxSizeCode = int(0)
        
        #Create the alphabet table in a priority queue
        pq = PriorityQueue()
        for element in alphabet.getAlphabetTable():
            pq.put((element[1], Node(element[0], element[1])))
        
        
        while pq.qsize() > 1:
            nodeLeft = pq.get()[1]
            nodeRight = pq.get()[1]
            
            nodeNew = Node(nodeLeft, nodeRight)
            pq.put((nodeNew.getProbability(), nodeNew))
        
        #The last node in the pq contains all the three
        self._nodeRoot = pq.get()[1]
        
        #Get the huffman code table
        strHuffmanCode = ""
        mapHuffmanCode = {}
        mapHuffmanCodeInverse = {}
        self._preorder(self._nodeRoot, strHuffmanCode, mapHuffmanCode, mapHuffmanCodeInverse)
        self._mapHuffmanCode = mapHuffmanCode
        self._mapHuffmanCodeInverse = mapHuffmanCodeInverse
        
    """
    Returns the map with every symbols and its corresponding huffman code
    """
    def getHuffmanCode(self):
        return self._mapHuffmanCode
    
    def getInverseHuffmanCode(self):
        return self._mapHuffmanCodeInverse
    
    def _preorder(self, nodeRoot, strHuffmanCode, mapHuffmanCode, mapHuffmanCodeInverse):
        nodeLeft = nodeRoot.getLeftNode()
        if nodeLeft is not None:
            self._preorder(nodeLeft, strHuffmanCode + "0", mapHuffmanCode, mapHuffmanCodeInverse)        
        
        nodeRight = nodeRoot.getRightNode()
        if nodeRight is not None:
            self._preorder(nodeRight, strHuffmanCode + "1", mapHuffmanCode, mapHuffmanCodeInverse)
        
        if nodeLeft is None and nodeRight is None:
            mapHuffmanCode[nodeRoot.getSymbol()] = strHuffmanCode   
            mapHuffmanCodeInverse[strHuffmanCode] = nodeRoot.getSymbol()
            
            if len(nodeRoot.getSymbol()) > self._intMaxSizeCode:
                self._intMaxSizeCode = len(nodeRoot.getSymbol())
    
    def getMaxSizeCode(self):
        return self._intMaxSizeCode