import pandas as pd
from datetime import datetime

"""
    Clase Producto
"""
class Producto:
   
    def IDProducto():
        """
        Método que regresa el ID unico creado para cada producto.
        """
        productos = pd.read_csv("Producto.csv")
        id = productos.iloc[-1,0]
        unicoID = id[0] + str(int(id[1:])+1)
        return unicoID
   
    def existeProducto(id):
        """
        Método que verifica si existe ya un Producto 
        """
        productos = pd.read_csv("Producto.csv")
        for i in range(0, len(productos)):
            if(productos.iloc[i,0] == id):
                return True

        return False
    
    def renglonProducto(id):
        """
        Método que devuelve el numero de reglon donde se encuentra el Producto
        """
        productos = pd.read_csv("Producto.csv")
        for i in range(0, len(productos)):
            if(productos.iloc[i,0] == id):
                return i
        return -1
    
def buscarProducto():
    """
    Método que nos permite buscar un empleado por su ID 
    """
    productos = pd.read_csv("Producto.csv") 
    id = input("ID del empleado que quieres buscar ")
    if(Producto.existeProducto(id) == True):
        print("\nResultado: \n")
        print(productos.loc[[Producto.renglonProducto(id)]])
    else:
        print("\nNo se encontro un producto con ese ID.")

def eliminarProducto():
    
    """
    Método para eliminar un Producto
    """
    productos = pd.read_csv("Producto.csv") 
    id = input("ID del empleado a eliminar: ")
    if(Producto.existeProducto(id) == True):
        resultado = productos.drop(productos.index[Producto.renglonProducto(id)])
        print("\nProducto eliminado.")
        resultado.to_csv("Producto.csv", index=False)
    else:
        print("\nNo se encontro un producto con ese ID.")

def agregarProducto():
    """
    Método para agregar un Producto
    """
    productos = pd.read_csv("Producto.csv") 
    id = Producto.IDProducto()
    nombre = input("\n- Escribe el nombre del producto: ")
    marca = input("\n- Escribe el nombre de la marca del producto: ")
    presentacion = input("\n- Escribe la presentación del producto (bolsa, lata, botella, etc.): ")
    precio = (int(input("\n- Escribe el precio del producto: ")))
    cantidad = (int(input("\n- Escribe la cantidad del producto: ")))
    stock = (int(input("\n- Escribe la cantidad de stock del producto: ")))
    respuestaRefrigeracion = 1
    while respuestaRefrigeracion != 1 or respuestaRefrigeracion != 2:
        respuestaRefrigeracion = (int(input("\n- ¿El producto requiere refrigeración?\n\n\t [1] Si [2] No\n\nOpcion: ")))
        if respuestaRefrigeracion == 1:
            refrigeracion = "Si"
            break
        elif respuestaRefrigeracion == 2:
            refrigeracion = "No"
            break
        else:
            print("\nPor favor, ingresa una opcion valida.")

    fechaElaboracion = input("\n- Escribe la fecha de elaboración del producto (Formato DD-MM-AAAA): " )
    elaboracion_dt = datetime.strptime(fechaElaboracion, '%d-%m-%Y')
    if(validaFechaProducto(fechaElaboracion, 1) == False):
        print("\nFecha invalida, por favor ingresa una fecha REAL en formato DD-MM-AAAA.")
        return
    fechaCaducidad = input("\n- Escribe la fecha de caducidad del producto (Formato DD-MM-AAAA): " )
    caducidad_dt = datetime.strptime(fechaCaducidad, '%d-%m-%Y')
    if(validaFechaProducto(fechaCaducidad, 2) == False):
        print("\nFecha invalida, por favor ingresa una fecha en formato DD-MM-AAAA.")
        return
    elif(caducidad_dt.date() < elaboracion_dt.date()):
        print("\nFecha invalida, la fecha de caducidad no puede ser menor a la fecha de elaboracion.")
        return
    nuevoProducto = pd.Series([id, nombre, marca, presentacion, precio, cantidad, stock, refrigeracion, fechaElaboracion, fechaCaducidad], index=["ID","Nombre","Marca","Presentacion","Precio","Cantidad","Stock","Refrigeracion","Elaboracion","Caducidad"])
    resultado = pd.concat([productos, nuevoProducto.to_frame().T], ignore_index=False)
    resultado.to_csv("Producto.csv", index=False)
    print("\nProducto agregado al archivo.")

