Algoritmo sin_titulo
	Definir NU Como Real
	Definir CA Como Real
	Definir TA Como Lógico
	Definir NA como real
	Escribir 'ingrese el nivel de acceso de su cuenta de 1 a 5'
	Leer NU
	Escribir "¿Hace cuantos dias actualizo su tarjeta?"
	Leer CA
	Escribir "¿Su tarjeta de verificacion esta activa? (0. Si, 1. No)"
	Leer TA
	Escribir "Ingrese el nivel al que quiere ingresar"
	Leer NA
	Si NU>=NA Entonces
		Si NU == 5 & TA == true & CA <= 30 Entonces
			Escribir "Acceso a Nivel 5 concedido"
		SiNo
			Si NU == 4 & TA == true & CA <= 30 Entonces
				Escribir "Acceso a Nivel 4 concedido"
			SiNo
				Si NU == 3 & TA == true & CA <= 30 Entonces
					Escribir "Acceso a Nivel 3 concedido"
				SiNo
					Si NU == 2 & TA == true & CA <= 30 Entonces
						Escribir "Acceso a Nivel 2 concedido"
					SiNo
						Si NU == 1 & TA == true & CA <= 30 Entonces
							Escribir "Acceso a Nivel 1 concedido"
						SiNo
							Si NU == 1 & TA == true & CA <= 30 Entonces
								Escribir "Acceso denegado"
							SiNo
								Escribir "Acceso denegado, verifique las condiciones"
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "Acceso denegado"
	FinSi
FinAlgoritmo
