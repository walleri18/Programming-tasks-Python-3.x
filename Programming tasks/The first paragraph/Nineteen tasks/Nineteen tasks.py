# Импортирование математической библиотеки
import math

# Скорости тел
oneSpeed, twoSpeed = 0, 0

# Ускорения тел
oneSpeedup, twoSpeedup = 0, 0

# Начальное расстояние между телами
initialDistance = 0

# Получение данных
oneSpeed = math.fabs(float(input("Введите начальную скорость первого тела: ")))
twoSpeed = math.fabs(float(input("Введите начальную скорость второго тела: ")))

while oneSpeedup == 0:
    oneSpeedup = math.fabs(float(input("Введите ускорение первого тела: ")))

while twoSpeedup == 0:
    twoSpeedup = math.fabs(float(input("Введите ускорение второго тела: ")))

while initialDistance == 0:
    initialDistance = math.fabs(float(input("Введите начальное расстояние: ")))

# Вычисление дискриминанта
D = ((oneSpeed + twoSpeed) ** 2) + 2 * initialDistance * (oneSpeedup + twoSpeedup)

# Вычисление времени до столкновения
time = 0

if D == 0:
    time = - (oneSpeed + twoSpeed) / (2 * (oneSpeedup + twoSpeedup))

elif D > 0:
    tmpTimeOne = (-(oneSpeed + twoSpeed) + math.sqrt(D)) / (oneSpeedup + twoSpeedup)
    tmpTimeTwo = (-(oneSpeed + twoSpeed) - math.sqrt(D)) / (oneSpeedup + twoSpeedup)

    time = tmpTimeOne if tmpTimeOne >= 0 else tmpTimeTwo

# Вывод результата
print("\nВремя до столкновения равно", time)

input("\nДля завершения программы нажмите любую клавишу...")