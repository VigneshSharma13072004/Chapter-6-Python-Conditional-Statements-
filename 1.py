# Write a program to find greatest of all four  number in the input 

N1 = int(input("Enter the number 1 : "))
N2 = int(input("Enter the number 2 : "))
N3 = int(input("Enter the number 3 : "))
N4 = int(input("Enter the number 4 : "))

if (N1>N2 and N1>N4 and N1>N3):
    print(f" {N1} is the Greatest number among all entered numbers.")
elif(N2>N1 and N2>N3 and N2 > N4):
  print(f" {N2} is the Greatest number among all entered numbers.")
elif(N3>N1 and N3>N4 and N3>N2):
  print(f" {N3} is the Greatest number among all entered numbers.")
else:
   print(f" {N4} is the Greatest number among all entered numbers")