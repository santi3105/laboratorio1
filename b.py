DA = int(input(print(f"Ingrese el numero de dias asignados: ")))
DR = int(input(print(f"Ingrese el numero de dias de retraso: ")))
porcentaje = int((DR/DA)*100)
print(f"el proyecto lleva una cantidad del {porcentaje}% de retraso en la entrega")