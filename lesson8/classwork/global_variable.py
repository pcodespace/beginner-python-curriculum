pet = "cat"

def show_pet():
    print("The pet is", pet)

show_pet()

def adopt_parrot():
    global pet  # Before changing a global variable inside a function, you need to do this.
    pet = "parrot"

adopt_parrot()
show_pet()