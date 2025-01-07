# Write a program to get the marks of student and check percentage of passed or faild 40% is passed and have atleast 33% in each subject 

mark1 = int(input("Marks in Math : "))
mark2 = int(input("Marks in Physics : "))
mark3 = int(input("Marks in Chemistry  : "))

# Checking percentage 
Total_percentage = 100*(mark1 + mark2 + mark3)/300

if(Total_percentage >= 40 ):
    print("Passed. Percentage : ",Total_percentage)
else:
    print("Failed, Better luck next time.")

if(mark2 < 33 ):
    print(" You are failed in Physics")
elif(mark1 < 33 ):
    print(" You are failed in Math")
elif(mark3 < 33 ):
    print("You are failed in Chemistry")