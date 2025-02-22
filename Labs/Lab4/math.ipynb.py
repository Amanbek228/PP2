#1
import math

def my_func(degr):
    return degr * (math.pi / 180)

degr = float(input())
radians = my_func(degr)
print(radians)

#2
import math

def my_func(a,b,h):
    return (a + b)/2 * h

a = float(input())
b = float(input())
h = float(input())

area = my_func(a, b, h)

print(f"Площадь трапеции: {area:.0f}")

#3
import math

def polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

n = int(input())
s = float(input())

print(f"{polygon_area(n, s):.6f}")

#4
import math

def parallelogram_area(base, height):
    return base * height

base = float(input())
height = float(input())

print(f"{parallelogram_area(base, height):.6f}")