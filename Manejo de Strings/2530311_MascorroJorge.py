"""
                    MANEJO DE STRINGS EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
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

                                   # PRINCIPIOS Y BUENAS PRÁCTICAS
"""
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
print("------------------------------------------------------------------------------------------------------")

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
print("------------------------------------------------------------------------------------------------------")

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
      Este programa revisa si una frase es un palíndromo ignorando espacios y mayúsculas/minúsculas.
      Primero normaliza el texto eliminando los espacios y convirtiéndolo a minúsculas.
      Luego compara la cadena normalizada con su versión invertida para determinar si ambas coinciden.
      Finalmente, muestra si la frase es palíndroma o no.

   - Inputs:
      - phrase .- String ingresado por el usuario mediante input("Type the phrase you wanna check: ").

   - Outputs:
      - "Is palindrome: True" si la frase normalizada es igual a su reverso.
      - "Is palindrome: False" si no es palíndromo o si no cumple la longitud.
      - "Normalized phrase: <phrase>" solo si es palíndromo.

   - Validations:
      - if len(phrase) > 3: .- Si no se cumple al momento de normalizar automaticamente se contempla como palíndromo.

  
   - Test Cases: 
      # CASO NORMAL

      Type the phrase you wanna check: anita lava la tina
      Is palindrome: True
      Normalized phrase:  anitalavalatina

      
      # CASO BORDE

      Type the phrase you wanna check: aa
      Is palindrome: False


      # CASO ERROR

      Type the phrase you wanna check: Hola mundo
      Is palindrome: False


"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

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

# Problem 4: Sentence word stats (lengths and first/last word)
"""
   - Descripción: 
      Este programa recibe una oración, elimina espacios sobrantes y la divide en palabras. Luego calcula distintas 
      estadísticas: cuántas palabras tiene, cuál es la primera y la última, y cuáles son la más corta y la más larga según su longitud. 
      Finalmente, muestra estos resultados de forma clara.

   - Inputs:
      - sentence.- String ingresado por el usuario.

   - Outputs:
      - "Word count: <n>"
      - "First word: <...>"
      - "Last word: <...>"
      - "Shortest word: <...>"
      - "Largest word: <...>"
      - "Error: you didn´t type a sentence"
      - "Error: invalid word"

   - Validations:
      - if sentence == "":
   print("Error: you didn´t type a sentence") .- Sucede cuando no se ingresa ninguna oración.
      - if len(separate_words) == 0:
      print("Error: invalid word") .- Debe haber al menos una palabra válida en la oración.

  
   - Test Cases: 
      # CASO NORMAL

      Type a sentence: The sun is bright
      Word count:  4
      First word:  The
      Last word:  bright
      Shortest word:  is
      Largest word:  bright

      
      # CASO BORDE

      Type a sentence: Hello
      Word count:  1
      First word:  Hello
      Last word:  Hello
      Shortest word:  Hello
      Largest word:  Hello


      # CASO ERROR

      Type a sentence: ""
      Error: you didn´t type a sentence

"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

sentence= input("Type a sentence: ")
sentence= sentence.strip()
if sentence == "":
   print("Error: you didn´t type a sentence")
else:
   separate_words= sentence.split()
   if len(separate_words) == 0:
      print("Error: invalid word")
   else:
      word_count= len(separate_words)
      first_word= separate_words[0]
      last_word= separate_words[-1]
      shortest_word= separate_words[0]
      largest_word= separate_words[0]

      for word in separate_words:
         if len(word) < len(shortest_word):
            shortest_word= word
         if len(word) > len(largest_word):
            largest_word= word
      
      print("Word count: ", word_count)
      print("First word: ", first_word)
      print("Last word: ", last_word)
      print("Shortest word: ", shortest_word)
      print("Largest word: ", largest_word)

# Problem 5: Password strength classifier
"""
   - Descripción: 
      Este programa evalúa una contraseña y determina si es weak, medium o strong según sus características. 
      Verifica la longitud del texto y analiza si contiene mezclas de mayúsculas, minúsculas, dígitos o símbolos especiales. 
      Dependiendo de estos criterios, clasifica la seguridad de la contraseña en uno de los tres niveles para informar al usuario 
      qué tan segura es.

   - Inputs:
      password: lo que el usuario escribe en el input("Type your password: ")

   - Outputs:
      "Error: didn´t type a password"
      "Password strenght: WEAK"
      "Password strenght: STRONG"
      "Password strenght: MEDIUM"

   - Validations:
      - if password == "": .- Revisa si el usuario no escribio nada.

   - Test Cases: 
      # CASO NORMAL

      Type your password: Hola123!
      Password strenght: STRONG

      
      # CASO BORDE

      Type your password: Hola1234
      Password strenght: MEDIUM


      # CASO ERROR

      Type your password: ""
      Error: didn´t type a password

