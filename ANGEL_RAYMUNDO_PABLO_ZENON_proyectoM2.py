#LONGITUD DE UNA FRASE
palabra_ingresada = input("Ingresa una palabra: ")  #Aqui pedimos que se ingrese una palabra y la guardamos en la variable palabra_ingresada

if len(palabra_ingresada) >= 4 and len(palabra_ingresada) <=8 :  #Si la longitud de la palabra ingresada es mayor o igual a 4 letras y menor o igual a 8
    print("La palabra se encuentra en el rango, ¡por lo tanto es correcta!!") #imprimimos que la palabra se encuentra en el rango 

elif len(palabra_ingresada) > 8 :   #Si la longitud de la palabra ingresada es meyor a 8 letras
    letras_faltantes = len(palabra_ingresada) - 8 #le resta 8 a la longitud de la palabra ingresada y la guardamos en letras_faltantes
    print(f"Solo tiene {len(palabra_ingresada)}Sobran {letras_faltantes} letras")

elif len(palabra_ingresada) < 4 :  #Ahora si la palabra ingresada en menor a 4 letras 
    letras_faltantes = 4 - len(palabra_ingresada)  # Se le resta la longitud de la palabra a 4
        #E imprimimos lo siguiente  la longitud de la palabra y cuantas palabras le sobran
    print(f"Tu palabra tiene {len(palabra_ingresada)} por lo tanto le faltan: {letras_faltantes} letras")

#Y por ultimo imprimimos la palabra con su respectiva longitud
print(f"Y la longitud de {palabra_ingresada} es igual a {len(palabra_ingresada)} letras")



# ENCUENTRA EL CUADRANTE 
intentos = 3  # Aqui declare una variable de intentos que nos permitira terminar el programa cuando estos se hayan usado
while intentos > 0: #Posteriormente usé el ciclo while mientras que el numero de intentos sea mayor a 0 se ejecutará el siguiente bloque de codigo
    eje_x = int(input("Ingrese una cordenada para el eje X(Que no sea el 0): ")) #Pedimos al isuario mediante un input un numero , casteamos el numero que ingreso a /
    #un int
    if eje_x != 0:
        break     #Despues use la sentencia brack para poder interrumpir la ejecucion de un ciclo si es que el valor de eje_x no es igual a 0

    while eje_x == 0 : #Volvi a usar el ciclo while , pero ahora por si el usuario ingresa el numero prohibido (0) 
        intentos -= 1  #Restasmos 1 intento
        print("El numero del eje X no debe ser 0") #Imprimimos este mensaje en pantalla 
        if intentos != 0: #si intentos no es 0 imprimimos lo siguente
            print(f"Le quedan {intentos} Intentos")
        elif intentos == 0: #Al igual aqui si intentos ya es sero
            print("Sus intentos se han acabado :(")
        break  #Y volvemos a usar break para terminar el ciclo while  y pasar con el siguiente bloque de codigo

    if intentos == 0:
        exit()   # Cuando intentos sea 0 detenemos el programa con la sentencia exit()

while intentos > 0:  # En el ciclo while mientras intentos en mayor a 0
    eje_y = int(input("Ingrese el numero para el eje Y(Que no sea el 0): ")) # Solicitamos la cordenada Y y las casteamos a un entero

    if eje_y != 0: #si el eje es distinto a nuestro numero prohibido terminamos el ciclo
        break

    while eje_y == 0 : #y en dado caso se que fuera igual a 0
        intentos -= 1  # le restamos 1 a los intentos
        print("El numero del eje Y no debe ser 0") # E inmrimimos el siguiente mensaje
        if intentos != 0:  #Si los intentos son distintos a 0 
            print(f"Le quedan {intentos} Intentos")  # le imprimimos cuantos intentos le quedan al ususario
        elif intentos == 0: #Si los intentos son 0 le indicmos al usuario que sus intentos se han acabado
            print("Sus intentos se han acabado :(")
        break

if eje_x and eje_y > 0 :   # si el ejeX y el ejeY es mayo a 0
    print("Te encuentras en el cuadrante | :) ") #Le imprimimos que esta en el cuadrante 1

elif eje_x < 0 and eje_y > 0 : #y si el ejeX es menor a 0 y el ejeY es mayor 
    print("Te encuentras en el cuadrante ||") #Le imprimos que se encuentra en el curadrante 2

elif eje_x and eje_y < 0 :  #si el ejeX y el ejeY son menores al 0
    print("Estas en el cuadrante |||") #Le imprimimos que se encuentra en el cuadrante 3

elif eje_x > 0 and eje_y < 0 :  #A l igual aqui si el ejeX es mayor a 0 yen ejeY es menor a 0
    print("Estas en el eje |v") #Imprime que se encuentra en el cuadrante 4

