# Импортирование математической библиотеки
import math

# Два действительных положительных числа
one_number, two_number = 0.1, 0.1

# Получение данных
one_number = float(input("Введите первое положительное число: "))
two_number = float(input("Введите второе положительное число: "))

one_number = one_number if (one_number > 0) else (-one_number)
two_number = two_number if (two_number > 0) else (-two_number)

# Вычисление среднего арифметического
average = (one_number + two_number) / 2.0

# Вычисление среднего геометрического
geometricMean = math.sqrt(one_number * two_number)

# Вывод результата
print("\nСреднее арифметическое: ", average)
print("\nСреднее геометрическое: ", geometricMean)

input("\nДля завершения программы нажмите любую клавишу...")