Выполнил Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1

Задание 1: Класс Vector3D

main.py:

from module import *
    
v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()

a = v4 * v3
print(a)

v4 = v1 * 10  
v4.display()

v4 = v1 @ v3 
v4.display()

module.py:

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if isinstance(other, Vector3D):  # Скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):  # Умножение на число
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Умножение возможно только на число или другой вектор")
    
    def __matmul__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )    
    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")
    
    def read(self):
        self.x = int(input("Введите x: "))
        self.y = int(input("Введите y: "))
        self.z = int(input("Введите z: "))
