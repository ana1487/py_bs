

val = 1
while val <=10:
    print(val)
    if val == 5:
        break
    val +=1

while val<=10:
    val +=1
    if val == 5:
        continue
    print(val)
else:
    print("Value is now equal to " + str(val))


while val <= 10:
    val += 1
    if val == 5:
        continue
    print(val)
else:
    print("Value is now equal to " + str(val))

names = ["Dave", "Sara", "John"]
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "Sara":
        break
    print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)

for x in range(4):
    print(x)

for x in range(2, 4):
    print(x)

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")