def editarProducto():
    """
    Método para modificar los datos de un empleado
    """
    productos = pd.read_csv("Producto.csv") 
    id = input("\nEscribe el ID del producto que quieres editar: ")
    if(Producto.existeProducto(id)):
        seguir = True
        while seguir:
            try:
                
                print("\n- Escribe el número del dato que quieras editar ")
                print("\n[1] Nombre")
                print("[2] Marca")
                print("[3] Presentación")
                print("[4] Precio")
                print("[5] Cantidad")
                print("[6] Cantidad de Stock")
                print("[7] Refrigeración")
                print("[8] Fecha de Elaboracion")
                print("[9] Fecha de Caducidad")
                print("[10] Atras")
                opcion = (int(input("\nOpcion: ")))
                
                if opcion == 1:
                    nuevo = input("\n- Escribe el nuevo nombre del producto: ")
                    productos.iloc[Producto.renglonProducto(id),1] = nuevo
                elif opcion == 2:
                    nuevo = input("\n- Escribe la nueva marca del producto: ")
                    productos.iloc[Producto.renglonProducto(id),2] = nuevo
                elif opcion == 3:
                    nuevo = input("\n- Escribe la nueva presentación del producto: ")
                    productos.iloc[Producto.renglonProducto(id),3] = nuevo
                elif opcion == 4:
                    nuevo = (int(input("\n- Escribe el nuevo precio del producto: ")))
                    productos.iloc[Producto.renglonProducto(id),4] = nuevo
                elif opcion == 5:
                    nuevo = (int(input("\n- Escribe la nueva cantidad del producto: ")))
                    productos.iloc[Producto.renglonProducto(id),5] = nuevo
                elif opcion == 6:
                    nuevo = (int(input("\n- Escribe la nueva cantidad de stock del producto: ")))
                    productos.iloc[Producto.renglonProducto(id),6] = nuevo
                elif opcion == 7:
                    nuevaRespuesta = 1
                    while nuevaRespuesta != 1 or nuevaRespuesta != 2:
                        nuevaRespuesta = (int(input("\n- ¿El producto requiere refrigeración?\n\n\t [1] Si [2] No\n\nOpcion: ")))
                        if nuevaRespuesta == 1:
                            nuevaRefrigeracion = "Si"
                            break
                        elif nuevaRespuesta == 2:
                            nuevaRefrigeracion = "No"
                            break
                        else:
                            print("\nPor favor, ingresa una opcion valida.")
                    productos.iloc[Producto.renglonProducto(id),7] = nuevaRefrigeracion
                elif opcion == 8:
                    nuevaFechaElab = input("\n- Escribe la nueva fecha de elaboración del producto (Formato DD-MM-AAAA): ")
                    nuevaElaboracion_dt = datetime.strptime(nuevaFechaElab, '%d-%m-%Y')
                    if(validaFechaProducto(nuevaFechaElab, 1) == False):
                        print("\nFecha invalida, por favor ingresa una fecha REAL en formato DD-MM-AAAA.")
                        return
                    productos.iloc[Producto.renglonProducto(id),8] = nuevaFechaElab
                    elaboracion_dt = nuevaElaboracion_dt
                elif opcion == 9:
                    nuevaFechaCad = input("\n- Escribe la nueva fecha de caducidad del producto (Formato DD-MM-AAAA): ")
                    nuevaCaducidad_dt = datetime.strptime(nuevaFechaCad, '%d-%m-%Y')
                    if(validaFechaProducto(nuevaFechaCad, 2) == False):
                        print("\nFecha invalida, por favor ingresa una fecha en formato DD-MM-AAAA.")
                        return
                    elif(nuevaCaducidad_dt.date() < elaboracion_dt.date()):
                        print("\nFecha invalida, la fecha de caducidad no puede ser menor a la fecha de elaboracion.")
                        return
                    productos.iloc[Producto.renglonProducto(id),9] = nuevaFechaCad
                    caducidad_dt = nuevaCaducidad_dt
                elif opcion == 10:
                    seguir = False
                else:
                    print("\nPor favor, ingresa una opcion valida.")
            except:
                print("\nPor favor, ingresa un numero.")
        productos.to_csv("Producto.csv", index=False)
    else:
        print("\nNo se encontro un producto con ese ID.")


def validaFechaProducto(fecha, funcion):
    """
    Metodo que verifica si la fecha es válida y real en formato DD-MM-AAAA.
    el parametro funcion se utiliza para diferenciar entre la modalidad de la funcion
    1 para que no cuente fechas futuras
    2 para que cuente fechas futuras
    """
    if funcion == 1:

        try:
            # Convierte la fecha en un objeto datetime.
            fecha_dt = datetime.strptime(fecha, '%d-%m-%Y')
            
            # Verifica si la fecha es anterior a la fecha actual.
            if fecha_dt.date() > datetime.now().date():
                return False
            
            return True
        except ValueError:
            return False

    elif funcion == 2:

        try:
            # Convierte la fecha en un objeto datetime.
            fecha_dt = datetime.strptime(fecha, '%d-%m-%Y')

            return True
        except ValueError:
            return False

    else:
        print("\nPor favor, ingresa una opcion valida.")

def manejaProductos():
    """
    Muestra todo el manejo de datos que se tiene para los empleados
    """
    seguir = True
    print("\n           Base de Datos para Productos         ")
    while seguir:
        try:
            productos = pd.read_csv("Producto.csv")
            print("\nEscribe que opcion quieres realizar")
            print("\n[1] Ver Productos")
            print("[2] Agregar producto")
            print("[3] Editar datos de un producto")
            print("[4] Eliminar producto")
            print("[5] Buscar producto mediante ID")
            print("[6] Atras")
            opcion = (int(input("\nOpcion: ")))
            if opcion == 1:
                print("\t\t\t\t\t\t  PRODUCTOS\n")
                print(productos)
            elif opcion == 2:
                productos = pd.read_csv("Producto.csv")
                agregarProducto()
            elif opcion == 3:
                productos = pd.read_csv("Producto.csv")
                editarProducto()
            elif opcion == 4:
                productos = pd.read_csv("Producto.csv")
                eliminarProducto()
            elif opcion == 5:
                productos = pd.read_csv("Producto.csv")
                buscarProducto()
            elif opcion == 6:
                seguir = False
            else:
                print("\nPor favor, introduce una opcion valida.")
        except:
            print("\nPor favor, introduce un numero.")
