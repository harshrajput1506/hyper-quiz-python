import json
import random


def playGame():
	print("\n----------QUIZ START-----------")
	score = 0
	with open("res/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(5):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1}. {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')

def rules():
	print('''\n---------RULES----------
1. Each round consists of 5 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative marking.''')

def aboutUS():
	print('''\n-------ABOUT US-------
This project has been developed by Harsh.''')

if __name__ == "__main__":
	choice = 1
	while choice != 4:
		print('\n---------WELCOME TO HYPER QUIZ---------')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. SEE RULES ON HOW TO PLAY THE QUIZ GAME')
		print('3. ABOUT US')
		print('4. EXIT')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			playGame()
		elif choice == 2:
			rules()
		elif choice == 3:
			aboutUS()
		elif choice == 4:
			break;
		else:
			print('WRONG CHOICE. ENTER THE CHOICE AGAIN')
