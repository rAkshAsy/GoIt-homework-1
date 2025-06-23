import re


def phone_number(number:str) -> str:

    dirty_num = ''.join(re.findall(r'[+,\d]', number))

    if dirty_num.startswith('+380'):
        nomrmalisate_number = f'{dirty_num}'
    elif dirty_num.startswith('380'):
        nomrmalisate_number = f'+{dirty_num[:12]}'
    elif dirty_num.startswith('80'):        
        nomrmalisate_number = f'+3{dirty_num[:11]}'
    else:
        nomrmalisate_number = f'+38{dirty_num[:10]}'
    
    
    return str(nomrmalisate_number)



test_list = ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
    ]

formated_numbers = []


for phone in test_list:
    formated_numbers.append(phone_number(phone))

print(formated_numbers)
