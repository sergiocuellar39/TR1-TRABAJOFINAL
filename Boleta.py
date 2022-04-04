from Trabajador import Trabajador

print("><"*20)
print("        >>>fERROTEXC<<<        ")
print("><"*20)
    
nom=""
while not (nom in range (1,6)):
          nom = int(input("SELECCIONE EL TRABAJADOR QUE DESEA PAGAR:\n [1]ROBERTO \n [2]MARIA \n [3]JUAN \n\nElija su opción: "))          
if not (nom in range(1,6)):

    print("Trabajador incorrecto....")

print("><"*20)

pro = ""
while not (pro in range (1, 6)):
    pro = int(input("SELLECIONE SU PUESTO DE TRABAJO:\n [1]GERENTE \n [2]ARQUITECTO \n [3]ING.CIVIL \n [4]RECURSOS HUMANOS \n [5]SUPERVISOR DE OBRA \n\nEliga la profesión: "))

if not (pro in range (1, 6)):
    print("Profesión no valida")

print("><"*20)

cat = ""

while not (cat == "A" or cat== "B" or cat == "C"):
   cat = str(input("CATEGORÍA [A / B / C]..: "))
if not (cat =="A" or cat== "B" or cat == "C"):
   print("Categoria incorrecta....")

he= float(input("HORAS EXTRAS:           "))
tar=float(input("TARDANZAS(minutos):     "))
alu= Trabajador(nom , cat, he,tar,pro)


print("")
print("><"*20)
print("        >>>BOLETA DE PAGO<<<     ")                                       
print("><"*20)
print("NOMBRE COMPLETO:            ",alu.Nombre())
print("DNI:                        ",alu.DNI())
print("PROFESIÓN:                  ", alu.Profesion())
print("SUELDO BASICO:              ",alu.Sueldo_basico(),"Soles")
print("DESCUENTO TARDANZAS:        ",alu.Descuento())
print("PAGO HORAS EXTRAS:          ",alu.Horas_extras())
print("SUELDO NETO:                ",alu.Sueldo_neto(),"Soles")
print("><"*20)


print("\nDesea seguir pagando a sus trabajadres [SI / NO] : " )
