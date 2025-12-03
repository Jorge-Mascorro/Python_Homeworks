"""
                    MANEJO DE FUNCIONES EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué es una función en Python y para qué sirve?
        Una función es un bloque de código reutilizable que realiza una tarea específica. En lugar de repetir el mismo código 
        varias veces, lo puedes definir una vez y usarlo cuando lo necesites. Una función sirve para organizar y estructurar mejor 
        el código, haciendo que sea más fácil de leer y mantener. Permite reutilizar bloques de código sin necesidad de repetirlos, 
        lo que reduce errores y facilita modificaciones. Además, ayuda a abstraer detalles complejos, de manera que puedas concentrarte 
        en qué hace la función sin preocuparte demasiado por cómo lo hace.
    
    - ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
        Un parámetro es una variable que se define en la declaración de la función es decir, en la parte donde defines la función. 
        Actúa como un “espacio reservado” que indica qué tipo de información espera la función.
        Un argumento es el valor real que le pasas a la función cuando la llamas. Ese valor concreta lo que la función va a usar 
        como datos de entrada.

    - ¿Por qué es útil separar la lógica en funciones reutilizables?
        Separar la lógica en funciones reutilizables es útil porque permite organizar el código de manera más clara y estructurada, 
        evitando repeticiones innecesarias. Cuando una tarea está encapsulada en una función, se puede usar varias veces en distintos 
        lugares sin tener que reescribirla, lo que ahorra tiempo y reduce errores.

    - ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
        Un valor de retorno es el dato que una función regresa después de ejecutar su tarea. Es la manera de enviar un resultado 
        desde la función hacia el lugar del programa donde se llamó. Devolver resultados hace que las funciones sean más flexibles 
        y reutilizables. Si solo imprimes el resultado, no puedes usar ese valor en otros cálculos o guardarlo en una variable. Con un valor 
        de retorno, puedes almacenar el resultado, pasarlo a otra función, compararlo o manipularlo de distintas maneras.

    - ¿Qué cubrira este documento? 
       En este documento se llevaran a cabo 6 problemas relacionados a las funciones en Python, en los cuales incluire el código, 
       sus entradas y validaciones, asi también incluyendo a cada problema 3 casos de prueba (normal, borde y error).   
"""

                                   # PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    - Preferir funciones pequeñas que hagan una sola cosa (single responsibility).
    - Evitar repetir código: si copias/pegas lógica, considera extraerla en una función.
    - Intentar que las funciones sean “puras” cuando sea posible (mismo input -> mismo output, sin efectos secundarios externos).
    - Documentar con comentarios simples qué hace cada función y qué parámetros espera.
    - Dar nombres claros a las funciones (calculate_bmi, not f1 o do_it).
"""

# Problem 1: Rectangle area and perimeter (basic functions)
"""
   - Descripción: 
      Este problema consiste en crear dos funciones para calcular el área y el perímetro de un rectángulo, usando sus 
      dimensiones de ancho y alto. Además, se debe validar que los valores ingresados sean positivos; si no lo son, se muestra 
      un mensaje de error y no se realizan los cálculos. El objetivo es practicar el uso de funciones, validaciones y operaciones básicas.

   - Inputs:
      - width= float(input("Width: ")) .- Pide al usuario el ancho.
      - height= float(input("Height: ")) .- Pide al usuario la altura.

   - Outputs:
      - print("Area: ", area) .- Imprime el área del rectángulo.
      - print("Perimeter: ", perimeter) .- Imprime el perimetro del rectángulo.

   - Validations:
      - if width > 0 and height > 0: .- Valida que el ancho y la altura sean mayores que 0, y si no se cumple muestra un mensaje de error.

   - Test Cases: 
      # CASO NORMAL

      Width: 5
      Height: 3
      Area:  15.0
      Perimeter:  16.0

      # CASO BORDE

      Width: 0.01
      Height: 0.01
      Area:  0.0001
      Perimeter:  0.04

      # CASO ERROR

      Width: -2
      Height: 5
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

def calculate_area(width,height):
    return width*height
def calculate_perimeter(width,height):
    return 2 * (width + height)

width= float(input("Width: "))
height= float(input("Height: "))

if width > 0 and height > 0:
    area= calculate_area(width,height)
    perimeter= calculate_perimeter(width,height)

    print("Area: ", area)
    print("Perimeter: ", perimeter)
else:
    print("Error: invalid input")


