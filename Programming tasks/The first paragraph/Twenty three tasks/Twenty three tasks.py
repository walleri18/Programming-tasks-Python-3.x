# Импортирование математической библиотеки
import math

# Стороны треугольника
a, b, c = 0, 0, 0

# Получение данных
while a == 0:
    a = math.fabs(float(input("Введите первую сторону"
                              " треугольника: ")))

while b == 0:
    b = math.fabs(float(input("Введите вторую сторону"
                              " треугольника: ")))

while c == 0:
    c = math.fabs(float(input("Введите третью сторону"
                              " треугольника: ")))

# Вычисления всех биссектрис треугольника
oneBisector, twoBisector, threeBisector = 0, 0, 0

oneBisector = (math.sqrt(a * b * (a + b + c) * (a + b - c))) / (a + b)

twoBisector = (math.sqrt(a * c * (a + c + b) * (a + c - b))) / (a + c)

threeBisector = (math.sqrt(b * c * (b + c + a) * (b + c - a))) / (b + c)

# Вычисления всех медиан треугольника
oneMedian, twoMedian, threeMedian = 0, 0, 0

oneMedian = (1 / 2) * math.sqrt(2 * (a ** 2) + 2 * (b ** 2) - (c ** 2))

twoMedian = (1 / 2) * math.sqrt(2 * (a ** 2) + 2 * (c ** 2) - (b ** 2))

threeMedian = (1 / 2) * math.sqrt(2 * (b ** 2) + 2 * (c ** 2) - (a ** 2))

# Вычисления всех высот треугольника
oneHeight, twoHeight, threeHeight = 0, 0, 0

perimetr = a + b + c

oneHeight = (2 / c) * math.sqrt(perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c))

twoHeight = (2 / b) * math.sqrt(perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c))

threeHeight = (2 / a) * math.sqrt(perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c))

# Радиус описанной и вписанной окружности
incircleRadius, circleRadius = 0, 0

properiter = perimetr / 2

incircleRadius = math.sqrt(((properiter - a) * (properiter - b) * (properiter - c)) / properiter)

circleRadius = (a * b * c) / (4 * math.sqrt(properiter * (properiter - a) * (properiter - b) * (properiter - c)))

# Вывод результата
print("\nДлины высот:",
      "\nОт стороны A:", threeHeight,
      "\nОт стороны B:", twoHeight,
      "\nОт стороны C:", oneHeight,
      "\n\nДлины медиан:",
      "\nОт стороны A:", threeMedian,
      "\nОт стороны B:", twoMedian,
      "\nОт стороны C:", oneMedian,
      "\n\nДлины биссектрис:",
      "\nОт стороны A:", threeBisector,
      "\nОт стороны B:", twoBisector,
      "\nОт стороны C:", oneBisector,
      "\n\nРадиусы вписанной и описанной окружности:",
      "\nРадиус вписанной окружности:", incircleRadius,
      "\nРадиус описанной окружности:", circleRadius)

input("\nДля завершения программы нажмите любую клавишу...")