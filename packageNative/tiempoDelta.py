from datetime import datetime,timedelta

fecha = datetime(2023,1,1)
fecha2 = datetime(2023,2,1)

delta = fecha2 - fecha

print("diferencias de dias",delta.days)