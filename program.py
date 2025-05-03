def find_max_even_number(numbers):
    current_max = 0
    for number in numbers:
        if number % 2 == 0:
            current_max = max(number, current_max)
    return current_max


max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number другие списки:
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f"Максимальное чётное число: {max_even}")
