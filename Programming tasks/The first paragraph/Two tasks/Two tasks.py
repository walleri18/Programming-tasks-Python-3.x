# Подключение математической библиотеки
import math

# Действительные числа x и y
x, y = 0.0, 0.0

# Получение данных
x = float(input("Пожалуйста введите число X: "))
y = float(input("Пожалуйста введите число Y: "))

# Вычисление результата
result = (math.fabs(x) - math.fabs(y)) / (1.0 + math.fabs(x * y))

# Вывод результата на экран
print("\nРезультат вычислений: ", result)

input("\nДля завершения программы нажмите любую клавишу...")