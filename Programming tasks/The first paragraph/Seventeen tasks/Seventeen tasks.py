# Импортирование математической библиотеки
import math

# Внутренний радиус кольца
innerRadius = 20

# Внешний радиус кольца
outerRadius = 0

# Получение данных
while outerRadius == 0 or outerRadius <= innerRadius:
    outerRadius = math.fabs(float(input("Введите внешний радиус кольца: ")))

# Вычисление площади кольца
area = math.pi * (outerRadius ** 2 - innerRadius ** 2)

# Вывод результата
print("\nВнутренний радиус:", innerRadius,
      "\nВнешний радиус:", outerRadius,
      "\nПлощадь кольца:", area)

input("\nДля завершения программы нажмите любую клавишу...")