#Function to check words against dictionary

import unittest

word_dict = {}
def create_word_dict():
    words = open("dictionary.txt", "r")
    for line in words:
        line = line.strip()
        word_dict[line] = 1
    words.close()

def wordCheck(word):
    word = word.lower()
    if word in word_dict:
        return True
    else:
        return False


def userResult(wordList):
    truecount = 0
    badwords = []
    for item in word_dict:
        if wordCheck(item):
            truecount +=1
        else:
            badwords.append(word)
    result = ''
    badwords = str(badwords)
    badpercentage = str((len(word_dict-truecount)/(len(word_dict))))
    #result+=' '+'your incorrectly spelled words are: '+badwords+" your percentage of incorrectly spelled words is "+badpercentage
    #return (result)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(wordCheck("Happy"), True)
    def test1(self):
        self.assertEqual(wordCheck("Meg"), False)

def main():
    create_word_dict()
    mytest = MyTest()
    mytest.test()
    mytest.test1()
main()