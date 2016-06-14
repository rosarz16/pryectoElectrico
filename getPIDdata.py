import mysql.connector
# import os

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     passwd='rosario',
                                     db='paretodatabase')

cursor = connection.cursor()
T = 0.7
a = 0.5
K = 1
L = 0.21
Jdimax = 0.6
Jdomax = 0.5
Jrmax = 0
t0 = L/T
Ms = 1.6
# Los normalizados son las columnas 9,10,11

# obtencion de los parametros de la base de datos en funcion de Ms

cursor.execute("SELECT * from paretopruebatabla where (Ms between %s-0.001 and %s+0.001);",
               (Ms, Ms))
resultados = cursor.fetchall()

# Averiguar cual de los cuatro casos tenemos
for resultado in resultados:


# Caso optimizando Jr
if Jrmax == 0:
    # Inicializacion de banderas
    maximo_Jdi = 0
    maximo_Jdo = 0
    minimo_Jdi = 10
    minimo_Jdo = 10

    # Normalizar los J dados por el usuario
    for resultado in resultados:
        if maximo_Jdi < resultado[6]:
            maximo_Jdi = float(resultado[6])
        if maximo_Jdo < resultado[7]:
            maximo_Jdo = float(resultado[7])
        if minimo_Jdi > resultado[6]:
            minimo_Jdi = float(resultado[6])
        if minimo_Jdo > resultado[7]:
            minimo_Jdo = float(resultado[7])

    Jdinorm_usuario = (Jdimax - minimo_Jdi)/(maximo_Jdi - minimo_Jdi)
    Jdonorm_usuario = (Jdomax - minimo_Jdo)/(maximo_Jdo - minimo_Jdo)

# Caso optimizando Jdi
elif Jdimax == 0:
    # Inicializacion de banderas
    maximo_Jr = 0
    maximo_Jdo = 0
    minimo_Jr = 10
    minimo_Jdo = 10

    # Normalizar los J dados por el usuario
    for resultado in resultados:
        if maximo_Jr < resultado[8]:
            maximo_Jr = resultado[8]
        if maximo_Jdo < resultado[7]:
            maximo_Jdo = resultado[7]
        if minimo_Jr > resultado[8]:
            minimo_Jr = resultado[8]
        if minimo_Jdo > resultado[7]:
            minimo_Jdo = resultado[7]

    Jrnorm_usuario = (Jrmax - minimo_Jr) / (maximo_Jr - minimo_Jr)
    Jdonorm_usuario = (Jdomax - minimo_Jdo) / (maximo_Jdo - minimo_Jdo)

# Caso optimizando Jdo
elif Jdomax == 0:
    # Inicializacion de banderas
    maximo_Jr = 0
    maximo_Jdi = 0
    minimo_Jr = 10
    minimo_Jdi = 10

    # Normalizar los J dados por el usuario
    for resultado in resultados:
        if maximo_Jr < resultado[8]:
            maximo_Jr = resultado[8]
        if maximo_Jdi < resultado[6]:
            maximo_Jdi = resultado[6]
        if minimo_Jr > resultado[8]:
            minimo_Jr = resultado[8]
        if minimo_Jdi > resultado[6]:
            minimo_Jdi = resultado[6]

    Jrnorm_usuario = (Jrmax - minimo_Jr) / (maximo_Jr - minimo_Jr)
    Jdinorm_usuario = (Jdimax - minimo_Jdi) / (maximo_Jdi - minimo_Jdi)

# print maximo_Jdi, minimo_Jdi, Jdinorm_usuario, Jdonorm_usuario

# Seleccionar los errores normalizados mas parecidos de la base de datos

# Optimizar para Jr
if Jrmax == 0:
    Jrmax = 2 #Tengo que cambiar por un 1 cuando la normalizacion funcione jaja
    for resultado in resultados:
    #     print resultado[0], resultado[1], resultado[5], resultado[13], resultado[6], resultado[7], resultado[8]
        if resultado[9] <= Jdimax and resultado[10] <= Jdomax and resultado[11] <=Jrmax:
            Jrmax = resultado[11]
            identificador = resultado[13]
    # print identificador
    # print maximo_Jdi, minimo_Jdi, maximo_Jdo, minimo_Jdo

# Optimizar para Jdi
if Jdimax == 0:
    Jdimax = 2 #Tengo que cambiar por un 1 cuando la normalizacion funcione jaja
    for resultado in resultados:
        if resultado[9] <= Jdimax and resultado[10] <= Jdomax and resultado[11] <=Jrmax:
            Jdimax = resultado[9]
            identificador = resultado[13]
    # print identificador

# Optimizar para Jdo
if Jdomax == 0:
    Jdomax = 2 #Tengo que cambiar por un 1 cuando la normalizacion funcione jaja
    for resultado in resultados:
        if resultado[9] <= Jdimax and resultado[10] <= Jdomax and resultado[11] <=Jrmax:
            Jdomax = resultado[10]
            identificador = resultado[13]
    # print identificador
