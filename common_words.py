'''Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. 
This will be an approximation because it will also count words such as 'then' and 'there'. 
Try counting 'the ', with a space in the string, and see how much lower your count is.'''


def word_count(filename):
	'''Count the approximate number of words in a file'''
	try:
		with open(filename , encoding = 'utf-8') as f :
			contents = f.read()
	except FileNotFoundError :
		print(f"Sorry , file {filename} does not exist.")
	else:
		num_words = contents.count('the ')
		print(f"File {filename} has  about {num_words} 'the 'words. ")
		
filenames = ['pride_and_prejudice.txt' , 'war_game.txt' , 'montezuma_castle.txt', 'life_and_adventure.txt']
for filename in filenames:
	word_count(filename)

