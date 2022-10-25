# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:27:47 2022

@author: QUISPE, Gerardo Fabián
"""
"""
Etapa I:
Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno.
Para ello se debe realizar primero una aplicación de consola la cual debe solicitar el nombre de un alumno y la cantidad de cursos en la que se encuentra inscripto.
Estos dos valores deben almacenarse como una lista de dos elementos (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.
"""

alumnos = {}

# Funcion que comprueba si se ingreso un numero entero
def es_numero(valor):
    while not valor.isdecimal():
        print('¡Error, solo números enteros!')
        valor = input('Vuelva a ingresar el número: ')
    return int(valor)


while True:
    print('''Ingreser el número de la operación que desea realizar:
1- Añadir un alumno a la listas.
2- Ver la lista de alumnos.
3. Ver la cantidad de cursos de un alumno.
4- Salir.''')
    num = es_numero(input())
    match num:
        case 1:
            nombre = input("Ingrese el nombre: ")
            cant = es_numero(input("Ingrese la cantidad de materias cursos: "))
            alumnos.update({nombre: cant})
        case 2:
            for nombre, cursos in alumnos.items():
                print(f"Nombre: {nombre}. Cantidad de Materias Inscriptas {cursos}")
        case 3:
            alumno = input("Ingrese el Nombre del Alumno: ")
            if alumno in alumnos:
                print(f"Nombre: {alumno}. Cursos: {alumnos[alumno]}")
            else:
                print(f"El alumno {alumno}, No se encuentra.")
        case 4:
            print("¡Gracias por útilizar el programa!")
            break
        case other:
            print("La opción ingresada no es correcta. Vuelva a intentarlo.")

      

