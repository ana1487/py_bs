
def try_rec(num):
    print('parameter:', num)
    if(num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return try_rec(total)




mynewtotal = try_rec(0)
print(mynewtotal)