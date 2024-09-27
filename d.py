usuario = int(input(f"Ingrese su nivel de usuario de 0-5: "))
tarjeta = input(f"Su tarjeta de identificacion esta activa? si o no: ")
nivel = int(input(f"Ingrese a que nivel quiere ingresar "))
if tarjeta == "si":
    tarjeta = True
else:
    tarjeta = False
contraseña = int(input(f"Hace cuantos dias cambio su contraseña: "))

if (nivel ==5 and usuario == 5 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 5 concedido")
elif ( nivel ==4 and usuario >= 4 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 4 concedido")
elif (nivel ==3 and usuario >= 3 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 3 concedido")
elif (nivel ==2 and usuario >= 2 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 2 concedido")
elif (nivel ==1 and usuario >= 1 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 1 concedido")
elif (nivel== 0 and usuario >= 0 and contraseña <= 30 and tarjeta == True):
    print("acceso denegado")
else:
    print("acesso no concedido, no cumple con las condiciones de acceso")