def get_initial(name, force_uppercase=True):
    #name[0:1] -- 0 is the character started from and 1 is the character it will read upto.
    #if condition isnt defined by anything it is automatically a True boolean
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

firstname = input('Enter first name: ')
firstnameinitial = get_initial(firstname)

lastname = input('Enter last name: ')
#unless it is defined here it will listen to the boolean defined in the function
lastnameinitial = get_initial(lastname, False)
#() parameters go in the order of which they were defined in the function

print('Youre initials are ' + firstnameinitial + lastnameinitial)