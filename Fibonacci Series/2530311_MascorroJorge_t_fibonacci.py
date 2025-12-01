"""
                    FIBONACCI SERIES WITH PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué es la serie de Fibonacci?
       

    - ¿Qué significa “calcular la serie hasta un número de términos n”?


    - ¿Qué cubrira tú programa? 
  
"""

# Problem: Fibonacci series up to n terms
"""
   - Descripción: 
      Este problema consiste en pedir al usuario un número n y generar la serie de Fibonacci con esa cantidad de términos, 
      comenzando siempre en 0 y 1. El programa debe validar que n sea un entero válido y mayor o igual que 1 antes de calcular 
      la serie. Una vez validado, debe usar un bucle para producir los valores y mostrarlos en una sola línea. Si la validación falla, 
      se debe mostrar un mensaje de error y no generar la serie.

   - Inputs:
      - n= int(input("Enter the value of 'n': ")) .- Pide al usuario hasta que número quiere generar la serie.

   - Outputs:
      - print(f"Number terms:{n}") .- Muestra la cantidad de términos.
      - print("Fibonacci Sequence: ") .- Imprime la serie de fibonacci.

   - Validations:
      - Valida que 'n' se pueda convertir a entero, esto se encuentra dentro de un try-excpet.
      - if n>1 and n<50: .- Valida que el término se encuentre entre 1 y 50 y si no se cumple imprime un mensaje de error.

   - Test Cases: 
      # CASO NORMAL

      Enter the value of 'n': 7
      Number terms:7
      Fibonacci Sequence:
      0 1 1 2 3 5 8

      # CASO BORDE

      Enter the value of 'n': 1
      Number terms:1
      Fibonacci Sequence:
      0

      # CASO ERROR

      Enter the value of 'n': -2
      Error: invalid input
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

try:
    n= int(input("Enter the value of 'n': "))
    if n>=1 and n<=50:
        a=0
        b=1
        suma=0
        count=1
        print(f"Number terms:{n}")
        print("Fibonacci Sequence: ")
        while(count<=n):
            print(suma, end = "")
            count +=1
            a=b
            b=suma
            suma= a+b
    else:
        print("Error: invalid input")
except:
    print("Put a valid number")
