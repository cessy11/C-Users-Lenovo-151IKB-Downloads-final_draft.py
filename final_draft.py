import os


global score 
score = 0



def mainfn():
	os.system('cls')
	print("==========QuizGame==========")
	name = input("USERNAME: ")
	print("Your age must be 10years old and above")
	age = int(input("YOUR AGE: "))

	if age >= 10:
		QuizStart()

def QuizStart():
	os.system('title QuizStart')
	os.system('cls')
	print("Would you like to proceed to our Quiz Game? Yes or No")
	proceed = input("Type your answer: ")
	Yes = ["YES", "Yes", "yes"]
	No = ["NO", "No", "no"]

	if proceed == proceed in Yes:
		instructions = '''
===========================================================================

BEFORE WE START BRIEF INSTRUCTION:

1.	You must choose first how choose a number between
	1-3 and each number has different difficulty
	from easiest which is 1 to Hardest questions which is 3.

2.	You must choose a subject you want to answer
	there are 3 subjects such as (MATH, SCIENCE, ENGLISH).
 
3.	Each has different difficulties and every difficulty has different
	corresponding scores.
	Easy(1) = 1pts
	Medium(2) = 6pts
	Hard(3) = 10pts

4.	Each difficulties has 5 different questions means you
	have different choices.

5. At last, take note of what subject and difficulties that your going to take.
===========================================================================
'''
		print(instructions)
		print("Let's Proceed!")
		os.system('pause')
		ChooseCategory()
	
	elif proceed == proceed in No:
		print("!!!Okieee!!!")
		os.system('pause')
		

	else:
		print("Aww Sad! hope you try this Quiz Game next time")
		os.system('pause')
		mainfn()


def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()

def math():
	difficulties = ''' 
===========================================================================
CHOOSE DIFFICULTIES and each 10 Question:

EASY (1-10 Questions)

MEDIUM (1-10 Questions)

HARD (1-10 Questions)

===========================================================================
	'''

	diffEasy = ["EASY", "Easy", "easy"]
	diffMedium = ["MEDIUM", "Medium", "medium"]
	diffHard = ["HARD", "Hard", "hard"]
	os.system('cls')
	print(difficulties)
	Math_difficulty_User_Input = input("Level of difficulties you want: ")

	if Math_difficulty_User_Input == Math_difficulty_User_Input in diffEasy:
		print("Let's Proceed to easy questions")
		os.system('pause')
		math_easy_questions()

	elif Math_difficulty_User_Input == Math_difficulty_User_Input in diffMedium:
		print("Let's Proceed to medium questions")
		os.system('pause')
		math_medium_questions()

	elif Math_difficulty_User_Input == Math_difficulty_User_Input in diffHard:
		print("Let's Proceed to hard questions")
		os.system('pause')
		math_hard_questions()
	
	else:
		print("Wrong answer please try again! ")
		print("Choose a subject again")
		os.system('pause')
		math_easy_questions()

def math_easy_questions():
	math_easy_1()

def math_easy_1():
	math_easy_Q1 = '''
============================================================
1. What is 5+7?  
A. 10 
B. 12 
C. 15 
D. 17 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q1 = ["B", "b"]
	os.system('title Questions Easy #1')
	os.system('cls')
	print(math_easy_Q1)
	UserAnswer_Math_Q1 = input("Letter of your answer: ")

	if UserAnswer_Math_Q1 == UserAnswer_Math_Q1 in math_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		math_easy_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_2()

def math_easy_2():

	math_easy_Q2 = '''
============================================================
2. What is 9×8?
A. 63 
B. 72  
C. 81 
D. 64 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q2 = ["B","b"]
	os.system('title Questions Easy #2')
	os.system('cls')
	print(math_easy_Q2)
	UserAnswer_Math_Q2 = input("Letter of your ansewer: ")

	if UserAnswer_Math_Q2 == UserAnswer_Math_Q2 in math_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		math_easy_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_3()

def math_easy_3():

	math_easy_Q3 = '''
============================================================
3. What is 15÷3? 
A. 4 
B. 5  
C. 6 
D. 3 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q3 = ["B", "b"]
	os.system('title Questions Easy #3')
	os.system('cls')
	print(math_easy_Q3)
	UserAnswer_Math_Q3 = input("Letter of your answer: ")

	if UserAnswer_Math_Q3 == UserAnswer_Math_Q3 in math_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		math_easy_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_4()
		
def math_easy_4():

	math_easy_Q4 = '''
============================================================
4. What is 18-6? 
A. 10 
B. 11
C. 12
D. 13
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q4 = ["C", "c"]
	os.system('title Questions Easy #4')
	os.system('cls')
	print(math_easy_Q4)
	UserAnswer_Math_Q4 = input("Letter of your answer: ")

	if UserAnswer_Math_Q4 == UserAnswer_Math_Q4 in math_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		math_easy_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_5()

def math_easy_5():

	math_easy_Q5 = '''
============================================================
5. What is 4×7? 
A. 21 
B. 24 
C. 28  
D. 32 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q5 = ["C", "c"]
	os.system('title Questions Easy #5')
	os.system('cls')
	print(math_easy_Q5)
	UserAnswer_Math_Q5 = input("Letter of your answer: ")

	if UserAnswer_Math_Q5 == UserAnswer_Math_Q5 in math_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		math_easy_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_6()

def math_easy_6():

	math_easy_Q6 = '''
============================================================
6. What is 10÷2? 
A. 4 
B. 6 
C. 3
D. 5
============================================================
'''
	#Inside the square bracket is the correct answer
	math_answer_Q6 = ["D", "d"]
	os.system('title Questions Easy #6')
	os.system('cls')
	print(math_easy_Q6)
	UserAnswer_Math_Q6 = input("Letter of your answer: ")

	if UserAnswer_Math_Q6 == UserAnswer_Math_Q6 in math_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		math_easy_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_7()

def math_easy_7():

	math_easy_Q7 = '''
============================================================
7. What is 10×10? 
A. 105 
B. 65 
C. 100 
D. 95 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q7 = ["C", "c"]
	os.system('title Questions Easy #7')
	os.system('cls')
	print(math_easy_Q7)
	UserAnswer_Math_Q7 = input("Letter of your answer: ")

	if UserAnswer_Math_Q7 == UserAnswer_Math_Q7 in math_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		math_easy_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_8()

def math_easy_8():

	math_easy_Q8 = '''
============================================================
8. What is 4+6? 
A. 10 
B. 11 
C. 9 
D. 14 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q8 = ["A", "a"]
	os.system('title Questions Easy #8')
	os.system('cls')
	print(math_easy_Q8)
	UserAnswer_Math_Q8 = input("Letter of your answer: ")

	if UserAnswer_Math_Q8 == UserAnswer_Math_Q8 in math_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		math_easy_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_9()


def math_easy_9():

	math_easy_Q9 = '''
