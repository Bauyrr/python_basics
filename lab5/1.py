import re

# ex1 = input(" ")
# print(re.findall(r'ab*', ex1))

# ex2 = input(" ")
# print(re.findall(r'ab{2,3}', ex2))

# ex3 = input(" ")
# print(re.findall(r'[a-z]+_[a-z]+', ex3))

# ex4 = input(" ")
# print(re.findall(r'[A-Z][a-z]+', ex4))

# ex5 = input(" ")
# print(re.findall(r'a.*b$', ex5))

# ex6 = input(" ")
# print(re.sub(r'[ ,.]', ':', ex6))

# ex7 = input(" ")
# def sncm(s):
#     return ''.join(word.title() if i != 0 else word for i, word in enumerate(s.split('_')))
# print(sncm(ex7))

# ex8 = input(" ")
# print(re.split(r'(?=[A-Z])', ex8))

# ex9 = input(" ")
# print(re.sub(r'(?=[A-Z])', ' ', ex9).strip())

ex10 = input(" ")
print(re.sub(r'([A-Z])', r'_\1', ex10).lower())