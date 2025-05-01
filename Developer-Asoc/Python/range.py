# This is a comment
# into your IDE
x=5
x*=3
y = 4.3
z = 8j
name = 'Jane'
age = 36

for counter in range(5):
    print ("Hello world", counter)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print (number)

count = 1
while count <= 5:
    print(count)
    count += 1
    
print (x)
print(f'Hello, {name}. You are {age}.')


print(type(x))
print(type(y))
print(type(z))

x = float(3)
y = str(2)
z = int(2.8)

print(x)
print(y)
print(z)

mystring = "Hello, World!"
print (mystring[2:5])
print(mystring[:5])

mystring = " Hello, World! "
print(mystring.strip())

mystring = " Jjonathan Smith"
print(mystring.strip().replace("Jjonathan", "Jonathan"))

zipcode = 98121
userinfo = "My name is Terry, and my zip code is {}"
print(userinfo.format(zipcode))

txt = "The total amount is {:+.2f} dollars."
print(txt.format(59000))

name = 'Terry'
age = 28
country = 'Poland'
info = 'Name:\t{}\nAge:\t{}\nCountry:\t{}'.format(name, age, country)
print(info)

customername = input("What's your name?")
print("Welcome " + customername)

x = 11
y = 200
if y > x:
    print('y is greater than x')
elif y == x:
    print('y and x are equal')
else:
    print('x is greater than y')