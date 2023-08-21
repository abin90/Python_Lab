import random
num=int(input("Guess a number between 1 and 9: "))
random_num=random.randrange(1,10);
print("The generated random number is ",random_num)
if num==random_num:
    print("You guessed exactly right")
elif num>random_num:
    print("You guessed too high")
else:
    print("You gussed too low")


