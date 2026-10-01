import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    cadena = cadena.lower()
    cadena = cadena.strip()
    cadena = cadena.replace("á","a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    cadena = cadena.replace("ä","a").replace("ë", "e").replace("ï", "i").replace("ö", "o").replace("ü", "u")
    return cadena

def enmascarar(palabra_secreta, letras_usadas=""):
    cadena_resultado = ""
    for c in palabra_secreta:
        if c in letras_usadas:
            cadena_resultado += c
        elif c == " ":
            cadena_resultado += " "
        else:
            cadena_resultado += "_"
    return cadena_resultado


def ha_ganado(palabra_enmascarada):
    todas_descubiertas = True
    for c in palabra_enmascarada:
        if c == "_":
            todas_descubiertas = False
    return todas_descubiertas


def mostrar_estado(palabra_enmascarada = "", letras_usadas = "", intentos_restantes = 0):
    print("Estado: " + " ".join(palabra_enmascarada))
    print("Letras usadas: " + letras_usadas)
    print("Intentos restantes: " + str(intentos_restantes))

def pedir_letra(letras_usadas = "abcd"):
    valido = False
    letra=""
    while valido == False:
        letra = input("Introduce una letra: ")
        if letra.isalpha():
            if len(letra)==1:
                if letra not in letras_usadas:
                    valido = True
                else:
                    print("Esta letra ya se ha usado")
            else:
                print("Escribe un solo caracter")
        else:
            print("Escribe un texto válido (solo una letra)")
    return letra.lower()


def jugar(palabra_secreta = "", intentos_maximos = 6):
    palabra_original = palabra_secreta
    palabra_secreta = normalizar(palabra_secreta)
    if palabra_secreta == "":
        return None
    palabra_enmascarada = enmascarar(palabra_secreta)
    intentos = intentos_maximos
    letras_usadas = ""
    while ha_ganado(palabra_enmascarada) == False and intentos >= 0:
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos)
        letra_recibida = pedir_letra(letras_usadas)
        letras_usadas += letra_recibida
        if letra_recibida not in palabra_secreta:
            intentos -= 1
            print("Esta letra NO está en la palabra secreta.")
        else: 
            print("Esta letra SI está en la palabra secreta")
            palabra_enmascarada = enmascarar(palabra_secreta, letras_usadas)

    if ha_ganado(palabra_enmascarada):
        print("Enhorabuena! Has ganado el juego.")
    else:
        print("Lo siento... Has perdido el juego.")
        print("La palabra hasta donde has descubierto era: " + palabra_enmascarada)
    print("La palabra original era: " + palabra_original)
        

jugar(elige_palabra())


# TODO: Escribe el programa principal
