from shapes_task.shape import Square, Triangle, Rectangle, Circle


def get_maximum_shapes_area(some_list):
    sorted_list = sorted(some_list, key=lambda x: x.get_area())
    return sorted_list[-1]


def get_second_maximum_shapes_perimeter(some_list):
    sorted_list = sorted(some_list, key=lambda x: x.get_perimeter())
    return sorted_list[-2]


square = Square(5)
triangle = Triangle(1, 1, 3, 3, 1, 6)
rectangle = Rectangle(5, 6)
circle = Circle(5)

print(f"Площадь квадрата {square} = {square.get_area()}")
print(f"Площадь треугольника {triangle} = {triangle.get_area()}")
print(f"Площадь прямоугольника {rectangle} = {rectangle.get_area()}")
print(f"Площадь круга {circle} = {circle.get_area()}")

square_2 = Square(4)
triangle_2 = Triangle(1, 1, 5, 5, 2, 6)
rectangle_2 = Rectangle(5, 2)
circle_2 = Circle(6)

shapes_list = [square, triangle, rectangle, circle, square_2, triangle_2,
               rectangle_2, circle_2]

print("Фигура с максимальной площадью", get_maximum_shapes_area(shapes_list))
print("Фигура с вторым по величине периметром", get_second_maximum_shapes_perimeter(shapes_list))
