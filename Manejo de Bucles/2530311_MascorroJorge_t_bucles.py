"""
                    MANEJO DE BUCLES EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué es un bucle for y para qué se usa típicamente?
       El for es un tipo de bucle, parecido al while pero con ciertas diferencias. La principal es que el número de iteraciones 
       de un for esta definido de antemano, mientras que en un while no. La diferencia principal con respecto al while es en la condición.
       El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar 
       un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál 
       se pueden aplicar una serie de operaciones.

    - ¿Qué es un bucle while y cuándo es más natural usarlo?
       El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará 
       mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. 
       Llamaremos iteración a una ejecución completa del bloque de código.

    - ¿Qué son un contador y un acumulador?
       Un contador es una variable que cuenta el número de veces que ocurre un evento, incrementando o decrementando su valor en una 
       cantidad constante, típicamente en 1. Un acumulador, por otro lado, es una variable que suma valores en un ciclo, donde el valor 
       que se suma a la variable puede variar en cada iteración

    - ¿Por qué es importante definir bien la condición de salida y evitar ciclos infinitos?
       Es crucial definir bien la condición de salida y evitar los ciclos infinitos en programación porque, de lo contrario, 
       el programa consumirá recursos excesivos del sistema, dejará de responder y eventualmente se bloqueará. Una condición de 
       salida bien definida asegura que el bucle complete su tarea y termine correctamente. 
          
    - ¿Qué cubrira este documento? 
       En este documento se llevaran a cabo 6 problemas relacionados a los bucles en Python, en los cuales incluire el código, 
       sus entradas y validaciones, asi también incluyendo a cada problema 3 casos de prueba (normal, borde y error).   
"""

                                   # PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    - Usar for cuando conoces de antemano cuántas iteraciones necesitas (por ejemplo, 1 a 10).
    - Usar while cuando la cantidad de iteraciones depende de una condición (por ejemplo, leer hasta que el usuario escriba "EXIT").
    - Inicializar correctamente contadores y acumuladores antes del bucle.
    - Actualizar las variables de control dentro del bucle while para no crear ciclos infinitos.
    - Mantener el cuerpo del bucle lo más simple posible; extraer lógica compleja en funciones si es necesario.
"""

# Problem 1: Sum of range with for
"""
   - Descripción: 
      Este problema busca que el programa recorra números desde 1 hasta un valor que indique el usuario y calcule cuánto suman todos juntos.
      Además, también se requiere obtener la suma únicamente de los números pares, usando un ciclo for. Antes de hacer cualquier operación, 
      el programa debe revisar que la entrada sea un número entero válido y que sea mayor o igual a 1, para evitar errores y asegurar 
      un resultado correcto.
 
   - Inputs:
      - n_limit= input("Enter the sum limit: ") .- Le pide al usuario que ingrese el límite.

   - Outputs:
      - print("Sum 1-n:", total_sum) .- Se muestra la suma de todos los números hasta el límite que ingreso el usuario.
      - print("Even sum 1-n:", even_sum) .- Se muestra solo la suma de los números pares dentro del límite.

   - Validations:
      - if not n_limit.isdigit():
            print("Error: cannot be converted to an integer") .- Valida que el límite puesto por el usuario se pueda convertir a entero.
      - if n_limit < 1:
            print("Error: invalid input") .- Valida que el número límite sea mayor que 1.

   - Test Cases: 
      # CASO NORMAL

      Enter the sum limit: 10
      Sum 1-n: 55
      Even sum 1-n: 30

      # CASO BORDE

      Enter the sum limit: 1
      Sum 1-n: 1
      Even sum 1-n: 0

      # CASO ERROR

      Enter the sum limit: 0
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

n_limit= input("Enter the sum limit: ")

if not n_limit.isdigit():
    print("Error: cannot be converted to an integer")
else:
     n_limit= int(n_limit)
     if n_limit < 1:
        print("Error: invalid input")
        exit()

     total_sum= 0
     even_sum= 0

     for number in range(1, n_limit + 1):
        total_sum += number
        if number % 2 == 0:
            even_sum += number

print("Sum 1-n:", total_sum)
print("Even sum 1-n:", even_sum)