============================================================
9. What is 100÷10? 
A. 20 
B. 10 
C. 30 
D. 9 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q9 = ["B", "b"]
	os.system('title Questions Easy #9')
	os.system('cls')
	print(math_easy_Q9)
	UserAnswer_Math_Q9 = input("Letter of your answer: ")

	if UserAnswer_Math_Q9 == UserAnswer_Math_Q9 in math_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		math_easy_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_easy_10()


def math_easy_10():

	math_easy_Q10 = '''
============================================================
10. What is 1-2? 
A. -2 
B. -1 
C. -0 
D. -3 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q10 = ["B", "b"]
	os.system('title Questions Easy #10')
	os.system('cls')
	print(math_easy_Q10)
	UserAnswer_Math_Q10 = input("Letter of your answer: ")

	if UserAnswer_Math_Q10 == UserAnswer_Math_Q10 in math_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice, you're done in math easy question. Get ready to choose your next category!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()

def math_easy_score():
	print("===============================================")
	print("You're total score")
	print("Math Easy Score: " + score)
	print("===============================================")
	os.system('pause')

def math_medium_questions():
	math_medium_1()

def math_medium_1():
	math_medium_Q1 = '''
============================================================
1. What is the square root of 144? 
A. 10 
B. 11 
C. 12 
D. 13 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q1 = ["C", "c"]
	os.system('title Questions medium #1')
	os.system('cls')
	print(math_medium_Q1)
	UserAnswer_Math_Q1 = input("Letter of your answer: ")

	if UserAnswer_Math_Q1 == UserAnswer_Math_Q1 in math_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		math_medium_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_2()

def math_medium_2():
	math_medium_Q2 = '''
============================================================
2. What is 0.5×10? 
A. 2.5 
B. 5 
C. 7.5 
D. 10 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q2 = ["B", "b"]
	os.system('title Questions medium #2')
	os.system('cls')
	print(math_medium_Q2)
	UserAnswer_Math_Q2 = input("Letter of your answer: ")

	if UserAnswer_Math_Q2 == UserAnswer_Math_Q2 in math_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		math_medium_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_3()

def math_medium_3():
	math_medium_Q3 = '''
============================================================
3. What is 10²? 
A. 50 
B. 75 
C. 100 
D. 150 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q3 = ["B", "b"]
	os.system('title Questions medium #3')
	os.system('cls')
	print(math_medium_Q3)
	UserAnswer_Math_Q3 = input("Letter of your answer: ")

	if UserAnswer_Math_Q3 == UserAnswer_Math_Q3 in math_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		math_medium_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_4()


def math_medium_4():
	math_medium_4 = '''
============================================================
4. What is 10% of 250? 
A. 20 
B. 25 
C. 30 
D. 35 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q4 = ["C", "c"]
	os.system('title Questions medium #4')
	os.system('cls')
	print(math_medium_4)
	UserAnswer_Math_Q4 = input("Letter of your answer: ")

	if UserAnswer_Math_Q4 == UserAnswer_Math_Q4 in math_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		math_medium_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_5()

def math_medium_5():
	math_medium_Q5 = '''
============================================================
5. What is 3³? 
A. 6 
B. 9 
C. 27 
D. 30 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q5 = ["B", "b"]
	os.system('title Questions medium #5')
	os.system('cls')
	print(math_medium_Q5)
	UserAnswer_Math_Q5 = input("Letter of your answer: ")

	if UserAnswer_Math_Q5 == UserAnswer_Math_Q5 in math_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		math_medium_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_6()

def math_medium_6():
	math_medium_Q6 = '''
============================================================
6. What is 45÷5(4)? 
A. 36 
B. 34 
C. 46 
D. 38 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q6 = ["B", "b"]
	os.system('title Questions medium #6')
	os.system('cls')
	print(math_medium_Q6)
	UserAnswer_Math_Q6 = input("Letter of your answer: ")

	if UserAnswer_Math_Q6 == UserAnswer_Math_Q6 in math_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		math_medium_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_7()

def math_medium_7():
	math_medium_Q7 = '''
============================================================
7. What is 4²(3)?  
A. 49 
B. 47 
C. 48 
D. 43 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q7 = ["A", "a"]
	os.system('title Questions medium #7')
	os.system('cls')
	print(math_medium_Q7)
	UserAnswer_Math_Q7 = input("Letter of your answer: ")

	if UserAnswer_Math_Q7 == UserAnswer_Math_Q7 in math_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		math_medium_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_8()

def math_medium_8():
	math_medium_Q8 = '''
============================================================
8. Give example of even numbers.  
A. 0,2,4,6,7 
B. 2,4,6,8,0 
C. 4,8,9,1 
D. 5,8,9,7 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q8 = ["C", "c"]
	os.system('title Questions medium #8')
	os.system('cls')
	print(math_medium_Q8)
	UserAnswer_Math_Q8 = input("Letter of your answer: ")

	if UserAnswer_Math_Q8 == UserAnswer_Math_Q8 in math_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		math_medium_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_9()

def math_medium_9():
	math_medium_Q9 = '''
============================================================
9. May bought 10 apple, 5 oranges and 11 mango. If the apple is 20 each, 
oranges is 15each and her change of 500 is 115. How much each of the mango?  
A. 115 
B. 10 
C. 225 
D. 11 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q9 = ["B", "b"]
	os.system('title Questions Medium #9')
	os.system('cls')
	print(math_medium_Q9)
	UserAnswer_Math_Q9 = input("Letter of your answer: ")

	if UserAnswer_Math_Q9 == UserAnswer_Math_Q9 in math_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		math_medium_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_medium_10()

def math_medium_10():
	math_medium_Q10 = '''
============================================================
10. What is 145 x 15?
A. 2,170
B. 2,175
C. 2,715
D. 1,251
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q10 = ["B", "b"]
	os.system('title Questions Medium #10')
	os.system('cls')
	print(math_medium_Q10)
	UserAnswer_Math_Q10 = input("Letter of your answer: ")

	if UserAnswer_Math_Q10 == UserAnswer_Math_Q10 in math_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Great! You're done in math medium question. Get ready to choose your next category!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def math_hard_questions():
	math_hard_1()

def math_hard_1():
	math_hard_Q1 = '''
============================================================
1. What is the common divisor(GCD) of 12 and 15? 
A. 1
B. 2
C. 3 
D. 5 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q1 = ["C", "c"]
	os.system('title Questions Hard #1')
	os.system('cls')
	print(math_hard_Q1)
	UserAnswer_Math_Q1 = input("Letter of your answer: ")

	if UserAnswer_Math_Q1 == UserAnswer_Math_Q1 in math_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		math_hard_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_2()

