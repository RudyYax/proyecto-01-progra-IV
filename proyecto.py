class Ingreso:
    def __init__(self, codigo,nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"El codigo ingresado es: {self.codigo}, el nombre del producto: {self.nombre}, con precio de {self.precio}, el stock de {self.stock} ")

class Registrar_Producto:
    def __init__(self):
        self.producto = {}

    def agregar_producto(self):
        while True:
            try:
                codigo = input("Ingresa el codigo del producto (ENTER para volver al menú de categorías, 0 para regresar al menú principal): ")
                if codigo == "":
                    break
                if codigo == "0":
                    return
                codigo = int(codigo)
                if codigo in self.producto:
                    print("El codigo del producto ya existe.")
                    error = input("Presione ENTER para ingresar nuevamente o 0 para salir:")
                    if error == "0":
                        break
                    else:
                        continue
                nombre_producto = input("Ingresa el nombre del producto: ")
                precio_producto = input("Ingresa el precio del producto: ")
                stock_producto = input("Ingresa el stock del producto: ")
                self.producto[codigo] = Ingreso(codigo, nombre_producto, precio_producto, stock_producto)
                print("Producto registrado correctamente.")
            except ValueError:
                print("No se puedo agregar un producto")
                continue


    def Mostrar_Productos(self):
        if not self.producto:
            print("No hay productos registrados.")
            return
        print("Productos registrados: ")
        for i, libros in enumerate(self.producto.values(), start= 0):
            print(f"{i}., end=")



registro_Codigo = Registrar_Producto()

opcion = 0
while opcion != 5:
    print("Bienvenidos a la tienda de Ropa ")
    print("1.- Registrar Producto")
    print("2.- Mostrar Productos")
    print("3.- Buscar Producto")
    print("4.- Gestion de Productos")
    print("5.- Salir")
    opcion = int(input("seleccione una de las opciones que desee: "))

    match opcion:
        case 1:
            print("Registrar Producto")
            print("A continuacion se le presenta las Categorias disponibles")
            print("1.- Playeras")
            print("2.- Pantalones")
            print("3.- Sueteres")
            print("4.- Zapatos")
            categoria = int(input("seleccione una de las opciones: "))
            match categoria:
                case 1:
                    while True:
                        print("Categoria Playeras")
                        registro_Codigo.agregar_producto()

                case 2:
                    print("Categoria Pantalones")
                    registro_Codigo.agregar_producto()
                case 3:
                    print("Categoria Sueteres")
                    registro_Codigo.agregar_producto()
                case 4:
                    print("Categoria Zapatos")
                    registro_Codigo.agregar_producto()



        case 2:
            print("Mostrar Productos")
            registro_Codigo.Mostrar_Productos()

        case 3:
            print("Buscar Producto")
        case 4:
            print("Gestion de Productos ")
        case 5:
            print("Salir")