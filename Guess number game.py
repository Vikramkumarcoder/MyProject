chance = 9
while True:
    user_input = int(input('Guess two digits number:\n'))
    if user_input == 18:
        print("You won the game\nLeft chances:", chance)
        break
    if chance == 0:
        print("Game Over")
        break
    elif user_input < 18:
        print('Number is less than the required value\nTry again!\nLeft chances:', chance)
        chance = chance - 1
    elif user_input > 18:
        print('Number is more than the required value\nTry again!\nLeft chances:', chance)
        chance = chance - 1
