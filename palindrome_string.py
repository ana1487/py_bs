# Palindrome Number1

number = 1123412133

numb_str = str(number)

rev_str = '' #Set this as a list instead of a string
for i in numb_str:
    rev_str = i + rev_str
    #if use of list is needed using rev_str.index(0, i)

print(str(rev_str))





