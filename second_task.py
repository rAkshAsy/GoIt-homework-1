import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:

    try:
        if min < 0 or max < 0 or quantity < 0:
            return 'Введіть валідні аргументи функції'
        
        all_nums = []
        for x in range(min, max+1):
            all_nums.append(x)
            x += 1

        sorted_result_list = sorted(random.sample(all_nums, quantity))
        return sorted_result_list
    except:
        return 'Введіть валідні аргументи функції'


test_cases = [
    (-10, 5, 3),
    (1, 5, 3),              #[2, 4, 5]
    (10, 100, 10),          #[16, 18, 31, 42, 54, 58, 67, 78, 87, 89]
    (10, 2, 5),             #Введіть валідні аргументи функції
    ('1', 10, 5),           #Введіть валідні аргументи функції
    (0.8, 5.1, 2)           #Введіть валідні аргументи функції
]

for case in test_cases:
    print(f'Ваші лотерейні числа: {get_numbers_ticket(*case)}')

