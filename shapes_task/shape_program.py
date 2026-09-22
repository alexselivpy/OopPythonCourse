from shapes_task.square import Square
from shapes_task.triangle import Triangle
from shapes_task.rectangle import Rectangle
from shapes_task.circle import Circle


def get_max_shapes_area(shapes):
    sorted_list = sorted(shapes, key=lambda x: x.get_area())
    return sorted_list[-1]


def get_second_max_shapes_perimeter(shapes):
    sorted_list = sorted(shapes, key=lambda x: x.get_perimeter())
    return sorted_list[-2]


square_1 = Square(5)
triangle_1 = Triangle(1, 1, 3, 3, 1, 6)
rectangle_1 = Rectangle(5, 6)
circle_1 = Circle(5)

print(f"Площадь квадрата {square_1} = {square_1.get_area()}")
print(f"Площадь треугольника {triangle_1} = {triangle_1.get_area()}")
print(f"Площадь прямоугольника {rectangle_1} = {rectangle_1.get_area()}")
print(f"Площадь круга {circle_1} = {circle_1.get_area()}")

square_2 = Square(4)
triangle_2 = Triangle(1, 1, 5, 5, 2, 6)
rectangle_2 = Rectangle(5, 2)
circle_2 = Circle(6)

shapes_list = [square_1, triangle_1, rectangle_1, circle_1, square_2, triangle_2, rectangle_2, circle_2]

print("Фигура с максимальной площадью", get_max_shapes_area(shapes_list))
print("Фигура с вторым по величине периметром", get_second_max_shapes_perimeter(shapes_list))
