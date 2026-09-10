from range_part_2_task.range_part_2 import Range

range_start = float(input("Введите число - начало диапазона: "))
range_end = float(input("Введите число - конец диапазона: "))

user_range = Range(range_start, range_end)
print(f"Длина диапазона = {user_range.length}")

user_number = float(input("Введите число, чтобы проверить, лежит ли число в данном диапазоне: "))

if user_range.is_inside(user_number):
    print(f"Число {user_number} лежит в диапазоне ({range_start}, {range_end})")
else:
    print(f"Число {user_number} не лежит в диапазоне ({range_start}, {range_end})")

first_range = Range(10, 20)
second_range_list = [Range(0, 5),
                     Range(25, 30),
                     Range(5, 10),
                     Range(20, 25),
                     Range(5, 15),
                     Range(15, 25),
                     Range(12, 18),
                     Range(5, 30),
                     Range(10, 15),
                     Range(15, 20),
                     Range(10, 20)
                     ]

for index, second_range in enumerate(second_range_list):
    print(f"{index + 1}. Для диапазонов {first_range} и {second_range} "
          f"пересечение = {first_range.get_intersection(second_range)}; "
          f"объединение = {first_range.get_union(second_range)}; "
          f"разность = {first_range.get_complement(second_range)}.")
