def hello_world():
    print("Hello world!")


hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)

def multiply(num1 = 0, num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 * num2

num1 = 10
num2 = 'Help'

print(multiply(num1, num2))
    


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")

def mul_items(*args):
    print(args)
    for i in args:
        print(i)
        print(type(i))
    print(type(args))


mul_items("Anurag", "Abhishek", "Rose")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")


def multi_named(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i,j in kwargs.items():
        print(i,j)


multi_named(name="Anurag", surname="Anand")