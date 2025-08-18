class Ingreso:
    def __init__(self, codigo, categoria, talla, precio, stock):
        self.codigo = codigo
        self.categoria = categoria
        self.talla = talla
        self.precio = precio
        self.stock = stock

    def Mostrar(self):
        print(f"El codigo ingresado es: {self.codigo}, el nombre del producto: {self.talla}, con precio de {self.precio}, el stock disponible es de:  {self.stock} ")

class Registrar_Producto:
    def __init__(self):
        self.producto = {}

    def agregar_producto(self, categoria):
            try:
                cantidad = int(input("Ingrese la cantidad de producto que va almacenar: "))
                for i in range(cantidad):
                    print("\n--------------------------------------")
                    print(f"Ingrese los datos del producto {i + 1}")
                    while True:
                        codigo = input("Ingrse el codigo del producto: ")
                        if codigo in self.producto:
                            print("El codigo del producto ya existe.")
                            error = input("Presione ENTER para ingresar nuevamente o 0 para salir:")
                            if error == "0":
                                break

                            else:
                                continue
                        break
                    while True:
                        talla_producto = input("Ingrese el la talla: ").upper()
                        if talla_producto in ["S", "M", "L", "XL"]:
                            break
                        else: 
                            print("Solo se permite tallas S, M, L, XL ")
                    while True:
                        try:
                            precio_producto = float(input("Ingrese el precio del producto: Q"))
                            break
                        except ValueError:
                            print("El precio deve ser númerico... ")
                    while True:
                        try:
                            stock_inicial = int(input("Ingrese le Stock inicial del producto: "))
                            break
                        except ValueError:
                            print("El Stock deve ser un número entero...")
                    self.producto[codigo] = Ingreso(codigo, categoria, talla_producto, precio_producto, stock_inicial)
                    print("Producto registrado correctamente.")
                    intento = input("Presione ENTER para continuar o ingrese 0 para registrar otra categoria ")
                    if intento == "0":
                        break
                    else:
                        continue
            except ValueError:
                print("No se puedo agregar un producto")

registro_Codigo = Registrar_Producto()

class Mostrar_Productos:
    def __init__(self, registro):
        self.registro = registro

    def Mostrar(self):
        if not  self.registro.producto:
            print("No hay productos registrados")
            return
        print("Productos Registrados")
        for i, producto in enumerate(self.registro.producto.values(), start=1):
            print(f"{i}- ", end="")
            producto.Mostrar()


class Ordenar_Productos:
    def __init__(self, productos):
        self.productos = productos

    def quick_sort(self, lista):
        if len(lista) <=1:
            return lista
        else:
            pivote = lista[0].stock
            mayores = [x for x in lista[1:] if x.stock > pivote]
            iguales = [x for x in lista[1:] if x.stock == pivote]
            menores = [x for x in lista[1:] if x.stock < pivote]
            return self.quick_sort(mayores) + [lista[0]] + iguales + self.quick_sort(menores)

    def MostrarPor_Stock(self):
        if not self.productos:
            print(f"No hay productos en esta categoria")
            return
        ordenados = self.quick_sort(self.productos)
        print("Productos ordenados por cantidad disponible: ")
        for i, producto in enumerate(ordenados, start=1):
            print(f"{i}- ", end="")
            producto.Mostrar()

opcion = 0
while opcion != 5:
    print("Bienvenidos a la tienda de Ropa ")
    print("1.- Registrar Producto")
    print("2.- Mostrar Productos")
    print("3.- Buscar Producto")
    print("4.- Gestion de Productos")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una de las opciones que desee: "))

        match opcion:
            case 1:
                    print("--------------------------------------------------------")
                    print("Registrar Producto")
                    print("A continuacion se le presenta las Categorias disponibles")
                    print("1.- Playeras")
                    print("2.- Pantalones")
                    print("3.- Sueteres")
                    print("4.- Zapatos")
                    try:
                        categoria_op = int(input("Seleccione una de las opciones o presione 0 para regresar al menú principal: "))
                        categoria = {1: "Playera", 2: "Pantalon", 3: "Sueter", 4: "Zapato" }
                        match categoria_op:
                            case 1:
                                while True:
                                    print("\n----------------------------")
                                    print("Categoria Playeras")
                                    registro_Codigo.agregar_producto(categoria[1])
                                    break
                            case 2:
                                while True:
                                    print("\n----------------------------")
                                    print("Categoria Pantalones")
                                    registro_Codigo.agregar_producto(categoria[2])
                                    break
                            case 3:
                                while True:
                                    print("\n----------------------------")
                                    print("Categoria Sueteres")
                                    registro_Codigo.agregar_producto(categoria[3])
                                    break
                            case 4:
                                while True:
                                    print("\n----------------------------")
                                    print("Categoria Zapatos")
                                    registro_Codigo.agregar_producto(categoria[4])
                                    break
                    except ValueError:
                        intente = input(f"\n Opcion no valida presione ENTER para intentar de nuevo categorias")
                        if intente == "":
                            continue
            case 2:
                opciones_case2 = 0
                print("Mostrar Productos por Categoria")
                print("1.- Playeras")
                print("2.- Pantalones")
                print("3.- Sueteres")
                print("4.- Zapatos")
                try:
                    opciones_case2 = int(input("Ingrese su opción: "))
                except ValueError:
                    print("Ingerse una opción valida... ")
                    break
                categorias = {1: "Playera", 2: "Pantalon", 3: "Sueter", 4: "Zapato"}
                if opciones_case2 in categorias:
                    categoria = categorias[opciones_case2]
                    productos_categoria = [p for p in registro_Codigo.producto.values()  if p.categoria == categoria]
                    if not productos_categoria:
                        print(f"No hay productos en registrados en la categoria {categoria}")
                    else:
                        ordenador = Ordenar_Productos(productos_categoria)
                        ordenador.MostrarPor_Stock()
                else:
                    print("Opcion de categoria no válida...")

            case 3:
                print("Buscar Producto")
            case 4:
                print("Gestion de Productos ")
            case 5:
                print("Salir")


    except ValueError:
        validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 5 para Salir del programa \n")
        if validar == "5":
            break
        else:
            continue
