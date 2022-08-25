Las reflexiones que me ha dejado el bootcamp hasta el momento:
He aprendido a usar las iteraciones y los ciclos  de manera excelente para modificar el flujo de la ejecucion de mis distintos programas aplicando distintas condiciones.  
De igual manera he dominado los distintos atributos aplicables a las listas y los distintos tipos de colecciones y en en todos los aspectos me he sentido satisfecho

EXPLICACION DEL PROGRAMA Longitud de una frase:

Al comienzo soliciye una palabra al usuario mediante un input, y despues la guarde en una variable llamada palabra_ingresada
Posteriormente use el ciclo if para que se ejecutase una cierta parte del codigo si la longitud de la palabra es mayor o igual a 4 letras y si es menor o igual a 8 letras, si fuese imprimiria en pantalla que la palabra se encuentra en el rango
Luego use el elif por si la longitud de la palabra es mayor a 8 letras, por lo tanto restaria la longitud de la palabra - 8 y la guardaria en una variable llamada letras_restantes y por ultimo imprimiria cuantas letras sobran 
Nuevamente volvi a usar el elif por si la longitud de la palabra es menor a 4 letras : lo que haria seria restar 4 menos la longitud de letra_ingresada y lo guardaria en la variable letras_faltantes  e imprimiria cuantas letras faltan
Y por ultimo imprimira la longitud y la palabra

EXPLICACION DEL PROGRAMA Encuentra el cuadrante

Declaro una variable de intentos que permitira llevar un control sobre los fallos del usuario,
Uso el ciclo while para que se ejecute mientras los intentos sean mayores a 0
mediante un input pido al usuario que ingrese una cordenada corrspondiente al ejeX y las convierto a un entero, ademas la guardo en una variable
Use if para corroborar que no haya ingresado un 0 si es asi contienua el ciclo while
Usamos  un while y en caso de haber ingresado un 0 le restaremos 1 a intentos e imprimiremos que el numero del ejeX no debe de ser un 0 
Despues usamos IF Si el numero de intentos es distintos a 0 o sea mayor conntinuamos con el programa y le imprimimos los intentos que le quedan al usuario
Pero si (elif) es igual a 0 : Le imprime que se han acabado sus intentos y termina el programa con exit() que lo que hace es salirse del programa o terminarlo 
Y lo mismo pasa con el ejeY

Y para determinar en que cuadrante esta usamos 
if para saber si el ejeX y el ejeY son mayores a 0, por lo tanto imprimimos que se encuentra en el cuadrante 1 
y asi con sus respectivos cuadrantes
