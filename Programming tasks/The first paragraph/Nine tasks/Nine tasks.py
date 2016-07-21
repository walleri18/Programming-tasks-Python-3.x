# Импортирование математической библиотеки
import math

# Сопротивления трёх резисторов
oneResistance, twoResistance, threeResistance = 0.1, 0.1, 0.1

# Получение данных
oneResistance = math.fabs(float(input("Введите сопротивление первого резистора: ")))
twoResistance = math.fabs(float(input("Введите сопротивление второго резистора: ")))
threeResistance = math.fabs(float(input("Введите сопротивление третьего резистора: ")))

while oneResistance <= 0:
    oneResistance = math.fabs(float(input("Введите сопротивление первого резистора: ")))

while twoResistance <= 0:
    twoResistance = math.fabs(float(input("Введите сопротивление второго резистора: ")))

while threeResistance <= 0:
    threeResistance = math.fabs(float(input("Введите сопротивление третьего резистора: ")))

# Вычисление сопротивления цепи соединённых параллельно
resultResistance = 1 / (1 / oneResistance + 1 / twoResistance + 1 / threeResistance)

# Вывод результата
print("\nОбщее сопротивление цепи соединённых параллельно: ", resultResistance)

input("\nДля завершения программы нажмите любую клавишу...")