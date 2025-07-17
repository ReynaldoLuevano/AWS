#creating a list
fruit=['appels','oranges', 'bananas']
vegetables=[]
candies = list()

#printing
print(fruit)
print(fruit[2])
print(fruit[-1])

#updating
fruit.append('kiwi')
print(fruit)

fruit.insert(0,'grapes')
print(fruit)

#sorting without modifiying
print(sorted(fruit))

#sorting modifiying
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)

#deleting
del fruit[0]
print(fruit)
fruit.remove('kiwi')
print(fruit)

#popping out
eaten_fruit=fruit.pop()
print(eaten_fruit)
print(fruit)
eaten_fruit=fruit.pop(0)
print(eaten_fruit)
