import random
import pandas as pd

censo = []
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOUAEOI"
numero = 0

print("Creando censo...")

for i in range(500_000):
	aumento = random.randint(1,2)
	numero += aumento

	letras = random.sample(alfabeto, 5)
	nombre = "".join(letras)

	edad = random.randint(18,99)

	impuestos = random.choice((True, True, True, False))

	censo.append([numero, nombre, edad, impuestos])

	if len(censo) % 100_000 == 0:
		print("Creados", len(censo), "registros")

print("Censo creado.")
print("Ultimo registro: ", censo[-1])

def busqueda_numero(lista, elemento):
	'''Busca registros por numero. Busqueda binaria'''

	inicio = 0
	final = len(lista) - 1

	while inicio <= final:
		medio = (inicio + final) // 2
		if lista[medio][0] == elemento:
			return lista[medio]
		elif lista[medio][0] < elemento:
			inicio = medio + 1
		elif lista[medio][0] > elemento:
			final = medio - 1
	return None

def busqueda_nombre(lista, elemento):
	'''Busca registros por nombre. Busqueda lineal'''

	encontrados = []

	for registro in lista:
		if registro[1] == elemento:
			encontrados.append(registro)
	if len(encontrados) == 0:
		return None
	else:
		return encontrados

def muestra_registro(registro):

	if registro == None:
		print("No existe registro con ese dato")
	else:
		print("--------------------------------")
		print("Numero:", registro[0]) # Cedula
		print("Nombre", registro[1])
		print("Edad:", registro[2])
		print("Impuestos:", registro[3])



def menu():

	print("--------------------------")
	print("- CENSO DE POBLACION -")
	print("1. Buscar por numero")
	print("2. Buscar por nombre")
	print("3. Salir")

	opcion = ""
	while opcion not in ("1", "2", "3"):
		opcion = input("--> ")
	return opcion


while True:
	op = menu()

	if op == "1":
		try:
			numero=int(input("Introduce numero: "))
		except ValueError:
			print("Introduce un numero entero")
		else:
			registro = busqueda_numero(censo, numero)
			muestra_registro(registro)

	elif op == "2":
		nombre=input("Introduce nombre: ").upper()
		registros = busqueda_nombre(censo,nombre)
		if registros == None:
			print("No existe registro con ese dato")
		else:
			for registro in registros:
				muestra_registro(registro)

	elif op == "3":
		break



"""
Instalar un sistema de bases de datos en local
Guardar el censo en la base de datos.
CENSO
	Tabla - Censo 2023
	Columnas -> Nombre, Numero, Edad, Impuestos
MYSQL
-> Como Crear una pagina web con un formulario de consulta usando python. 
Flask y Django
Opcional -> Pycharm
"""

# se crea DataFrame con la informacion de censo
column_name =["Numero", "Nombre", "Edad", "Impuestos"]
df = pd.DataFrame(censo, columns=[column_name])

from sqlalchemy import create_engine

# Configurar la conexión a la base de datos (en este caso, SQLite)
engine = create_engine('sqlite:///censo.db')

# Creando La base de datos a partir de DataFrame
df.to_sql('usuarios', con=engine, index=False, if_exists='replace')