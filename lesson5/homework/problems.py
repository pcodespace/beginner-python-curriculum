import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.

operating_systems=["macOS", "Linux", "Windows"]
print("Operating systems before the reverse:",operating_systems)
last_length=len(operating_systems)-1
print("The last operating system in the list:",operating_systems[last_length])
operating_systems.reverse()
print("Operating systems after the reverse:",operating_systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.

school_subject=["Math", "Social Studies", "ELA", "Science"]
print("The list of subjects:",school_subject)
print("The second subject:",school_subject[1])
school_subject.sort()
print("School subjects after the alphebetical sort:", school_subject)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes=["400", "401", "403", "404", "500"]
print("List of error codes:", error_codes)
length_error_codes=len(error_codes)
print("Total number of error codes:",length_error_codes)
index_codes=error_codes.index ("403")
print("The index of 403 is:", index_codes)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programming_languages=["Java", "Python"]
random_language= random.choice(programming_languages)
print(random_language)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords=["a826hdfa", "jsf63826s", "6382sfsdsd", "ksfd63163", "7261sjsjw", "836fsf25"]
print("The list of all passwords:", passwords)
last_password = len(passwords) - 1
middle_password = int(last_password/2)
print("The middle password is:", passwords[middle_password] )
passwords.remove("a826hdfa")
print("After removing the first password:", passwords )