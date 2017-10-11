#Function​ ​that​ ​asks​ ​the​ ​user​ ​to submit​ ​input​ ​(words​ ​
#to​ ​check, and​ ​returns​ ​list​ ​of​ ​words​ ​split by​ ​spaces)  

def input_list_words(user_input):
	input_words = user_input.lower().split(" ")
	return input_words

def main():
	user_input = input("write in your sentence? ")

	print(input_list_words(user_input))

main()
