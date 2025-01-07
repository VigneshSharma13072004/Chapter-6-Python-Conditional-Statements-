# Check the input name is there in list or not 
list = ["Harry","Ded","Vignesh","Jeet"]
name = input("Enter the name : ")
if (name in list):
    print(f" {name} is present in the list")
else:
    print("Error")