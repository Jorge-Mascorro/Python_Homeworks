"""
                        CRUD IN PYTHON

                    - Nombre: Jorge Mascorro
                    - Matrícula: 2530311
                    - Grupo: IM 1-1
"""

                                          # RESUMEN EJECUTIVO
"""
    - ¿Qué es un CRUD y qué significan Create, Read, Update, Delete?
       CRUD es el acrónimo de CREAR , LEER , ACTUALIZAR y ELIMINAR . Estos términos describen las cuatro operaciones esenciales para 
       crear y gestionar elementos de datos persistentes, principalmente en bases de datos relacionales y NoSQL. CRUD se utiliza ampliamente 
       en aplicaciones de bases de datos.

       - CREATE.- Se utiliza para añadir nuevos registros o elementos a una base de datos.
       - READ.- Se emplea para recuperar y mostrar datos de una base de datos.
       - UPDATE.- Se usa para modificar datos existenteS.
       - DELETE.- Se emplea para borrar registros de una base de datoS.

    - ¿Qué estructura de datos elegiste (dict o list de dicts) y por qué?
        Elegí utilizar un diccionario (dict) donde cada clave es el ID del producto porque ofrece un acceso mucho más rápido y directo 
        a los elementos, lo cual facilita todas las operaciones CRUD. Al usar un dict, no es necesario recorrer toda una lista para 
        encontrar un producto, sino que se puede acceder inmediatamente mediante su ID, haciendo el programa más eficiente y sencillo de 
        implementar.

    - ¿Cómo te ayuda usar funciones para organizar la lógica del CRUD?
        Usar funciones para organizar la lógica del CRUD ayuda porque permite separar claramente cada operación, evitando que todo el 
        programa quede mezclado dentro del menú principal. Al tener funciones independientes como create_item, read_item o update_item, 
        el código se vuelve más fácil de entender, mantener y modificar, ya que cada función realiza una tarea específica y bien definida. 
        Además, esto permite reutilizar código sin repetir instrucciones y facilita detectar errores, pues si algo falla en una operación, 
        solo es necesario revisar la función correspondiente.

    - ¿Qué cubre tu programa?: menú principal, operación de creación, lectura, actualización, eliminación y listado de elementos.
        Mi programa cubre todos los elementos esenciales de un CRUD completo, comenzando por un menú principal interactivo que permite al 
        usuario elegir la operación que desea realizar. Incluye una función de creación que agrega nuevos elementos al inventario validando 
        los datos ingresados; una función de lectura que busca y muestra un producto por su ID; una función de actualización que modifica 
        los datos de un elemento existente; y una función de eliminación que borra un item si se encuentra en la estructura de datos. 
        Además, incorpora una función de listado que muestra todos los elementos almacenados de manera clara.
"""

# Problem: CRUD with functions
"""
   - Descripción: 
      Este programa implementa un sistema CRUD para gestionar productos dentro de un inventario usando un diccionario. El usuario puede 
      crear, leer, actualizar, eliminar y listar elementos mediante un menú interactivo. El programa recibe datos como ID, nombre, precio 
      y cantidad, y valida que sean correctos antes de operar.

   - Inputs:
      - item_id = input("ID: ").strip() .— Pide el identificador del producto.
      - name = input("Nombre: ").strip() .— Pide el nombre del producto.
      - price = float(input("Precio: ")) .— Solicita el precio del artículo.
      - quantity = int(input("Cantidad: ")) .— Solicita la cantidad disponible.

   - Outputs:
      - print("Item created") .— Confirma que un producto fue creado.
      - print(item) .— Muestra la información de un producto al leerlo.
      - print("Item updated") .— Indica que un artículo fue actualizado.
      - print("Item deleted") .— Indica que un producto fue eliminado.
      - list_items(inventario) .— Muestra todos los artículos del inventario.

   - Validations:
      - if item_id in inventario .— Verifica que el ID no esté duplicado al crear.
      - if item_id not in inventario .— Comprueba que el producto exista para leer, actualizar o borrar.
      - except ValueError: .— Valida que precio y cantidad sean numéricos.
      - if price < 0 or quantity < 0: .— Asegura que no se ingresen valores negativos.
      - if not inventario: .— Verifica si el inventario está vacío al listar.

   - Test Cases: 
      # CASO NORMAL

      --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 1
        ID: p1
        Nombre: Lapiz
        Precio: 5.5
        Cantidad: 10
        Item created

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 2
        ID: p1
        {'name': 'Lapiz', 'price': 5.5, 'quantity': 10}

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 3
        ID: p1
        Nuevo nombre: Lapiz HB
        Nuevo precio: 6
        Nueva cantidad: 12
        Item updated

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 4
        ID: p1
        Item deleted

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 0
        Saliendo...

      # CASO BORDE

      --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 1
        ID: p2
        Nombre: Goma
        Precio: 3
        Cantidad: 0
        Item created

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 2
        ID: p2
        {'name': 'Goma', 'price': 3.0, 'quantity': 0}

        --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 0
        Saliendo...

      # CASO ERROR

      --- CRUD DE PRODUCTOS ---
        1) Create item
        2) Read item by ID
        3) Update item
        4) Delete item
        5) List all items
        0) Exit
        Selecciona una opción: 9
        Error: invalid option
"""
print("\n")
print("------------------------------------------------------------------------------------------------------")

