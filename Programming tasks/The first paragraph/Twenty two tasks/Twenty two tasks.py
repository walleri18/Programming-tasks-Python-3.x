# Импортирование математической библиотеки
import math

# Основания равнобедренной трапеции
a, b = 0, 0

# Угол alpha при большем основании a
alpha = 0

# Получение данных
while a == 0:
    a = math.fabs(float(input("Введите большее основание"
                              " равнобедренной трапеции: ")))

while b == 0 or b >= a:
    b = math.fabs(float(input("Введите меньшее основание"
                              " равнобедренной трапеции: ")))

while alpha == 0 or alpha >= 90:
    alpha = math.fabs(float(input("Введите угол при "
                                  "большем основании "
                                  "равнобедренной "
                                  "трапеции(в градусах): ")))

# Вычисление боковой строны равнобедренной трапеции
c = ((a - b) / 2) * math.cos(math.radians(alpha))

# Вычисление площади равнобедренной трапеции
area = c * math.sin(math.radians(alpha)) *\
       (b + c * math.cos(math.radians(alpha)))

# Вывод результата
print("\nБоковая сторона равнобедренной трапеции равно", c,
      "\nПлощадь равнобедренной трапеции равно", area)

input("\nДля завершения программы нажмите любую клавишу...")