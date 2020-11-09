from datetime import  datetime, timedelta

data = datetime(2020, 11, 9, 8, 46, 35)
print(data.strftime('%d%m%Y %H:%M:%S'))

data2 = datetime.strptime('9/11/2020', '%d/%m/%Y')
print(data2.timestamp)

d1= datetime.strptime('20/04/1987', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987','%d/%m/%Y %H:%M:%S')