n = int(input ('Enter any number for rows:\n')) 

binary1=int(input ('Enter one boolean variable 0 or 1\n')) 

if bool(binary1)==False:
	while (n>0):
		print(n*'*')
		n=n-1
i=0
if bool(binary1)==True:
		while (i<n):
			i=i+1
			print(i*'*')