def math_hard_2():
	math_hard_Q2 = '''
============================================================
2. What is the value of 7×(6+4)? 
A. 40 
B. 56 
C. 64 
D. 70 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q2 = ["D", "d"]
	os.system('title Questions Hard #2')
	os.system('cls')
	print(math_hard_Q2)
	UserAnswer_Math_Q2 = input("Letter of your answer: ")

	if UserAnswer_Math_Q2 == UserAnswer_Math_Q2 in math_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		math_hard_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_3()

def math_hard_3():
	math_hard_Q3 = '''
============================================================
3. What is the least common multiple (LCM) of 4 and 5? 
A. 10 
B. 15 
C. 20 
D. 25 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q3 = ["C", "c"]
	os.system('title Questions Hard #3')
	os.system('cls')
	print(math_hard_Q3)
	UserAnswer_Math_Q3 = input("Letter of your answer: ")

	if UserAnswer_Math_Q3 == UserAnswer_Math_Q3 in math_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		math_hard_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_4()


def math_hard_4():
	math_hard_4 = '''
============================================================
4. What is the sum of the angles in triangle? 
A. 90⁰ 
B. 120⁰ 
C. 180⁰ 
D. 360⁰ 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q4 = ["C", "c"]
	os.system('title Questions Hard #4')
	os.system('cls')
	print(math_hard_4)
	UserAnswer_Math_Q4 = input("Letter of your answer: ")

	if UserAnswer_Math_Q4 == UserAnswer_Math_Q4 in math_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		math_hard_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_5()

def math_hard_5():
	math_hard_Q5 = '''
============================================================
5. What is the area of a circle with radius of 3 units? ( Use π ≈ 3.14) 
A. 18.84 square units 
B. 28.26 square units 
C. 38.48 square u its 
D. 48.66 square units 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q5 = ["B", "b"]
	os.system('title Questions Hard #5')
	os.system('cls')
	print(math_hard_Q5)
	UserAnswer_Math_Q5 = input("Letter of your answer: ")

	if UserAnswer_Math_Q5 == UserAnswer_Math_Q5 in math_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		math_hard_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_6()

def math_hard_6():
	math_hard_Q6 = '''
============================================================
6. What is 5+9×2? ( Follow the order of operations) 
A. 18 
B. 19 
C. 23 
D. 31 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q6 = ["C", "c"]
	os.system('title Questions Hard #6')
	os.system('cls')
	print(math_hard_Q6)
	UserAnswer_Math_Q6 = input("Letter of your answer: ")

	if UserAnswer_Math_Q6 == UserAnswer_Math_Q6 in math_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		math_hard_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_7()

def math_hard_7():
	math_hard_Q7 = '''
============================================================
7. If rectangle has length of 6 units and a width of 3 units, what is its area? 
A. 9 square units 
B. 12 square u its 
C. 14 square units 
D. 18 square units 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q7 = ["D", "d"]
	os.system('title Questions Hard #7')
	os.system('cls')
	print(math_hard_Q7)
	UserAnswer_Math_Q7 = input("Letter of your answer: ")

	if UserAnswer_Math_Q7 == UserAnswer_Math_Q7 in math_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		math_hard_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_8()

def math_hard_8():
	math_hard_Q8 = '''
============================================================
8. What is ¾ + 2/4?  
A. ¾ 
B. 5/4 
C. ½ 
D. 1 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q8 = ["B","b"]
	os.system('title Questions Hard #8')
	os.system('cls')
	print(math_hard_Q8)
	UserAnswer_Math_Q8 = input("Letter of your answer: ")

	if UserAnswer_Math_Q8 == UserAnswer_Math_Q8 in math_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		math_hard_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_9()

def math_hard_9():
	math_hard_Q9 = '''
============================================================
9. What is ⅚ - ⅓? 
A. ⅔ 
B. ½ 
C. ⅙ 
D. 3/6 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q9 = ["A", "a"]
	os.system('title Questions Hard #9')
	os.system('cls')
	print(math_hard_Q9)
	UserAnswer_Math_Q9 = input("Letter of your answer: ")

	if UserAnswer_Math_Q9 == UserAnswer_Math_Q9 in math_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		math_hard_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		math_hard_10()

def math_hard_10():
	math_hard_Q10 = '''
============================================================
10. What is ⅖ × ¾? 
A. 5/9 
B. 6/9 
C. 6/20 
D. 3/10 
============================================================
	'''
	#Inside the square bracket is the correct answer
	math_answer_Q10 = ["D", "d"]
	os.system('title Questions Hard #10')
	os.system('cls')
	print(math_hard_Q10)
	UserAnswer_Math_Q10 = input("Letter of your answer: ")

	if UserAnswer_Math_Q10 == UserAnswer_Math_Q10 in math_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice job, you're done in math hard questions. Get ready to choose your next category!!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def science():
	difficulties = ''' 
===========================================================================
CHOOSE DIFFICULTIES and each 10 Question:

EASY (1-10 Questions)

MEDIUM (1-10 Questions)

HARD (1-10 Questions)

===========================================================================
	'''
	diffEasy = ["EASY", "Easy", "easy"]
	diffMedium = ["MEDIUM", "Medium", "medium"]
	diffHard = ["HARD", "Hard", "hard"]
	os.system('cls')
	print(difficulties)
	science_difficulty_User_Input = input("Level of difficulties you want: ")

	if science_difficulty_User_Input == science_difficulty_User_Input in diffEasy:
		print("Let's Proceed to easy questions")
		os.system('pause')
		science_easy_questions()

	elif science_difficulty_User_Input == science_difficulty_User_Input in diffMedium:
		print("Let's Proceed to easy questions")
		os.system('pause')
		science_medium_questions()

	elif science_difficulty_User_Input == science_difficulty_User_Input in diffHard:
		print("Let's Proceed to easy questions")
		os.system('pause')
		science_hard_questions()
	
	else:
		print("Wrong answer please try again! ")
		print("Choose a subject again")
		os.system('pause')
		science_easy_questions()

def science_easy_questions():
	science_easy_1()

def science_easy_1():
	science_easy_Q1 = '''
============================================================
1.What is the largest planet in our solar system?
A. Earth
B. Jupiter
C. Mars
D. Saturn
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q1 = ["B", "b"]
	os.system('title Questions Easy #1')
	os.system('cls')
	print(science_easy_Q1)
	UserAnswer_science_Q1 = input("Letter of your answer: ")

	if UserAnswer_science_Q1 == UserAnswer_science_Q1 in science_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		science_easy_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_2()

def science_easy_2():

	science_easy_Q2 = '''
