"""
existen dos variables,uno con un nombre y otra con un apellido.primero se ha de comprobar el nombre,si es igual a daniel,se comprueba el apellido, si es igua a ramos,se imprime por pantalla el texto nombre y apellido correcytos.en caso de que el nombre sea daniel,
pero el apellido no sea ramos,se imprime por pantalla el texto apellido incorrecto.en caso de que el nombre no sea daniel,se imprime por pantalla el texto usuario desconocido.
"""
nombre="Daniel"
apellido="Ramos"
if nombre=="Daniel" and apellido=="Ramos":
    print("Nombre y apellido correctos")
elif nombre=="Daniel" and apellido!="Ramos":
    print("apellido incorrecto")
elif nombre!="Daniel" and apellido!="Ramos":
    print("nombre incorrecto")
else:
    print("usuario desconocido")