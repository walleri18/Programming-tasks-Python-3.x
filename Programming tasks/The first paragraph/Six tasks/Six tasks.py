# Ипортирование мматематической библиотеки
import math

# Катеты прямоугольного треугольника
oneCathetus, twoCathetus = 1, 1

# Получение данных
oneCathetus = float(input("Введите первый катет прямоугольного треугольника: "))
twoCathetus = float(input("Введите второй катет прямоугольного треугольного: "))

oneCathetus = math.fabs(oneCathetus)
twoCathetus = math.fabs(twoCathetus)

# Вычисление гипотенузы прямоугольного треугольника
hypotenuse = math.sqrt((oneCathetus ** 2) + (twoCathetus ** 2))

# Вычисление площади прямоугольного треугольника
area = (oneCathetus * twoCathetus) / 2.0

# Вывод результата
print("\nГипотенуза прямоугольного треугольника: ", hypotenuse)
print("\nПлощадь прямоугольного треугольника: ", area)

input("\nДля завершения программы нажмите любую клавишу...")