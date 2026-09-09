from range_part_2_task.range_part_2 import Range

user_A_range = Range(10, 20)
user_B_range_list = [Range(0, 5),
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

for index, user_B_range in enumerate(user_B_range_list):
    print(f"{index + 1}. Для диапазонов {user_A_range} и {user_B_range} "
          f"пересечение = {user_A_range.get_intersection(user_B_range)}; "
          f"объединение = {user_A_range.get_union(user_B_range)}; "
          f"разность = {user_A_range.get_complement(user_B_range)}.")
