#dictionaries

band = {
    "instrument" : "guitar",
    "name" : "Novocaine"
}

next_band = dict(instrument="piano", name="delta9")

print(band)
print(next_band)

print(type(band))
print(len(next_band))

for k,v in next_band.items():
    print (f'The {k} : {v}')


# for i in band:
#     print(i)

# Access items
print(band["instrument"])
print(band.get("name"))





# list all keys
print(band.keys())
print(next_band.keys())

# list all values
print(band.values())
print(next_band.values())

# list of key/value pairs as tuples
print(band.items())
print(next_band.items())


for value in next_band.values():
    print(value)

for key in next_band.keys():
    print(key)
for value in band.values():
    print(value)
for key in band.keys():
    print(key)


print("instrument" in band)
print("instrument" in band.keys())
print("guitar" in band.keys())

print("guitar" in band.values())
print("instrument" in band.values())

band["name"] = "Coverdale"
band["members"] = 5
band.update({"bass": "JPJ"}) #update function for dictionaries
band.update({"members": 10})

next_band["name"] = "Southwave"
next_band["members"] = 7
next_band.update({"bass": "PPx"}) #update function for dictionaries
next_band.update({"members": 9})


print(band)
print(next_band)


# removing tems in dictionary
print(next_band.pop('name'))
print(next_band)

next_band.update({'name':'Southdale'})
print(next_band)

print(next_band.popitem())
print(next_band)

next_band['name'] = "Southdale"
print(next_band)


#deleloing and clearing

print(band) 
del band["members"]  
print(band) 

# Copy method
new_band = next_band.copy()
print(new_band)

next_band.clear()
print(next_band)

next_band = dict(drums ="Dave", members=4, name="BestB")
print(next_band)


next_band["instrument"] = "Sitar"
print(next_band)

old_band = band.copy()
print(old_band)
old_band["intrument"] = "violin"
print("Good copy!")
print(band)

just_band = dict(old_band)

print(just_band, old_band)



# Nested dictionaries

one_mem = {
    'name': 'plant',
    'instrument': 'vocals'
}

two_mem = {
    "name": "Page",
    "instrument": "guitar"
}


nest_band = {
    'member1': one_mem,
    'member2': two_mem
}

print(nest_band)
print(nest_band["member1"]['name'])
print(nest_band["member1"]['instrument'])
print(nest_band["member2"]['name'])

# # Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))
nums3 = set((2,33,444))

print(nums3)
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
nums1 = {1, True, 1, False, 0}
print(nums)

print(nums1)

# # check if a value is in a set
print(2 in nums)

# # but you cannot refer to an element in the set with an index position or a key
# print(nums(0)) This gives error as the position in a set is randomized
# # Add a new element to a set
nums.add(8)
print(nums)

# # Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# # you can use update with lists, tuples, and dictionaries, too.

# # Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# # Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}


mynewset1 = one.intersection(two)
print(mynewset1) # intersection does it but kinda tedious

one.intersection_update(two)
print(one) #intersection update does it easily

# # Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two) # Remember .symmetric_difference_update() method
print(one)