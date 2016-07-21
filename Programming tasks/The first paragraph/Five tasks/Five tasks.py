# Импортирование математической библиотеки
import math

# Два действительных положительных числа
one_number, two_number = 0.1, 0.1

# Получение данных
one_number = float(input("Введите первое число: "))
two_number = float(input("Введите второе число: "))

# Вычисление среднего арифметического
average = (one_number + two_number) / 2.0

# Вычисление среднего геометрического модулей
geometricMean = math.sqrt(math.fabs(one_number) * math.fabs(two_number))

# Вывод результата
print("\nСреднее арифметическое: ", average)
print("\nСреднее геометрическое: ", geometricMean)

input("\nДля завершения программы нажмите любую клавишу...")