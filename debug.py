x = 34
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print('Cant divide zero')
else:
    print('Something else went wrong')
finally:
    print('Debugged code')
print()

# this syntax is to be used when the terminal detects an error,
# traceback to the line of code whatever it may be and test the function through this conditional logic to figure out a solution