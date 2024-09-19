usuario = int(input(print(f"Ingrese su nivel de usuario de 0-5: ")))
tarjeta = input(print(f"Su tarjeta de identificacion esta activa? si o no: "))
if tarjeta == "si":
    tarjeta = True
else:
    tarjeta = False
contraseña = int(input(print(f"Hace cuantos dias cambio su contraseña: ")))

if (usuario == 5 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 5 concedido")
elif (usuario == 4 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 4 concedido")
elif (usuario == 3 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 3 concedido")
elif (usuario == 2 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 2 concedido")
elif (usuario == 1 and contraseña <= 30 and tarjeta == True):
    print("acceso a nivel 1 concedido")
elif (usuario == 0 and contraseña <= 30 and tarjeta == True):
    print("acceso denegado")
else:
    print("acesso no concedido, no cumple con las condiciones de acceso")