print("sistema de sueldo liquido")
nombre= input("ingrese su nombre: ")
sueldob=float(input("ingrese su sueldo bruto: "))
afp = int(input("ingrese cuanto % le descuentan por afp: "))
afp1= afp/100
prevision=input("ingrese si es FONASA o ISAPRE: ")
previsionPorc=int(input(f"ingrese cuanto % le descuentan en {prevision}:"))
prev1=previsionPorc/100
seguro=int(input("ingrese cuanto % le descuentan en el seguro de cesantia: "))
seg1=seguro/100


#calculos y metodos
afpsueldo=sueldob*afp1
previsueldo=sueldob*prev1
segsueldo=sueldob*seg1
totaldescuentos=(afpsueldo+previsueldo+segsueldo)
sueldoimponible=sueldob-totaldescuentos

#print(f" su sueldo imponible es: {sueldoimponible}")
#print(f"sus descuentos son afp: {afpsueldo}, {prevision}: {previsueldo}, seguro: {segsueldo}, y total descuentos: {totaldescuentos}")


while True:
    print("Menu de opciones:")
    print("1: calcular el sueldo imponible")
    print("2: calcular los descuentos")
    print("3: salir")
    opc = int(input("ingrese que opcion desea:"))
    if opc==1:
        print(f"su sueldo imponible es: {sueldoimponible}")

    elif opc==2:
        print(f"su descuento es afp: {afpsueldo}, {prevision}:{previsueldo}, seguro:{segsueldo} y el total es: {totaldescuentos}")
    else:
        print("Hasta pronto")
        break
