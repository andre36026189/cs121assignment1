import re
import sys
# print(sys.argsv)

def tokenize(text):
    #takes in a filepath and tokenzies the content
    #time complexity = O(n): goes thru all items once 
    text1 = ""
    with open(text,'r') as f:
        text1 = f.read()
        texts = (text1.split()).replace("\n"," ")

    rlist = [] 
    # the list containing the tokens
    # [turned into lower case,disposed of unneccesarry info such as apostrophes/hyphens/potentially quotemarks] that we will return
    for i in texts:
        i = (i.lower())
        if not re.match('[a-zA-Z0-9]', i[-1]):
            i = i[:-1]
        if '-' in i or "'" in i: #handling hypens
            for x in i.split('-'):
                if re.match('[a-zA-Z0-9]', x):
                    rlist.append(x)
                    print(x)
        elif re.match('[a-zA-Z0-9]', i): #if doesnt have hyphen just split
            rlist.append(i)
            print(i)
    return rlist

def computewordfrequencies(rlist): 
    #counts the number of times a word occurs in a tokenized list
    #returns a dictionary with keys(the word) and value(the number of times the word appears in the tokenized list)
    #O(N) goes thru all elements once
    dict = {}
    for i in rlist:
        # print(rlist.count(i))
        if i in dict.keys():
            pass
        else:
            dict[i] = rlist.count(i)
    # print(dict)
    return dict

def printword(dict):
    #take in the dictionary that was returned from computewordfrequencies and prints out a formatted output
    #O(N) goes thru all elements once only
    for k,v in dict.items():
        print(k + " - " + str(v) )


    

printword(computewordfrequencies(tokenize(sys.argv[1])))


