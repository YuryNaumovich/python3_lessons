'''
 Напишите программу, которая будет запрашивать у пользователя радиус
и сохранять его в переменной r. После этого она должна вычислить площадь круга
с заданным радиусом и объем шара с тем же радиусом. Используйте в своих вычислениях константу pi из модуля math.
Подсказка. 
Площадь круга вычисляется по формуле area = πr 2
, а объем шара – поформуле volume = (4/3)πr 3.
'''

import math
from math import pi

r = float(input('Enter radius (Example: 100.00 cm)') or 100.00)

def circle_area(r):
    return  float("{:.3f}".format(math.pi * r ** 2))

def volume_of_sphere(r):
    return   float("{:.3f}".format((4 / 3) * math.pi * r ** 3))

print("Circle area:", circle_area(r), "cm2")
print("Volume of sphere:", volume_of_sphere(r), "cm3")