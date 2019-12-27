# name = input('Your Name: ')
# print('Hello ' + name.upper())

first_name = 'Taine'
last_name = 'Collins'
# print('Hello my Name is ' + first_name + ' ' + last_name)

# name = input('Your Name: ')
# print('Hello\n{0} {1}'.format(first_name, last_name))

# the 'f' function does not run properly -- some kind of syntax error with it for Python 3.8
output = f'Hello, {first_name} {last_name}'
# output = f'testing'
print(output)