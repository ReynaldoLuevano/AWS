import my_module
import math
import datetime

#from my_module import *
#from my_module import add_numbers

total = my_module.add_numbers(1,2,3)
print(total)

for x in dir(math):
    print(x)

#Retrieves the description of the library
print(math.__doc__)

#working with infinity
print (math.inf)
print (math.inf > 1000)
print (-math.inf > 0 )


timestamp_date = datetime.date.fromtimestamp(1682350249)
print (timestamp_date)

today = datetime.date.today()
now = datetime.datetime.now()
past_date = datetime.datetime(2015, 3, 14, 9, 26)
print (today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) # weekday returns the day of week as a number
                       # Monday  is 0, Tuesday is 1, and so on.
                        
start_date = datetime.date(2023, 7, 15) # known date
end_date = start_date + datetime.timedelta(weeks=2) #unknown date

print(start_date)
print (end_date)

new_date_obj = date.fromisoformat("2023-07-15")
print (new_date_obj)

date_string = "1/1/2000"
date_format = "%m/%d/%Y"

new_date = datetime.strptime(date_string, date_format)
print (new_date)



new_date = datetime(2020, 7, 31)
print (new_date.strftime("%B"))