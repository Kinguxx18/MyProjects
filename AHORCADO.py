INTENTOS_MAX = 7

def ahorcado ():
    """Subrutina principal del juego ahorcado.
    Entradas y Restricciones:ninguna.
    Salidas:El juego de ahorcado.
    """
    global INTENTOS_MAX
    limpiarPantalla()
    imprimirEntrada()
    continuar = True
    while continuar:
        textoOriginal = leerTextoOriginal()
        limpiarPantalla()
        texto = preparar(textoOriginal)
        intentadas = ""
        intentos = 0
        ronda = 1
        while intentos < INTENTOS_MAX and\
              not adivino(texto,intentadas):
            limpiarPantalla()
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento = leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos += 1
            intentadas += letraIntento
            ronda += 1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar = leerJugarNuevamente()
    imprimirMensajeDespedida()
def limpiarPantalla():
    """
    Subrutina que imprime líneas en blanco para limpiar la pantalla.
    Entradas y Restricciones:ninguna.
    Salidas: 40 líneas en blanco.
    """
    print("\n" *40)

def imprimirEntrada():
    """
    Subrutina que imprime un mensaje de bienvenida.
    Entradas y Restricciones: ninguna.
    Salidas: Mensaje de Bienvenida.
    """
    print("Bienvid@ al Juego de")
    print("""─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████████─████████████████───██████████████─██████████████─████████████───██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─
─██░░██████░░██─██░░██──██░░██─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████░░██─██░░████░░░░██─██░░██████░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██████░░██─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██─────────██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██████░░██─██░░██████░░██─██░░██──██░░██─██░░██████░░████───██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██████░░██─██░░██──██░░██████─██░░██████████─██░░██──██░░██─██░░████░░░░██─██░░██████░░██─
─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██─
─██████──██████─██████──██████─██████████████─██████──██████████─██████████████─██████──██████─████████████───██████████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    print("""

             ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀.⠀⢠⠞⠉⠙⠲⡀ 
              ⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀  ⡏⠀⠀⠀⠀⠀⢷
            ⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀ ⢸⠀⠀⠀⠀⠀ ⡇
            ⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀ ⣸⠀ OK⠀ ⡇
            ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀ ⣿⠀  ⢹⠀⠀⠀⠀⠀ ⡇
            ⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀   ⡇⠀⠀⠀⠀ ⡼ 
              ⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀  ⠘⠤⣄⣠⠞  
              ⢸⣷⡦⢤⡤⢤⣞⣁                
          ⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦.           
        ⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿          
        ⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸
            ⣿⣿⣧⣀⣿………⣀⣰⣏⣘⣆⣀ """)                                                        
    print()                                                                        
    print("Creado por Jeramy mairena Reyes")
def leerTextoOriginal():
    """
    Función que lee de la consola la palabra o frase a ser
    adivinada y retorna como resultado el texto leído.
    Entradas: texto del usuario
    Salidas:texto del ingresado.
    Restricciones: ninguna.
    """
    texto = input("Ingrese la palabra o frase que se adivinará:")
    while not esTextoValido(texto):
        print("El texto solo puede contener letra y espacios:")
        texto = input("Ingrese la palabra o frase que se adivinará. Solo puede contener letra y espacios:")
    return texto

def esTextoValido(texto):
    """
    Función booleana que dice si un string es un texto válido
    para adivinar en el juego.
    Entradas: texto a analizar.
    Salidas: True si el texto contiene sólo letras,espacios y algunos caracteres, Falso si no.
    Restricciones: texto debe ser un string.
    """
    if type(texto) != str:
        raise Exception("Texto debe ser un string")
    if texto == "":
        return False
    for letra in texto:
        if letra.lower() not in "aábcdeeéfghiíjklmnñoópqrstuúüvwxyz":
            return False
    return True  
def preparar(texto):
    """
    Convierte el texto a minúsculas,sustituye acentos y elimina
    espacios al inicio y al final.
    Entradas: texto a procesar.
    Salidas: texto sin minúsculas,acentos y espacios al inico y al final.
    Restricciones: texto debe ser un string.
    """
    if type(texto) != str:
        raise Exception("texto debe ser un string.")
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.replace("á","a")
    texto = texto.replace("é","e")
    texto = texto.replace("í","i")
    texto = texto.replace("ó","o")
    texto = texto.replace("ú","u")
    texto = texto.replace("ü","u")
    return texto
def adivino(texto,intentadas):
    """
    Función booleana que dice si el usuario ya adivinó el texto.
    Entradas:
    -texto:Texto preparado (sin tildes, ni acentos)
    -intentadas:letras que el usuario ha intentado
    Salidas:True si todas las letras del texto ya han sido intentadas,False si no.
    Restricciones:
    -texto debe ser un string de letras sin acentos.
    .intentadas debe ser un string de letras sin acentos.
    """
    if type(texto) != str or type(intentadas) != str:
        raise Exception("El texto y las letras deben ser ser string.")
    if not esTextoValido(texto):
        raise Exception("El texto y las intentadas continen caracteres no válidos.")
    for letra in texto:
        if letra != " ":
            if letra not in intentadas:
                return False
    return True

def imprimirRonda(texto, intentadas, intentos,ronda):
    """
    Esta función imprime los mensajes requeridos para cada
    ronda del juegp.
    Imprime el número de ronda actual, un mensaje indica
    las letras que ya fueron utilizadas, cantidad de intentos
    fallidos y también escribe el texto enmascarado.
    Entradas:
    -texto: texto preparado sin tildes ni acentos.
    -intentadas: letras que le usuario ha intentado.
    -ronda: número de ronda por la que va el juego.
    Salidas:Impresión en pantalla de la información de la ronda.
    Restricciones: ninguna.
    """
    print()
    print("RONDA NÚMERO", ronda)
    print("Letras que ya fueron utilizadas:", intentadas)
    print("Cantidad de intentos fallidos:", intentos)
    print()
    print(enmascarar(texto, intentadas))
    print()

def enmascarar(texto, intentadas):
    """
    Retorna un sting con un guión bajo por cada letra que
     no ha sido adivinada. Si una letra del texto aparece en las
     letras intentadas, entonces le agrega como tal un lugar del
      guion.
     Si el texto original tiene espacios , los sustituye con guiones normales.
     Entradas:
     -texto: texto a divinar
     -intentadas: letras que el usuario ha intentado.
     Salidas: string con el texto enmascarado.
     Restricciones: ninguna.
     """
    listaPalabras = texto.split()
    resultado = ""
    for palabra in listaPalabras:
         for letra in palabra:
             if letra in intentadas:
                 resultado += letra + " "
             else:
                 resultado += "_ "
         resultado += "- "
    return resultado[:-2]

def  leerIntento(intentadas):
    """
    Función que pide al usuario que escriba una letra 
    para adivinar. Si ya se encuentra en las intentadas o no es una
    letra, debe imprimir un mensaje de error y volver a pedir
    la letra.
    Entradas:
    - intentadas: letras que el usuario ha intentado.
    Salidas: string con la letra elegida por el usuario.
    Restricciones: ninguna.
    """
    print()
    letra = input("Digite una letra: ")
    letra = letra.lower()
    while len(letra) != 1 or letra not in "abcdefghijklmnñopqrstuvwxyz"\
        or letra in intentadas:
        print("Por favor ingrese una letra que no haya intentado",intentadas)
        letra = input("Digite una letra:")
        letra = letra.lower()
    print()
    return letra

def aciertaIntento(texto, letra):
    """
    Función booleana que dice si un intento es correcto o no.
    Entradas:
    -texto que se está adivinando.
    -letra que intentó el usuario.
    Salidas: True si la letra se encuentra en el texto a adivinar
     False si no.
    Restricciones: ninguna.
    """
    return letra in texto

def imprimirMensajeAcierto():
    """
    Subrutina que imprime si acerto una letra.
    Entradas:letra ingresada.
    Salidas:Acertó la letra.
    Restricciones:ninguna.
    """
    print("¡Ha adivinado! XD")
def imprimirMensajeNoAcierto():
    """
    Subrutina que imprime no acerto una letra.
    Entradas: letra ingresada.
    Salidas: No acerto la letra
    Restricciones: ninguna.
    """
    print("¡Letra no encuentrada! :(")

def imprimirMensajeVictoria(textoOriginal):
    """
    Subrutina que imprime las felicitaciones por acertar la palabra.
    Entradas: palabra completa
    Salidas: las felicidades por acertar el texto.
    Restricciones: ninguna.
    """
    print("¡FELICIDADES HA ACERTADO LA PALABRA ERA:", textoOriginal)

def imprimirMensajeDerrota(textoOriginal):
    """
    Subrutina que imprime la derrota por lo acertar la palabra o el texto.
    Entradas: La palabra
    Salidas: La derrota por no acertar el texto.
    Restricciones: ninguna.
    """
    print("LO SENTIMOS PERO NO ACERTÓ EL TEXTO .SUERTE LA PRÓXIMA.EL TEXO ERA:",textoOriginal)

def leerJugarNuevamente():
    """
    Función booleana que pregunta al usuario si desea jugar
    de nuevo. Sólo acepta "S" o "N" como respuesta.
    Entradas: ninguna.
    Salidas: True si el usuario escribe "S" , False si no.
    Restricciones: ninguna.
    """
    print()
    respuesta = input("¿Desea volver a jugar de nuevo? (S/N) ")
    respuesta = respuesta.lower()
    while respuesta not in ["s","n"]:
        respuesta = input("¿Desea volver a jugar de nuevo?")
        respuesta = respuesta.lower()
    return respuesta == "s"

def imprimirMensajeDespedida():
    """
    Subrutina que imprime la despedida para salir del juego.
    Entradas y Restricciones: ninguna.
    Salida:Despedida.
    """
    print("GRACIAS POR JUGAR LO ESPERAMOS LA PRÓXIMA VES QUE DESÉE JUGAR DE NUEVO .")

ahorcado()  
