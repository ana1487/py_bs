# def convert_to_snake_case(pascal_or_camel_cased_string):

#     snake_cased_char_list = [
#         '_' + char.lower() if char.isupper()
#         else char
#         for char in pascal_or_camel_cased_string
#     ]

#     return ''.join(snake_cased_char_list).strip('_')

# def main():

#     print(convert_to_snake_case('IAmAPascalCasedString'))

    

# main()


#Understood three main things, using .join() to join everything in a list, strip(), and list comprehension
def pascal_case(string_input):
    converted_to_pascal = [
        '_'+char.lower()
        if char.isupper() 
        else char
        for char in string_input
    ]
    return''.join(converted_to_pascal).strip('_')
    # print(converted_to_pascal)


print(pascal_case("helloMyNameIsAnuraG"))



