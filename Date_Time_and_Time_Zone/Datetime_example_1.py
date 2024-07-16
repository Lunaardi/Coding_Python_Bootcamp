# Example 1
from datetime import date, datetime
					
data = date(2023, 7, 10)
print(data) 	# >>> 2023-07-10
print(date.today())

# Example 2
import datetime
					
d = datetime.date(2023, 7, 19)
print(d) 	# >>> 2023-07-19

# Example 3 
datahora = datetime.datetime(2024, 7, 15, 18, 10, 23)
datahora2 = datetime.datetime(2023, 8, 12)

print(datahora)
print(datahora2)


# Example 4
print(datetime.datetime.today())
