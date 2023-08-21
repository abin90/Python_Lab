num=int(input('Enter a number: '))
list=[]
if num==0:
    print("Enter a positive or negative integer")
elif num>0:
    for x in range(1,num+1):
         if num%x==0:
             list.append(x)
    print("Divisors of ",num," are: ",list)
else:
    for x in range(num,0):
        if num%x==0:
            list.append(x)
    print("Divisors of ",num," are: ",list)