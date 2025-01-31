# Programa 1: Verificar la longitud de una palabra
def verificar_longitud(palabra):
    longitud = len(palabra)  # Calculamos la cantidad de letras

    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

# Solicitar palabra al usuario
palabra = input("Ingresa una palabra: ")
verificar_longitud(palabra)


# Programa 2: Determinar el cuadrante de un punto en el plano cartesiano
def determinar_cuadrante(x, y):
    if x == 0 or y == 0:
        print("Las coordenadas no pueden ser 0 en ninguno de sus valores.")
        return  # Salir de la función si X o Y son 0

    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    else:
        print("El punto se encuentra en el cuadrante IV")

# Solicitar coordenadas al usuario
x = int(input("Ingrese la coordenada X: "))
y = int(input("Ingrese la coordenada Y: "))

determinar_cuadrante(x, y)