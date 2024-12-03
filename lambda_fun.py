my_lists = [12,23,11,234,122]

squared_list = lambda my_lists : my_lists ** 2

mapped_vals = map(squared_list, [12,23,11,234,122])

print(list(mapped_vals))


my_dict = dict(name="Anurag", age= 26, height =175, personality='Special')
print(my_dict)


changing_dict = lambda my_dict: my_dict['name']
print(changing_dict(my_dict))

sum = lambda a , b: a+b
print(sum(1,2))

# checking how parameters work using lambda in a function
def checking_num(x):
    return lambda n : n + x

add_10 = checking_num(10)
add_20 = checking_num(20)


print(add_10(3))
print(add_20(22))

# Using map in a lambda function

sq_root = lambda x: int(x**(0.5))

new_list = [1, 23, 11, 123, 444, 21]

print(map(sq_root, new_list))
print(list(map(sq_root, new_list)))


print(21**2)

new_dict = {"class_name":"Physics", "class_time": "9am", "stnumber": 40}

dict_val_changer = lambda new_dict: new_dict['stnumber']

print(dict_val_changer(new_dict))

print(dict_val_changer({'class_name': 'Math', "class_time":"10am", "stnumber":45}))



