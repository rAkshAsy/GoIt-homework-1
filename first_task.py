from datetime import datetime, date

def get_days_from_today(date:str) -> int:

    try:
        some_day = datetime.strptime(date, '%Y-%m-%d').date()
    except:
        result = 'Please, Enter the date in the format YYYY-MM-DD'
    else:
        today = datetime.now().date()
        days_delta = some_day - today
        result = days_delta.days
    
    return result



input_list = [
                '2025-10-28', # 128
                '2025-02-31', # Please, Enter the date in the format YYYY-MM-DD
                '2025-05-20', # -33
                '2025.10.28' # Please, Enter the date in the format YYYY-MM-DD                
            ]

for date in input_list:
    print(f'{get_days_from_today(date)}')