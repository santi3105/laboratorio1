cantidad = float(input(print(f"Ingrese el valor total de la compra: ")))
vip = input(print(f"Es un usuario VIP? si o no: "))
total = 0
descuento = 0
if vip == "si":
    vip = True
else:
    vip = False
codigo = input(print(f"Tiene un codigo de descuento? si o no: "))
if codigo == "si":
    codigo = True
else:
    codigo = False

if cantidad> 100:
    descuento = descuento+(cantidad*0.2)
if vip == True:
    descuento = descuento+(cantidad*0.1)
if codigo == True:
    descuento = descuento+(cantidad*0.05)
total =cantidad-descuento

print(f"el total a pagar con los descuentos incluidos es {total}")