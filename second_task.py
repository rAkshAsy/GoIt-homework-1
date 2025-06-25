import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:

    if type(min) == int and type(max) == int and type(quantity) == int:
        if min > 0 and max < 1000 and min < max and (quantity > min and quantity < max):
            all_nums = []
            for x in range(min, max+1):
                all_nums.append(x)
                x += 1

            sorted_result_list = sorted(random.sample(all_nums, quantity))
            return sorted_result_list
    
    return []
    
    


test_cases = [
    (1, 5, 3),              #[2, 4, 5]
    (10, 100, 11),          #[20, 27, 28, 59, 64, 74, 75, 85, 94, 96, 98]
    (1000, 1300, 10),       #[]
    (10, 2, 5),             #[]
    ('1', 10, 5),           #[]
    (0.8, 5.1, 2),           #[]]
    (-10, 5, 3),            #[]]
]

for case in test_cases:
    print(f'Ваші лотерейні числа: {get_numbers_ticket(*case)}')

