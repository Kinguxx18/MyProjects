def  cesarCod(texto,desplazamiento):
    """
    Usuario.
    Esto es una función que recibe como párametro los siguientes=
    -Texto: parámetro en donde se introduce un texto para después
    codificarlo en cifrado de césar.
    -Desplazamiento: parámetro en donde se introduce un número el
    cual será el desplamiento por letras en el abecedario,para
    posteriormente codificar el texto o mensaje.
    Entradas: un texto y un número de desplazamiento.
    Salidas: texto codificado en cifrado de césar según el
    desplazamiento digitado.
    Restricciones:
    -El parámetro texto tiene que se un string.
    -El parámetro desplazamiento tiene que ser número entero no negativo,mayor o igual que 1 y menor o igual a 27.
    """
    #codifica  usando  cifrado  césar  con  el  desplazamiento  indicado
    alfabeto = "abcdefghijklmnñopqrstuvwxyzabcdefghijklmnñopqrstuvwxyz"
    codificado = ""
    if type(texto) != str:
        print("El parámetro texto tiene que ser un string.")
    print("El codificado del texto :" ,texto)
    if type(desplazamiento) != int:
        print("El parámetro desplazamiento es tiene que ser un entero.")
    texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    while not desplazamiento <= 27 and desplazamiento >= 1:
        print("El número del parámetro desplazamiento tiene que ser un número entre 1 y 27.")
        
    for  i  in  range(len(texto)):
        if texto[i] == ' ':
            i = codificado
            codificado = codificado + ' '
        else:
            codificado = codificado + (alfabeto[alfabeto.index(texto[i]) + desplazamiento])
    print("es: ", codificado)   

def  cesarDec(texto,desplazamiento):
    """
    Usuario.
    Esto es una función que recibe como párametro los siguientes.
    -Texto: parámetro en donde se introduce un texto coficado con cifrado
    de césar ,para después decodificarlo en cifrado de césar.
    Desplazamiento: parámetro en donde se introduce un número el
    cual será el desplamiento por letras en el abecedario,para
    posteriormente decodificar el texto o mensaje.
    Entradas: un texto codificado en cifrado de césar y un número de desplazamiento.
    Salidas: texto decodificado en cifrado de césar según el
    desplazamiento digitado.
    Restricciones:
    -El parámetro texto tiene que se un string.
    -El parámetro desplazamiento tiene que ser número entero no negativo,mayor o igual que 1 y menor o igual a 27.
    """
    #decodifica  usando  cifrado  césar  con  el  desplazamiento  indicado
    alfabeto = "abcdefghijklmnñopqrstuvwxyzabcdefghijklmnñopqrstuvwxyz"
    decodificado = ""
    if type(texto) != str:
        print("El parámetro texto tiene que ser un string.")
    print("El decodificado de la texto= ",texto)
    if type(desplazamiento) != int:
        print("El parámetro desplazamiento es tiene que ser un entero.")
    texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    while not desplazamiento <= 27 and desplazamiento >= 1:
        print("El número del parámetro desplazamiento tiene que ser un número entre 1 y 27.")
        desplazamiento = int(input("Por Favor.Digite el número de desplazamientos en el abecedario, para hacer el decodificado="))
    for  i  in  range(len(texto)):
        if texto[i] == ' ':
            i = decodificado
            decodificado = decodificado + ' '
        else:
            decodificado = decodificado + (alfabeto[alfabeto.index(texto[i]) - desplazamiento])
    return decodificado



