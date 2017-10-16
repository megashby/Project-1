import unittest

def userInput():
    user_input = ""
    while user_input == "":
            user_input = str(input("Write in your sentence? "))
            user_input=user_input.strip()
    input_list_words(user_input)
    #print (user_input)

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
    #print(wordList)
    truecount = 0
    badwords = []
    if len(wordList)==1:
        if wordCheck(wordList[0]):
            truecount +=1
        else:
            badwords.append(wordList[0])
    else:
        for item in wordList:
            if wordCheck(item):
                truecount +=1
            else:
                badwords.append(item)
    result = ''
    #print (badwords)
    badwords = str(badwords)
    badpercentage = ((len(wordList)-truecount)/(len(wordList)))
    badpercentage = str(round(badpercentage, 2))
    result='your incorrectly spelled words are: '+badwords+" your percentage of incorrectly spelled words is "+badpercentage
    print(result)
    return (result)

def input_list_words(user_input):
    input_words = user_input.lower().split(" ")
   #print(input_words)
    #return (input_words)
    userResult(input_words)
    return input_words

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(wordCheck("Happy"), True)
    def test1(self):
        self.assertEqual(wordCheck("Meg"), False)
    def test2(self):
        self.assertEqual(userResult(["thot", "ught", "ugh"]), "your incorrectly spelled words are: ['thot', 'ught'] your percentage of incorrectly spelled words is 0.67")
    def test3(self):
        self.assertEqual(userResult(["jkfsdl"]), "your incorrectly spelled words are: ['jkfsdl'] your percentage of incorrectly spelled words is 1.0")
    def test4(self):
        self.assertEqual(userResult(['hello', 'can']), "your incorrectly spelled words are: [] your percentage of incorrectly spelled words is 0.0")
    def test5(self):
        self.assertEqual(input_list_words("I like corn"), ['i', 'like', 'corn'])
    #Testing input_list_words
    def test_InputListWords_negative(self):
        self.assertNotEqual(input_list_words("hello"),["hello", "world"], "Test FAILED: actual should not equal expected")
        print("test_InputListWords_negative PASS")
    def test_InputListWords_postive(self):
        self.assertEqual(input_list_words("hello WoRld"),["hello", "world"], "Test FAILED: actual should equal  Expected")
        print("test_InputListWords_negative PASS")
    def test_InputListWords_postive_len(self):
        self.assertEqual(len(input_list_words("hello WoRld")),2, "Test FAILED: actual should equal  Expected")
        print("test_InputListWords_positve_len PASS")
    def test_InputListWords_positive_notAWord(self):
        self.assertEqual(input_list_words("sSG !234Sg ss"),["ssg", "!234sg","ss"], "Test FAILED: actual should equal  Expected")
        print("test_InputListWords_positive_notAWord PASS")
def main():
    create_word_dict()
    userInput()
    mytest = MyTest()
    #mytest.test()
    #mytest.test1()
    #mytest.test2()
    #mytest.test3()
    #mytest.test4()
    #mytest.test5()

    mytest.test_InputListWords_negative()
    mytest.test_InputListWords_postive()
    mytest.test_InputListWords_postive_len()
    mytest.test_InputListWords_positive_notAWord()


main()
