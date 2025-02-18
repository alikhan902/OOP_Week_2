class Vector3D:
    """
    Класс для работы с трехмерными векторами.
    """
    def __init__(self, x=0, y=0, z=0):
        """
        Инициализация вектора.
        :param x: Координата x
        :param y: Координата y
        :param z: Координата z
        """
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        """
        Сложение двух векторов.
        :param other: Другой вектор
        :return: Новый вектор - сумма
        """
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """
        Вычитание двух векторов.
        :param other: Другой вектор
        :return: Новый вектор - разность
        """
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        """
        Умножение вектора на число или скалярное произведение двух векторов.
        :param other: Число или другой вектор
        :return: Число (скалярное произведение) или новый вектор
        """
        if isinstance(other, Vector3D):  # Скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):  # Умножение на число
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Умножение возможно только на число или другой вектор")
    
    def __matmul__(self, other):
        """
        Векторное произведение двух векторов.
        :param other: Другой вектор
        :return: Новый вектор - результат векторного произведения
        """
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )    
    def display(self):
        """
        Выводит координаты вектора в консоль.
        """
        print(f"({self.x}, {self.y}, {self.z})")
    
    def read(self):
        """
        Считывает координаты вектора с клавиатуры.
        """
        self.x = int(input("Введите x: "))
        self.y = int(input("Введите y: "))
        self.z = int(input("Введите z: "))
