total = 0
price=100
p=0
while(p!=5):
    age=int(input())
    p+=1
    if age<3:
        continue 
    else:
        total+=price
print(total)