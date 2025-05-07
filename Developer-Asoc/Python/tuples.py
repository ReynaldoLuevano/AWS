tuple_w_brackets = (2, 3, 4)
tuple_no_brackets = 2, 3, 4
tuple_w_brackets_one = (1,)
tuple_no_brackets_one = 1,

print (type(tuple_w_brackets))
print (type(tuple_no_brackets))
print (type(tuple_w_brackets_one))
print (type(tuple_no_brackets_one))

print(tuple_w_brackets[0])
print(tuple_w_brackets[-1])

my_tuple = (1, 2, 3, 4, 1, 2, 3, 4)

print (my_tuple.count(1))  # the number of times 1 appears in the tuple
print(my_tuple.index(2))   # the index of the first occurence of a 2

purchase = ("product-1", 2, "6-1-2023", 5.99)

item, quantity, date, price  = purchase

print(item)
print(quantity)
print(date)
print(price)

tuple1 = (1, 2, 3)

repeat_tuple = tuple1*2
print (repeat_tuple )