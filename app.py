#menu
import funciones as fun
from os import system
system('cls')

lista = []
while True:
    print('1. Registrar trabajador \n2. Listar los todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Salir del Programa')
    op = input()
    if op == '1':
        fun.reg(lista)
    elif op == '2':
        fun.filtro(lista)

    elif op == '3':
        fun.imprimir(lista)
    elif op == '4':
        break
