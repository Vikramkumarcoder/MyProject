# Lottery number finder

while True:
	i=int(input('Enter your 3 digits lottery number\n'))
	if i>101 and i<201:
		print('Congratulation you have won $100000000\n')
		break
	else:
		print('Try again!\n')
