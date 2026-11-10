# ==============================================================
# PARCIAL 3 - LÓGICA DE PROGRAMACIÓN
# Sistema de pedidos de una cafetería universitaria
#
# Integrantes del grupo:
#   - Diego Torres
#   - Juan Bernal
#
# Distribución del trabajo:
#   Punto 1 -> Diego Torres  (diccionario y tuplas)
#   Punto 2 -> Juan Bernal   (mostrar_productos)
#   Punto 3 -> Diego Torres  (lista pedido)
#   Punto 4 -> Juan Bernal   (registrar_producto)
#   Punto 5 -> Diego Torres  (menú y ciclo del pedido)
#   Punto 6 -> Juan Bernal   (calcular_total y descuento)
# ==============================================================


# --------------------------------------------------------------
# PUNTO 1 - Diccionario y tuplas: catálogo de productos
# Diego Torres
# --------------------------------------------------------------
productos = {
    1: ("Cafe", 3000, 20),
    2: ("Jugo natural", 5000, 15),
    3: ("Sandwich", 8000, 10),
    4: ("Empanada", 2500, 25),
    5: ("Hamburguesa", 12000, 8)
}


# --------------------------------------------------------------
# PUNTO 2 - Función para mostrar el catálogo
# Juan Bernal
# --------------------------------------------------------------
def mostrar_productos(productos):
    print("\n========== CATALOGO ==========")
    print("Codigo  Producto         Precio   Existencias")
    print("---------------------------------------------")
    for codigo, datos in productos.items():
        nombre, precio, existencias = datos 
        print(f"{codigo:<7} {nombre:<16} ${precio:<8} {existencias}")
    print("---------------------------------------------")


# --------------------------------------------------------------
# PUNTO 3 - Lista para almacenar el pedido
# Diego Torres
# --------------------------------------------------------------
pedido = []


# --------------------------------------------------------------
# PUNTO 4 - Función para registrar productos
# Juan Bernal
# --------------------------------------------------------------
def registrar_producto(productos, pedido, codigo, cantidad):
    # 1. Verificar que el código exista en el diccionario
    if codigo not in productos:
        print("Producto no encontrado.")
        return

    # 2. Verificar que la cantidad sea mayor que cero
    if cantidad <= 0:
        print("Cantidad no valida.")
        return

    nombre, precio, existencias = productos[codigo]

    # 3. Comprobar que existan suficientes unidades
    if cantidad > existencias:
        print("No hay suficientes unidades disponibles.")
        return

    # 4. Calcular el subtotal
    subtotal = precio * cantidad

    # 5. Agregar la tupla a la lista pedido
    pedido.append((codigo, nombre, cantidad, subtotal))

    # 6. Actualizar las existencias en el diccionario
    productos[codigo] = (nombre, precio, existencias - cantidad)

    print(f"Agregado: {cantidad} x {nombre} = ${subtotal}")

# --------------------------------------------------------------
# PUNTO 5 - Ciclo para registrar el pedido (menú)
# Diego Torres
# --------------------------------------------------------------
def menu(productos, pedido):
    opcion = ""
    while opcion != "3":
        print("\n========== CAFETERIA ==========")
        print("1. Mostrar productos")
        print("2. Agregar producto al pedido")
        print("3. Finalizar pedido")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            codigo_txt = input("Codigo del producto: ").strip()
            cantidad_txt = input("Cantidad: ").strip()

            if not codigo_txt.isdigit():
                print("Producto no encontrado.")
            elif not cantidad_txt.isdigit():
                print("Cantidad no valida.")
            else:
                registrar_producto(productos, pedido, int(codigo_txt), int(cantidad_txt))

        elif opcion == "3":
            mostrar_resumen(pedido)

        else:
            print("Opcion no valida.")

# --------------------------------------------------------------
# PUNTO 6 (definición) - Función para calcular el total
# Juan Bernal
# --------------------------------------------------------------
def calcular_total(pedido):
    total = 0
    for item in pedido:
        total += item[3]
    return total

# --------------------------------------------------------------
# PUNTO 6 (descuento y resumen)
# Juan Bernal
# --------------------------------------------------------------
def mostrar_resumen(pedido):
    total = calcular_total(pedido)

    # Descuento del 10 % si el total es igual o superior a 50000
    if total >= 50000:
        descuento = total * 0.10
    else:
        descuento = 0

    total_final = total - descuento

    print("\n========== RESUMEN DEL PEDIDO ==========")
    print(f"{'Producto':<18}{'Cantidad':<10}{'Subtotal'}")
    print("-" * 41)
    for codigo, nombre, cantidad, subtotal in pedido:
        print(f"{nombre:<18}{cantidad:<10}{subtotal}")
    print("-" * 41)
    print(f"Total : ${int(total)}")
    print(f"Descuento : ${int(descuento)}")
    print(f"TOTAL A PAGAR : ${int(total_final)}")
    print("=" * 40)


# --------------------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------------------
menu(productos, pedido)
