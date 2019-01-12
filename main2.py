"""WORKOUT WITH PYTHON GYM BOT!!This program will allow a user to log 
exercise completed, sets, reps, wieght and when completed output the a 
workout summary of total excercises total sets, total reps and total 
weight lifted"""

"""This is V 1.0 I'm new to python so I'd like to eventually use json to
store all the user input data and keep track overtime - if anyone more
experianced than me can help I'm all up for the help!""" 

import time
from threading import Thread


#Dict & lists for the program.
user_exercise_list = {}
user_sets = []
user_reps = []
user_weights = [] 

#Greeting to user
print(
	"Hello, you must love computers AND staying healthy!"
	"\nOnly a crazy python programmer would use python to stay healty!")
	
#Prompts for user name. 
user_name = input("\nWhat's your name?" " ")

#Greeting to user using the now aquired user name. 
print(
	"\nWelcome " +user_name.title()+ 
	" to Champ's Python Workout Logger!"
	"\nYou can type quit at any time to exit the program" )

#Champ's Gym Bot waking up! 
def bot_wake_up():
	time.sleep(2)
	print("\nHold on let me let me wake up!...It's too early for this...")
	time.sleep(2)
	print("\n........almost........")
	time.sleep(2)
	print("\nOk, (yawn) - I'm ready to log yo data! Lets get started!")
	time.sleep(1)
	print("-------------------------------------------------------------")
	print("           " " NOW ENTERING GYM BOT BEAST MODE" "           ")
	print("-------------------------------------------------------------")
	
Thread(target = bot_wake_up()).start()




#Greeting continued...
print(
	  "\nTo enter your exercises please enter one at a time!\n"
	  "\nWe will go through each one and add sets, reps & weight!\n"
	  "\n**Don't worry it's super easy - your a programmer!**\n")

def exercise_logging():
	"""Function to store exercise, sets, reps and weight in a dict."""	
	while True:
		print("-------------------------------------------------------")
		print("           "       " ENTER EXERCISES" "                ")
		print("-------------------------------------------------------")
		exercise = input(
						"\nWhat exercises did you do today? Or type quit"
						" to get your WORKOUT SUMMARY!" 
						"\nEnter the exercise then press enter"
						" to continue------->" " ")
		if 'quit' in exercise: 
			break
		
		print("-------------------------------------------------------")
		print("           "       " ENTER TOTAL SETS" "               ")
		print("-------------------------------------------------------")
		sets = input("\n**How many sets did you do?**-------->" " " )
		if 'quit' in sets:
			break
			
		print("-------------------------------------------------------")
		print("           "       " ENTER REPS" "                     ")
		print("-------------------------------------------------------")
		reps = input(
					"\n**Now, please enter the reps for each set.**\n"
					"\nFor example enter 8 8 10 10 (notice the spaces)."
					"\nThis would mean you did 8 reps for first set..."
					"2nd...3rd...and finally" 
					" 10 for your 4th set.------->" " ")
		if 'quit' in reps:
			break
		print("-------------------------------------------------------")
		print("           "       "ENTER WEIGHT LIFTED" "            ")
		print("-------------------------------------------------------")
		weight = input(
					  "\n**Now, enter the weight for each set in the same"
					  " manner 50 80 90 100 (notice the spaces).**\n"
					  "\nThis would mean you lifted 50lbs for your 1st" 
					  " set...2nd...3rd..."
					  "\nand finally 100lbs for your 4th set------->" " ")
		if 'quit' in weight: 
			break
	  #Stores user exercsie inputs into a dict 
		user_exercise_list[exercise] = ''
		
	  #Converts a multi-numbered user input 'string' into integers,
	  #Stores the input in the appropriate list for later outsput summary. 	  
		for y in sets:
			sets1 = sets.split()
   
		for x in sets1:
			sets2 = int(x)
			user_sets.append(sets2)
		
		for y in reps:
			reps1 = reps.split()
   
		for x in reps1:
			reps2 = int(x)
			user_reps.append(reps2)
		
		for y in weight:
			weight1 = weight.split()
   
		for x in weight1:
			weight2 = int(x)
			user_weights.append(weight2)
			
			
		
def workout_summary():
	"""Outputs a WORKOUT SUMMARY to the user!"""
	print("\n--------------------------------------------------")
	print("\n           " "WORKOUT SUMMARY" "                ")
	print("\n--------------------------------------------------")
	print(
		 "\n<<<<<Good job " +user_name.title()+ 
		 ", you completed the following exercises>>>>> \n")
	for key in user_exercise_list:
		print("** " +key.title()+ " **")
	
											
	user_reps_total = sum(user_reps)
	user_weights_total = sum(user_weights)
	user_set_total = sum(user_sets)	
	
	#Tell user total amount of sets completed in wokout
	print("\nYou completed the following total number of sets: ")	
	print("** " +str(user_set_total)+ " **")	
	#Tell you user total amount of reps in their workout
	print(
		 "\nYou pumped put a total of ** " +str(user_reps_total)+ 
		 " ** reps!")	  
	#Tell user total amount of weight lifted during workout.
	print(
		 "\nHoly crap you lifted ** " +str(user_weights_total)+ 
		 " ** pounds during your workout - great job!")


#Call for functions to run program
exercise_logging()
workout_summary()





