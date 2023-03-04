import pandas as pd

class Sucursal:

    """
        Clase sucursal
    """

    def IDSucursal():
        """
        Método que regresa el ID unico creado para cada sucursal.
        """
        sucursales = pd.read_csv("Sucursal.csv")
        id = sucursales.iloc[-1,0]
        unicoID = id[0] + str(int(id[1:])+1)
        return unicoID

    def existeSucursal(id):
        """
        Método que verifica si existe ya una sucursal
        """
        sucursales = pd.read_csv("Sucursal.csv")
        for i in range(0, len(sucursales)):
            if(sucursales.iloc[i,0] == id):
                return True

        return False

    def renglonSucursal(id):
        """
        Método que devuelve el numero de reglon donde se encuentra la sucursal
        """
        sucursales = pd.read_csv("Sucursal.csv")
        for i in range(0, len(sucursales)):
            if(sucursales.iloc[i,0] == id):
                return i
        return -1

    def infoSucursal(id):
        """
        Metodo que filtra la informacion de la sucursal
        por los atributos y los regresa. 

        Args:
            id: id de la sucursal
        """
        # Cargamos el archivo csv de sucursales
        sucursales = pd.read_csv("Sucursal.csv") 

        # Busca por IdSucursal
        sucursales.set_index("IdSucursal",inplace=True)

        menu ="""

            [1] Nombre
            [2] Direccion
            [3] Telefono
            [4] Fecha de apertura

        """

        resultado = None

        while True:
            
            print(menu)

            opcion = int(input("Elige una opcion: "))

            if opcion == 1:
                nombre = sucursales.loc[id,"Nombre"]
                resultado = nombre
            elif opcion == 2:
                direccion = sucursales.loc[id,"Direccion"]
                resultado = direccion
            elif opcion == 3:
                telefono = sucursales.loc[id,"Telefono"]
                resultado = telefono
            elif opcion == 4:
                fecha_de_apertura = sucursales.loc[id,"FechaApertura"]
                resultado = fecha_de_apertura
            elif opcion == 5:
                break
            else:
                print("Esa no es una opcion valida")

            return resultado

def buscarSucursal():
    """
    Método que nos permite buscar una sucursal por su ID 
    """
    sucursales = pd.read_csv("Sucursal.csv")
    id = input("Pon el ID de la sucursal que quieres buscar ")
    if(Sucursal.existeSucursal(id) == True):
        menu = """

            [1] Resumen
            [2] Filtrar
            [3] Salir

        """
        while True:
            print(menu)
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                print("Resultado: ")
                print(sucursales.loc[[Sucursal.renglonSucursal(id)]])
            elif opcion == 2:
                resultado = Sucursal.infoSucursal(id=id)
                print(f"Resultado: {resultado}")
            elif opcion == 3:
                break
            else:
                print("Esa no es una opcion valida")
    else:
        print("Esa sucursal no existe")

def eliminarSucursal():
    
    """
    Método para eliminar una sucursal
    """
    sucursales = pd.read_csv("Sucursal.csv") 
    id = input("ID de la sucursal a eliminar")
    if(Sucursal.existeSucursal(id) == True):
        resultado = sucursales.drop(sucursales.index[Sucursal.renglonSucursal(id)])
        print("Se borro la sucursal")
        resultado.to_csv("Sucursal.csv", index=False)
    else:
        print("No existe esa sucursal")

def agregarSucursal():
    """
    Método para agregar una sucursal
    """
    sucursales = pd.read_csv("Sucursal.csv") 
    id = Sucursal.IDSucursal()
    nombre = input("\n- Escribe nombre de la sucursal: ")
    direccion = input(" Escribe la direccion de la sucursal ")
    telefono = input(" Escribe el número de telefono de la sucursal ")
    fechaApertura = input(" Escribe la fecha de apertura de la sucursal (Formato DD-MM-AAAA): ")
    nuevaSucursal = pd.Series([id, nombre, direccion, telefono, fechaApertura], index=["IdSucursal","Nombre","Direccion","Telefono","FechaApertura"])

    resultado = pd.concat([sucursales, nuevaSucursal.to_frame().T], ignore_index=False)
    print(resultado)
    resultado.to_csv("Sucursal.csv", index=False)
    print("Sucursal agregada al archivo.")
        
def editarSucursal():

    """
    Método para modificar los datos de una Sucursal
    """
    sucursales = pd.read_csv("Sucursal.csv") 
    id = input("\n-> Escribe el ID de la sucursal que quieres editar: ")
    if(Sucursal.existeSucursal(id)):
        seguir = True
        while seguir:
            try:
                
                print("\n- Escribe el número del dato que quieras editar ")
                print("1.- Nombre")
                print("2.- Direccion")
                print("3.- Telefono")
                print("Escogiste la opcion: ")
                opcion = (int(input()))
                
                if opcion == 1:
                    nuevo = input(" Escribe el nuevo nombre de la sucursal: ")
                    sucursales.iloc[Sucursal.renglonSucursal(id),1] = nuevo
                    seguir = False
                elif opcion == 2:
                    nuevo = input(" Escribe la direccion de la sucursal: ")
                    sucursales.iloc[Sucursal.renglonSucursal(id),2] = nuevo
                    seguir = False
                elif opcion == 3:
                    nuevo = input(" Escribe el telefono de la sucursal: ")
                    sucursales.iloc[Sucursal.renglonSucursal(id),3] = nuevo
                    seguir = False
    
                else:
                    print("Escribe una opcion valida")
            except:
                print("Escribe un numero")
        sucursales.to_csv("Sucursal.csv", index=False)
    else:
        print("No existe esa sucursal, intenta de nuevo")

def manejaSucursales():
    """
    Muestra todo el manejo de datos que se tiene para las sucursales
    """
    seguir = True
    print("           Base de Datos para Sucursales       ")
    while seguir:
        try:
            sucursales = pd.read_csv("Sucursal.csv")
            print("\n-> Escribe que opcion quieres realizar")
            print("1. Ver sucursales")
            print("2. Agregar una sucursal")
            print("3. Editar datos de una sucursal")
            print("4. Eliminar una sucursal")
            print("5. Buscar a una sucursal mediante su ID")
            print("6. Atras")
            opcion = (int(input()))
            if opcion == 1:
                print(sucursales)
            elif opcion == 2:
                sucursales = pd.read_csv("Sucursal.csv")
                agregarSucursal()
            elif opcion == 3:
                sucursales = pd.read_csv("Sucursal.csv")
                editarSucursal()
            elif opcion == 4:
                sucursales = pd.read_csv("Sucursal.csv")
                eliminarSucursal()
            elif opcion == 5:
                sucursales = pd.read_csv("Sucursal.csv")
                buscarSucursal()
            elif opcion == 6:
                seguir = False
            else:
                print("Introduce una opcion valida")
        except:
            print("Introduce un numero.")