# Импортирование математической библиотеки
import math

# Даны x, y, z. Нужно вычислить a, b.
x, y, z = 0.1, 0.1, 0.1

# Получение данных
x = float(input("Введите X: "))
y = float(input("Введите Y: "))
z = float(input("Введите Z: "))

# Вычисление а)
a = (math.sqrt(math.fabs(x - 1)) -
     math.fabs(y) ** (1 / 3)) \
    / (1 + (x ** 2) / 2 + (y ** 2) / 4)

b = x * (math.atan(z) + math.exp(-(x + 3)))

# Вывод a)
print("\na) a =", a, "; b =", b)

# Вычисление б)
a = (3 + math.exp(y - 1)) \
    / (1 + (x ** 2) * math.fabs(y - math.tan(z)))

b = 1 + math.fabs(y - x) + ((y - x) ** 2) / 2 \
    + (math.fabs(y-x) ** 3)/3

# Вывод б)
print("\nб) a =", a, "; b =", b)

# Вычисление в)
a = (1 + y) * ((x + y / (x ** 2 + 4)) /
               (math.exp(-x - 2) + 1 / (x ** 2 + 4)))

b = (1 + math.cos(y - 2)) / ((x ** 4) / 2 + (math.sin(z)) ** 2)

# Вывод в)
print("\nв) a =", a, "; b =", b)

# Вычисление г)
a = y + x / (y ** 2 + math.fabs((x ** 2) / (y + (x ** 3) / 3)))

b = 1 + (math.tan(z / 2)) ** 2

# Вывод г)
print("\nг) a =", a, "; b =", b)

# Вычисление д)
a = (2 * math.cos(x - math.pi / 6)) / (1 / 2 + (math.sin(y)) ** 2)

b = 1 + (z ** 2) / (3 + (z ** 2) / 5)

# Вывод д)
print("\nд) a =", a, "; b =", b)

# Вычисление е)
a = (1 + (math.sin(x + y)) ** 2) \
    / (2 + math.fabs(x - 2 * x / (1 + (x * y) ** 2)))

b = (math.cos(math.atan(1 / z))) ** 2

# Вывод е)
print("\nе) a =", a, "; b =", b)

# Вычисление ж)
a = math.log(math.fabs((y - math.sqrt(math.fabs(x)))
                       * (x - y / (z + (x ** 2) / 4))), math.e)

b = x - (x ** 2) / math.factorial(3) + (x ** 5) / math.factorial(5)

# Вывод ж)
print("\nж) a =", a, "; b =", b)

input("\nДля завершения программы нажмите любую клавишу...")