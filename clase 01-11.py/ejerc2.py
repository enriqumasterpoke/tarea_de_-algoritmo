import random

#Genera un numero aleatorio entre 1 y 100
numero_secreto=random.randint(1,100)
intentos=0

print("!Bienvenidos al juego de adivinanzas!")
print("Estoy pensando en un numero entre 1 y 100.")

while True:
    #Solicita la entrada del usuario
    suposicion=int(input("Adivina el numero:"))
    intentos +=1

    #compara la suposicion con el numero secreto
    if suposicion<numero_secreto:
        print("Demasiado bajo")
    elif suposicion>numero_secreto:
        print("Demasiado alto")
    else:
        print(f"!Correcto! Lo adivinaste en {intentos}intentos.")
        break

    if __name__=="_main_":
        while True:
            rand()
            op=int(input("0-continuar jugando.\n1-Salir\n_"))
            if op !=0:
                break