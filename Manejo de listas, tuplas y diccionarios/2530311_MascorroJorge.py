"""
                    MANEJO DE LISTAS, TUPLAS Y DICCIONARIOS EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
       Una LISTA es un tipo de dato que permite almacenar varios elementos en una misma variable, de manera ordenada, 
       cada elemento se separa por una coma y se pone entre corchetes.
       Las TUPLAS son muy similar a las listas por el simple hecho de que tambien almacena varios elementos en una misma variables,
       de manera ordenada, sin embargo hay una diferencia entre estas dos y es que las tuplas son INMUTABLES, estas se definen usando 
       paréntesis y separando cada elemento por una coma.
       Un DICCIONARIO es una estructura que almacena datos mediante pares clave–valor, se escribe con llaves {} y sí se puede 
       modificar; además, permite acceder a la información usando una clave en lugar de un índice.
    
    - ¿Qué significa que una lista sea mutable y una tupla inmutable?
       Que una lista sea mutable significa que se puede cambiar su contenido después de crearla: agregar elementos, eliminarlos o modificar 
       cualquier valor usando índices o métodos propios de las listas. En cambio, que una tupla sea inmutable significa que no se puede 
       alterar una vez creada; no puedes cambiar sus elementos, ni agregar nuevos, ni eliminar existentes.

    - ¿Cómo se usan los diccionarios para asociar claves con valores?
       Los diccionarios en Python se usan para asociar claves con valores, funcionando como una especie de “tabla” donde cada clave 
       apunta a un dato específico. Se escriben usando llaves {}, y cada par tiene la forma clave : valor. Para acceder a un valor, 
       simplemente usas la clave entre corchetes.

    - ¿Qué cubrira este documento? 
       En este documento se llevaran a cabo 6 problemas relacionados a las listas, tuplas y diccionarios en Python, en los cuales
       incluire el código, sus entradas y validaciones, asi también incluyendo a cada problema 3 casos de prueba (normal, borde y error).   
"""

                                   # PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    - Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
    - Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
    - Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
    - Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
    - Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
    - Escribir código legible y mensajes claros para el usuario.
"""

# Problem 1: Shopping list basics (list operations)
"""
   - Descripción: 
      Este problema consiste en gestionar una lista de compras a partir de una cadena de productos separados por comas. 
      El programa debe limpiar y convertir esa cadena en una lista, permitir agregar un nuevo artículo, mostrar la cantidad 
      total de elementos y verificar si un producto específico se encuentra en la lista. Además, requiere validar entradas vacías 
      y manejar adecuadamente espacios extra o elementos vacíos.

   - Inputs:
      - initial_items_text= input("What items are you carrying?: ") .- Pide al usuario los items que tiene
      - new_item= input("Which object do you want to add?: ").strip() .- Pregunta al usuario que objeto agregara a la lista
      - search_item= input("What product are you looking for?: ").strip() .- Pregunta al usuario que item se buscara en la lista

   - Outputs:
      - print("Items list: ", items_list) .- Se muestra la lista ya ordenada y normalizada.
      - print("Total items: ", len(items_list)) .- Se muestra la cantidad total de items que se encuentran en la lista
      - print("Found item: ", search_item in items_list) .- Se muestra si el item que el usuario pidio buscar si se encuentra o no.

   - Validations:
      - if initial_items_text.strip() == "":
            print("Error: the items cannot be empty") .- Se valida que los items que proporciona el usuario no se encuentre vacíos.
      - if new_item == "" or search_item == "": .- Si el usuario no agrega ningun item o pide buscar uno manda el mensaje de error.
            print("the items cannot be empty")

   - Test Cases: 
      # CASO NORMAL

      What items are you carrying?: apple,banana,orange
      Which object do you want to add?: grapes
      What product are you looking for?: banana
      Items list:  ['apple', 'banana', 'orange', 'grapes']
      Total items:  4
      Found item:  True

      # CASO BORDE

      What items are you carrying?: mango,,peach,kiwi,
      Which object do you want to add?: papaya
      What product are you looking for?: kiwi
      Items list:  ['mango', 'peach', 'kiwi', 'papaya']
      Total items:  4
      Found item:  True

      # CASO ERROR

      What items are you carrying?:
      Error: the items cannot be empty
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

initial_items_text= input("What items are you carrying?: ")

if initial_items_text.strip() == "":
    print("Error: the items cannot be empty")
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

    new_item= input("Which object do you want to add?: ").strip()
    search_item= input("What product are you looking for?: ").strip()

    if new_item == "" or search_item == "":
        print("the items cannot be empty")
    else:
        items_list.append(new_item)
    
    print("Items list: ", items_list)
    print("Total items: ", len(items_list))
    print("Found item: ", search_item in items_list)


