# Read in the file
# And put into list 

word_dict = {}
def create_word_dict():
	words = open("words.txt", "r")
	for line in words:
		line = line.strip("\n")
		word_dict[line] = 1
	words.close()

def main ():

main ()
