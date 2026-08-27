from range_task.range import Range

user_start = float(input("Введите число - начало диапазона: "))
user_end = float(input("Введите число - конец диапазона: "))
user_range = Range(user_start, user_end)
print(f"Длина диапазона = {user_range.get_len()}")
user_number = float(input("Введите число, чтобы проверить, лежит ли число в данном диапазоне: "))
if user_range.is_inside(user_number) is True:
    print(f"Число {user_number} лежит в диапазоне ({user_start},{user_end})")
else:
    print(f"Число {user_number} не лежит в диапазоне ({user_start},{user_end})")
