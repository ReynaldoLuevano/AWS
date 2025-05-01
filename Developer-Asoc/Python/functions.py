def my_function():
    #Print a welcome message for users visiting the website.
    print("Welcome to our website!")

my_function()

def add_numbers(x, y):
    sum = x + y
    return sum

result = add_numbers(3,5)
print(result)

#Assign value of 10 to global variable 'x'
x = 10

def my_function2():
  # Define a local variable 'x' with a value of 5,   then print it.
  x = 5
  print('Local', x)

my_function2() # output: Local 5

# try to access variable outside of function
print('Global', x) #output: Global 10

def my_function3():
  global y
  y = 10
my_function3()

print(y)

def my_food(food = "burgers"):
  print("My favorite food is " + food)
"""
Print a message about the programmer's favorite food.
"""

# call function with 'pizza' as an argument.
my_food("pizza")

# call function with 'tacos' as an argument.
my_food("tacos")

# call function with no argument.
my_food()

def my_friend(friend_name, friend_city):
	print(f"My friend {friend_name} lives in {friend_city}.")

my_friend(friend_city='New York', friend_name='Jane')


def my_colors(*args):
    for color in args:
  	  print(color)
my_colors("red","green")

def user_info(**kwargs): 
	#Take in keyword arguments as inputs and print  out the key-value pairs.
	for key, value in kwargs.items(): 
		print(f"{key}: {value}") 

user_info(Name="Jane", Age=33, City="Paris", Language="French")

def my_key(employee):
    #Return the tenure of a given employee tuple"
    return employee[1]

employees = [('Alicia', 7.2, 40), ('Jackie', 3.5, 33), ('Gary', 9.1, 55)]
employees.sort()
print(employees)
employees.sort(key=my_key)
print(employees)