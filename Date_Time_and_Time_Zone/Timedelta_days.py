from datetime import datetime, timedelta, date

type_car = 'P' # P, M, G
time_small_car = 30
time_medium_car = 45
time_big_car = 60
current_date = datetime.now()

if type_car == 'P':
    estimated_date = current_date - timedelta(days=time_small_car)
    print(f"O carro sairá da oficina dia: {current_date} pois chegou dia {estimated_date}")
elif type_car == 'M':
    estimated_date = current_date - timedelta(days=time_medium_car)
    print(f"O carro sairá da oficina dia: {current_date} pois chegou dia {estimated_date}")
else:
    estimated_date = current_date - timedelta(days=time_big_car)
    print(f"O carro sairá da oficina dia: {current_date} pois chegou dia {estimated_date}")
    
# Example 2
print(date.today() - timedelta(days=1))
resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado)
print(resultado.time())

# Example3
print(datetime.now().date())