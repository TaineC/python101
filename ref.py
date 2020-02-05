import pdb

#python3 -i ref.py -- interactive shell

def add(first,second):
    return first + second
#>> call function(condition(s))



#python debugger -- (Pdb) n >> return broken code
add(2,1)
# pdb.set_trace()
# add(1,'2')



#dict comprehension
fruit = [
    {'name': 'apple', 'price': 20},
    {'name': 'orange', 'price': 30},
    {'name': 'avocado', 'price': 15},
]

print({fruit['name']: fruit['price'] for fruit in fruit})
