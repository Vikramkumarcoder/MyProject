# This prograam justify according to their age 
#whether a person can get driving licence or not.
print('What is your age')
age = int(input())
if age>100 or age<7:
	print('invalid age')

elif age>18:
	print('You can drive👍')

elif age==18:
	print('We will think 🙏')

else:
	print('You cannot drive👎')		
