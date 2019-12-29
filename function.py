from datetime import datetime

# function
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

print_time('start')

# loop
for x in range(0,10):
    print(x)

print()
print_time('end')

