from os import name


def fullName(myName):

    fName = input('Enter Your First Name: ')
    lName = input('Enter Your Last Name: ')

    name = str(fName) + ' ' + str(lName)
    print(f"Your Full Name is {name}")
    return name

fullName(name)