============================================================
2.What is the main function of the brain?
A. To pump blood
B. To control movement
C. To process information  
D. To produce energy
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q2 = ["C", "c"]
	os.system('title Questions Easy #4')
	os.system('cls')
	print(science_easy_Q2)
	UserAnswer_science_Q2 = input("Letter of your answer: ")

	if UserAnswer_science_Q2 == UserAnswer_science_Q2 in science_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		science_easy_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_3()

def science_easy_3():

	science_easy_Q3 = '''
============================================================
3.What is the force that pulls objects towards the Earth?
A. Gravity
B. Magnetism
C. Friction
D. Tension
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q3 = ["A", "a"]
	os.system('title Questions Easy #3')
	os.system('cls')
	print(science_easy_Q3)
	UserAnswer_science_Q3 = input("Letter of your answer: ")

	if UserAnswer_science_Q3 == UserAnswer_science_Q3 in science_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		science_easy_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_4()
		
def science_easy_4():

	science_easy_Q4 = '''
============================================================
4.What is the process of combining two or more substances to form a new substance?
A. Physical change
B. Chemical change
C. Decomposition
D. Synthesis
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q4 = ["B", "b"]
	os.system('title Questions Easy #4')
	os.system('cls')
	print(science_easy_Q4)
	UserAnswer_science_Q4 = input("Letter of your answer: ")

	if UserAnswer_science_Q4 == UserAnswer_science_Q4 in science_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		science_easy_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_5()

def science_easy_5():

	science_easy_Q5 = '''
============================================================
5.What is the largest ocean on Earth?
A. Atlantic Ocean
B. Pacific Ocean
C. Indian Ocean
D. Arctic Ocean
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q5 = ["B", "b"]
	os.system('title Questions Easy #5')
	os.system('cls')
	print(science_easy_Q5)
	UserAnswer_science_Q5 = input("Letter of your answer: ")

	if UserAnswer_science_Q5 == UserAnswer_science_Q5 in science_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		science_easy_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_6()

def science_easy_6():

	science_easy_Q6 = '''
============================================================
6. What is the name of the process by which a substance changes from liquid to gas?
Choose the letter of the correct answer
A.Melting 
B. Freezing 
C. Evaporation 
D. Condensation 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q6 = ["C", "c"]
	os.system('title Questions Easy #6')
	os.system('cls')
	print(science_easy_Q6)
	UserAnswer_science_Q6 = input("Letter of your answer: ")

	if UserAnswer_science_Q6 == UserAnswer_science_Q6 in science_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		science_easy_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_7()

def science_easy_7():

	science_easy_Q7 = '''
============================================================
7. What is the smallest unit of matter?
A. Cell
B. Atom
C. Molecule
D. Organelle
============================================================
	''' 
	#Inside the square bracket is the correct answer
	science_answer_Q7 = ["B", "b"]
	os.system('title Questions Easy #7')
	os.system('cls')
	print(science_easy_Q7)
	UserAnswer_science_Q7 = input("Letter of your answer: ")

	if UserAnswer_science_Q7 == UserAnswer_science_Q7 in science_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		science_easy_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_8()

def science_easy_8():

	science_easy_Q8 = '''
============================================================
8. What is the process by which plants make their own food?
A. Respiration 
B. Photosynthesis 
C. Digestion 
D. Evaporation
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q8 = ["B", "b"]
	os.system('title Questions Easy #8')
	os.system('cls')
	print(science_easy_Q8)
	UserAnswer_science_Q8 = input("Letter of your answer: ")

	if UserAnswer_science_Q8 == UserAnswer_science_Q8 in science_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		science_easy_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_9()


def science_easy_9():

	science_easy_Q9 = '''
============================================================
9. What is the name of the force that holds atoms together?
A. Gravity 
B. Fiction 
C. Magnetism
D. Electromagnetism
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q9 = ["D", "d"]
	os.system('title Questions Easy #9')
	os.system('cls')
	print(science_easy_Q9)
	UserAnswer_science_Q9 = input("Letter of your answer: ")

	if UserAnswer_science_Q9 == UserAnswer_science_Q9 in science_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		science_easy_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_easy_10()


def science_easy_10():

	science_easy_Q10 = '''
============================================================
10. What is the name of the layer of the Earth's atmosphere that contains the ozone layer?
A. Troposphere 
B. Stratosphere 
C. Mesosphere 
D. Thermosphere 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q10 = ["B", "b"]
	os.system('title Questions Easy #10')
	os.system('cls')
	print(science_easy_Q10)
	UserAnswer_science_Q10 = input("Letter of your answer: ")

	if UserAnswer_science_Q10 == UserAnswer_science_Q10 in science_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Wow good job! you're done in science easy questions. Get ready to choose you next category")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def science_medium_questions():
	science_medium_1()

def science_medium_1():
	science_medium_Q1 = '''
============================================================
1.What is the largest organ in the human body?
A. Liver
B. Skin
C. Heart
D. Lungs
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q1 = ["B", "b"]
	os.system('title Questions medium #1')
	os.system('cls')
	print(science_medium_Q1)
	UserAnswer_science_Q1 = input("Letter of your answer: ")

	if UserAnswer_science_Q1 == UserAnswer_science_Q1 in science_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		science_medium_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_2()

def science_medium_2():
	science_medium_Q2 = '''
============================================================
2.Who is considered the father of modern physics?
A. Albert Einstein
B. Isaac Newton
C. Galileo Galilei
D. Stephen Hawking
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q2 = ["A", "a"]
	os.system('title Questions medium #2')
	os.system('cls')
	print(science_medium_Q2)
	UserAnswer_science_Q2 = input("Letter of your answer: ")

	if UserAnswer_science_Q2 == UserAnswer_science_Q2 in science_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		science_medium_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_3()

def science_medium_3():
	science_medium_Q3 = '''
============================================================
3.What is the name of the process by which cells divide to produce new cells?
A. Mitosis
B. Meiosis
C. Apoptosis
D. Endocytosis
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q3 = ["A", "a"]
	os.system('title Questions medium #3')
	os.system('cls')
	print(science_medium_Q3)
	UserAnswer_science_Q3 = input("Letter of your answer: ")

	if UserAnswer_science_Q3 == UserAnswer_science_Q3 in science_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		science_medium_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_4()


def science_medium_4():
	science_medium_4 = '''
============================================================
4. What is the Earth's outermost layer called?
A. Mantle
B. Core
C. Crust
D. Lithosphere
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q4 = ["C", "c"]
	os.system('title Questions medium #4')
	os.system('cls')
	print(math_medium_4)
	UserAnswer_science_Q4 = input("Letter of your answer: ")

	if UserAnswer_science_Q4 == UserAnswer_science_Q4 in science_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		science_medium_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_5()

def science_medium_5():
	science_medium_Q5 = '''