# Problem 2: Multiplication table with for
"""
   - Descripción: 
      Este problema consiste en generar la tabla de multiplicar de un número elegido por el usuario, mostrando cada resultado 
      desde 1 hasta un límite que también se ingresa. La idea es practicar el uso de ciclos for y el formato de salida con f-strings 
      para que cada operación se muestre claramente. Antes de hacer la tabla, el programa debe asegurarse de que los valores sean 
      enteros válidos y que el límite sea por lo menos 1 para evitar errores.

   - Inputs:
      - base= input("Enter the base: ") .- Pide al usuario la base a multiplicar.
      - m= input("Enter the m: ") .- Pide al usuario hasta que número quiere multiplicar.

   - Outputs:
      - print(f" {base} x {i}= {multiplication}") .- Esta hecho con f-strings para que se muestre en forma de tabla.

   - Validations:
      - if not base.isdigit() or not m.isdigit():
            print("Error: cannot be converted to an integer") .- Valida que la base y la m se puedan convertir en enteros.
      - if m < 1:
            print("Error: invalid input") .- Valida que m sea mayor que 1.

   - Test Cases: 
      # CASO NORMAL

      Enter the base: 5
      Enter the m: 4
      5 x 1= 5
      5 x 2= 10
      5 x 3= 15
      5 x 4= 20

      # CASO BORDE

      Enter the base: 7
      Enter the m: 1
      7 x 1= 7

      # CASO ERROR

      Enter the base: abc
      Enter the m: 5
      Error: cannot be converted to an integer
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

base= input("Enter the base: ")
m= input("Enter the m: ")

if not base.isdigit() or not m.isdigit():
    print("Error: cannot be converted to an integer")
else:
    base= int(base)
    m= int(m)

    if m < 1:
        print("Error: invalid input")
        exit()
    else:
        for i in range(1, m+1):
            multiplication= base * i
            print(f" {base} x {i}= {multiplication}")


# Problem 3: Average of numbers with while and sentinel
"""
   - Descripción: 
      Este problema consiste en pedir números al usuario uno por uno hasta que ingrese un valor especial llamado sentinela 
      (en este caso, -1), que indica que ya no desea continuar. Mientras el usuario escriba números válidos, el programa los suma 
      y los cuenta para calcular su promedio al final. Si el usuario termina el programa sin haber ingresado ningún número válido, 
      debe mostrarse un mensaje indicando que no hay datos suficientes para hacer el cálculo.

   - Inputs:
      - number= input("Enter a number: ") .- Pide al usuario el número.
      - if number== "-1": .- Está fijo en el código pero si el usuario ingresa -1 se detiene el programa.
            break

   - Outputs:
      - print("Count: ", counter) .- Muestra la cantidad de números ingresados.
      - print("Average: ", average) .- Muestra el promedio de los números ingresados antes del sentinela.
      - if len(number)== 0:
            print("Error: no data") .- Se muestra únicamente si no se ingresan datos válidos.

   - Validations:
      - Cada lectura intenta convertirse en float, esto se encuentra dentro de un try-excpet.

   - Test Cases: 
      # CASO NORMAL

      Enter a number: 10
      Enter a number: 5
      Enter a number: 3
      Enter a number: -1
      Count:  3
      Average:  6.0

      # CASO BORDE

      Enter a number: 8
      Enter a number: -1
      Count:  1
      Average:  8.0

      # CASO ERROR

      Enter a number: -1
      Error: no data
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

counter= 0
total= 0.0

while True:
    number= input("Enter a number: ")
    if number== "-1":
        break

    if len(number)== 0:
        print("Error: no data")
    
    try: 
        quantity= float(number)
        counter += 1
        total += quantity
        average= total / counter
    except:
        print("Error: cannot be converted to a float")

print("Count: ", counter)
print("Average: ", average)


