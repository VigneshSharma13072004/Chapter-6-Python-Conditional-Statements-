# Write a program to detect the message is a spam message
P1 = "Make alot of money"
P2 = "Buy this"
P3 = "Click here"
P4 = "Massage spa"
message = input("Enter the comment : ")
if((P1 in message)or(P2 in message)or(P3 in message)or(P4 in message)):
    print("Message is a spam")
else:
    print("Message is not spam")