"""
# CRUD de productos usando un diccionario
# Elegí diccionario porque permite acceder rápido por ID.

"""

def create_item(inventario, item_id, name, price, quantity):
    if item_id in inventario:
        return False  # ID duplicado
    inventario[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(inventario, item_id):
    return inventario.get(item_id)


def update_item(inventario, item_id, name, price, quantity):
    if item_id not in inventario:
        return False
    inventario[item_id]["name"] = name
    inventario[item_id]["price"] = price
    inventario[item_id]["quantity"] = quantity
    return True


def delete_item(inventario, item_id):
    if item_id not in inventario:
        return False
    del inventario[item_id]
    return True


def list_items(inventario):
    if not inventario:
        print("Inventario vacío.")
    else:
        for item_id, datos in inventario.items():
            print(f"ID: {item_id} - {datos}")


# ---------------- MENÚ PRINCIPAL --------------------

def main():
    inventario = {}  # Diccionario principal

    while True:
        print("\n--- CRUD DE PRODUCTOS ---")
        print("1) Create item")
        print("2) Read item by ID")
        print("3) Update item")
        print("4) Delete item")
        print("5) List all items")
        print("0) Exit")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            item_id = input("ID: ").strip()
            name = input("Nombre: ").strip()

            try:
                price = float(input("Precio: "))
                quantity = int(input("Cantidad: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if create_item(inventario, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: ID already exists")

        elif opcion == "2":
            item_id = input("ID: ").strip()
            item = read_item(inventario, item_id)
            if item:
                print(item)
            else:
                print("Item not found")

        elif opcion == "3":
            item_id = input("ID: ").strip()

            if item_id not in inventario:
                print("Item not found")
                continue

            name = input("Nuevo nombre: ").strip()

            try:
                price = float(input("Nuevo precio: "))
                quantity = int(input("Nueva cantidad: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if update_item(inventario, item_id, name, price, quantity):
                print("Item updated")
            else:
                print("Item not found")

        elif opcion == "4":
            item_id = input("ID: ").strip()
            if delete_item(inventario, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        elif opcion == "5":
            print("\nItems list:")
            list_items(inventario)

        else:
            print("Error: invalid option")
            break

if __name__ == "__main__":
    main()

print("------------------------------------------------------------------------------------------------------")

# CONCLUSIONES
"""
   El uso de funciones hizo que el CRUD fuera mucho más fácil de construir y entender, porque cada parte del programa quedó bien 
   organizada y con una tarea clara. Trabajar con un diccionario también ayudó bastante, ya que permitió encontrar y actualizar los 
   productos de forma rápida sin recorrer todo el inventario. Al validar entradas me encontré con errores comunes, como precios escritos 
   con letras o IDs vacíos, pero pude solucionarlos revisando cada dato antes de procesarlo y usando try/except para evitar que el 
   programa se detuviera.
"""

# REFERENCIAS
"""
   1) ¿Qué son las operaciones CRUD? - https://realpython.com/crud-operations/
   2) What is CRUD? - https://www.crowdstrike.com/en-us/cybersecurity-101/observability/crud/ 
   3) Usos del CRUD - https://www.youtube.com/watch?v=ItoGxXGaAS8 
"""