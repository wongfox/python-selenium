from datetime import date, timedelta, datetime
import os

nomDirectorio = datetime.today().strftime('%d%m%Y%H%M%S')
dirImagen = nomDirectorio + "/img"

try:
    os.mkdir(nomDirectorio)
    os.mkdir(dirImagen)
except OSError:
    print("La creación del directorio %s falló" % dirImagen)
else:
    print("Se ha creado el directorio: %s " % dirImagen)

os.rename(nomDirectorio, 'JUAN')

today_date = date.today()

print("CURRENT DAY : ", today_date)

# as said earlier it takes argument as day by default
numDia = timedelta(5)
print("AFTER 5 DAYS DATE WILL BE : ", today_date + numDia)

fecActual = date.today()
fecViajeIda = (fecActual + timedelta(5))

print((fecActual + timedelta(5)).strftime('%d/%m/%Y'))
