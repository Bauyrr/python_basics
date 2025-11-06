# def xx (numbers):
#     x = 1
#     for i in numbers:
#         x = x * int(i)
#     return x
# numbers = input(" ").split()
# print(xx(numbers))


# def uplow (tex):
#     low = 0
#     up = 0
#     for i in tex:
#         if i.isupper():
#             up+=1
#         else:
#             low+=1
#     return up,low
# tex=input('')
# up,low = uplow(tex)
# print(up,low)


# def polindrome(n):
#     if n == n[::-1]:
#         print("да")
#     else:
#         print("нет")
# n = input("ввод: ")
# polindrome(n)




import math, time

def fun(x, y):
    time.sleep(y/1000)
    return math.sqrt(x)
print("Sample Input: ")
x = int(input())
y = int(input())

print(f"Sample output:\nSquare root of ",x," after ",y," miliseconds is ",fun(x, y))



