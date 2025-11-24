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
      Este programa le pide al usuario que escriba su nombre completo y se encarga de limpiarlo, corrigiendo mayúsculas, minúsculas 
      y espacios de más para dejarlo perfectamente presentable. También verifica que el usuario haya ingresado un nombre válido con 
      al menos dos palabras. Después, muestra el nombre ya formateado en un estilo claro y profesional, y finalmente genera automáticamente 
      las iniciales correspondientes.

   - Inputs:
      - full_name (string): El nombre completo ingresado por el usuario, que puede venir en mayúsculas, minúsculas o con espacios extra.

   - Outputs:
      - Name in Title Case: Es el nombre del usuario ya limpio, sin espacios extra y con mayúsculas correctamente aplicadas.
      - The Initials are: Son las iniciales generadas automáticamente tomando la primera letra de cada palabra del nombre.

   - Validations:
      - if full_name == "": # Verifica que el usuario no deje el nombre en blanco.
      - if len(parts) < 2: # Verifica que el usuario haya ingresado al menos dos nombres.
      
   - Test Cases: 
      # CASO NORMAL

        What is your name?: jorge mascorro barraza
        Name in Title Case: Jorge Mascorro Barraza
        The Initials are: J.M.B.
      
      # CASO BORDE

        What is your name?: jorge
        Error: invalid input, you only enter one name

      # CASO ERROR

        What is your name?:
        Error: invalid input, you didn´t enter a name
"""
full_name= input("What is your name?: ")
full_name= full_name.lower().strip()
if full_name == "":
    print("Error: invalid input, you didn´t enter a name")
    exit()
parts= full_name.split()
if len(parts) < 2:
    print("Error: invalid input, you only enter one name")
    exit()
full_name= " ".join(parts)
full_name= full_name.title()
print("Name in Title Case: ", full_name)

initials= ""
for name in parts:
    initial= name[0].upper()
    initials += initial + "."
print("The Initials are: ", initials)
    

# Problem 2: Simple email validator (structure + domain)
"""
   - Descripción: 
      Este problema consiste en crear un validador sencillo de correos electrónicos que revise si el formato básico es correcto. 
      Debe verificar que el texto tenga exactamente un símbolo '@', que el dominio incluya al menos un punto y que no existan espacios. 
      Si el correo es válido, también debe mostrar la parte del dominio que aparece después del '@'.

   - Inputs:
      - email_text = input("Set your email: ").- Le solicita al usuario que ingrese que correo que desea verificar.

   - Outputs:
      - Valid email: True, Valid email: False .- Ambos muestran si el correo es válido dependiendo si cumple con las validaciones estipuladas.
      - print("The domain is:", domain).- Se imprime la parte que sigue después del arroba solamente si es válido el correo.

   - Validations:
      - email_text.count("@") == 1 .- Valida que el correo solo contenga un arroba.
      - " " not in email_text .- Valida que el correo no contenga espacios en blanco.
      - "." in domain .- Valida que tenga un "." en el dominio después del arroba.
  
   - Test Cases: 
      # CASO NORMAL

      Set your email: mascorro@123.mx
      Valid email: True
      The domain is: 123.mx
      
      # CASO BORDE

      Set your email: a@b.c
      Valid email: True
      The domain is: b.c

      # CASO ERROR

      Set your email: jorgeeegmail.com
      Valid email: False

"""
print("\n")

email_text= input("Set your email: ")

if email_text.count("@") == 1 and " " not in email_text:
   at= email_text.find("@")
   domain= email_text[at+1:]
   if "." in domain:
      print("Valid email: True")
      print("The domain is:", domain)
   else:
      print("Valid email: False")
else:
    print("Valid email: False")

# Problem 3: Palindrome checker (ignoring spaces and case)
"""
   - Descripción: 

   - Inputs:

   - Outputs:

   - Validations:
  
   - Test Cases: 
      # CASO NORMAL

      
      # CASO BORDE


      # CASO ERROR


"""
print("\n")

phrase= input("Type the phrase you wanna check: ")
phrase= phrase.replace(" ","").lower()
reverse= phrase[::-1]
if len(phrase) > 3:

   if reverse == phrase:
      print("Is palindrome: True")
      print("Normalized phrase: ", phrase)

   else:
      print("Is palindrome: False")
      
else:
   print("Is palindrome: False")