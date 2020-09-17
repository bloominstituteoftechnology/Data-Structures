ar = [1,2,3,3,4]

def sumAnArray(ar):
    theSum = 0
    for i in ar:
        theSum = theSum + ar[i]
    print(theSum)
    return theSum
