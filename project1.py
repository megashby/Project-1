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
    #badwords = str(badwords)
    badpercentage = ((len(wordList)-truecount)/(len(wordList)))
    badpercentage = str(round(badpercentage, 2))
    result='your incorrectly spelled words are: '+str(badwords)+" your percentage of incorrectly spelled words is "+badpercentage

    #print(badwords)
    frequent_misspelled(badwords)

    print(result)
    return (result)


def input_list_words(user_input):
    input_words = user_input.lower().split(" ")
   #print(input_words)
    #return (input_words)
    userResult(input_words)

def frequent_misspelled(badwords):
    badwords_dict = {}
    for word in badwords:
        if word not in badwords_dict:
            badwords_dict[word] = 1
        else:
            badwords_dict[word]+=1

    alotmisspelled = {}
    for item in badwords_dict.keys():
        if badwords_dict[item] >= 2:
            alotmisspelled[item] = badwords_dict[item]

    if len(alotmisspelled) !=0:
        print ("word misspelled :"+ " number of times misspelled" )
        for item in alotmisspelled.keys():
            print(item, ":", alotmisspelled[item])

    return(alotmisspelled)







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
    def test6(self):
        self.assertEqual(input_list_words('sunflower'), ['sunflower'])
    def test7(self):
        self.assertEqual(frequent_misspelled(["uhhh", "uhhh", "uhhh", 'djklfdsjkl', 'hfdjkjfkd', 'ttt', 'ttt']), {'uhhh': 3, 'ttt': 2})
    def test8(self):
        self.assertEqual(frequent_misspelled(["dogg", "catt", "socer"]), {})
    def test9(self):
        self.assertEqual(frequent_misspelled([]),{})

def main():
    create_word_dict()
    #userInput()

   
    mytest = MyTest()
    mytest.test()
    mytest.test1()
    mytest.test2()
    mytest.test3()
    mytest.test4()
    mytest.test5()
    mytest.test6()
    mytest.test7()
    mytest.test8()
    mytest.test9()


main()
    