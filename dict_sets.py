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