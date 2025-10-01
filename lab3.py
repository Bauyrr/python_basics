import itertools
import math
import random



# ex1

# class StringKeeper:
#     def __init__(self):
#         self.s = ""

#     def getString(self):

#         self.s = input("Введите строку: ")

#     def printString(self):

#         print(self.s.upper())

# if __name__ == "__main__":
#     sk = StringKeeper()
#     sk.getString()
#     sk.printString()
    
    
    
    
# EX2

# class Shape:
#     def __init__(self):
#         pass

#     def area(self):
#         return 0


# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length


# if __name__ == "__main__":
#     s = Shape()
#     print("Площадь фигуры:", s.area())

#     sq = Square(5)
#     print("Площадь квадрата:", sq.area())
    
    
    
#EX3

# class Shape:
#     def __init__(self):
#         pass

#     def area(self):
#         return 0


# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# if __name__ == "__main__":
#     length = int(input("длинa: "))
#     width = int(input("ширинa: "))

#     rect = Rectangle(length, width)
#     print("Площадь:", rect.area())



#EX4
# import math

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Координаты точки: {self.x}, {self.y}")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


# if __name__ == "__main__":

#     x1 = float(input("x1 "))
#     y1 = float(input("y1 "))
#     p1 = Point(x1, y1)

#     x2 = float(input("x2: "))
#     y2 = float(input("y2: "))
#     p2 = Point(x2, y2)

#     p1.show()
#     p2.show()

#     print("Расстояние между точками:", p1.dist(p2))


#EX5
# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Пополнение: {amount}. Новый баланс: {self.balance}")
#         else:
#             print("Сумма должна быть положительной!")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостаточно средств! Операция отклонена.")
#         elif amount <= 0:
#             print("Сумма должна быть положительной!")
#         else:
#             self.balance -= amount
#             print(f"Снятие: {amount}. Новый баланс: {self.balance}")


# if __name__ == "__main__":
#     owner = input("Введите имя владельца счёта: ")
#     acc = Account(owner)

#     while True:
#         action = input("\nВыберите действие: deposit / withdraw / exit: ").lower()
#         if action == "deposit":
#             amount = float(input("Введите сумму для пополнения: "))
#             acc.deposit(amount)
#         elif action == "withdraw":
#             amount = float(input("Введите сумму для снятия: "))
#             acc.withdraw(amount)
#         elif action == "exit":
#             print(f"До свидания, {acc.owner}! Ваш баланс: {acc.balance}")
#             break
#         else:
#             print("Неверная команда!")





#EX6
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# if __name__ == "__main__":
#     numbers = list(map(int, input("Введите числа через пробел: ").split()))
#     primes = list(filter(lambda x: is_prime(x), numbers))
#     print("Простые числа:", primes)


#EX7
# def grams_to_ounces(grams):
#     return 28.3495231 * grams


# if __name__ == "__main__":
#     grams = float(input("Введите массу в граммах: "))
#     print(f"{grams} грамм = {grams_to_ounces(grams)} унций")


#EX8
# def fahrenheit_to_celsius(f):
#     return (5 / 9) * (f - 32)


# if __name__ == "__main__":
#     f = float(input("Введите температуру в Фаренгейтах: "))
#     c = fahrenheit_to_celsius(f)
#     print(f"{f}°F = {c:.2f}°C")


#EX9
# def solve(numheads, numlegs):
#     for chickens in range(numheads + 1):
#         rabbits = numheads - chickens
#         if 2 * chickens + 4 * rabbits == numlegs:
#             return chickens, rabbits
#     return None, None


# if __name__ == "__main__":
#     heads = int(input("Введите количество голов: "))
#     legs = int(input("Введите количество ног: "))

#     chickens, rabbits = solve(heads, legs)
#     if chickens is not None:
#         print(f"Курицы: {chickens}, Кролики: {rabbits}")
#     else:
#         print("Решения нет!")



#EX10
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def filter_prime(numbers):
#     return [x for x in numbers if is_prime(x)]


#EX11
# import itertools

# def print_permutations(s):
#     perms = itertools.permutations(s)
#     for p in perms:
#         print("".join(p))

# if __name__ == "__main__":
#     text = input("Введите строку: ")
#     print("Все перестановки:")
#     print_permutations(text)






    
    
 
 
#EX12
#def reverse_words(sentence):
#     words = sentence.split()
#     reversed_sentence = " ".join(reversed(words))
#     return reversed_sentence