============================================================
5. What is the Earth's approximate age?
A. 4.5 billion years
B. 3.5 billion years
C. 2.5 billion years
D. 1.5 billion years
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q5 = ["A", "a"]
	os.system('title Questions medium #5')
	os.system('cls')
	print(science_medium_Q5)
	UserAnswer_science_Q5 = input("Letter of your answer: ")

	if UserAnswer_science_Q5 == UserAnswer_science_Q5 in science_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		science_medium_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_6()

def science_medium_6():
	science_medium_Q6 = '''
============================================================
6. What is the name of the chemical bond that involves the sharing of electrons between atoms?
A. Ionic bonds
B. Covalent bonds
C. Metallic bonds
D. Hydrogen bonds B
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q6 = ["B", "b"]
	os.system('title Questions medium #6')
	os.system('cls')
	print(science_medium_Q6)
	UserAnswer_science_Q6 = input("Letter of your answer: ")

	if UserAnswer_science_Q6 == UserAnswer_science_Q6 in science_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		science_medium_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_7()

def science_medium_7():
	science_medium_Q7 = '''
============================================================
7. What is the name of the hypothetical particle that is thought to be responsible for the expansion of the universe?
A. Higgs boson
B. Graviton 
C. Dark matter 
D. Dark energy 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q7 = ["D", "d"]
	os.system('title Questions medium #7')
	os.system('cls')
	print(science_medium_Q7)
	UserAnswer_science_Q7 = input("Letter of your answer: ")

	if UserAnswer_science_Q7 == UserAnswer_science_Q7 in science_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		science_medium_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_8()

def science_medium_8():
	science_medium_Q8 = '''
============================================================
8. What is the function of lysosomes in a cell?
A. Synthesize proteins 
B. To package and modify proteins
C. To break down waste products
D. To generate energy 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q8 = ["C", "c"]
	os.system('title Questions medium #8')
	os.system('cls')
	print(science_medium_Q8)
	UserAnswer_science_Q8 = input("Letter of your answer: ")

	if UserAnswer_science_Q8 == UserAnswer_science_Q8 in science_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		science_medium_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_9()

def science_medium_9():
	science_medium_Q9 = '''
============================================================
9. What is the name of the part of the cell that contains the genetic material?
Choose the letter of the correct answer
A. Nucleus 
B. Cytoplasm 
C. Mitochondria 
D. Ribosomes 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q9 = ["A", "a"]
	os.system('title Questions medium #9')
	os.system('cls')
	print(science_medium_Q9)
	UserAnswer_science_Q9 = input("Letter of your answer: ")

	if UserAnswer_science_Q9 == UserAnswer_science_Q9 in science_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		science_medium_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_medium_10()

def science_medium_10():
	science_medium_Q10 = '''
============================================================
10. What is the name of the scientist who developed the theory of relativity?
A. Isaac Newton 
B. Albert Einstein 
C. Galileo Galilei 
D. Alexis Jhon
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q10 = ["B", "b"]
	os.system('title Questions medium #10')
	os.system('cls')
	print(science_medium_Q10)
	UserAnswer_science_Q10 = input("Letter of your answer: ")

	if UserAnswer_science_Q10 == UserAnswer_science_Q10 in science_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice! You're done in science medium questions. Get ready to choose your next category!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def science_hard_questions():
	science_hard_1()

def science_hard_1():
	science_hard_Q1 = '''
============================================================
1.What is the smallest known living organism?
A. Bacteria
B. Virus
C. Mycoplasma
D. Protozoa
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q1 = ["A", "a"]
	os.system('title Questions Hard #1')
	os.system('cls')
	print(science_hard_Q1)
	UserAnswer_science_Q1 = input("Letter of your answer: ")

	if UserAnswer_science_Q1 == UserAnswer_science_Q1 in science_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		science_hard_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_2()

def science_hard_2():
	science_hard_Q2 = '''
============================================================
2. What is the chemical symbol for gold?
A. Au
B. Ag
C. Fe
D. Cu
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q2 = ["A", "a"]
	os.system('title Questions Hard #2')
	os.system('cls')
	print(science_hard_Q2)
	UserAnswer_science_Q2 = input("Letter of your answer: ")

	if UserAnswer_science_Q2 == UserAnswer_science_Q2 in science_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		science_hard_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_3()

def science_hard_3():
	science_hard_Q3 = '''
============================================================
3. What is the smallest particle of an element that retains its properties?
A. Atom
B. Molecule
C. Ion
D. Electron
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q3 = ["A", "a"]
	os.system('title Questions Hard #3')
	os.system('cls')
	print(science_hard_Q3)
	UserAnswer_science_Q3 = input("Letter of your answer: ")

	if UserAnswer_science_Q3 == UserAnswer_science_Q3 in science_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		science_hard_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_4()


def science_hard_4():
	science_hard_4 = '''
============================================================
4.What is the most abundant element in the Earth's atmosphere?
A. Nitrogen
B. Oxygen
C. Argon
D. Carbon Dioxide
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q4 = ["A", "a"]
	os.system('title Questions Hard #4')
	os.system('cls')
	print(science_hard_4)
	UserAnswer_science_Q4 = input("Letter of your answer: ")

	if UserAnswer_science_Q4 == UserAnswer_science_Q4 in science_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		science_hard_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_5()

def science_hard_5():
	science_hard_Q5 = '''
============================================================
5. What is the name of the force that holds atoms together in a molecule?
A. Gravitational force
B. Electromagnetic force
C. Strong nuclear force
D. Weak nuclear force
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q5 = ["B", "b"]
	os.system('title Questions Hard #5')
	os.system('cls')
	print(science_hard_Q5)
	UserAnswer_science_Q5 = input("Letter of your answer: ")

	if UserAnswer_science_Q5 == UserAnswer_science_Q5 in science_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		science_hard_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_6()

def science_hard_6():
	science_hard_Q6 = '''
============================================================
6. What is the phenomenon responsible for the northern lights?
A. Solar wind
B. Moon's reflection 
C. Earth's rotation 
D. Snowflakes 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q6 = ["A", "a"]
	os.system('title Questions Hard #6')
	os.system('cls')
	print(science_hard_Q6)
	UserAnswer_science_Q6 = input("Letter of your answer: ")

	if UserAnswer_science_Q6 == UserAnswer_science_Q6 in science_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		science_hard_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_7()

def science_hard_7():
	science_hard_Q7 = '''
