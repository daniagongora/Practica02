import pandas as pd
import re
from datetime import datetime

"""
    Clase Sucursal
"""
class Sucursal:

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
        Método que verifica si existe ya una sucursal.
        """
        sucursales = pd.read_csv("Sucursal.csv")
        for i in range(0, len(sucursales)):
            if(sucursales.iloc[i,0] == id):
                return True

        return False

    def renglonSucursal(id):
        """
        Método que devuelve el numero de reglon donde se encuentra la sucursal.
        """
        sucursales = pd.read_csv("Sucursal.csv")
        for i in range(0, len(sucursales)):
            if(sucursales.iloc[i,0] == id):
                return i
        return -1

def buscarSucursal():
    """
    Método que nos permite buscar una sucursal por su ID.
    """
    sucursales = pd.read_csv("Sucursal.csv")
    id = input("\nID de la sucursal que quieres buscar: ")
    if(Sucursal.existeSucursal(id) == True):
            print("\nResultado: ")
            print(sucursales.loc[[Sucursal.renglonSucursal(id)]])
    else:
        print("\nNo se encontro una sucursal con ese ID.")

def eliminarSucursal():
    """
    Método para eliminar una sucursal.
    """
    sucursales = pd.read_csv("Sucursal.csv") 
    id = input("\nID de la sucursal a eliminar: ")
    if(Sucursal.existeSucursal(id) == True):
        resultado = sucursales.drop(sucursales.index[Sucursal.renglonSucursal(id)])
        print("\nSucursal eliminada.")
        resultado.to_csv("Sucursal.csv", index=False)
    else:
        print("\nNo se encontro una sucursal con ese ID.")

def agregarSucursal():
    """
    Método para agregar una sucursal.
    """
    sucursales = pd.read_csv("Sucursal.csv") 
    id = Sucursal.IDSucursal()
    nombre = input("\n- Escribe nombre de la sucursal: ")
    direccion = input("\n- Escribe la direccion de la sucursal: ")
    telefono = input("\n- Escribe el número de telefono de la sucursal: ")
    if(validaNumeroTelefonico(telefono) == False):
        print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
        return
    telefonos = telefono
    seguirTelefono = True    
    while seguirTelefono:
        print("\n¿Desea agregar otro numero telefonico?\n\n\t [1] Si [2] No\n\nOpcion: ")
        respuestaTelefono = (int(input("Opcion: ")))
        if respuestaTelefono == 1:
            telefono = input("\n- Escribe el número de telefono de la sucursal: ")
            if(validaNumeroTelefonico(telefono) == False):
                print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
                return
            telefonos = telefonos+" "+telefono
            seguirTelefono = True
        elif respuestaTelefono == 2:
            seguirTelefono = False
        else:
            print("\nPor favor, ingresa una opcion valida.")
            seguirTelefono = True
    fechaApertura = input("\n- Escribe la fecha de apertura de la sucursal (Formato DD-MM-AAAA): ")
    if(validaFechaApertura(fechaApertura) == False):
        print("\nFecha invalida, por favor ingresa una fecha de nacimiento REAL en formato DD-MM-AAAA.")
        return
    nuevaSucursal = pd.Series([id, nombre, direccion, telefonos, fechaApertura], index=["ID","Nombre","Direccion","Telefono","Apertura"])

    resultado = pd.concat([sucursales, nuevaSucursal.to_frame().T], ignore_index=False)
    print(resultado)
    resultado.to_csv("Sucursal.csv", index=False)
    print("\nSucursal agregada al archivo.")
        
def editarSucursal():
    """
    Método para modificar los datos de una sucursal.
    """
    
    sucursales = pd.read_csv("Sucursal.csv") 
    id = input("\n- Escribe el ID de la sucursal que quieres editar: ")
    if(Sucursal.existeSucursal(id)):
        seguir = True
        while seguir:
            try:
                print("\n- Escribe el número del dato que quieras editar: ")
                print("\n[1] Nombre")
                print("[2] Direccion")
                print("[3] Telefono")
                print("[4] Apertura")
                print("[5] Atras")
                opcion = (int(input("\nOpcion: ")))
                
                if opcion == 1:
                    nuevo = input("\n- Escribe el nuevo nombre de la sucursal: ")
                    sucursales.iloc[Sucursal.renglonSucursal(id),1] = nuevo
                elif opcion == 2:
                    nuevo = input("\n- Escribe la direccion de la sucursal: ")
                    sucursales.iloc[Sucursal.renglonSucursal(id),2] = nuevo
                elif opcion == 3:
                    nuevo = input("\n- Escribe el telefono de la sucursal: ")
                    if(validaNumeroTelefonico(nuevo) == False):
                        print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
                        return
                    nuevos = nuevo
                    seguirTelefono = True    
                    while seguirTelefono:
                        print("\n¿Desea agregar otro numero telefonico?\n\n\t [1] Si [2] No")
                        respuestaTelefono = (int(input("\nOpcion: ")))
                        if respuestaTelefono == 1:
                            nuevo = input("\n- Escribe el número de telefono de la sucursal: ")
                            if(validaNumeroTelefonico(nuevo) == False):
                                print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
                                return
                            nuevos = nuevos+" "+nuevo
                            seguirTelefono = True
                        elif respuestaTelefono == 2:
                            seguirTelefono = False
                        else:
                            print("\nPor favor, ingresa una opcion valida.")
                            seguirTelefono = True
                    sucursales.iloc[Sucursal.renglonSucursal(id),3] = nuevos
                elif opcion == 4:
                    nuevo = input("\n- Escribe la nueva fecha de apertura (Formato DD-MM-AAAA): ")
                    if(validaFechaApertura(nuevo) == False):
                        print("\nFecha invalida, por favor ingresa una fecha de nacimiento REAL en formato DD-MM-AAAA.")
                        return
                    sucursales.iloc[Sucursal.renglonSucursal(id),4] = nuevo
                elif opcion == 5:
                    seguir = False
                else:
                    print("\nPor favor, ingresa una opcion valida.")
            except:
                print("\nPor favor, ingresa un numero.")
        sucursales.to_csv("Sucursal.csv", index=False)
    else:
        print("\nNo se encontro una sucursal con ese ID.")

def validaNumeroTelefonico(telefono):
    """
    Método que verifica si el número de teléfono es válido.
    """
    # Expresión regular para verificar si el teléfono es válido.
    patron = re.compile(r'^\d{10}$')
    
    # Verifica si el número de teléfono coincide con el patrón.
    if patron.match(telefono):
        return True
    else:
        return False


def validaFechaApertura(fecha):
    """
    Método que verifica si la fecha es válida y real en formato DD-MM-AAAA.
    """
    try:
        # Convierte la fecha en un objeto datetime.
        fecha_dt = datetime.strptime(fecha, '%d-%m-%Y')
        
        # Verifica si la fecha es anterior a la fecha actual.
        if fecha_dt.date() > datetime.now().date():
            return False
        
        return True
    except ValueError:
        return False

def manejaSucursales():
    """
    Muestra todo el manejo de datos que se tiene para las sucursales.
    """
    seguir = True
    print("\n           Base de Datos para Sucursales       ")
    while seguir:
        try:
            sucursales = pd.read_csv("Sucursal.csv")
            print("\n- Escribe que opcion quieres realizar: ")
            print("\n[1] Ver sucursales")
            print("[2] Agregar sucursal")
            print("[3] Editar datos de una sucursal")
            print("[4] Eliminar sucursal")
            print("[5] Buscar sucursal mediante ID")
            print("[6] Atras")
            opcion = (int(input("\nOpcion: ")))
            if opcion == 1:
                print("\t\t\t  SUCURSALES\n")
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
                print("\nPor favor, ingresa una opcion valida.")
        except:
            print("\nPor favor, ingresa un numero.")