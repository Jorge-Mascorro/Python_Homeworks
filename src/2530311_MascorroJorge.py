"""
                    MANEJO DE STRINGS EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

"""
                    RESUMEN EJECUTIVO

    - ¿Qué es un string en Python?
       Son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str 
       y se delimitan mediante el uso de comillas simples o dobles.
    
    - ¿Qué operaciones básicas se pueden realizar: concatenar, obtener longitud, extraer sub-cadenas, buscar patrones, reemplazar texto?
       En Python, se pueden realizar diversas operaciones que involucra el manejo de string, como:
         - Concatenar: Unir dos o más cadenas de texto utilizando el operador +.
         - Obtener longitud: Utilizar la función len() para obtener el número de caracteres en una cadena.
         - Extraer sub-cadenas: Utilizar el operador de slicing para obtener partes específicas de una cadena.
         - Buscar patrones: Utilizar métodos como find() o index() para localizar sub-cadenas dentro de una cadena.
         - Reemplazar texto: Utilizar el método replace() para sustituir partes de una cadena por otras.

    - ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, nombres, contraseñas)?
       La validación de las entradas es esencial para mantener la integridad de los datos. Cuando un programa solicita la intervención 
       del usuario, no hay garantía de que éste siga las instrucciones. Pueden introducir letras donde se esperan números, o dejar campos 
       en blanco. Por eso es tan importante validar las entradas del usuario antes de utilizarlas.
    
    - ¿Qué cubrira este documento? 
       En este documento se llevaran a cabo 6 problemas relacionados a los strings en Python, en los cuales
       incluire el código, sus entradas y validaciones, asi también incluyendo a cada problema 3 casos de prueba (normal, borde y error).   
"""

"""
                     PRINCIPIOS Y BUENAS PRÁCTICAS

    - Los strings son inmutables: cualquier cambio genera una nueva cadena.
    - Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
    - Evitar "números mágicos" en índices; documentar qué extrae cada slice.
    - Usar métodos de string en lugar de reescribir lógica básica.
    - Diseñar validaciones claras: primero que no esté vacío, luego el formato.
    - Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""

# Problem 1: Full name formatter (name + initials)
"""
   - Descripción: 
   - Inputs:
   - Outputs:
   - Validations:
   - Test Cases: 
"""
full_name= input("What is your name?: ")
full_name= full_name.lower().strip()
if full_name == "":
    print("Error: invalid input, you didn´t enter a name")
parts= full_name.split()
if len(parts) < 2:
    print("Error: invalid input, you only enter one name")
full_name= " ".join(parts)
full_name= full_name.title()
print("Name in Title Case: ", full_name)

initials= ""
for name in parts:
    initial= name[0].upper()
    initials += initial + "."
print("The Initials are: ", initials)
    
    