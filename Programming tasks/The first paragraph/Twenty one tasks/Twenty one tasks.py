# Импортирование математической библиотеки
import math

# Действительные числа
c, d = 0, 0

# Корни уравнения x_one, x_two
x_one, x_two = 0, 0

# Получаем данные
c = float(input("Введите коэффициент C: "))
d = float(input("Введите коэффициент D: "))

# Находим корни уравнения
D = (-3) ** 2 - 4 * (-math.fabs(c * d))

if D == 0:
    x_one = x_two = 3 / 2

elif D > 0:
    tmpX_one = (3 + math.sqrt(D)) / 2
    tmpX_two = (3 - math.sqrt(D)) / 2

    x_one = max(tmpX_one, tmpX_two)
    x_two = min(tmpX_one, tmpX_two)

    del tmpX_one, tmpX_two

# Вычисление главного ответа задачи
result = math.fabs((math.sin(math.fabs(c * (x_one ** 3)
                                       + d * (x_two ** 2) - c * d)))
                   / math.sqrt((c * (x_one ** 3)
                                + d * (x_two ** 2) - x_one) ** 2 + 3.14)) \
         + math.tan(c * (x_one ** 3) + d * (x_two ** 2) - x_one)

# Вывод результата
print("\nРезультат вычислений равен", result)

input("\nДля завершения программы нажмите любую клавишу...")