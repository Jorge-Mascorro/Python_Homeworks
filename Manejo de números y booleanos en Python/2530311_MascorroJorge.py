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
