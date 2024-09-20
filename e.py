cantidad = float(input(print(f"Ingrese el valor total de la compra: ")))
vip = float(print(f"Es un usuario VIP? si o no: "))
total = 0
if vip == "si":
    vip = True
    descuento1 = (cantidad*0.1)/100
else:
    vip = False
codigo = input(print(f"Tiene un codigo de descuento? si o no: "))
if codigo == "si":
    codigo = True
else:
    codigo = False

if(cantidad>= 100 and vip == True and codigo == True):
    cantidad = (cantidad/100)*0.4
    total = cantidad

print({descuento1})