# Problem 2: Grade classifier (function with return string)
"""
   - Descripción: 
      Este problema consiste en crear una función que reciba una calificación numérica y la clasifique en una letra según rangos 
      establecidos (A, B, C, D, F). Además, se debe validar que la calificación esté entre 0 y 100, mostrando un mensaje de error 
      si no lo está.

   - Inputs:
      - score = float(input("Enter your grade (0-100): ")) .- Pide al usuario su calificación.

   - Outputs:
      - print("Score: ", score) .- Muestra la calificación del estudiante.
      - print("Category: ", grade) .- Muestra la categoría en la que se encuentra el estudiante.

   - Validations:
      - if score < 0 or score > 100: .- Valida que el score no sea menor que 0 o mayor que 100, y si lo es muestra mensaje de error.
            return None

   - Test Cases: 
      # CASO NORMAL

      Enter your grade (0-100): 85
      Score:  85.0
      Category:  B

      # CASO BORDE

      Enter your grade (0-100): 90
      Score:  90.0
      Category:  A

      # CASO ERROR

      Enter your grade (0-100): 120
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")


def classify_score(score):
    if score < 0 or score > 100:
        return None
    elif score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60:
        return "F" 

try: 
    score = float(input("Enter your grade (0-100): "))
    grade = classify_score(score)
    if grade is None:
        print("Error: invalid input")
    else:
        print("Score: ", score)
        print("Category: ", grade)
except ValueError:
    print("Error: invalid input")


# Problem 3: List statistics function (min, max, average)
"""
   - Descripción: 
      Este problema consiste en crear una función que reciba una lista de números y devuelva un diccionario con su valor mínimo, 
      máximo y promedio. Además, se deben validar las entradas para asegurar que sean números y que la lista no esté vacía, 
      mostrando un mensaje de error si no se cumple.

   - Inputs:
      - numbers_text= input("Enter numbers separated by commas: ").strip() .- Pide al usuario los números separados por comas.

   - Outputs:
      - print("Min: ", stats["min"]) .- Muestra el valor mínimo de la lista.
      - print("Max: ", stats["max"]) .- Muestra el valor máximo de la lista.
      - print("Average: ", stats ["average"]) .- Muestra el promedio de la lista.

   - Validations:
      - if not numbers_text:
            print("Error: invalid input") .- Valida que los números no se encuentren vacíos tras el strip().
      - if not numbers_list:
            print("Error: invalid input") .- Valida que la lista no se encuentre vacía después de la conversión.
   
   - Test Cases: 
      # CASO NORMAL

        Enter numbers separated by commas: 10,20,30,40,50
        Min:  10.0
        Max:  50.0
        Average:  30.0

      # CASO BORDE

        Enter numbers separated by commas: 42
        Min:  42.0
        Max:  42.0
        Average:  42.0

      # CASO ERROR

        Enter numbers separated by commas: 10,abc,30
        Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

def summarize_numbers(numbers_list):
    return{
          "min": min(numbers_list),
          "max": max(numbers_list),
          "average": sum(numbers_list) / len(numbers_list)
          }

numbers_text= input("Enter numbers separated by commas: ").strip()
if not numbers_text:
    print("Error: invalid input")
else:
    try:
        numbers_list = [float(x.strip()) for x in numbers_text.split(",")]
        if not numbers_list:
            print("Error: invalid input")
        else:
            stats= summarize_numbers(numbers_list)
            print("Min: ", stats["min"])
            print("Max: ", stats["max"])
            print("Average: ", stats ["average"])

    except ValueError:
        print("Error: invalid input")