# Problem 4: Password attempts with while
"""
   - Descripción: 
      Este problema simula un sistema básico de inicio de sesión donde el usuario debe ingresar una contraseña correcta 
      dentro de un número limitado de intentos. El programa compara cada intento con la contraseña real y, si el usuario 
      acierta, muestra un mensaje de acceso exitoso. En caso de que falle todos los intentos permitidos, se muestra un 
      mensaje indicando que la cuenta ha sido bloqueada

   - Inputs:
      - user_password= input("Enter the password: ") .- Pide al usuario la contraseña.

   - Outputs:
      - print("Login success!!!") .- Se muestra si el usuario ingreso la contraseña correcta.
      - print("Account locked") .- Se muestra si el usuario no ingreso la contraseña antes del número máximo de intentos.

   - Validations:
      - MAX_ATTEMPTS= 3 .- Lo válido como una constante en el código.
      - if remaining_attempts > 0:
            print(f"Wrong password you has {remaining_attempts} attempts") .- Se cuenta cuantos intentos le quedan al usuario.

   - Test Cases: 
      # CASO NORMAL

      Enter the password: hola
      Wrong password you has 2 attempts
      Enter the password: 2530311
      Login success!!!

      # CASO BORDE

      Enter the password: hola
      Wrong password you has 2 attempts
      Enter the password: blacky
      Wrong password you has 1 attempts
      Enter the password: 2530311
      Login success!!!

      # CASO ERROR

      Enter the password: hola
      Wrong password you has 2 attempts
      Enter the password: 260346
      Wrong password you has 1 attempts
      Enter the password: pepito
      Account locked
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

VALID_PASSWORD= "2530311" 
MAX_ATTEMPTS= 3
attempts= 0

while attempts < MAX_ATTEMPTS:
    user_password= input("Enter the password: ")
    if user_password == VALID_PASSWORD:
        print("Login success!!!")
        break
    else:
        attempts +=1
        remaining_attempts= MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            print(f"Wrong password you has {remaining_attempts} attempts")
        else:
            print("Account locked")


# Problem 5: Simple menu with while
"""
   - Descripción: 
      Este problema consiste en crear un menú interactivo que permita al usuario elegir entre varias opciones y ejecutar acciones 
      diferentes según su selección. El menú debe repetirse continuamente hasta que el usuario escriba 0, lo que indica que desea 
      salir del programa. Además, el sistema debe mostrar mensajes específicos según la opción elegida y manejar correctamente los 
      casos en que el usuario ingrese una opción no válida.

   - Inputs:
      - option= int(input("Choose your option: ")) .- Se le pide al usuario que elija la opción que desea ejecutar.

   - Outputs:
      - if option == 1:
            print("Hello!!") .- Si elije 1 imprime "Hello!!".
      - elif option == 2:
            print(f"Your counter so far: {count}") .- Si elije 2 imprime el contador hasta ese momento.
      - elif option == 3:
            count +=1
            print("Counter incremented") .- Si elije 3 incrementa en 1 el contador.
      - elif option == 0: 
            print("Bye!") .- Si elije 0 imprime "Bye!".
      
   - Validations:
      - else: 
            print("Invalid option") .- Si elije otra opción que no sea 0,1,2,3 imprime "Invalid option" y rompe el while.
            break

   - Test Cases: 
      # CASO NORMAL

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 1
      Hello!!

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 3
      Counter incremented

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 2
      Your counter so far: 1

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 0
      Bye!

      # CASO BORDE

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 0
      Bye!

      # CASO ERROR

      --- MENU ---
      1) Show greeting
      2) Show current counter value
      3) Increment counter
      0) Exit
      Choose your option: 5
      Invalid option
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

option= -1
count= 0
while option != 0:
    print("\n--- MENU ---")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option= int(input("Choose your option: "))


    if option == 1:
        print("Hello!!")
    elif option == 2:
        print(f"Your counter so far: {count}")
    elif option == 3:
        count +=1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else: 
        print("Invalid option")
        break


# Problem 6: Pattern printing with nested loops
"""
   - Descripción: 

   - Inputs:
 
   - Outputs:

   - Validations:

   - Test Cases: 
      # CASO NORMAL

      
      Enter the number of rows: 6
      Normal pattern:
      *
      **
      ***
      ****
      *****
      ******

      # CASO BORDE

      Enter the number of rows: 1
      Normal pattern:
      *

      # CASO ERROR

      Enter the number of rows: 0
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

n= input("Enter the number of rows: ")

if not n.isdigit():
    print("Error: invalid input")
else:
    n = int(n)

    if n < 1:
        print("Error: invalid input")
    else:
        print("\nNormal pattern:")
        for i in range(1, n + 1):
            print("*" * i)

print("------------------------------------------------------------------------------------------------------")

# CONCLUSIONES
"""
   Al trabajar con bucles me di cuenta de que usar for y usar while se sienten muy diferentes: el for es más directo cuando ya 
   sabes cuántas veces repetir algo, mientras que el while se parece más a estar “esperando” a que pase cierta condición. 
   También noté lo útiles que son los contadores y acumuladores, porque te ayudan a llevar control sin perderte entre tantos números. 
   Eso sí, descubrí que el while puede ser peligroso si no lo manejas bien, porque un simple descuido puede dejar el programa atrapado 
   en un ciclo infinito. Los ejercicios de menús y contraseñas mostraron situaciones muy reales donde el while es perfecto para repetir 
   intentos o preguntas. Y, por último, los bucles anidados me ayudaron a ver cómo se pueden crear patrones visuales paso a paso, como 
   si estuviera dibujando con código.
"""

# REFERENCIAS
"""
   1) Bucle For - https://ellibrodepython.com/for-python 
   2) Bucle For en python - https://j2logo.com/bucle-for-en-python/#for-en-python
   3) Bucles While - https://ellibrodepython.com/while-python
   4) Qué es un acumulador? - https://www.youtube.com/watch?v=L51HqhsvG68&t=27s
   5) Python range() y uso del For - https://docs.python.org/3/tutorial/controlflow.html#for-statements
"""
