import os
import json

FILE = 'data/dictionary.json'
FILE2 = 'data/simple_english_dictionary.json'
FILECUSTOM = 'data/custom_dictionary.json'

readFile = json.load(open(FILE))
readFile2 = json.load(open(FILE2))
try:
    readFileCustom = json.load(open(FILECUSTOM))
except FileNotFoundError:
    readFileCustom = json.load(open(FILECUSTOM,'a'))
    

def searchWord(searchTerm):
    
    return readFile.get(f'{searchTerm.upper()}'), readFile2.get(f'{searchTerm.lower()}')


def searchCustom(searchTerm):
    
    return readFileCustom.get(f'{searchTerm.upper()}')


def putCustom(word, defn):
    data = {word:defn}
    with open(FILECUSTOM, 'r+') as file:
        fileData = json.load(file)
        
        fileData.update(data)
        file.seek(0)
        json.dump(fileData, file, indent=4)
    return 201
