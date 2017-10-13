import unittest

def userInput():
    user_input = str(input("Write in your sentence? "))
    return(user_input)
    # print(input_list_words(user_input))

# word_dict = {}
# def create_word_dict():
#     words = open("dictionary.txt", "r")
#     for line in words:
#         line = line.strip()
#         word_dict[line] = 1
#     words.close()

# def wordCheck(word):
#     word = word.lower()
#     if word in word_dict:
#         return True
#     else:
#         return False

# def userResult(wordList):
#     truecount = 0
#     badwords = []
#     if len(wordList)==1:
#         if wordCheck(wordList[0]):
#             truecount +=1
#         else:
#             badwords.append(wordList[0])
#     else:
#         for item in wordList:
#             if wordCheck(item):
#                 truecount +=1
#             else:
#                 badwords.append(item)
#     result = ''
#     badwords = str(badwords)
#     badpercentage = str((len(wordList)-truecount)/(len(wordList)))
#     result+=' '+'your incorrectly spelled words are: '+badwords+" your percentage of incorrectly spelled words is "+badpercentage
#     return (result)

# def input_list_words(user_input):
#     input_words = user_input.lower().split(" ")
#     return input_words

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(wordCheck("Happy"), True)
#     def test1(self):
#         self.assertEqual(wordCheck("Meg"), False)
#     def test2(self):
#         self.assertEqual(userResult(["thot", "ught", "ugh"]), "result" )
#     def test3(self):
#         self.assertEqual(userResult(["jkfsdl"]), 'jfjf')


def main():

    #userInput()

    myname = input("enter your name:")
    #return myname
    # create_word_dict()
    # mytest = MyTest()
    # mytest.test()
    # mytest.test1()
    # mytest.test2()
    # mytest.test3()

main()