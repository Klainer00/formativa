#registrar
import csv 
def reg (lista:list):
    while True:
        nombre = input('Nombre: ')
        if nombre =='':
            continue
        else:
            break

    while True:
        apellido = input('Apellido: ')
        if apellido =='':
            continue
        else:
            break
    while True:
        print('1. CEO \n 2. Desarrollador \n 3. Analista de Datos')
        cargo = input('Cargo: ')
        if cargo == '1':
            cargo = 'CEO'  
            break 
        elif cargo == '2':
            cargo = 'Desarrollador' 
            break
        elif cargo == '3':
            cargo = 'Analista de Datos'
            break
        else:
            continue
    while True:
        try:
            sueldo_bruto = input('Sueldo Bruto')
            if sueldo_bruto =='' and sueldo_bruto.isalpha():
                continue
            else:
                sueldo_bruto = int(sueldo_bruto)
                print(type(sueldo_bruto))
                break
        except:
            print('error')
            continue
    dtosalud = sueldo_bruto *.07
    dtoafp = sueldo_bruto *.12
    sueldo_liquido= sueldo_bruto - dtosalud -dtoafp
    empleados = {
        'nombre': nombre,
        'apellido':apellido,
        'cargo': cargo,
        'sueldo_bruto':sueldo_bruto,
        'dstoafp':dtoafp,
        'dstsalud': dtosalud,
        'sueldo_liquido': sueldo_liquido
    } 
    lista.append(empleados)
def pausa():
    input('presione una tecla para volver')
def filtro(lista:list):


    print('{:<15} {:<10} {:<15} {:<12} {:<10} {:<15}'.format(
        'Trabajador', 'Cargo', 'Sueldo Bruto', 'Desc. Salud', 'Desc. AFP', 'Líquido a pagar'))
    print('-' * 80)

    for empleado in lista:
        nombre = empleado['nombre']
        apellido = empleado['apellido']
        cargo = empleado['cargo']
        sueldo_bruto =empleado['sueldo_bruto']
        dtoafp= empleado['dstoafp']
        dtosalud = empleado['dstsalud']
        sueldo_liquido = empleado['sueldo_liquido']
        print('{:<15} {:<10} {:<15} {:<12} {:<10} {:15}'.format(
        f'{nombre} {apellido}', cargo, sueldo_bruto ,dtosalud,dtoafp,sueldo_liquido))
    pausa()
def imprimir(lista:list):
    print('1. imprimir todos ')
    print('2. imprimir por cargo')
    op = input()
    if op == '1':
        with open('archivo.csv' , 'w', newline='',encoding='utf-8') as archivocsv:
            writer = csv.writer(archivocsv, delimiter=';')
            writer.writerow(['Empleado', 'Cargo', 'Sueldo Bruto', 'Descuento AFP', 'Descuento Salud', 'Sueldo Líquido'])
            for empleado in lista:
                nombre = empleado['nombre']
                apellido = empleado['apellido']
                cargo = empleado['cargo']
                sueldo_bruto =empleado['sueldo_bruto']
                dtoafp= empleado['dstoafp']
                dtosalud = empleado['dstsalud']
                sueldo_liquido = empleado['sueldo_liquido']
                writer.writerow([f'{nombre} {apellido}', cargo, sueldo_bruto, dtoafp, dtosalud, sueldo_liquido])
    elif op == '2':
        print('CARGOS')
        op = input('1. CEO 2. Desarrollador 3. Analista de datos')
        for empleado in lista:
            nombre = empleado['nombre']
            apellido = empleado['apellido']
            cargo = empleado['cargo']
            sueldo_bruto =empleado['sueldo_bruto']
            dtoafp= empleado['dstoafp']
            dtosalud = empleado['dstsalud']
            sueldo_liquido = empleado['sueldo_liquido']
            if op == '1':
                op ='CEO'
                with open(f'archivo{op}.csv','w' ,newline='') as archivo:
                    writer = csv.writer(archivo , delimiter=';')
                    if op in cargo:
                        writer.writerow(['Empleado', 'Cargo', 'Sueldo Bruto', 'Descuento AFP', 'Descuento Salud', 'Sueldo Líquido'])
                        nombre = empleado['nombre']
                        apellido = empleado['apellido']
                        cargo = empleado['cargo']
                        sueldo_bruto =empleado['sueldo_bruto']
                        dtoafp= empleado['dstoafp']
                        dtosalud = empleado['dstsalud']
                        sueldo_liquido = empleado['sueldo_liquido']
                        writer.writerow([f'{nombre} {apellido}', cargo, sueldo_bruto, dtoafp, dtosalud, sueldo_liquido])
                    else:                                       
                        print('error')
            elif op == '2':
                op = 'Desarrollador'
            elif op == '3':
                op = 'Analista de Datos'
            




    