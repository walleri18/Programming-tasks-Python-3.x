# Импортирование математической библиотеки
import math

# Координаты точек
one_x, one_y, two_x, two_y = 0, 0, 0, 0

# Получение данных
one_x = float(input("Введите X one: "))
one_y = float(input("Введите Y one: "))
two_x = float(input("Введите X two: "))
two_y = float(input("Введите Y two: "))

# Вычисление расстояния между точками
distance = math.sqrt((two_x - one_x) ** 2 + (two_y - one_y) ** 2)

# Вывод результата
print("\nРасстояние между точками равно", distance)

input("\nДля завершения программы нажмите любую клавишу...")