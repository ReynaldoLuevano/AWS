my_list = ["first", "second", "third", "fourth"]

# print single element using the positive index
print(my_list[1])
# print single element using the negative index
print(my_list[-1])
# print range of values using the slice operator
print(my_list[1:3])

# initializes colors list
colors = ["orange", "yellow", "green", "blue"]

# adds purple to the end of the colors list
colors.append("purple")
# inserts red at the beginning of the colors list
colors.insert(0, "red")
more_colors = ["indigo", "pink"]
colors.extend(more_colors)
print(colors)

colors.pop()
colors.pop(0)
print(colors)

colors.remove("orange")
print(colors)
#colors.clear()
print(colors)

copied_colors = colors.copy()
copied_colors2 = colors[:]
print(copied_colors2)
print(copied_colors)

new_list = list((1, 2, 3))  # converts a tuple to a list

# sort alphanumeric string
my_list = ["car", "boat", "truck", "1", "Car"]
my_list.sort()
print("Mixed case alphanumeric sort:", my_list)

# sort with optional reverse argument
my_list.sort(reverse=True)
print("Sort with optional reverse argument:", my_list)

# sort using reverse method
groceries = ["apples", "berries", "cabbage"]
groceries.reverse()
print("groceries after reverse()", groceries)

rainfall = [2, 3, 5, 4, 4, 3, 1, 1, 2, 4, 3]
print (rainfall.index(4))  # returns the index 3 

rainfall = [2, 3, 5, 4, 4, 3, 1, 1, 2, 4, 3]
print (rainfall.count(4))  # returns the number of times 4 occurs on this list. 

#Membership
rainfall = [2, 3, 5, 4, 4, 3, 1, 1, 2, 4, 3]
print (2 in rainfall)
print (2 not in rainfall)

#Sets
myset = set([1,2,2,1,3,4])
myset2 = {1,2,3,4}
print(f'myset: {myset}') #it will print myset: {1, 2, 3, 4}
print(f'myset2: {myset2}')

print(myset.isdisjoint(myset2)) #it returns False because myset contains same elemets as myset2

wild_animals = {"pig", "lion", "koala", "kangaroo"}
farm_animals = {"cow", "chicken", "sheep", "pig"}
australian_animals = {"koala", "kangaroo"}

msg = 'Is australian animals subset of wild animals'
msg2 = 'Is wild animals subset of australian animals'
print (f'{msg} {australian_animals.issubset(wild_animals)}')
print (f'{msg2} {wild_animals.issubset(australian_animals)}')
print (wild_animals.issuperset(australian_animals))


setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}

diff_set = setB.difference(setA)
print(diff_set)

setB.difference_update(setA) #setB has been updated to include only elements contained in original setB, but not in setA.
print(setB)

setA={"Python", "JavaScript", "PHP"}
listB = ["Python", "JavaScript", "Java", "C++"]

common_set = setA.intersection(listB)
print(f'common set {common_set}')

setA={"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}
setA.intersection_update(setB)
print(setA)

setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}
sym_diff_set = setB.symmetric_difference(setA) #Inverse of Intersection
print(sym_diff_set)

print('update')
setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}

setB.update(setA) #updates setB including elements that has setA
print (setB)
print (setA)

insects = {"ant", "bee", "cricket", "dragonfly"}


# discard()
insects.discard("ant")
print ('After discard("ant"), the insects sets is:', insects)

# remove()
# remove raises an error if the specified element is not in the set
insects.remove("ant")  #change ant to some other set value and rerun
print("After remove(), the insects set includes:", insects)

insects = {"ant", "bee", "cricket", "dragonfly"}

# pop removes a random element and returns that value
removed_item = insects.pop()
print ("The removed element is", removed_item)
print ("The remaining set includes", insects)