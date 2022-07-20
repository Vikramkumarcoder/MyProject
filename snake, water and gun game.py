import random

print("Welcome to Snake, Water and Gun game\n")
choice=input ("""Choose any one:
1 for Play
2 for Rules\n""")

object= ["s", "w", "g"]
x=9
score1=0
score2=0
if choice=="1":
	while (x>=0):
		yourinput=input("""Choose any one:
"s" for snake
"w" for water
"g" for gun\n""")
		
		computer= random. choice(object)
		
		if computer=="w" and yourinput=="s":
			print("You won!")
			print("The computer's choice: water")
			print("Your choice: snake")
			print("The remaining rounds:", x)
			x-=1
			score1+=100
		
		elif computer=="w" and yourinput=="g":
			print("You lose!")
			score2+=100
			print("The computer's choice: water")
			print("Your choice: gun")
			print("The remaining rounds:", x)
			x-=1
		
		elif computer=="g" and yourinput=="s":
			print("You lose!")
			score2+=100
			print("The computer's choice: gun")
			print("Your choice: snake")
			print("The remaining rounds:", x)
			x-=1
	
		elif computer=="g" and yourinput=="w":
			print("You won!")
			score1+=100
			print("The computer's choice: gun")
			print("Your choice: water")
			print("The remaining rounds:", x)
			x-=1
		
		elif computer=="s" and yourinput=="g":
			print("You won!")
			print("The computer's choice: snake")
			print("Your choice: gun")
			print("The remaining rounds:", x)
			x-=1
			score1+=100
		
		elif computer=="s" and yourinput=="w":
			print("You lose!")
			score2+=100
			print("The computer's choice: snake")
			print("Your choice: water")
			print("The remaining rounds:", x)
			x-=1
		
		elif computer=="w" and yourinput=="w":
			score1+=50
			score2+=50
			print("Draw!")
			print("The computer choice: water")
			print("Your choice: water")
			print("The remaining rounds:", x)
			x-=1
		
		elif computer=="s" and yourinput=="s":
			print("Draw!")
			score1+=50
			score2+=50
			print("The computer's choice: snake")
			print("Your choice: snake")
			print("The remaining rounds:", x)
			x-=1
		
		elif computer=="g" and yourinput=="g":
			score1+=50
			score2+=50
			print("Draw!")
			print("The computer choice: gun")
			print("Your choice: gun")
			print("The remaining rounds:", x)
			x-=1
		
		else:
			print("Check your input!")
			print("The remaining rounds:", x)
			print("Computer's choice:", computer)
		
	print("\nYour score:    The computer's score:\n\n","  ",  
	               score1, "                ", score2,"\n")
	
	if score1>score2:
		print("Congratulation! You won the game.")
	
	elif score1<score2:
		print("Sorry! You lose.\nTry again!")
		
	elif score1==score2:
		print("Draw!")
		
elif choice=="2":
	print("""The person that plays the strongest  “object” is the winner of the game.
Here we have its Binit version where Binit will choose any one object from snake ,water or gun . water will win from gun , gun will win from snake, snake will win from water.
If you win then 100 points is awarded.
If draw then 50 points is awarded to both.
If You lose computer will get 100 points""")

else:
	print("Please check your input")