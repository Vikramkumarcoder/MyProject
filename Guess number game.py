while(True):
	i2 = 9
	i1= int(input('Guess two digits number\n')) 
	if i1==18:
		print('You won the game', i2-1)
		break
		i2=i2-1
	elif i1<18:
		print('Number is less than \n' , 'Try again!\n', i2-1)
		continue
		i2=i2-1
	elif i1>18:
		print('Number is more than required value\n' , 'Try again!\n', i2-1)
		continue
		i2=i2-1
	if i2==9:
		break
		i2=i2-1
	else:
		continue