import random
def leetCod(texto):
    """
    Función que utiliza el cifrado de 1337 o leet para codificar un texto,
    en donde recibe como parámetro un texto: que este se utilizará para
    codificar el mensaje o texto.
    Entradas: un texto
    Salidas:codificación en cifrado 1337 o leet ,del texto.
    Restricciones:el parámetro texto tiene que ser un string.
    """
    if type(texto) != str:
        print("El parámetro texto tiene que ser un string o texto")
        quit()
    texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    dic= {
        "a": ["4","@","/-\\","/\\","/\\","^"],
        "b": ["8","|3","6","13","|3","]3]"],
        "c": ["[","<","¢","{","©"],
        "d": ["|]","[]","]]","I>","|>","cl"],
        "e": ["3","&","€","[-"],
        "f": ["|=","]=","}","ph","[="],
        "g": ["6","[_+"],
        "h": ["|-|","#","]-[","[-]","]-[","[-]","=-=","}{","}-{"],
        "i": ["!","1","|","¡"],
        "j": ["_|","_/","]","</","_]"],
        "k": ["|<","|X","|{"],
        "l": ["1","|_","|","|_","¬"],
        "m": ["44","/\/\\","|\/|","|v|","IYI","IVI","[V]","^^","nn","//\\//\\","[V]","[\/]","/|\\","/|/||",".\\","/^^\\","/V\\","|^^|"],
        "n": ["|\|","/\/","//\\//","[\]","<\>","{\},\"//","[]\[]","]\[","~"],
        "o": ["0","[]","[]","¤"],
        "p": ["|*","|o","|º","|>","|","¶",],
        "q": ["0_","0,","[,]","<|","9"],
        "r": ["|2","/2","I2","|^","|~","®","|2,\"[z","l2"],
        "s": ["5","$","z","§"],
        "t": ["7","+","-|-"],
        "u": ["|_|","[_]","µ","[_]","\_/","\_\\","/_/"],
        "v": ["\/","\\//"],
        "w": ["\/\/","vv","'//","\\'","\^/","[n]","\X/","\|/","\_|_/","\\//\\//","\_=_/","]I[","UU"],
        "x": ["%","><","}{","×","]["],
        "y": ["`/","`[","-/","'/"],
        "z": ["2","~/_","7_"]}
    codificado = []
    for i in texto:
        if i == " ":
            codificado.append(i)
        else:
            x = dic.get(i)
            w = random.choice(x)
            codificado.append(w)
    return codificado

def vigereCod(texto,palabra):
    """
    Función que utiliza el cifrado de vigenere para codificar un mensaje.
    Que recibe como parámetros un texto y una palabra:
    -Texto :es el mensaje que se va a codificar en cifrado vigenere.
    -Palabra: es la clave para realizar el codificado del texto.
    Entradas:
    -Texto para realizar el codificado.
    -Palabra que será la clave del cifrado.
    Salidas:Codificación del texto ingresado por el usuario.
    Restricciones:
    Los parámetros texto y palabra tienen que ser un string.
    """
    if type(texto) != str:
        quit()
        print("El parámetro texto tiene que ser un string.")
    if type(palabra) != str:
        print("El parámetro palabra tiene que ser un string.")
        quit()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    indiceDeLetra = dict(zip(alfabeto, range(len(alfabeto))))
    letraDeIndice = dict(zip(range(len(alfabeto)),alfabeto))
    codificado = ""
    separarTexto = [texto[i:i + len(palabra)]for i in range(0, len(texto),len(palabra))]
    for porCadaSeparado in separarTexto:
        i = 0
        for letra in porCadaSeparado:
                numero = (indiceDeLetra[letra] + indiceDeLetra[palabra[i]]) % len(alfabeto)
                codificado += letraDeIndice[numero]
                i += 1
                
    return codificado

def vigereDec(texto,palabra):
    """
    Función que utiliza el cifrado de vigenere para decodificar un mensaje.
    Que recibe como parámetros un texto y una palabra:
    -Texto:es un mensaje codificado que se utilizará para decodificarlo.
    -Palabra: es la clave para realizar el decodificado del texto.
    Entradas:
    -Texto para realizar el decodificado.
    -Palabra que será la clave del cifrado.
    Salidas:Decodificación del texto ingresado por el usuario.
    Restricciones:
    Los parámetros texto y palabra tienen que ser un string.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    indiceDeLetra = dict(zip(alfabeto, range(len(alfabeto))))
    letraDeIndice = dict(zip(range(len(alfabeto)),alfabeto))
    if type(texto) != str:
        print("El parámetro texto tiene que ser un string.")
        quit()
    if type(palabra) != str:
        print("El parámetro palabra tiene que ser un string.")
        quit()
    print("El texto codificado que ingresó es: ",texto)
    decodificado = ""
    separarTexto = [texto[i:i + len(palabra)]for i in range(0, len(texto),len(palabra))]
    for porCadaSeparado in separarTexto:
        i = 0
        for letra in porCadaSeparado:
            #se aplica el inverso del codigo "codificar" para obtener el texto decodificicado
            numero = (indiceDeLetra[letra] - indiceDeLetra[palabra[i]]) % len(alfabeto)
            decodificado += letraDeIndice[numero]
            i += 1
    print("El texto decodificado es: ",decodificado)
