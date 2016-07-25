# Импортирование математической библиотеки
import math

# Первый элемент арифметической прогрессии
oneElement = 0

# Дельта элементов
delta = 0

# Количество элементов
countElement = 0

# Получение данных
oneElement = float(input("Введите значение первого элемента: "))
delta = float(input("Введите дельту элементов: "))

while countElement == 0:
    countElement = math.fabs(float(input("Введите количество элементов: ")))

# Вычисление суммы арифметической прогрессии
summaArithmeticProgression = ((2 * oneElement + delta * (countElement - 1)) / 2) * countElement

# Вывод результата
print("\nСумма арифметической прогрессии равна", summaArithmeticProgression)

input("\nДля завершения программы нажмите любую клавишу...")