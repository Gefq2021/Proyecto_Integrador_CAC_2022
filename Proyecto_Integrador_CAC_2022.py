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
num = 0
alumnos = []

while num != 3:
    alumno = []
    print('''Ingreser el número de la operación que desea realizar:
1- Añadir un alumno a la listas.
2- Ver la lista de alumnos.
3- Salir.''')
    num = int(input())
    match num:
        case 1:
            nombre = input("Ingrese el nombre: ")
            alumno.append(nombre)
            cant = int(input("Ingrese la cantidad de materias cursos: "))
            alumno.append(cant)
            alumnos.append(alumno)
        case 2:
            for a in alumnos:
                print(f"Nombre: {a[0]}. Cantidad de Materias Inscriptas {a[1]}")
        case 3:
            print("¡Gracias por útilizar el programa!")
            break
        case other:
            print("La opción ingresada no es correcta. Vuelva a intentarlo.")

      

