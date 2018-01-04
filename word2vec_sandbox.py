# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:30:49 2018

@author: Derek
"""



import gensim, pandas as pd



def getData(path):
    """Load in data from Excel into a Pandas dataframe for analysis"""
    xl = pd.ExcelFile(path)
    return xl.parse("Sheet1") 


def buildSentences(df, textColumn):
    """Word2Vec takes in lists of lists, where the inner most list can
    be thought of as a bag of words representing a sentence - this constructs
    that data structure from the dataframe df"""
    sentences = []
    
    for description in df[textColumn].values:
        descriptions_split = description.replace('?', '.').replace('!', '.').split('.')
        
        for sentence in descriptions_split:
            sentences.append(sentence.split(' '))
            
    return sentences


def buildModel(sentences, minCount, _window):
    """Builds the model"""
    return gensim.models.Word2Vec(sentences, min_count = minCount, window = _window)



if __name__ == '__main__':
    path = "*your path here*"
    dataFrame = getData(path)
    textColumn = 'Description'
    IDField = 'Name'
    minCount = 1
    _window = 3
    
    model = buildModel(buildSentences(dataFrame, textColumn), minCount, _window)
