"""
                    MANEJO DE NÚMEROS Y BOOLEANOS EN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué son los tipos int y python en float en python y en que se diferencian?
       En Python, int representa números enteros sin decimales, mientras que float representa números con decimales y usa punto flotante, lo 
       que puede generar pequeñas imprecisiones. Los enteros son exactos y se usan para conteos o valores discretos, mientras que los flotantes 
       sirven para cálculos con medidas o promedios.
    
    - ¿Qué es un booleano (True/False) y cómo se obtiene a partir de comparaciones?
       Un booleano en Python es un tipo de dato que solo puede tomar dos valores: True (verdadero) o False (falso). Se obtiene principalmente 
       mediante operadores de comparación, como ==, !=, >, <, >= o <=, los cuales evalúan una expresión y devuelven uno de esos dos valores. 
       Por ejemplo, 5 > 3 devuelve True y "hola" == "adiós" devuelve False.

    - ¿Por qué es importante validar rangos y evitar división entre cero?
       Es importante validar rangos porque a veces los usuarios pueden escribir valores que no tienen sentido, y si no los revisamos, el 
       programa podría dar resultados absurdos o fallar sin explicación. Revisar que los datos estén dentro de lo esperado ayuda a que todo 
       funcione de forma más segura y clara. Lo mismo pasa con la división entre cero: si no la evitamos, el programa se detiene de golpe 
       porque esa operación no existe en matemáticas. Por eso siempre conviene comprobar primero que el divisor no sea cero antes de hacer 
       la cuenta.
    
    - ¿Qué cubrira este documento? 
       En este documento se llevaran a cabo 6 problemas relacionados a los números y booleanos en Python, en los cuales
       incluire el código, sus entradas y validaciones, asi también incluyendo a cada problema 3 casos de prueba (normal, borde y error).   
"""

                                   # PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    - Usar tipos apropiados: int para contadores, float para cantidades con decimales.
    - Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
    - Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
    - Usar nombres de variables descriptivos y mensajes claros para el usuario.
    - Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).
"""

# Problem 1: Temperature converter and range flag
"""
   - Descripción: 
    Este problema pide convertir una temperatura en Celsius a Fahrenheit y Kelvin, y además indicar si la temperatura es considerada alta. 
    Primero se valida que el dato ingresado sea un número válido y que no genere valores imposibles en Kelvin. Después se realizan las 
    conversiones y se determina si la temperatura es mayor o igual a 30°C. Al final, el programa muestra las dos conversiones y el valor 
    booleano correspondiente.

   - Inputs:
      - celsius= input("Set temperature in Celsius: ") .- el usuario ingresa el valor de los grados celsius que desea convertir.

   - Outputs:
      - print("Fahrenheit: ", temp_f) .- se muestra la conversión en grados fahrenheit.
      - print("Kelvin: ", temp_k) .- se muestra la conversión en grados kelvin.
      - print("High Temperature: ", is_high_temperature) .- se muestra si es verdadero o falso que es alta temperatura.

   - Validations:
      - temp_c= float(celsius) .- valida que los grados puestos se puedan convertir en flotantes dentro de un try-except.
      - if temp_k < 0:
        print("Error: temperature below absolute zero") .- se valida que no se puedan obtener temperaturas imposibles.
      
   - Test Cases: 
      # CASO NORMAL

      Set temperature in Celsius: 25
      Fahrenheit:  77.0
      Kelvin:  298.15
      High Temperature:  False

      # CASO BORDE

      Set temperature in Celsius: 30
      Fahrenheit:  86.0
      Kelvin:  303.15
      High Temperature:  True

      # CASO ERROR

      Set temperature in Celsius: -300
      Error: temperature below absolute zero
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")
celsius= input("Set temperature in Celsius: ")

try:
    temp_c= float(celsius)

    if temp_c >= 30:
        is_high_temperature= True
    else:
        is_high_temperature= False

    temp_f= temp_c * 9 / 5 + 32
    temp_k= temp_c + 273.15

    if temp_k < 0:
        print("Error: temperature below absolute zero")
        exit()
    print("Fahrenheit: ", temp_f)
    print("Kelvin: ", temp_k)
    print("High Temperature: ", is_high_temperature)

except:
    print("The value cannot be converted to a float")