============================================================
7. What is the current estimated age of the universe?
A. 4.5  billion years
B. 13.7 billion years 
C. 10.6 billion years 
D. 20.3 billion years 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q7 = ["B", "b"]
	os.system('title Questions Hard #7')
	os.system('cls')
	print(science_hard_Q7)
	UserAnswer_Math_Q7 = input("Letter of your answer: ")

	if UserAnswer_Math_Q7 == UserAnswer_Math_Q7 in science_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		science_hard_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_8()

def science_hard_8():
	science_hard_Q8 = '''
============================================================
8. What is the name of the process by which  cells break down glucose to release energy?
A. Photosynthesis 
B. Cellular respiration
C. Mitosis
D. Meiosis
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q8 = ["B", "b"]
	os.system('title Questions Hard #8')
	os.system('cls')
	print(science_hard_Q8)
	UserAnswer_science_Q8 = input("Letter of your answer: ")

	if UserAnswer_science_Q8 == UserAnswer_science_Q8 in science_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		science_hard_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_9()

def science_hard_9():
	science_hard_Q9 = '''
============================================================
9. What is the name of the process by which water vapor in the atmosphere condenses into liquid water?
A. Evaporation 
B. Precipitation 
C. Sublimation 
D. Deposition 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q9 = ["B", "b"]
	os.system('title Questions Hard #9')
	os.system('cls')
	print(science_hard_Q9)
	UserAnswer_science_Q9 = input("Letter of your answer: ")

	if UserAnswer_science_Q9 == UserAnswer_science_Q9 in science_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		science_hard_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		science_hard_10()

def science_hard_10():
	science_hard_Q10 = '''
============================================================
10. What is the term for the process by which oceanic crust sink into the mantle at convergent boundaries 
A. Rift formation
B. Seafloor spreading 
C. Orogeny
D. Subduction 
============================================================
	'''
	#Inside the square bracket is the correct answer
	science_answer_Q10 = ["D", "d"]
	os.system('title Questions Hard #10')
	os.system('cls')
	print(science_hard_Q10)
	UserAnswer_science_Q10 = input("Letter of your answer: ")

	if UserAnswer_science_Q10 == UserAnswer_science_Q10 in science_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice job! You're done in science hard questions. Get ready to choose your next category!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def english():
	difficulties = ''' 
===========================================================================
CHOOSE DIFFICULTIES and each 10 Question:
 
EASY (1-10 Questions)

MEDIUM (1-10 Questions)

HARD (1-10 Questions)

===========================================================================
	'''

	diffEasy = ["EASY", "Easy", "easy"]
	diffMedium = ["MEDIUM", "Medium", "medium"]
	diffHard = ["HARD", "Hard", "hard"]
	os.system('cls')
	print(difficulties)
	english_difficulty_User_Input = input("Level of difficulties you want: ")

	if english_difficulty_User_Input == english_difficulty_User_Input in diffEasy:
		print("Let's Proceed to easy questions")
		os.system('pause')
		english_easy_questions()

	elif english_difficulty_User_Input == english_difficulty_User_Input in diffMedium:
		print("Let's Proceed to easy questions")
		os.system('pause')
		english_medium_questions()

	elif english_difficulty_User_Input == english_difficulty_User_Input in diffHard:
		print("Let's Proceed to easy questions")
		os.system('pause')
		english_hard_questions()
	
	else:
		print("Wrong answer please try again! ")
		print("Choose a subject again")
		os.system('pause')
		ChooseCategory()

def english_easy_questions():
	english_easy_1()

def english_easy_1():
	english_easy_Q1 = '''
============================================================
1. What is the synonym of "happy"?
a) Sad
b) Joyful
c) Angry
d) Bored
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q1 = ["B", "b"]
	os.system('title Questions Easy #1')
	os.system('cls')
	print(english_easy_Q1)
	UserAnswer_english_Q1 = input("Letter of your ansewer: ")

	if UserAnswer_english_Q1 == UserAnswer_english_Q1 in english_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		english_easy_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_2()

def english_easy_2():

	english_easy_Q2 = '''
============================================================
2. What is the opposite of "big"?
a) Large
b) Huge
c) Small
d) Gigantic
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q2 = ["C", "c"]
	os.system('title Questions Easy #2')
	os.system('cls')
	print(english_easy_Q2)
	UserAnswer_english_Q2 = input("Letter of your ansewer: ")

	if UserAnswer_english_Q2 == UserAnswer_english_Q2 in english_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		english_easy_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_3()

def english_easy_3():

	english_easy_Q3 = '''
============================================================
3. Which word means "to run slowly"?
a) Jump
b) Jog
c) Fly
d) Walk
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q3 = ["B", "b"]
	os.system('title Questions Easy #3')
	os.system('cls')
	print(english_easy_Q3)
	UserAnswer_english_Q3 = input("Letter of your answer: ")

	if UserAnswer_english_Q3 == UserAnswer_english_Q3 in english_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		english_easy_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_4()
		
def english_easy_4():

	english_easy_Q4 = '''
============================================================
4. What is the synonym of "tired"?
a) Sleepy
b) Energized
c) Awake
d) Busy
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q4 = ["A", "a"]
	os.system('title Questions Easy #4')
	os.system('cls')
	print(english_easy_Q4)
	UserAnswer_english_Q4 = input("Letter of your answer: ")

	if UserAnswer_english_Q4 == UserAnswer_english_Q4 in english_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		english_easy_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_5()

def english_easy_5():

	english_easy_Q5 = '''
============================================================
5. Which word means "to eat quickly"?
a) Munch
b) Devour
c) Sip
d) Taste
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q5 = ["B", "b"]
	os.system('title Questions Easy #5')
	os.system('cls')
	print(english_easy_Q5)
	UserAnswer_english_Q5 = input("Letter of your answer: ")

	if UserAnswer_english_Q5 == UserAnswer_english_Q5 in english_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		english_easy_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_6()

def english_easy_6():

	english_easy_Q6 = '''
============================================================
6. Which of these is a type of vehicle?
a) House
b) Chair
c) Car
d) Pencil
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q6 = ["C", "c"]
	os.system('title Questions Easy #6')
	os.system('cls')
	print(english_easy_Q6)
	UserAnswer_english_Q6 = input("Letter of your answer: ")

	if UserAnswer_english_Q6 == UserAnswer_english_Q6 in english_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		english_easy_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_7()

def english_easy_7():

	english_easy_Q7 = '''
============================================================
7. What is the opposite of "young"?
a) Fast
b) Old
c) Slow
d) Small
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q7 = ["B", "b"]
	os.system('title Questions Easy #7')
	os.system('cls')
	print(english_easy_Q7)
	UserAnswer_english_Q7 = input("Letter of your answer: ")

	if UserAnswer_english_Q7 == UserAnswer_english_Q7 in english_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		english_easy_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_8()

def english_easy_8():

	english_easy_Q8 = '''
