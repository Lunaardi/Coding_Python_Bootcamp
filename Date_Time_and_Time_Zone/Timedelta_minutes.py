from datetime import datetime, timedelta

type_car = 'M' # P, M, G
time_small_car = 30
time_medium_car = 45
time_big_car = 60
current_date = datetime.now()

if type_car == 'P':
    estimated_date = current_date + timedelta(minutes=time_small_car)
    print(f"O carro chegou: {current_date} e ficará pronto ás {estimated_date}")
elif type_car == 'M':
    estimated_date = current_date + timedelta(minutes=time_medium_car)
    print(f"O carro chegou: {current_date} e ficará pronto ás {estimated_date}")
else:
    estimated_date = current_date + timedelta(minutes=time_big_car)
    print(f"O carro chegou: {current_date} e ficará pronto ás {estimated_date}")





