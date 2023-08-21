string=input("Enter a string: ")
string=string.casefold()
if(string==string[::-1]):
    print("The entered string is Palindrome")
else:
    print("The entered string is not Palindrome")