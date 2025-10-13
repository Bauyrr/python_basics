import datetime
import math 
import json


# ex1

# def kvadraty(n):
#     for i in range(n+1):
#         yield i ** 2
# n=int(input(" "))
# for j in kvadraty(n):
#     print(j)


# ex2
# def chetnye(n):
#     for i in range(n+1):
#         if i % 2==0:
#             n=i
#             yield i
# n=int(input(" "))
# for j in chetnye(n):
#     print(j)


#ex3
# def natrichetyre(n):
#     for i in range(n+1):
#         if i % 3==0 and i % 4==0:
#             n=i
#             yield i
# n=int(input(" "))
# for j in natrichetyre(n):
#     print(j)

# ex4
# def kvadraty(n):
#     for i in range(a,n+1):
#         yield i ** 2
# a=int(input(" "))        
# n=int(input(" "))

# for j in kvadraty(n):
#     print(j)


# ex5
# def obratny(n):
#     for i in range(n, 0, -1):
#         yield i

# n=int(input("Enter number: "))
# for j in obratny(n):
#     print(j)

# ex1
# n=datetime.datetime.now() - datetime.timedelta(days=5)
# print(n)


# ex2
# a=datetime.datetime.now()
# b=datetime.datetime.now() - datetime.timedelta(days=1)
# c=datetime.datetime.now() + datetime.timedelta(days=1)
# print(b)
# print(a)
# print(c)


# ex3
# a = datetime.datetime.now()
# b = a.replace(microsecond=0)
# print(b)

# ex4
# ne pon

# ex1
# g=int(input())
# r=math.radians(g)
# print(r)


# ex2
# h=int(input())
# f1=int(input())
# f2=int(input())
# s=((f1+f2)/2)*h
# print(s)

#ex3
# a=int(input())
# b=int(input())
# s=(a * b**2) / (4 * math.tan(math.pi / a))
# print(s)

#ex4
# a=int(input())
# b=int(input())
# s=a*b
# print(s)



# Открываем и читаем JSON-файл
# with open("sample-data.json", "r") as file:
#     data = json.load(file)

# # Заголовок таблицы
# print("Interface Status")
# print("=" * 80)
# print("DN                                                 Description           Speed    MTU  ")
# print("-" * 80)

# # Проходимся по каждому элементу
# for item in data["imdata"]:
#     dn = item["l1PhysIf"]["attributes"]["dn"]
#     descr = item["l1PhysIf"]["attributes"]["descr"]
#     speed = item["l1PhysIf"]["attributes"]["speed"]
#     mtu = item["l1PhysIf"]["attributes"]["mtu"]

#     print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")