============================================================
8. Which word means "a place to live"?
a) Shelter
b) Game
c) Picture
d) Song
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q8 = ["A", "a"]
	os.system('title Questions Easy #8')
	os.system('cls')
	print(english_easy_Q8)
	UserAnswer_english_Q8 = input("Letter of your answer: ")

	if UserAnswer_english_Q8 == UserAnswer_english_Q8 in english_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		english_easy_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_9()


def english_easy_9():

	english_easy_Q9 = '''
============================================================
9. What is the synonym of "difficult"?
a) Easy
b) Hard
c) Simple
d) Light
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q9 = ["B", "b"]
	os.syste
	os.system('title Questions Easy #4')
	os.system('cls')
	print(english_easy_Q9)
	UserAnswer_english_Q9 = input("Letter of your answer: ")

	if UserAnswer_english_Q9 == UserAnswer_english_Q9 in english_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		english_easy_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_easy_10()


def english_easy_10():

	english_easy_Q10 = '''
============================================================
10. What is the opposite of "hot"?
a) Cold
b) Warm
c) Cool
d) Mild
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q10 = ["A", "a"]
	os.system('title Questions Easy #10')
	os.system('cls')
	print(english_easy_Q10)
	UserAnswer_english_Q10 = input("Letter of your answer: ")

	if UserAnswer_english_Q10 == UserAnswer_english_Q10 in english_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice job! Get ready to choose you next category!")
		os.system('pause')
		ChooseCategory()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()



def english_medium_questions():
	english_medium_1()

def english_medium_1():
	english_medium_Q1 = '''
============================================================
1. What does "benevolent" mean?
a) Kind and generous
b) Unfriendly
c) Clever
d) Foolish
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q1 = ["A", "a"]
	os.system('title Questions medium #1')
	os.system('cls')
	print(english_medium_Q1)
	UserAnswer_english_Q1 = input("Letter of your answer: ")

	if UserAnswer_english_Q1 == UserAnswer_english_Q1 in english_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #2")
		os.system('pause')
		english_medium_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_2()

def english_medium_2():
	english_medium_Q2 = '''
============================================================
2. What is the synonym of "rapid"?
a) Slow
b) Fast
c) Calm
d) Lazy
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q2 = ["B", "b"]
	os.system('title Questions medium #2')
	os.system('cls')
	print(english_medium_Q2)
	UserAnswer_english_Q2 = input("Letter of your answer: ")

	if UserAnswer_english_Q2 == UserAnswer_english_Q2 in english_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		english_medium_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_3()

def english_medium_3():
	english_medium_Q3 = '''
============================================================
3. What is the opposite of "genuine"?
a) Fake
b) Real
c) True
d) Honest
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q3 = ["A", "a"]
	os.system('title Questions medium #3')
	os.system('cls')
	print(english_medium_Q3)
	UserAnswer_english_Q3 = input("Letter of your answer: ")

	if UserAnswer_english_Q3 == UserAnswer_english_Q3 in english_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		english_medium_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_4()


def english_medium_4():
	english_medium_4 = '''
============================================================
4. Which word means "to lower in rank"?
a) Promote
b) Demote
c) Praise
d) Award
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q4 = ["B", "b"]
	os.system('title Questions medium #4')
	os.system('cls')
	print(english_medium_4)
	UserAnswer_english_Q4 = input("Letter of your answer: ")

	if UserAnswer_english_Q4 == UserAnswer_english_Q4 in english_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		english_medium_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_5()

def english_medium_5():
	english_medium_Q5 = '''
============================================================
5. What does "diligent" mean?
a) Careless
b) Hardworking
c) Lazy
d) Unfocused
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q5 = ["B", "b"]
	os.system('title Questions medium #5')
	os.system('cls')
	print(english_medium_Q5)
	UserAnswer_english_Q5 = input("Letter of your answer: ")

	if UserAnswer_english_Q5 == UserAnswer_english_Q5 in english_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		english_medium_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_6()

def english_medium_6():
	english_medium_Q6 = '''
============================================================
6. What is the synonym of "frequent"?
a) Rare
b) Often
c) Seldom
d) Occasional
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q6 = ["B", "b"]
	os.system('title Questions medium #6')
	os.system('cls')
	print(english_medium_Q6)
	UserAnswer_english_Q6 = input("Letter of your answer: ")

	if UserAnswer_english_Q6 == UserAnswer_english_Q6 in english_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		english_medium_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_7()

def english_medium_7():
	english_medium_Q7 = '''
============================================================
7. What is the opposite of "vague"?
a) Uncertain
b) Ambiguous
c) Confusing
d) Clear
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q7 = ["D", "d"]
	os.system('title Questions medium #7')
	os.system('cls')
	print(english_medium_Q7)
	UserAnswer_english_Q7 = input("Letter of your answer: ")

	if UserAnswer_english_Q7 == UserAnswer_english_Q7 in english_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		english_medium_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_8()

def english_medium_8():
	english_medium_Q8 = '''
============================================================
8. What does "mandatory" mean?
a) Suggested
b) Choice
c) Forbidden
d) Required
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q8 = ["D", "d"]
	os.system('title Questions medium #8')
	os.system('cls')
	print(english_medium_Q8)
	UserAnswer_english_Q8 = input("Letter of your answer: ")

	if UserAnswer_english_Q8 == UserAnswer_english_Q8 in english_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		english_medium_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_9()

def english_medium_9():
	english_medium_Q9 = '''
============================================================
9. What is the synonym of "eager"?
a) Reluctant
b) Indifferent
c) Excited
d) Uninterested
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q9 = ["C", "c"]
	os.system('title Questions Medium #9')
	os.system('cls')
	print(english_medium_Q9)
	UserAnswer_english_Q9 = input("Letter of your answer: ")

	if UserAnswer_english_Q9 == UserAnswer_english_Q9 in english_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		english_medium_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_medium_10()

def english_medium_10():
	english_medium_Q10 = '''
============================================================
10. Which word means "to improve"?
a) Enrich
b) Worsen
c) Diminish
d) Weaken
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q10 = ["A", "a"]
	os.system('title Questions Medium #10')
	os.system('cls')
	print(english_medium_Q10)
	UserAnswer_english_Q10 = input("Letter of your answer: ")

	if UserAnswer_english_Q10 == UserAnswer_english_Q10 in english_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		ChooseCategory()
	

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		ChooseCategory()

