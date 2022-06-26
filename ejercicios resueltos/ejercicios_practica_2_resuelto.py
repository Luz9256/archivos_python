# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
csvfile = open(archivo,'r')
data = list(csv.DictReader(csvfile))
csvfile.close()

tornillos = 0

for elemento in data:
    tornillos += int(elemento['tornillos'])

print(f'stock de tornillos: {tornillos}')

def ej4():
    print('Ejercicios con archivos CSV 2º')
archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

with open (archivo, 'r') as csvfile:
    data = list(csv.DictReader(csvfile))

dpto_2_ambientes = 0
dpto_3_ambientes = 0

for propiedad in data:

    try:
        if propiedad['ambientes'] == '2':
            dpto_2_ambientes += 1
        elif propiedad['ambientes'] == '3':
            dpto_3_ambientes += 2
    except:
        print(f'Se desconoce la cantidad de ambientes de {propiedad}')

    print(f'Cantidad de propiedades 2 ambientes: {dpto_2_ambientes}')
    print(f'Cantidad de propiedades 3 ambientes: {dpto_3_ambientes}')

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print('/n')
    ej3()
    print('/n')
    ej4()