# Problem 2: Points and distances with tuples
"""
   - Descripción: 
      Este problema consiste en trabajar con dos puntos en un plano 2D usando tuplas para almacenar sus coordenadas. A partir 
      de los valores ingresados, el programa debe calcular la distancia euclidiana entre ambos puntos y obtener el punto medio 
      entre ellos. También requiere validar que las coordenadas puedan convertirse a números flotantes.

   - Inputs:
      - x_1= float(input("Set value of x1: ")) .- Pide el valor de x1
      - x_2= float(input("Set value of x2: ")) .- Pide el valor de x2
      - y_1= float(input("Set value of y1: ")) .- Pide el valor de y1
      - y_2= float(input("Set value of y2: ")) .- Pide el valor de y2

   - Outputs:
      - print("Point A: ",point_a) .- Imprime el punto A en forma de tupla.
      - print("Point B: ",point_b) .- Imprime el punto B en forma de tupla.
      - print("Distance: ", distance) .- Imprime la distancia entre los puntos A y B.
      - print("Midpoint: ", midpoint) .- Imprime el punto medio en forma de tupla.

   - Validations:
      - La validacion de que los valores de las coordenadas se puedan convertir a flotante se encuentran dentro de un try-except.

   - Test Cases: 
      # CASO NORMAL

      Set value of x1: 0
      Set value of x2: 3
      Set value of y1: 0
      Set value of y2: 4
      Point A:  (0.0, 0.0)
      Point B:  (3.0, 4.0)
      Distance:  5.0
      Midpoint:  (1.5, 2.0)

      # CASO BORDE

      Set value of x1: 0.000000001
      Set value of x2: 1000000000
      Set value of y1: -0.000000001
      Set value of y2: 1000000000
      Point A:  (1e-09, -1e-09)
      Point B:  (1000000000.0, 1000000000.0)
      Distance:  1414213562.373095
      Midpoint:  (500000000.0, 500000000.0)

      # CASO ERROR

      Set value of x1: 10
      Set value of x2: 5.5
      Set value of y1: abc
      Error: Inputs cannot be converted to floats
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

try:
    x_1= float(input("Set value of x1: "))
    x_2= float(input("Set value of x2: "))
    y_1= float(input("Set value of y1: "))
    y_2= float(input("Set value of y2: "))

    point_a= (x_1,y_1)
    point_b= (x_2,y_2)
    distance= ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5
    midpoint_x= (x_1 + x_2)/2 
    midpoint_y= (y_1 + y_2)/2
    midpoint= (midpoint_x, midpoint_y)

    print("Point A: ",point_a)
    print("Point B: ",point_b)
    print("Distance: ", distance)
    print("Midpoint: ", midpoint)
except:
    print("Error: Inputs cannot be converted to floats")
    exit()


# Problem 3: Product catalog with dictionary
"""
   - Descripción: 
      Este problema consiste en gestionar un catálogo de productos utilizando un diccionario donde cada clave es el nombre 
      del producto y cada valor es su precio. El programa debe verificar si un producto solicitado existe, calcular el total 
      a pagar según la cantidad ingresada y mostrar un mensaje de error si el producto no está en el catálogo. Además, se valida 
      que el nombre del producto no esté vacío y que la cantidad sea mayor que cero.

   - Inputs:
      - product_name = input("Enter product name: ").strip() .- El usuario debe ingresar el nombre del producto.
      - quantity = int(input("Enter quantity: ")) .- El usuario debe ingresar la cantidad que llevara de ese producto.

   - Outputs:
      - print("Unit price:", unit_price) .- Se muestra el precio unitario.
      - print("Quantity:", quantity) .- Se muestra la cantidad de producto.
      - print("Total:", total_price) .- Se muestra el total de la compra
      - print("Error: product not found") .- Se muestra unicamente cuando el producto ingresado por el usuario no se encuentra 
                                             dentro del diccionario.

   - Validations:
      - if quantity <= 0:
            print("Error: quantity must be greater than 0") .- Valida que la cantidad de producto sea mayor que 0.
            exit()
      - if product_name == "":
            print("Error: product name cannot be empty") .- Valida que el usuario si haya escrito un producto.
            exit()
      - if product_name in product_prices:
            unit_price = product_prices[product_name] .- Verifica que el producto se encuentre dentro del diccionario.
            total_price = unit_price * quantity

   - Test Cases: 
      # CASO NORMAL

      Enter product name: apple
      Enter quantity: 3
      Unit price: 10.0
      Quantity: 3
      Total: 30.0

      # CASO BORDE

      Enter product name: banana
      Enter quantity: 1
      Unit price: 6.5
      Quantity: 1
      Total: 6.5

      # CASO ERROR

      Enter product name: watermelon
      Enter quantity: 2
      Error: product not found
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

