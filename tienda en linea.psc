Algoritmo sin_titulo
	Definir compra Como Real
	Definir DT Como Real
	Definir VIP Como L�gico
	Definir Codigo Como L�gico
	Definir total Como Real
	Escribir 'Ingrese el valor total de su compra: '
	Leer compra
	Escribir '�Es cliente VIP? (0. Si, 1. No): '
	Leer VIP
	Escribir '�Tiene un c�digo de descuento? (0. Si, 1: No): '
	Leer Codigo
	DT = 0
	Si compra>100 Entonces
		DT = DT+(compra*0.20)
	FinSi
	Si VIP==true Entonces
		DT = DT+(compra*0.10)
	FinSi
	Si Codigo==true Entonces
		DT = DT+(compra*0.05)
	FinSi
	total = compra-DT
	Escribir 'El total a pagar despu�s de aplicar los descuentos es: $', total
FinAlgoritmo
