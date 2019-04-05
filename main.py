#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:07:40 2019

@author: venomousboxer
"""

import speech_recognition as sr
from text_translation import mydict
from text_translation import buildDict


def convert(word):
    for ch in word :
        if ch.isdigit() :
            word=word.replace( ch , '' )
    return word

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Start saying something")
    audio=r.listen(source)
    print("Time over thanks")
    
try :
    text = r.recognize_google(audio)
    print("Text : "+ text)
    
except:
    pass;
    
buildDict()
words = list()
newText = ''
newtext2 = ''
words = text.split()
#print(mydict)
for word in words :
    word = word.upper()
    print(word)
    if word in mydict.keys():
        newText += '  ' + mydict[word]
        newtext2 += ' . ' + convert(mydict[word])
    else :
        newText = newText + ' . ?'
        newtext2 = newtext2 + ' . ?'
#print(newText)
print(newtext2)