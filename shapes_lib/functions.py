import math

def calculate_circle_area(radius):
    if radius <= 0:
        raise ValueError("Радиус круга не может быть ноль или отрицательным.")
    return math.pi * radius * 2

def calculate_triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Сторона треугольника не может быть равна 0 или отрицательной")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Треугольник задан неправильно. Почитайте про неравенство треугольника")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def calculate_rectagle_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Сторона не может быть равно 0 или отрицательной")
    return a * b 

def is_right_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Сторона не может быть равно 0 или отрицательной")
    return (max(a, b, c) ** 2 == (a ** 2 + b ** 2)) or (max(a, b, c) ** 2 == (b ** 2 + c ** 2)) or (max(a, b, c) ** 2 == (a ** 2 + c ** 2))

