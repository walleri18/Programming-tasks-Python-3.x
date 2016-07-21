# Импортирование математической библиотеки
import math

# Количество углов n-угольника
numberAngle = 1

# Радиус окружности вокруг которой описан n-угольник
radius = 1

# Получение данных
numberAngle = math.fabs(float(input("Введите количество углов n-угольника: ")))
radius = math.fabs(float(input("Введите радиус вокруг которой описан n-угольник: ")))

# Вычисление периметра n-угольника описанного вокруг окружности радиуса r
perimeter = 2 * radius * numberAngle * math.sin(math.pi / numberAngle) * math.cos(math.pi / numberAngle)

# Вывод результата
print("\nПериметр n-угольника: ", perimeter)

input("\nДля завершения программы нажмите любую клавишу...")