# Problem 2: Work hours and overtime payment
"""
   - Descripción: 
      Este problema consiste en calcular el pago semanal de un trabajador considerando tanto horas regulares como horas extra. Las primeras 
      40 horas se pagan a la tarifa normal, mientras que las horas adicionales se compensan al 150% del salario por hora. Además, el programa 
      determina si el trabajador realizó tiempo extra mediante un valor booleano. También incluye validaciones básicas para asegurar que las 
      horas y la tarifa ingresadas sean valores válidos.

   - Inputs:
      - hours_worked= float(input("How many hours did you work on the weekend?: ")) .- pregunta cuantas horas trabajo a la semana
      - hourly_rate= float(input("How much are you paid per hour?: ")) .- pregunta cuanto pagan por hora

   - Outputs:
      - print("Regular pay:", regular_pay) .- muestra el pago regular sin horas extra aplicadas. 
      - print("Overtime pay:", overtime_pay) .- muestra el pago con horas extra aplicadas.
      - print("Total pay:", total_pay) .- muestra el pago en total.
      - print("Has overtime:", has_overtime) .- indica si trabajo mas tiempo o no.

   - Validations:
      - if hours_worked < 0 or hourly_rate < 0:
            print("Error: invalid input") .- se muestra solo si alguno de los dos no cumple la validación estipulada.

   - Test Cases: 
      # CASO NORMAL

      How many hours did you work on the weekend?: 48
      How much are you paid per hour?: 100
      Regular pay: 4000.0
      Overtime pay: 1200.0
      Total pay: 5200.0
      Has overtime: True

      # CASO BORDE

      How many hours did you work on the weekend?: 40
      How much are you paid per hour?: 80
      Regular pay: 3200
      Overtime pay: 0
      Total pay: 3200
      Has overtime: False

      # CASO ERROR

      How many hours did you work on the weekend?: -5
      How much are you paid per hour?: 120
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

hours_worked= float(input("How many hours did you work on the weekend?: "))
hourly_rate= float(input("How much are you paid per hour?: "))

if hours_worked < 0 or hourly_rate < 0:
    print("Error: invalid input")

else:
   if hours_worked > 40:
      has_overtime= True
   else:
      has_overtime= False
   
   regular_hours = min(hours_worked, 40)
   overtime_hours = max(hours_worked - 40, 0)

   regular_pay= regular_hours * hourly_rate
   overtime_pay= overtime_hours * hourly_rate * 1.5
   total_pay= regular_pay + overtime_pay

   print("Regular pay:", regular_pay)
   print("Overtime pay:", overtime_pay)
   print("Total pay:", total_pay)
   print("Has overtime:", has_overtime)

# Problem 3: Discount eligibility with booleans
"""
   - Descripción: 
      Este problema consiste en determinar si un cliente puede recibir un descuento del 10% 
      según ciertas condiciones, como ser estudiante, ser adulto mayor o realizar una compra 
      de al menos $1000. Para ello, el programa convierte las respuestas del usuario a valores 
      booleanos y valida que sean correctas. Con base en estas condiciones, calcula si el 
      descuento aplica y muestra el total final a pagar.

   - Inputs:
      - purchase_total = float(input("What is the purchase amount?: ")) .- Pide el monto de la compra
      - is_student_text = input("Are you a student? (YES/NO): ").strip().upper() .- Pregunta si eres estudiante
      - is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper() .- Pregunta si eres adulto 

   - Outputs:
      - print("Discount eligible:", discount_eligible) .- Muestra si eres elegible para descuento
      - print("Final total:", final_total) .- Muestra el total de la compra, ya sea con descuento o sin descuento.

   - Validations:
      - if purchase_total < 0.0:
            print("Error: invalid purchase amount") .- Si el total sin descuento es menor que 0 marca error.
            exit()
      - if (is_student_text != "YES" and is_student_text != "NO") or \
            (is_senior_text != "YES" and is_senior_text != "NO"): .- Si el texto no es "YES" ni "NO", mostrar Error: invalid input.
            print("Error: invalid input")
            exit()


   - Test Cases: 
      # CASO NORMAL

      What is the purchase amount?: 850
      Are you a student? (YES/NO): YES
      Are you a senior? (YES/NO): NO
      Discount eligible: True
      Final total: 765.0

      # CASO BORDE

      What is the purchase amount?: 1000
      Are you a student? (YES/NO): NO
      Are you a senior? (YES/NO): NO
      Discount eligible: True
      Final total: 900.0

      # CASO ERROR

      What is the purchase amount?: 500
      Are you a student? (YES/NO): MAYBE
      Are you a senior? (YES/NO): NO
      Error: invalid input
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

purchase_total = float(input("What is the purchase amount?: "))
is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

if purchase_total < 0.0:
    print("Error: invalid purchase amount")
    exit()

