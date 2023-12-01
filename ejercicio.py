#podes entrar a la disco

def verificar_edad():
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad >= 18:
            print("¡Bienvenido/a a la discoteca! Disfruta de la fiesta.")
        else:
            print("Lo siento, eres menor de edad. No puedes entrar a la discoteca.")
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")

if __name__ == "__main__":
    print("¡Bienvenido/a al verificador de edad para la discoteca!")
    verificar_edad()
