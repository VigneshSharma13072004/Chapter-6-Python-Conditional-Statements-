#  Write a program to find weather given username contains less then 5 characters or not

username = input("Enter your name : ")

if (len(username)>5):
    print("Valid Username ")
else:
    print("Invalid username. Your user name contain more than 5 characters")