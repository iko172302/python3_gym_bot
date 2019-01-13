"""This is a pyhthon Gym logger! Allows user to enter unlimited exercises, sets, reps and weight and outputs
the total sets, total reps, total weight and creates a .txt file to save the date for the user"""

"""I would like to update it to grab th previous stats from the last log and manipulate that data for 
user goals i.e. 'Great job you lifted xxxxx pounds more than last time!' But, I'm still new to that"""

import time
from threading import Thread
import datetime
from operator import mul


#Dict, lists, filename, variables for the program.
user_exercise_list = {}
user_sets = []
user_reps = []
user_weights = [] 
filename = 'user_data.txt'
now = datetime.datetime.now()

# ~ #Greeting to user
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
	time.sleep(1)
	print("------------------------------------------------")
	print("     " " NOW ENTERING GYM BOT BEAST MODE" "     ")
	print("------------------------------------------------")
	time.sleep(1)
	
Thread(target = bot_wake_up()).start()


#Greeting continued...
print(
     "\nTo enter your exercises please enter one at a time!\n"
     "\nWe will go through each one and add sets, reps & weight!\n"
     "\n**Don't worry it's super easy - your a programmer!**\n")

def exercise_logging():
	"""Function to store exercise, sets, reps and weight in a dict."""	
	while True:
		print("--------------------------------------")
		print("       " " ENTER EXERCISES" "         ")
		print("--------------------------------------")
		exercise = input(
				"\nWhat exercises did you do today? Or type quit"
				" to get your WORKOUT SUMMARY!" 
				"\nEnter the exercise then press enter"
				" to continue------->" " ")
		if 'quit' in exercise: 
			break
		
		print("--------------------------------------")
		print("        " "ENTER TOTAL SETS" "        ")
		print("--------------------------------------")
		sets = input("\n**How many sets did you do?" " ")
		if 'quit' in sets:
			break
			
		print("-------------------------------------")
		print("        "  " ENTER REPS" "           ")
		print("-------------------------------------")
		reps = input(
			     "\n**Now, please enter the reps for each set.**\n"
			     "\nFor example enter 8 8 10 10 (notice the spaces)."
			     "\nThis would mean you did 8 reps for first set..."
			     "2nd...3rd...and finally" 
			     " 10 for your 4th set.------->" " ")
		if 'quit' in reps:
			break
		print("-------------------------------------")
		print("      "  "ENTER WEIGHT LIFTED" "     ")
		print("-------------------------------------")
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
		user_sets1 = list(map(int, sets.split()))
		user_sets.append(user_sets1)
		
		
		user_reps1 = list(map(int, reps.split()))
		user_reps.append(user_reps1)
		
		
		user_weights1 = list(map(int, weight.split()))
		res = list(map(mul, user_reps1, user_weights1))
		user_weights.append(res)
		
def workout_summary():
	"""Outputs a WORKOUT SUMMARY to the user!"""
	print("-----------------------------------------")
	print("             " "WORKOUT SUMMARY" "       ")
	print("-----------------------------------------")
	print(
	     "\n<<<<<Good job " +user_name.title()+ 
	     ", you completed the following exercises>>>>> \n")
	
		 
	for key in user_exercise_list:
		print("** " +key.title()+ " **")
		
	#Calculates all data sets, reps, wieght lifted 	
	user_reps_total1 = sum(user_reps, [])
	user_reps_total2 = sum(user_reps_total1)
		
    		
	user_sets_total1 = sum(user_sets, [])
	user_sets_total2 = sum(user_sets_total1)
	
	
	user_weights_total1 = sum(user_weights, [])
	user_weights_total2 = sum(user_weights_total1)

				
	#Tell user total amount of sets completed in wokout
	print("\nYou completed the following total number of sets: \n")	
	print("** " +str(user_sets_total2)+ " **")	
	#Tell you user total amount of reps in their workout
	print(
	     "\nYou pumped put a total of ** " +str(user_reps_total2)+ 
	     " ** reps!")	  
	##Tell user total amount of weight lifted during workout.
	print(
	     "\nHoly crap you lifted ** " +str(user_weights_total2)+ 
	     " ** pounds during your workout - great job!")
		 		 
		 
def storing():
	"""Store the workout summary in a text file. Every time the user
	logs with this program it will add the date & time and summary 
	to the ext file""" 
	
		
	with open(filename, 'a') as ud_1:
		
		ud_1.write("***NEW WORKOUT LOG ENTRY***" +str(now)+ "\n")		
		ud_1.write("\nYou completed the following exercsies: \n")
		
		for key in user_exercise_list:
			ud_1.write("\n** " +key.title()+ " **")	
				   
	with open (filename, 'a') as ud_1:
		
		user_reps_total1 = sum(user_reps, [])
		user_reps_total2 = sum(user_reps_total1)
			
    		
		user_sets_total1 = sum(user_sets, [])
		user_sets_total2 = sum(user_sets_total1)
		
	
		user_weights_total1 = sum(user_weights, [])
		user_weights_total2 = sum(user_weights_total1)
		
		
		
		ud_1.write("\nYou completed ** "
			  +str(user_sets_total2)+ " ** total sets.\n")			
		ud_1.write("\nYou completed ** " 
			  +str(user_reps_total2)+ " ** total reps.\n")				
		ud_1.write("\nYou lifted ** " 
			  +str(user_weights_total2)+ " ** total pounds.\n")
		
		
	print("\n--------------------------------------")
	print("\n         " "WORKOUT SUMMARY" "        ")
	print("\n               " "FOR" "              ")
	print("\n         " +user_name.upper()+ "      ")
	print("\n         " "RECORED & STORED" "       ")
	print("\n--------------------------------------")					  
	

#Call for functions to run program
exercise_logging()
workout_summary()
storing()