"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

password= input("Type your password: ")
if password == "":
   print("Error: didn´t type a password")
else:
   has_upper= False
   has_lower= False
   has_symbol= False
   has_digit= False

   for character in password:
      if character.isupper():
         has_upper= True
      elif character.islower():
         has_lower= True
      elif character.isdigit():
         has_digit= True
      elif not character.isalnum():
         has_symbol= True

   if len(password) < 8:
      print("Password strenght: WEAK")
   elif has_upper and has_lower and has_digit and has_symbol:
      print("Password strenght: STRONG")
   else:
      print("Password strenght: MEDIUM")

# Problem 6: Product label formatter (fixed-width text)
"""
   - Descripción: 
      Este programa recibe el nombre de un producto y su precio, y genera una etiqueta formateada 
      con el texto: Product: <NAME> | Price: $<PRICE>. La etiqueta final debe medir exactamente 30 caracteres, por lo que 
      el programa debe recortar si excede ese tamaño o rellenar con espacios si es más corta. También valida que el nombre no 
      esté vacío y que el precio sea un número positivo antes de generar la etiqueta.

   - Inputs:
      - product_name = ingresado por el usuario con input("Type the product name: ")
      - price_value = ingresado por el usuario con input("Type the product price: $")

   - Outputs:
      - print("Error: invalid product name") .- Mensaje de error si el nombre es inválido.
      - print("Error: invalid price value") .- Mensaje de error si el precio no es válido (no numérico o no positivo).
      - print("Label:", "" + label + "") .- Etiqueta formateada exactamente de 30 caracteres:

   - Validations:
      - product_name == "" .- Error si está vacío tras strip().
      - price_value .- Convertible a float usando try/except.
  
   - Test Cases: 
      # CASO NORMAL

      Type the product name: Apples
      Type the product price: $12.5
      Label: Product: Apples Price: 12.5

      
      # CASO BORDE

      Type the product name: ExtraLargeWatermelonFruit
      Type the product price: $10
      Label: Product ExtraLargeWatermel


      # CASO ERROR

      Type the product name: "  "
      Type the product price: $abc
      Error: invalid product name
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

product_name= input("Type the product name: ")  
product_name= product_name.strip()
price_value= input("Type the product price: $")
if product_name == "":
   print("Error: invalid product name")
else:
   try:
      price_num= float(price_value)
      if price_num <= 0:
         print("Error: invalid price value")
      else:
         label= "Product " + product_name + " Price: " + str(price_num)
         if len(label) > 30:
            label= label[:30]
         while len(label) < 30:
            label = label + " "
         print("Label:", "" + label + "")
   except:
      print("Error: invalid price value")

print("------------------------------------------------------------------------------------------------------")

# CONCLUSIONES
"""
   El manejo de strings es fundamental porque casi todos los programas reciben y muestran información en formato de texto, así que 
   aprender a limpiarlo y transformarlo es clave para que los datos tengan sentido. Funciones como lower(), strip(), split() o join() 
   son muy útiles dependiendo de la situación: por ejemplo, lower() cuando necesitas comparar sin importar mayúsculas, strip() para 
   quitar espacios basura, y split() para separar palabras de una oración. Normalizar el texto antes de compararlo evita errores comunes, como 
   detectar diferencias que realmente no importan. También entendí que diseñar buenas validaciones ayuda a prevenir datos incorrectos que 
   afectarían los resultados del programa. Por último, aprendí que los strings en Python son inmutables, lo cual significa que cada cambio 
   crea uno nuevo, y que los slices son una forma muy práctica de acceder solo a las partes del texto que necesitas.
"""

# REFERENCIAS
"""
   1) Fundamentos de strings en Python: https://www.programaenpython.com/fundamentos/strings-en-python/ 
   2) Manejo de entradas: https://www.datacamp.com/es/tutorial/python-user-input
   3) Booleanos en Python: https://ellibrodepython.com/booleano-python 
   4) isupper(), islower(), lower(), upper() en Python y sus aplicaciones: https://www.geeksforgeeks.org/python/isupper-islower-lower-upper-python-applications/
   5) Qué son y cómo usar Slices en Python: https://www.luisllamas.es/python-slices/
"""