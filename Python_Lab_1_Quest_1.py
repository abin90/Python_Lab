from datetime import datetime
name=input("Enter your name: ")
age=int(input("Enter your age: "))
current=datetime.now()
current_year=int(current.strftime("%Y"))
year=(100-age)+current_year
print("Welcome "+name+" you will be 100 years old in "+str(year))