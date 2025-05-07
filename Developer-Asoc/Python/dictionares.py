inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2
}

print (inventory)

inv_with_dups = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "apples": 1
}

print (inv_with_dups)

inventory = {
    "apples": {"prod":"Oregon", "inventory": 4},
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

num_dates = inventory["dates"]
#num_apples = inventory["apples"]["inventory"]
num_apples = inventory["apples"]

print (f"There are {num_dates} dates and {num_apples['inventory']} apples in the inventory.")


#updating inventory, adding a new item, if the key already exists update else create a new element
inventory.update({"dates": 2})
inventory.update({"avocado": 2})
print ("The updated dictionary items are", inventory)

inventory = {
    "apples": {"prod":"Oregon", "inventory": 4},
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

print (inventory.get("apples"))

# print keys in the dictionary
inv_keys = inventory.keys()
print(inv_keys)

# print values in the dictionary
inv_values = inventory.values()
print(inv_values)

# print items in the dictionary
inv_items = inventory.items()
print(inv_items)

#copying the dictionary and settings values to 0
copied_inv = inventory.copy()
print("The copied_inv holds these key-value pairs:", copied_inv)

#copying the dictionary and settings values to 0
new_store_inv = inventory.fromkeys(inv_keys, 0)
print("The new_store_inv holds these key-value pairs:", new_store_inv)

inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10,
    "avocado": 2
}

removed_item = inventory.pop("apples")
print ("The item that was removed with pop() was", removed_item)
print("The remaining dictionary items are", inventory)

last_item = inventory.popitem()
print ("The item that was removed with popitem() was last item", last_item)
print ("The remaining dictionary items are", inventory)