product_prices = {
    "apple": 10.0,
    "banana": 6.5,
    "orange": 8.0
                 }

product_name = input("Enter product name: ").strip()

if product_name == "":
    print("Error: product name cannot be empty")
    exit()

try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Error: quantity must be an integer")
    exit()

if quantity <= 0:
    print("Error: quantity must be greater than 0")
    exit()

if product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")


# Problem 4: Student grades with dict and list
"""
   - Descripción: 
      Este programa gestiona las calificaciones de varios estudiantes utilizando un diccionario donde cada nombre está 
      asociado a una lista de notas. El usuario ingresa el nombre de un estudiante y el sistema calcula su promedio para 
      determinar si está aprobado. También incluye validaciones básicas, como verificar que el nombre exista en el diccionario y que 
      cuente con calificaciones registradas. Si el estudiante no se encuentra, se muestra un mensaje de error.

   - Inputs:
      - student_1 .- nombre del estudiante 1 
      - grade1_1 .- calificación 1 del estudiante 1 
      - grade1_2 .- calificación 2 del estudiante 1 
      - grade1_3 .- calificación 3 del estudiante 1 
      - student_2 .- nombre del estudiante 2 
      - grade2_1 .- calificación 1 del estudiante 2 
      - grade2_2 .- calificación 2 del estudiante 2 
      - grade2_3 .- calificación 3 del estudiante 2 
      - student_3 .- nombre del estudiante 3 
      - grade3_1 .- calificación 1 del estudiante 3 
      - grade3_2 .- calificación 2 del estudiante 3 
      - grade3_3 .- calificación 3 del estudiante 3 

   - Outputs:
      - print("Grades:", list) .- Muestra las calificaciones en una lista
      - print("Average:", average) .- Muestra el promedio del alumno
      - print("Passed:", is_passed) .- Muestra si paso o no.

   - Validations:
      - if student_name == "":
            print("Error: you didn´t enter a student") .- Verifica que student_name no se encuentre vacío al hacer strip().
      - elif student_name not in grades:
            print("Error: student not found") .- Valida que el estudiante se encuentre en el diccionario.
      - if len(list) == 0:
            print("Error: no grades available") .- Valida que la lista de calificaciones no este vacía.
      

   - Test Cases: 
      # CASO NORMAL

      Student´s name: Ana
      School Grade: 85
      School Grade: 90
      School Grade: 88
      --------------------------
      Student´s name: Luis
      School Grade: 70
      School Grade: 75
      School Grade: 72
      --------------------------
      Student´s name: Maria
      School Grade: 95
      School Grade: 94
      School Grade: 96
      --------------------------
      Student: Luis
      Grades: [70.0, 75.0, 72.0]
      Average: 72.33333333333333
      Passed: True

      # CASO BORDE

      Student´s name: Pepe
      School Grade: 70
      School Grade: 70
      School Grade: 70
      --------------------------
      Student´s name: Juan
      School Grade: 100
      School Grade: 100
      School Grade: 100
      --------------------------
      Student´s name: Rosa
      School Grade: 69.9
      School Grade: 70
      School Grade: 70.1
      --------------------------
      Student: Pepe
      Grades: [70.0, 70.0, 70.0]
      Average: 70.0
      Passed: True

      # CASO ERROR

      Student´s name: Ana
      School Grade: 80
      School Grade: 90
      School Grade: 70
      --------------------------
      Student´s name: Jose
      School Grade: 60
      School Grade: 50
      School Grade: 40
      --------------------------
      Student´s name: Karla
      School Grade: 100
      School Grade: 95
      School Grade: 90
      --------------------------
      Student: Pedro
      Error: student not found
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

grades= {}

student_1= input("Student´s name: ").strip()
grade1_1= float(input("School Grade: "))
grade1_2= float(input("School Grade: "))
grade1_3= float(input("School Grade: "))
grades[student_1]= [grade1_1, grade1_2, grade1_3]

student_2= input("Student´s name: ").strip()
grade2_1= float(input("School Grade: "))
grade2_2= float(input("School Grade: "))
grade2_3= float(input("School Grade: "))
grades[student_2]= [grade2_1, grade2_2, grade2_3]


student_3= input("Student´s name: ").strip()
grade3_1= float(input("School Grade: "))
grade3_2= float(input("School Grade: "))
grade3_3= float(input("School Grade: "))
grades[student_3]= [grade3_1, grade3_2, grade3_3]

student_name= input("Student: ").strip()

if student_name == "":
    print("Error: you didn´t enter a student")
elif student_name not in grades:
    print("Error: student not found")
else:
    list= grades[student_name]
    if len(list) == 0:
        print("Error: no grades available")
    else:
        average= sum(list) / len(list) 
        is_passed= average >= 70

        print("Grades:", list)
        print("Average:", average)
        print("Passed:", is_passed)