if (is_student_text != "YES" and is_student_text != "NO") or \
   (is_senior_text != "YES" and is_senior_text != "NO"):
    print("Error: invalid input")
    exit()

is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

if discount_eligible:
    final_total = purchase_total * 0.9   
else:
    final_total = purchase_total

print("Discount eligible:", discount_eligible)
print("Final total:", final_total)

# Problem 4: Basic statistics of three integers
"""
   - Descripción: 
      Este problema solicita leer tres números enteros y calcular con ellos la suma, el promedio, el máximo y el mínimo. 
      Además, determina si los tres valores son pares mediante un booleano. Solo requiere validar que las entradas puedan 
      convertirse a enteros, permitiendo también números negativos.

   - Inputs:
      - n1 = int(input("Enter number 1: ")) .- Pide al usuario el valor del número 1.
      - n2 = int(input("Enter number 2: ")) .- Pide al usuario el valor del número 2.
      - n3 = int(input("Enter number 3: ")) .- Pide al usuario el valor del número 3.

   - Outputs:
      - print("Sum: ", sum_value) .- Muestra el valor de la suma de los números
      - print("Average: ", average_value) .- Muestra el promedio de los números.
      - print("Minimum: ", minimum) .- Muestra el número menor.
      - print("Maximum: ", maximum) .- Muestra el número mayor.
      - print("All even: ", all_even) .- Muestra si todos los números son pares.

   - Validations:
      - Verificar que los 3 números puedan convertirse a enteros, pero yo desde las entradas los defini como enteros.

   - Test Cases: 
      # CASO NORMAL

      Enter number 1: 10
      Enter number 2: 5
      Enter number 3: 7
      Sum:  22
      Average:  7.333333333333333
      Minimum:  5
      Maximum:  10
      All even:  False

      # CASO BORDE

      Enter number 1: 2
      Enter number 2: 4
      Enter number 3: 6
      Sum:  12
      Average:  4.0
      Minimum:  2
      Maximum:  6
      All even:  True

      # CASO ERROR

      Enter number 1: abc
      Enter number 2: 5
      Enter number 3: 7
      Error: invalid input
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    n3 = int(input("Enter number 3: "))
    minimum= None
    maximum= None
    all_even= False

    sum_value= n1 + n2 + n3

    average_value= sum_value/3

    minimum= min(n1, n2, n3)
    maximum= max(n1, n2, n3)

    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
        all_even= True 

    print("Sum: ", sum_value)
    print("Average: ", average_value)
    print("Minimum: ", minimum)
    print("Maximum: ", maximum)
    print("All even: ", all_even)
except ValueError:
    print("Error: invalid input")
    exit()


# Problem 5: Loan eligibility (income and debt ratio)
"""
   - Descripción: 
      Este problema evalúa si una persona cumple los requisitos para obtener un préstamo utilizando su ingreso mensual, su nivel de 
      deuda y su puntaje de crédito. Primero se calcula el índice de deuda (debt_ratio) y, con base en este valor, se determina si la 
      persona es elegible siguiendo reglas específicas. Además, se validan las entradas para evitar valores inválidos y se muestra un 
      mensaje de error si no cumplen los criterios mínimos. Finalmente, el programa imprime el índice de deuda y un indicador booleano que 
      confirma o niega la elegibilidad.

   - Inputs:
      - monthly_income= float(input("Enter your monthly income: ")) .- El usuario ingresa su ingreso mensual.
      - monthly_debt= float(input("Enter your total monthly debt payments: ")) .- El usuario ingresa los pagos mensuales de deuda.
      - credit_score= int(input("Enter your credit score: ")) .- El usuario ingresa su puntaje de crédito.

   - Outputs:
      - print("Debt ratio: ", debt_radio) .- Se muestra el índice de deuda del usuario.
      - print("Eligible: ", has_elegible) .- Se muestra si es elegible o no para el préstamo dependiendo de la regla estipulada.

   - Validations:
      - if monthly_income < 0 or monthly_debt < 0 or credit_score < 0: .- Muestra el error si no se cumple la validación.

   - Test Cases: 
      # CASO NORMAL

      Enter your monthly income: 10000
      Enter your total monthly debt payments: 3000
      Enter your credit score: 700
      Debt ratio:  0.3
      Eligible:  True

      # CASO BORDE

      Enter your monthly income: 8000
      Enter your total monthly debt payments: 3200
      Enter your credit score: 650
      Debt ratio:  0.4
      Eligible:  True

      # CASO ERROR

      Enter your monthly income: 0
      Enter your total monthly debt payments: 1000
      Enter your credit score: 700
      Error: invalid input
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

