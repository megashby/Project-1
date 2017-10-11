#Function to check words against dictionary


def wordCheck(word):
    if word in wordList:
        return True
    else:
        return False


def userResult(wordList):
    truecount = 0
    badwords = []
    for item in wordList:
        if wordCheck(item):
            truecount +=1
        else:
            badwords.append(word)
    result = ''
    badwords = str(badwords)
    badpercentage = str((len(wordList)-truecount)/(len(wordList))
    result+' '+'your incorrectly spelled words are: '+badwords+" your percentage of incorrectly spelled words is "+badpercentage
    return (result)
