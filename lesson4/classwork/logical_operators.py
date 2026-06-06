age = int(input("What is your age? "))
print("age",age)

has_ticket = input("Do you have a movie ticket?(yes/no)")

if age >= 13 and has_ticket == "yes":   # AND: both conditions are true
    print("You can enter the PG-13 movie.")
else:
    print("Sorry, you can't see the movie.")
print("Movie check complete.")

has_pass = input("Do you have a buss pass? (yes/no)")
has_coins = input("Do you have coins to pay? (yes/no)")

if has_pass == "yes" or has_coins == "yes":  #OR: at least one condition is true
    print("You can ride the bus.")
else:
    print("Sorry, you cannot ride the bus.")
print("Bus check complete.")

homework_done = input("Did you do your homework? (yes/no)")

if not homework_done == "yes":
    print("Go finish your homework!")
else:
    print("Nice job! You're all done.")
print("Homework check complete.")

# You can combine multiple logical operators.
has_permission = input("Do you have a signed permision slip?(yes/no) ")
has_chaperone = input("Do you have a chaperone? (yes/no)")
is_sick = input("Are you sick today? (yes/no)")

if has_permission == "yes" and has_chaperone == "yes" and not is_sick == "yes":
    print("You can go on a field trip.")
elif is_sick == "yes":
    print("Sorry, you can't go on the field trip.")
elif has_permission == "yes" or has_chaperone:
    print("You are almost ready, but you are missing something.")
else:
    print("You need a permission slip and a chaperone.")
print("Field trip check complete.")