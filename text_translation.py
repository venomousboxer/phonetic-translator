#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:07:40 2019

@author: venomousboxer
"""

import sys

mydict = {}

def buildDict() :
    sys.stdin = open("cmudict.txt","r")

    for line in sys.stdin:
    	line = line.strip()
    	if line.startswith(';'): continue
    	word, phones = line.split("  ")
    	mydict[word]=phones