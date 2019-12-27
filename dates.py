from datetime import datetime, timedelta

# timedelta goes from microseconds up to weeks

date = datetime.now()
# print('Todays date is: ' + str(date))

# print('Todays date is: '+str(date.day)+'/'+str(date.month)+'/'+str(date.year))
# add_day = timedelta(days=1)
# tomorrow = date + add_day
# print('Tomorrows date will be: ' + str(tomorrow.day))

# add_hours = timedelta(hours=12)
# hours = date - add_hours
# print('The time was ' + str(hours) + ' twelve hours ago.')

birthday = input('Enter Birthday dd/mm/yyyy: ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Your Birthday: ' + str(birthday_date))