monthly_income= float(input("Enter your monthly income: "))
monthly_debt= float(input("Enter your total monthly debt payments: "))
credit_score= int(input("Enter your credit score: "))

if monthly_income < 0 or monthly_debt < 0 or credit_score < 0:
    print("Error: Invalid input")

debt_radio= monthly_debt / monthly_income
has_elegible= False

if monthly_income >= 8000 and debt_radio <= 0.4 and credit_score >= 650:
    has_elegible= True

print("Debt ratio: ", debt_radio)
print("Eligible: ", has_elegible)


# Problem 6: Body Mass Index (BMI) and category flag
"""
   - Descripción: 
      Este problema calcula el Índice de Masa Corporal (BMI) de una persona usando su peso y estatura, y determina 
      si se encuentra en categoría de bajo peso, normal o sobrepeso. El programa valida que las entradas sean mayores que cero
      para evitar errores y luego clasifica el BMI según rangos establecidos. Finalmente, muestra el BMI redondeado y los indicadores 
      booleanos que corresponden a cada categoría.
      
   - Inputs:
      - weight_kg= float(input("Enter your weight in kilograms: ")) .- Pide al usuario su peso en kg.
      - height_m= float(input("Enter your height in meters: ")) .- Pide al usuario su estatura en metros (m).
      
   - Outputs:
      - print("BMI: ",round(bmi,2)) .- Muestra el BMI del usuario redondeado en 2 decimales.
      - print("Underweight: ",is_underweight) .- Determina si tiene escases de peso.
      - print("Normal: ",is_normal) .- Determina si está en peso normal.
      - print("Overweight: ",is_overweight) .- Determina si tiene sobrepeso.

   - Validations:
      - if weight_kg < 0 or height_m < 0: .- Si alguno de los dos es menor que 0 muestra error.
            print("Error: invalid input")

   - Test Cases: 
      # CASO NORMAL

      Enter your weight in kilograms: 70.0
      Enter your height in meters: 1.75
      BMI:  22.86
      Underweight:  False
      Normal:  True
      Overweight:  False

      # CASO BORDE

      Enter your weight in kilograms: 62.5
      Enter your height in meters: 1.58
      BMI:  22.86
      Underweight:  False
      Normal:  False
      Overweight:  True

      # CASO ERROR

      Enter your weight in kilograms: 70.0
      Enter your height in meters: 0.0
      Error: invalid input
"""

print("\n")
print("------------------------------------------------------------------------------------------------------")

weight_kg= float(input("Enter your weight in kilograms: "))
height_m= float(input("Enter your height in meters: "))

if weight_kg < 0 or height_m < 0:
    print("Error: invalid input")

is_underweight= False
is_normal= False
is_overweight= False

bmi= float(weight_kg / (height_m * height_m))

if bmi < 18.5:
    is_underweight= True
elif 18.5 <= bmi < 25:
    is_normal= True
elif bmi >= 25:
    is_overweight= True

print("BMI: ",round(bmi,2))
print("Underweight: ",is_underweight)
print("Normal: ",is_normal)
print("Overweight: ",is_overweight)

print("------------------------------------------------------------------------------------------------------")

# CONCLUSIONES
"""
En estos ejercicios me di cuenta de que los enteros y flotantes se combinan todo el tiempo para resolver problemas reales, porque 
casi nada en la vida se maneja con números “exactos”; siempre hay promedios, divisiones y medidas con decimales. También entendí que 
las comparaciones generan valores booleanos y que esos true o false son los que realmente deciden qué camino toma un programa 
dentro de un if. Otra cosa importante es validar rangos y evitar errores como dividir entre cero, porque sin esas validaciones el 
programa podría fallar aunque el código esté bien escrito. Además, aprendí a diseñar condiciones combinadas con operadores 
como and, or y not, y cómo estos permiten crear reglas más completas. Lo interesante es que estos patrones se repiten en muchos 
contextos, como nóminas, descuentos o préstamos, donde siempre hay que calcular, comparar y tomar decisiones basadas en datos.
"""

# REFERENCIAS
"""
   1) Documentación oficial de Python: https://docs.python.org/3/library/
   2) Conversión de tipos y manejo de errores: https://docs.python.org/3/library/functions.html
   3) Operadores lógicos y estructuras condicionales: https://docs.python.org/3/reference/expressions.html#boolean-operations
   4) Tipo booleano y expresiones lógicas (and, or, not): https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
   5) Instrucciones condicionales if / else: https://docs.python.org/3/tutorial/controlflow.html#if-statements
"""