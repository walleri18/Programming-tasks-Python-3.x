# Импортирование математической библиотеки
import math

# Радиус окружности описанной вокруг треугольника
radius = 0

# Углы в треугольнике
alpha, betta, gamma = 0, 0, 0

# Получение данных
while radius == 0:
    radius = math.fabs(float(input("Введите радиус описанной окружности: ")))

while alpha == 0 or alpha >= 180:
    alpha = math.fabs(float(input("Введите величину первого угла в градусах: ")))

while betta == 0 or betta >= (180 - alpha):
    betta = math.fabs(float(input("Введите величину второго угла в градусах(не более " + str(180 - alpha) + "):")))

gamma = 180 - alpha - betta

# Вычисление сторон
oneSide = 2 * radius * math.sin(math.radians(alpha))
twoSide = 2 * radius * math.sin(math.radians(betta))
threeSide = 2 * radius * math.sin(math.radians(gamma))

# Вывод результата
print("\nПри радиусе описанной окружности", radius,
      "\nПри первом угле равный", alpha, "градусов",
      "\nПри втором угле равный", betta, "градусов",
      "\nПри третьем угле равный", gamma, "градусов",
      "\nПервая сторона равна", oneSide,
      "\nВторая сторона равна", twoSide,
      "\nТретья сторона равна", threeSide)

input("\nДля завершения программы нажмите любую клавишу...")