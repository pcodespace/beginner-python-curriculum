# if statement: runs only when the condition is true
age = int(input("What is your age: "))
if age >= 18:
    print("You can vote!")
print("Vote check complete!")

# if/else: choose one of two paths
if age <18:
    print("You can't vote yet.")

    
temp = int(input("What is the temperature outside?"))
if temp < 10:
    print("It's cold, wear a jacket.")   
else:
    print("No jacket needed.")  
    print("Weather check done.")
    #if/elif/else: handle multiple specific cases
    grade = int(input("Enter your score out of 100: "))

if grade >= 100:
    print("You got an A+.")
elif grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >=70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You failed.")    
print("Grading complete.") 