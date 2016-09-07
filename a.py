blank = ["__1__", "__2__", "__3__", "__4__"]

level_easy = """If you are thinking about programming in general, I suggest you understand some basic principles. 
				One is the __1__, the way to begin a __1__ is with def. After using def, you must supply inputs
				these are also known as __2__. A __1__ is essentially inputs and __3__. To close a function you must put 
				__4__  

"""
#MED
level_medium = """So you picked the medium level, okay. Within functions, there are times when you need to implement repetitive
				  actions for the computer to do. They are called either __1__ loops or __2__ loops. These loops can either be 
				  nested in __3__ but can also be outside. You must remember to close your loops, otherwise they will go on
				  __4__.

"""
#HARD
level_hard = """To be honest, the hardest question should probably be the most easiest. This question pertains to __1__
				statements. Oh, you probably need more context, okay it's like if you do this thing then you do that thing
				get it? Oh I know that was convoluted. The __1__ statement is followed by an __2__ and then by a __3__. 
				This the proper syntax for such thing. Extra credit -- what is the best food in the world? __4__
"""

#ANSWERS
level_easy_answer = ["function", "parameters", "outputs", "return"]
level_medium_answer = ["for", "while", "function", "infinitely" ]
level_hard_answer = ["if", "else", "semicolon", "ramen" ]


def quiz_answers():
	"""Calls upon the function play_game and matches the level and answer to the level 
	based on a players response to the intitial user_response"""
	print ("\nWelcome to Justin's Code Quiz!")
	player_answer = raw_input("\nWhat level do you feel best at, easy, medium or hard?: ")
	""" Asks the user for the input that will determine which level and answer we will match from"""
	while True:
		if player_answer == "easy":
			play_game(level_easy_answer, level_easy)
		elif player_answer == "medium":
			play_game(level_medium_answer, level_medium)
		elif player_answer == "hard":
			play_game(level_hard_answer, level_hard)
		else:
			print ("\nSilly, that's not a level. Codequiz running again...")
			print ("\nTo exit infinite loop press 'CTRL-C'.")
			quiz_answers()
	return	

def play_game(chosen_answer, chosen_level):
	"""This function takes a player's reponse to a question 1 - 4 and matches it to
	the answer for the specific level. If a user fails to answer the question
	right 3 times, the game resets. """
	attempts = 3
	player_blank = 0
	while player_blank < len(blank):
		print chosen_level
		player_answers = raw_input("What is the answer to " + blank[player_blank] + "?")
		if player_answers == chosen_answer[player_blank]:
			print ("Congratulations, you've solved problem " + blank[player_blank] + ".")
			chosen_level = chosen_level.replace(blank[player_blank], player_answers)
			#print var2	
			player_blank += 1
			if player_blank == len(blank):
				print chosen_level
				print ("Congratulations, you have finished the game.")
				exit()
		else:	
			attempts -= 1
			print ("Wrong answer, try again. You have " + str(attempts) + " chances left.")
			if attempts == 0:
				print("Sorry, max number of attempts reached. Program closed...")
				exit()	
	


quiz_answers()
