# Calculate the Grade of the student

Mark1 = int(input("Marks in Math : "))
Mark2 = int(input("Marks in Physics : "))
Mark3 = int(input("Marks in Chemistry : "))

total_percent = ((Mark1+Mark2+Mark3)*100)/300

if (total_percent>=90):
    print(f"""Grade A+ Excellent
    Percentage : {total_percent} """)
elif (total_percent>=80):
    print(f"""Grade A Better
    Percentage : {total_percent} """)
elif (total_percent>=70):
    print(f"""Grade B Good
    Percentage : {total_percent} """)
elif (total_percent>=60):
    print(f"""Grade C 
    Percentage : {total_percent} """)
elif (total_percent>=50):
    print(f"""Grade D 
    Percentage : {total_percent} """)
elif (total_percent>=40):
    print(f"""Grade E 
    Percentage : {total_percent} """)
else:
    print(f'''You are Faild 
    Percentage : {total_percent}''')