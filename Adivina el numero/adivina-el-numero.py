import random

def adivina_el_numero(x):
    print("***********************************************")
    print("¡Bienvenido al juego!")
    print("Adiviná el numero que la computadora genera:")
    print("***********************************************")


    numero_aleatorio = random.randint(1, x)

    intento = 0

    while intento != numero_aleatorio:
        intento = int(input(f"Ingresa un numero entre 1 y {x}: "))

        if intento < numero_aleatorio:
            print("El numero que ingresaste es menor. Intentá de nuevo")
        elif intento > numero_aleatorio:
            print("Ese numero es muy grande. Intentá otra vez")

    print(f"¡Felicidades! El numero era {numero_aleatorio}")


adivina_el_numero(15)
