# Импортирование математической библиотеки
import math

# Графитационная постоянная
G = 6.7385 * (10 ** (-11))

# Массы тел
oneWeight, twoWeight = 0, 0

# Расстояние между телами
distance = 0

# Получение данных
oneWeight = math.fabs(float(input("Введите массу первого тела: ")))
twoWeight = math.fabs(float(input("Введите массу второго тела: ")))

while distance == 0:
    distance = math.fabs(float(input("Введите расстояние между телами: ")))

# Вычисление силы гравитационного притяжения
F = G * (oneWeight * twoWeight) / (distance ** 2)

# Вывод результата
print("\nСила графитационного притяжения тел массами m1 =", oneWeight,
      "и m2 =", twoWeight, "на расстоянии", distance, "равно", F)

input("\nДля завершения программы нажмите любую клавишу...")