import partA
import sys 

def partB(f1,f2):
    #finds the integer count of both file path's identical key's from the dictionarys
    #O(N) goes thru all only once
    count = 0 
    d1ct= partA.computewordfrequencies(partA.tokenize(f1))
    d2ct= partA.computewordfrequencies(partA.tokenize(f2))

    d1ctkeys = list(d1ct.keys()) 
    d2ctkeys = list(d2ct.keys()) 
    for i in d1ctkeys:
        if i in d2ctkeys:
            count += 1

    return count

f1 = sys.argv[1]
f2 = sys.argv[2]
partB(f1,f2)