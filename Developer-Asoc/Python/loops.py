names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

for name in names:
    name = name.title()
    print (f"Hello, {name}!")

for name in names: print(f"Hello, {name.title()}")

for i in range(len(names)):
    print (f"{names[i]} is at position {i}")

for i in range(len(names)):
    print (f"{names[i]} is at position {i}")

for i in range(len(names)):
        name =  names[i].title()
        print (f"{i+1}.{name}")

for i, name in enumerate(names):
    print (f"{i}: {name.title()}")


sales_wk1 = {
    "Monday": 10,
    "Tuesday": 10,
    "Wednesday": 5,
    "Thursday": 5,
    "Friday": 15,
    "Saturday": 20,
    "Sunday": 15
}

total_sales = 0

for k in sales_wk1:
    total_sales += sales_wk1[k]

print (f"TotalSales: {total_sales}")

#Students

students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]

for student in students:
    # grades holds the grades list for the loops current iteration
    grades = student['grades']
    # sum of grades divided by length of list is an average calculation
    avg_grade = sum(grades) / len(grades)
    # creates a new key-value for each student
    student['avg_grade'] = round(avg_grade,2)

print (students)


inventory = {
    "apples": {"prod":"Forest", "inventory": 4},
    "bananas": {"prod":"Costa", "inventory": 5},
    "coconuts": {"prod":"Beach", "inventory": 6},
    "dates": {"prod":"Dessert", "inventory": 7},
}


#añadir un nuevo valor al Diccionario
inventory["watermelons"] = {"prod":"Field", "inventory": 10}

print("inventory nuevo")
print(inventory)

#ejemplo de creación de un array a partir de otro
numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]
doubled_numbers = [n*2 for n in numbers]
print (doubled_numbers)

#ejemplo de creación de un array a partir de otro con condicion
numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]
doubled_highs = [n*2 for n in numbers if n*2 >= 20]
print (doubled_highs)

#ejemplo de creación de un dict (Dict Comprehensions)
names = ["Alice", "Bob", "Carlos", "Olivia", "Jane"]
ages = [ 27, 32, 56, 47, 29]

people = {key: value for key, value in zip(names, ages)}

print (people)