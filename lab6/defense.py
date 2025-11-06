def inst(text):
    a = 0
    b = 0
    for i in text:
        if i.isdigit():     
            a += 1
        else:
            b += 1

    return a,b

n = input("Введите строку: ")

ints, strings = inst(n)

print(ints,strings)