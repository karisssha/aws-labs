#def verificar_edad():

        #edad = int(input("que edad tienes? ")) 
        #try edad >= 18:
            #print("bienvenido!")
        #except: 
            #print("no podes entrar")
            #verificar_edad()
#def verificar_año():    
        #año = int(input("ingresa tu año del dni"))

#if __name__ == "__main__":
    #print("¡Bienvenido/a al verificador de edad para la discoteca!")
    #verificar_edad()
def verificar_edad_documento():
    try:
        edad = int(input("¿Cuántos años tienes? "))
        documento = int(input("¿Cuál es tu año de nacimiento (documento)? "))
    except ValueError:
        print("Por favor, ingresa números válidos para la edad y el año de nacimiento.")
        return  # Salir de la función si hay un error de valor

    # Verificar si la edad corresponde al año del documento y si es mayor de edad
    if edad >= 18 and (2023 - documento) == edad:
        print("¡Bienvenido/a a la discoteca! Disfruta de la fiesta.")
    else:
        print("Lo siento, no cumples con los requisitos para entrar a la discoteca.")

if __name__ == "__main__":
    print("¡Bienvenido/a al verificador de edad y documento para la discoteca!")
    verificar_edad_documento()


#if true or false***