# Problem 4: Apply discount list (pure function)
"""
   - Descripción: 
      Este problema consiste en crear una función que reciba una lista de precios y una tasa de descuento, y devuelva una 
      nueva lista con los precios ya descontados sin modificar la original. El programa debe validar que los precios sean 
      positivos y que la tasa esté entre 0 y 1.

   - Inputs:
      - prices_text = input("Enter prices separated by commas: ").strip() .- Pide al usuario los precios separados por comas.
      - discount_input = input("Enter discount rate (0–1): ").strip() .- Pide al usuario la tasa de descuento en formato decimal (0 a 1).

   - Outputs:
      - print("Original prices:", prices_list) .- Muestra la lista original de precios ingresada por el usuario.
      - print("Discounted prices:", discounted_list) .- Muestra la nueva lista con los precios ya descontados.

   - Validations:
      - if not prices_text or not discount_input: .- Valida que el texto de precios y la tasa de descuento no estén vacíos después del strip().
      - if not prices_list or any(price <= 0 for price in prices_list): .- Valida que la lista no esté vacía y que todos los precios sean mayores a 0. 
      - if discount_rate < 0 or discount_rate > 1: .- Valida que la tasa de descuento esté entre 0 y 1.

   - Test Cases: 
      # CASO NORMAL

        Enter prices separated by commas: 100,200,300,400
        Enter discount rate (0–1): 0.10
        Original prices: [100.0, 200.0, 300.0, 400.0]
        Discounted prices: [90.0, 180.0, 270.0, 360.0]

      # CASO BORDE

        Enter prices separated by commas: 50
        Enter discount rate (0–1): 0
        Original prices: [50.0]
        Discounted prices: [50.0]

      # CASO ERROR

        Enter prices separated by commas: 100,-20,50
        Enter discount rate (0–1): 0.2
        Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

prices_text = input("Enter prices separated by commas: ").strip()
discount_input = input("Enter discount rate (0–1): ").strip()

if not prices_text or not discount_input:
    print("Error: invalid input")
else:
    try:
        prices_list = [float(x.strip()) for x in prices_text.split(",")]

        if not prices_list or any(price <= 0 for price in prices_list):
            print("Error: invalid input")
        else:
            discount_rate = float(discount_input)

            if discount_rate < 0 or discount_rate > 1:
                print("Error: invalid input")
            else:
                discounted_list = apply_discount(prices_list, discount_rate)

                print("Original prices:", prices_list)
                print("Discounted prices:", discounted_list)
    except ValueError:
        print("Error: invalid input")


# Problem 5: Greeting function with default parameters
"""
   - Descripción: 
      Este problema consiste en crear una función que genere un saludo personalizado usando un nombre y, de manera opcional, 
      un título como “Dr.” o “Eng.”. La función debe construir el saludo combinando correctamente título y nombre, y regresar 
      un mensaje completo. Además, el programa debe validar que el nombre no esté vacío y debe permitir llamadas posicionales y 
      nombradas para practicar parámetros por defecto en Python.

   - Inputs:
      - name_input = input("Enter name: ").strip() .- Pide al usuario el nombre y elimina espacios.
      - title_input = input("Enter title (optional): ").strip() .- Pide el título opcional del usuario y elimina espacios.

   - Outputs:
      - print("Greeting:", greeting2) .- Muestra el mensaje final de saludo generado por la función.

   - Validations:
      - if not name_input: .- Valida que el nombre no esté vacío tras el strip(). Si está vacío, muestra "Error: invalid input".
      - title_input = title_input.strip() .- El título se normaliza quitando espacios; puede estar vacío sin causar error.

   - Test Cases: 
      # CASO NORMAL

        Enter name: Alice
        Enter title: Dr
        Greeting: Hello, Dr Alice!

      # CASO BORDE

        Enter name: Bob
        Enter title:
        Greeting: Hello, Bob!

      # CASO ERROR

        Enter name:
        Enter title: Eng
        Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name

    return f"Hello, {full_name}!"

name_input = input("Enter name: ").strip()
title_input = input("Enter title: ").strip()

if not name_input:
    print("Error: invalid input")
else:
    greeting1 = greet(name_input)

    if title_input:
        greeting2 = greet(name=name_input, title=title_input)
    else:
        greeting2 = greet(name=name_input)

    print("Greeting:", greeting2)


# Problem 6: Factorial function (iterative or recursive)
"""
   - Descripción: 
      El programa calcula el factorial de un número entero no negativo usando una función factorial(n). Se valida que n sea entero, 
      mayor o igual a cero y que no exceda un límite razonable para evitar resultados enormes. Luego llama a la función factorial 
      y muestra el resultado al usuario.

   - Inputs:
      - n_text = input("Enter a non-negative integer: ").strip() .- Solicita al usuario un entero no negativo.

   - Outputs:
      - print("n:", n) .- Muestra el número ingresado ya validado.
      - print("Factorial:", value) .- Muestra el resultado del factorial calculado.

   - Validations:
      - if n < 0 or n > 20: print("Error: invalid input") .- Valida que n sea mayor o igual a 0 y no exceda el límite permitido.

   - Test Cases: 
      # CASO NORMAL

        Enter a non-negative integer: 6
        n: 6
        Factorial: 720

      # CASO BORDE

        Enter a non-negative integer: 0
        n: 0
        Factorial: 1

      # CASO ERROR

        Enter a non-negative integer: -3
        Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

"""
    Versión iterativa: se elige para evitar límites de recursión y ser más eficiente.
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n_text = input("Enter a non-negative integer: ").strip()

if not n_text.isdigit():
    print("Error: invalid input")
else:
    n = int(n_text)

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        value = factorial(n)
        print("n:", n)
        print("Factorial:", value)

print("------------------------------------------------------------------------------------------------------")

# CONCLUSIONES
"""
   Las funciones me ayudaron a mantener el código más ordenado, porque pude separar cada tarea en una parte clara y reutilizable, 
   en vez de repetir lo mismo varias veces. También entendí que usar return es mucho más útil que solo imprimir, porque te permite 
   trabajar con los resultados después, combinarlos o validarlos. Algo que me gustó fue usar parámetros con valores por defecto, ya 
   que hacen el código más flexible y fácil de usar sin tanta configuración. Noté que "guardar" la lógica en funciones es especialmente 
   cómodo cuando hay cálculos repetidos o validaciones que se usan en varios lugares.
"""

# REFERENCIAS
"""
   1) Defining Functions - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
   2) Diferencia entre parámetros y argumentos - https://www.geeksforgeeks.org/computer-science-fundamentals/difference-between-parameters-and-arguments/?utm_source 
   3) La declaración return de Python: uso y mejores prácticas - https://realpython.com/python-return-statement/?utm_source 
   4) Funciones en Python - https://ellibrodepython.com/funciones-en-python?utm_source
   5) Python Functions - https://www.programiz.com/python-programming/function
"""


