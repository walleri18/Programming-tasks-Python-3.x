# Импортирование математической библиотеки
import math

# Количество литров воды
oneManyLiters, twoManyLiters = 0.1, 0.1

# Температура каждого кувшина
oneTemperaturePitcher, twoTemperaturePitcher = 0.1, 0.1

# Получение данных
oneManyLiters = math.fabs(float(input("Введите первый объём кувшина: ")))
twoManyLiters = math.fabs(float(input("Введите второй объём кувшина: ")))
oneTemperaturePitcher = float(input("Введите температуру первого кувшина: "))
twoTemperaturePitcher = float(input("Введите температуру второго кувшина: "))

# Вычисление объема образовавшейся смеси
volumeMixture = oneManyLiters + twoManyLiters

# Вычисление температуру смеси
temperatureMixture = (oneTemperaturePitcher * oneManyLiters + twoTemperaturePitcher * twoManyLiters) / volumeMixture

# Вывод результатов
print("\nОбъём смеси: ", volumeMixture)
print("\nТемпература смеси: ", temperatureMixture)

input("\nДля завершения программы нажмите любую клавишу...")