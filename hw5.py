from math import pi


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class IInnerCircle:
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None: ...

    def square(self) -> float: ...

    def perimeter(self) -> float: ...


class ISquare:
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None: ...

    def square(self) -> float: ...

    def perimeter(self) -> float: ...


class IRectangle:
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point) -> None: ...

    def square(self) -> float: ...

    def perimeter(self) -> float: ...


class ConvexQuadrilateral:
    """Выпуклый четырёхугольник."""

    def __init__(self, point1, point2, point3, point4):
        self.A, self.B, self.C, self.D = point1, point2, point3, point4
        self.a = ConvexQuadrilateral._get_distance(self.A, self.B)
        self.b = ConvexQuadrilateral._get_distance(self.B, self.C)
        self.c = ConvexQuadrilateral._get_distance(self.C, self.D)
        self.d = ConvexQuadrilateral._get_distance(self.D, self.A)
        self.ABC = ConvexQuadrilateral._get_angle_cos(self.A, self.B, self.C)
        self.BCD = ConvexQuadrilateral._get_angle_cos(self.B, self.C, self.D)
        self.CDA = ConvexQuadrilateral._get_angle_cos(self.C, self.D, self.A)
        self.DAB = ConvexQuadrilateral._get_angle_cos(self.D, self.A, self.B)
        self._validate()

    def _validate(self):
        for angle_cos in [self.ABC, self.BCD, self.CDA, self.DAB]:
            if 1 - angle_cos < 1e-4:
                raise ValueError('Угол ConvexQuadrilateral не может быть равен нулю.')

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return 0.5 * abs(
            (self.A.x - self.B.x) * (self.A.y + self.B.y) + (self.B.x - self.C.x) * (self.B.y + self.C.y) + (
                        self.C.x - self.D.x) * (self.C.y + self.D.y) + (self.D.x - self.A.x) * (self.D.y + self.A.y))

    @staticmethod
    def _get_distance(point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

    @staticmethod
    def _get_angle_cos(point1, point2, point3):
        a = ConvexQuadrilateral._get_distance(point1, point3)
        b = ConvexQuadrilateral._get_distance(point1, point2)
        c = ConvexQuadrilateral._get_distance(point2, point3)
        return (a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)


class Rectangle(ConvexQuadrilateral, IRectangle):
    def _validate(self):
        super()._validate()
        for angle_cos in [self.ABC, self.BCD, self.CDA, self.DAB]:
            if abs(angle_cos) > 1e-4:
                raise ValueError('Угол прямоугольника должен быть прямым.')

    def square(self):
        return self.a * self.c

    def perimeter(self):
        return (self.a + self.c) * 2


class Square(Rectangle, ISquare):
    def _validate(self):
        super()._validate()
        if not (self.a == self.b == self.c == self.d):
            raise ValueError('Стороны квадрата должны быть одинаковы.')

    def square(self):
        return pow(super()._get_distance(self.A, self.B), 2)

    def perimeter(self):
        return super()._get_distance(self.A, self.B) * 4


class InnerCircle(ConvexQuadrilateral, IInnerCircle):
    def __init__(self, point1, point2, point3, point4):
        super().__init__(point1, point2, point3, point4)
        self.r = 2 * super().square() / super().perimeter()

    def _validate(self):
        super()._validate()
        if self.a + self.c != self.b + self.d:
            raise ValueError('ConvexQuadrilateral не может быть вписан в окружность.')

    def perimeter(self):
        return 2 * pi * self.r

    def square(self):
        return pi * self.r ** 2


if __name__ == '__main__':
    square = Square(Point(-100, 100), Point(100, 100), Point(100, -100), Point(-100, -100))
    rectangle = Rectangle(Point(-35, 1), Point(35, 1),
                          Point(35, -1), Point(-35, -1))
    circle = InnerCircle(Point(-35, 5), Point(5, 5),
                         Point(5, -35), Point(-35, -35))
    print(square.perimeter(), square.square(),
          rectangle.perimeter(), rectangle.square(), circle.perimeter(), circle.square())
