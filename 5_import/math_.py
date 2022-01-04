# factorial - факториал числа
# exp - экспонента
# log, log2, log10 - логарифмы
# sqrt - квадратный корень
# sin, cos, asin, asoc, ...
import math

# 1. Найти длину окружности с определенным радиусом
r = 100
print(2 * r * math.pi)

# 2.найти площадь окружности с определенным радиусом
print((r ** 2) * math.pi)
print(math.pow(r, 2) * math.pi)

# 3. По координатам 2-х точек определить расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(l)

# 4. Найти факториал числа 9
print(math.factorial(9))