# if __name__ == "__main__":
#     text = input("Введите предложение: ")
#     print("Результат:", reverse_words(text))


# 13. 
# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False

# if __name__ == "__main__":
#     print(has_33([1, 3, 3]))      
#     print(has_33([1, 3, 1, 3]))  
#     print(has_33([3, 1, 3]))      


# 14
# def spy_game(nums):
#     code = [0, 0, 7]
#     idx = 0
#     for n in nums:
#         if n == code[idx]:
#             idx += 1
#         if idx == len(code):
#             return True
#     return False


# if __name__ == "__main__":
#     print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
#     print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
#     print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

# 15. 

# import math

# def sphere_volume(radius):
#     return (4/3) * math.pi * (radius ** 3)

# if __name__ == "__main__":
#     r = float(input("Введите радиус сферы: "))
#     print("Объем сферы:", sphere_volume(r))


# 16.
# def unique_list(lst):
#     unique = []
#     for item in lst:
#         if item not in unique:
#             unique.append(item)
#     return unique

# if __name__ == "__main__":
#     nums = list(map(int, input("Введите числа через пробел: ").split()))
#     print("Уникальные элементы:", unique_list(nums))


# 17. 

# def is_palindrome(s):
#     s = s.replace(" ", "").lower()  # убираем пробелы и приводим к нижнему регистру
#     return s == s[::-1]

# if __name__ == "__main__":
#     text = input("Введите слово или фразу: ")
#     if is_palindrome(text):
#         print("Это палиндром ")
#     else:
#         print("Это не палиндром ")


# # 18.
# def histogram(numbers):
#     for n in numbers:
#         print("*" * n)

# if __name__ == "__main__":
#     nums = list(map(int, input("Введите числа через пробел: ").split()))
#     print("Гистограмма:")
#     histogram(nums)


# 19. 
# import random

# def guess_number():
#     name = input("Hello! What is your name?\n")
#     number = random.randint(1, 20)
#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

#     attempts = 0
#     while True:
#         guess = int(input("Take a guess.\n"))
#         attempts += 1
#         if guess < number:
#             print("Your guess is too low.")
#         elif guess > number:
#             print("Your guess is too high.")
#         else:
#             print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#             break

# if __name__ == "__main__":
#     guess_number()


# 20.
# main.py
from movies import (
    movies,
    is_high_score,
    high_score_movies,
    movies_by_category,
    average_score,
    average_score_by_category,
)

def print_movies_list(m_list):
    for i, m in enumerate(m_list):
        print(f"{i}: {m['name']} (IMDB {m['imdb']}, {m['category']})")

def menu():
    print("\nВыбери действие:")
    print("1 - Проверить один фильм по индексу (is_high_score)")
    print("2 - Список фильмов с imdb > порог")
    print("3 - Фильмы по категории")
    print("4 - Средний рейтинг всех фильмов")
    print("5 - Средний рейтинг по категории")
    print("0 - Выход")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Введите номер: ").strip()
        if choice == "0":
            break

        if choice == "1":
            print("\nСписок фильмов (индекс : название):")
            print_movies_list(movies)
            idx = int(input("Введите индекс фильма: "))
            movie = movies[idx]
            thresh = input("Порог imdb (Enter = 5.5): ").strip()
            thresh = float(thresh) if thresh else 5.5
            print(f"Фильм '{movie['name']}' имеет IMDB {movie['imdb']}. > {thresh}? {is_high_score(movie, thresh)}")

        elif choice == "2":
            thresh = input("Порог imdb (Enter = 5.5): ").strip()
            thresh = float(thresh) if thresh else 5.5
            res = high_score_movies(movies, thresh)
            print(f"\nФильмы с IMDB > {thresh}:")
            print_movies_list(res)

        elif choice == "3":
            cat = input("Введите название категории (например Romance): ").strip()
            res = movies_by_category(movies, cat)
            if res:
                print(f"\nФильмы в категории '{cat}':")
                print_movies_list(res)
            else:
                print("Фильмов в этой категории не найдено.")

        elif choice == "4":
            avg = average_score(movies)
            print(f"\nСредний IMDB по всем фильмам: {avg:.2f}")

        elif choice == "5":
            cat = input("Введите категорию для среднего рейтинга: ").strip()
            avg = average_score_by_category(movies, cat)
            if avg == 0:
                print("Фильмов в этой категории не найдено или средний = 0.")
            else:
                print(f"Средний IMDB в категории '{cat}': {avg:.2f}")

        else:
            print("Неверный ввод, попробуй снова.")