def ChooseCategory():
	subject = '''
===========================================================================
CHOOSE A SUBJECT THAT YOU WANT TO ANSWER:

(MATH)
(SCIENCE)
(ENGLISH)

===========================================================================
	'''
	os.system('title Choose Choose Category')
	os.system('cls')
	print(subject)
	users_input = input("WHAT SUBJECT YOU WANT TO TAKE?: ")
	os.system('pause')

	math_Sub = ["MATH", "Math", "math"]
	science_Sub = ["SCIENCE", "Science", "science"]
	english_Sub = ["ENGLISH", "English", "english"]

	if users_input == users_input in math_Sub:
		math()

	elif users_input == users_input in science_Sub:
		science()

	elif users_input == users_input in english_Sub:
		english()

	else:
		print("Wrong answer please try again!!")
		os.system('pause')
		ChooseCategory()


def english_hard_questions():
	english_hard_1()

def english_hard_1():
	english_hard_Q1 = '''
============================================================
1. What does "ephemeral" mean?
a) Permanent
b) Temporary
c) Predictable
d) Eternal
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q1 = ["B", "b"]
	os.system('title Questions Hard #1')
	os.system('cls')
	print(english_hard_Q1)
	UserAnswer_english_Q1 = input("Letter of your answer: ")

	if UserAnswer_english_Q1 == UserAnswer_english_Q1 in english_answer_Q1:
		print("That's Correct you gain a points (+1)")
		global score

		score += 1
		print("Next Question #2")
		os.system('pause')
		english_hard_2()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_2()

def english_hard_2():
	english_hard_Q2 = '''
============================================================
2. What is the synonym of "obfuscate"?
a) Clarify
b) Simplify
c) Confuse
d) Explain
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q2 = ["C", "c"]
	os.system('title Questions Hard #2')
	os.system('cls')
	print(english_hard_Q2)
	UserAnswer_english_Q2 = input("Letter of your answer: ")

	if UserAnswer_english_Q2 == UserAnswer_english_Q2 in english_answer_Q2:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #3")
		os.system('pause')
		english_hard_3()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_3()

def english_hard_3():
	english_hard_Q3 = '''
============================================================
3. What is the opposite of "loquacious"?
a) Talkative
b) Reserved
c) Friendly
d) Honest
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q3 = ["B", "b"]
	os.system('title Questions Hard #3')
	os.system('cls')
	print(english_hard_Q3)
	UserAnswer_english_Q3 = input("Letter of your answer: ")

	if UserAnswer_english_Q3 == UserAnswer_english_Q3 in english_answer_Q3:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #4")
		os.system('pause')
		english_hard_4()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_4()


def english_hard_4():
	english_hard_4 = '''
============================================================
4. What does "ignominious" mean?
a) Honorable
b) Shameful
c) Famous
d) Lucky
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q4 = ["B", "b"]
	os.system('title Questions Hard #4')
	os.system('cls')
	print(english_hard_4)
	UserAnswer_english_Q4 = input("Letter of your answer: ")

	if UserAnswer_english_Q4 == UserAnswer_english_Q4 in english_answer_Q4:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #5")
		os.system('pause')
		english_hard_5()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_5()

def english_hard_5():
	english_hard_Q5 = '''
============================================================
5. What is the synonym of "gregarious"?
a) Lonely
b) Shy
c) Quiet
d) Sociable
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q5 = ["D", "d"]
	os.system('title Questions Hard #5')
	os.system('cls')
	print(english_hard_Q5)
	UserAnswer_english_Q5 = input("Letter of your answer: ")

	if UserAnswer_english_Q5 == UserAnswer_english_Q5 in english_answer_Q5:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #6")
		os.system('pause')
		english_hard_6()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_6()

def english_hard_6():
	english_hard_Q6 = '''
============================================================
6. Which word means "having a harmful effect"?
a) Beneficial
b) Safe
c) Noxious
d) Wholesome
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q6 = ["C", "c"]
	os.system('title Questions Hard #6')
	os.system('cls')
	print(english_hard_Q6)
	UserAnswer_english_Q6 = input("Letter of your answer: ")

	if UserAnswer_english_Q6 == UserAnswer_english_Q6 in english_answer_Q6:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #7")
		os.system('pause')
		english_hard_7()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_7()

def english_hard_7():
	english_hard_Q7 = '''
============================================================
7. What is the opposite of "ostentatious"?
a) Modest
b) Flashy
c) Lavish
d) Extravagant
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q7 = ["A", "a"]
	os.system('title Questions Hard #7')
	os.system('cls')
	print(english_hard_Q7)
	UserAnswer_english_Q7 = input("Letter of your answer: ")

	if UserAnswer_english_Q7 == UserAnswer_english_Q7 in english_answer_Q7:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #8")
		os.system('pause')
		english_hard_8()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_8()

def english_hard_8():
	english_hard_Q8 = '''
============================================================
8. What does "paradox" mean?
a) A self-contradictory statement
b) A mystery
c) An illusion
d) A false belief
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q8 = ["A", "a"]
	os.system('title Questions Hard #8')
	os.system('cls')
	print(english_hard_Q8)
	UserAnswer_english_Q8 = input("Letter of your answer: ")

	if UserAnswer_english_Q8 == UserAnswer_english_Q8 in english_answer_Q8:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #9")
		os.system('pause')
		english_hard_9()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_9()

def english_hard_9():
	english_hard_Q9 = '''
============================================================
9. What is the synonym of "prodigious"?
a) Small
b) Massive
c) Mediocre
d) Ordinary
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q9 = ["B", "b"]
	os.system('title Questions Hard #9')
	os.system('cls')
	print(english_hard_Q9)
	UserAnswer_english_Q9 = input("Letter of your answer: ")

	if UserAnswer_english_Q9 == UserAnswer_english_Q9 in english_answer_Q9:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Next Question #10")
		os.system('pause')
		english_hard_10()

	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')
		english_hard_10()

def english_hard_10():
	english_hard_Q10 = '''
============================================================
10. What does "recalcitrant" mean?
a) Obedient
b) Rebellious
c) Cooperative
d) Friendly
============================================================
	'''
	#Inside the square bracket is the correct answer
	english_answer_Q10 = ["B", "b"]
	os.system('title Questions Hard #10')
	os.system('cls')
	print(english_hard_Q10)
	UserAnswer_english_Q10 = input("Letter of your answer: ")

	if UserAnswer_english_Q10 == UserAnswer_english_Q10 in english_answer_Q10:
		print("That's Correct you gain a points (+1)")
		global score
		score += 1
		print("Nice job, you're done!!")
		os.system('pause')
 
	else:
		print("Wrong Answer! Nice Try :)) you lose a points ")
		score += 1
		os.system('pause')

mainfn()