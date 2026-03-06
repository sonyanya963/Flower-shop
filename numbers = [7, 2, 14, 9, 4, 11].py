# numbers = [7, 2, 14, 9, 4, 11]
# numbers.sort()
# print(numbers[0] + numbers[1])
# books = [21, 30, 18, 7, 28, 25, 35, 10]
# books.sort()
# print(books[-1] - books[0])
# names = ["Мария", "Ева", "Даниил", "Ия"]
# names.sort(key= len, reverse= True)
# print(names)


# Дан список чисел: mixed = [15, -3, 0, 8, -12, 7, 4, -1]

# Создай новый список, содержащий только положительные числа.
# Создай новый список, содержащий только чётные числа.
# *Создай новый список, содержащий числа, которые больше 5 или меньше -5.

# mixed = [15, -3, 0, 8, -12, 7, 4, -1]
# plus = list(filter(lambda x: x>0, mixed))
# two = list(filter(lambda x: x%2 == 0, mixed))
# five = list(filter(lambda x: x<-5 or x>5, mixed))
# print(plus, two, five)

# s = input()
# s = s.split(sep = "+")
# s = list(map(int, s))
# s.sort()
# strn = ""
# for i in range(0,len(s)):
#     strn += str(s[i])
#     if i != len(s) - 1:
#         strn += '+'
    
# print(strn)
 
a = {}
b = {"c": "ц", "b": "b"}
b["v"] = "римская пять"
b.pop("v")
print(b)
