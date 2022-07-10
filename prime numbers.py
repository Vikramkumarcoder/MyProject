nums=int(input())

for nums in range(nums):
	print(nums)
	if nums%2==0:
		continue
	if nums%3==0:
		continue
	if nums%5==0:
		continue
	if nums%7==0:
		continue
print(nums, 1, 2, 3, 5, 7)	
	