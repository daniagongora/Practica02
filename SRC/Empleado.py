import pandas as pd
import re
from datetime import datetime

"""
    Clase Empleado
"""
class Empleado:
    
    def IDEmpleado():
        """
        Método que regresa el ID unico creado para cada empleado.
        """
        empleados = pd.read_csv("Empleado.csv")
        id = empleados.iloc[-1,0]
        unicoID = id[0] + str(int(id[1:])+1)
        return unicoID
      
    def existeEmpleado(id):
        """
        Método que verifica si existe ya un empleado.
        """
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                return True

        return False
    
    def renglonEmpleado(id):
        """
        Método que devuelve el numero de reglon donde se encuentra el empleado.
        """
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                return i
        return -1
    
    def sucursalEmpleado(id):
        """
        Método que regresa la sucursal a la que pertenece un empleado.
        """
        renglon = 0
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                renglon = i
        return empleados.iloc[renglon,8]

def buscarEmpleado():
        """
        Método que nos permite buscar un empleado por su ID.
        """
        empleados = pd.read_csv("Empleado.csv") 
        id = input("\nID del empleado que quieres buscar: ")
        if(Empleado.existeEmpleado(id) == True):
            print("\nResultado: \n")
            print(empleados.loc[[Empleado.renglonEmpleado(id)]])
        else:
            print("\nNo se encontro un empleado con ese ID.")

def eliminarEmpleado():
        """
        Método para eliminar un empleado.
        """
        empleados = pd.read_csv("Empleado.csv") 
        id = input("\nID del empleado a eliminar: ")
        if(Empleado.existeEmpleado(id) == True):
            resultado = empleados.drop(empleados.index[Empleado.renglonEmpleado(id)])
            print("\nEmpleado eliminado.")
            resultado.to_csv("Empleado.csv", index=False)
        else:
            print("\nNo se encontro un empleado con ese ID.")

def agregarEmpleado():
        """
        Método para agregar un empleado.
        """
        empleados = pd.read_csv("Empleado.csv") 
        id = Empleado.IDEmpleado()
        nombre = input("\n- Escribe el nombre del empleado: ")
        if(validaNombre(nombre) == False):
            print("\nNombre invalido, por favor utiliza caracteres alfabeticos.")
            return
        correo = input("\n- Escribe el correo del empleado: ")
        if(validaCorreo(correo) == False):
            print("\nCorreo invalido, por favor ingresa una direccion de correo valida.")
            return
        correos = correo
        seguirCorreo = True
        while seguirCorreo:
            print("\n¿Desea agregar otro correo electronico?\n\n\t [1] Si [2] No\n\n")
            respuestaCorreo = (int(input("Opcion: ")))
            if respuestaCorreo == 1:
                correo = input("\n- Escribe el correo electronico del empleado: ")
                if(validaCorreo(correo) == False):
                    print("\nCorreo invalido, por favor ingresa una direccion de correo valida.")
                    return
                correos = correos+" "+correo
                seguirCorreo = True
            elif respuestaCorreo == 2:
                seguirCorreo = False
            else:
                print("\nOpcion invalida.")
                seguirCorreo = True
        telefono = input("\n- Escribe el número de telefono del empleado: ")
        if(validaNumeroTelefonico(telefono) == False):
            print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
            return
        telefonos = telefono
        seguirTelefono = True    
        while seguirTelefono:
            print("\n¿Desea agregar otro numero telefonico?\n\n\t [1] Si [2] No\n\nOpcion: ")
            respuestaTelefono = (int(input("Opcion: ")))
            if respuestaTelefono == 1:
                telefono = input("\n- Escribe el número de telefono del empleado: ")
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
        direccion = input("\n- Escribe la direccion del empleado: ")
        salario = (int(input("\n- Escribe el salario del empleado: ")))
        fechaNac = input("\n- Escribe la fecha de nacimiento del empleado (Formato DD-MM-AAAA): ")
        if(validaFechaNacimiento(fechaNac) == False):
                print("\nFecha invalida, por favor ingresa una fecha de nacimiento REAL en formato DD-MM-AAAA.")
                return
        puesto = input("\n- Escribe el puesto del empleado: ")
        sucursal = input("\n- Escribe la sucursal a la que pertence el empleado (Recuerda que solo puede pertenecer a una): ")
        nuevoEmpleado = pd.Series([id, nombre, correos, telefonos, direccion, salario, fechaNac, puesto, sucursal], index=["ID","Nombre","Correo Electronico","Telefono","Direccion","Salario","Nacimiento","Puesto","Sucursal"])
        resultado = pd.concat([empleados, nuevoEmpleado.to_frame().T], ignore_index=False)
        resultado.to_csv("Empleado.csv", index=False)
        print("\nEmpleado agregado al archivo.")

def editarEmpleado():
        """
        Método para modificar los datos de un empleado.
        """
        empleados = pd.read_csv("Empleado.csv") 
        id = input("\n- Escribe el ID del empleado que quieres editar: ")
        if(Empleado.existeEmpleado(id)):
            seguir = True
            while seguir:
                try:
                    print("\n- Escribe el número del dato que quieras editar: ")
                    print("\n[1] Nombre")
                    print("[2] Correo Electronico")
                    print("[3] Telefono")
                    print("[4] Direccion")
                    print("[5] Salario")
                    print("[6] Fecha de Nacimiento")
                    print("[7] Puesto de Trabajo")
                    print("[8] Sucursal")
                    print("[9] Atras")
                    opcion = (int(input("\nOpcion: ")))
                    
                    if opcion == 1:
                        nuevo = input("\n- Escribe el nuevo nombre del empleado: ")
                        empleados.iloc[Empleado.renglonEmpleado(id),1] = nuevo
                    elif opcion == 2:
                        nuevo = input("\n- Escribe el nuevo correo del empleado: ")
                        if(validaCorreo(nuevo) == False):
                            print("\nCorreo invalido, por favor ingresa una direccion de correo valida.")
                            return
                        nuevos = nuevo
                        seguirCorreo = True
                        while seguirCorreo:
                            print("\n¿Desea agregar otro correo electronico?\n\n\t [1] Si [2] No\n\nOpcion: ")
                            respuestaCorreo = (int(input("Opcion: ")))
                            if respuestaCorreo == 1:
                                nuevo = input("\n- Escribe el correo electronico del empleado: ")
                                if(validaCorreo(nuevo) == False):
                                    print("\nCorreo invalido, por favor ingresa una direccion de correo valida.")
                                    return
                                nuevos = nuevos+" "+nuevo
                                seguirCorreo = True
                            elif respuestaCorreo == 2:
                                seguirCorreo = False
                            else:
                                print("\nPor favor, ingresa una opcion valida.")
                                seguirCorreo = True
                        empleados.iloc[Empleado.renglonEmpleado(id),2] = nuevos
                    elif opcion == 3:       
                        nuevo = input("\n- Escribe el nuevo telefono del empleado: ")
                        if(validaNumeroTelefonico(nuevo) == False):
                            print("\nTelefono invalido, por favor ingresa un numero de 10 digitos.")
                            return
                        nuevos = nuevo
                        seguirTelefono = True    
                        while seguirTelefono:
                            print("\n¿Desea agregar otro numero telefonico?\n\n\t [1] Si [2] No")
                            respuestaTelefono = (int(input("\nOpcion: ")))
                            if respuestaTelefono == 1:
                                nuevo = input("\n- Escribe el número de telefono del empleado: ")
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
                        empleados.iloc[Empleado.renglonEmpleado(id),3] = nuevos
                    elif opcion == 4:
                        nuevo = input("\n- Escribe la nueva dirección del empleado: ")
                        empleados.iloc[Empleado.renglonEmpleado(id),4] = nuevo
                    elif opcion == 5:
                        nuevo = (int(input("\n- Escribe el nuevo salario del empleado: ")))
                        empleados.iloc[Empleado.renglonEmpleado(id),5] = nuevo
                    elif opcion == 6:
                        nuevo = input("\n- Escribe la nueva fecha de nacimiento del empleado (Formato DD-MM-AAAA): ")
                        if(validaFechaNacimiento(nuevo) == False):
                            print("\nFecha invalida, por favor ingresa una fecha de nacimiento REAL en formato DD-MM-AAAA.")
                            return
                        empleados.iloc[Empleado.renglonEmpleado(id),6] = nuevo
                    elif opcion == 7:
                        nuevo = input("\n- Escribe el nuevo puesto de trabajo del empleado: ")
                        empleados.iloc[Empleado.renglonEmpleado(id),7] = nuevo
                    elif opcion == 8:
                        nuevo = input("\n- Escribe la nueva sucursal donde trabajara el empleado: ")
                        empleados.iloc[Empleado.renglonEmpleado(id),8] = nuevo
                    elif opcion == 9:
                        seguir = False
                    else:
                        print("\nPor favor, ingresa una opcion valida.")
                except:
                    print("\nPor favor, ingresa un numero.")
            empleados.to_csv("Empleado.csv", index=False)
        else:
            print("\nNo se encontro un empleado con ese ID.")


def validaNombre(nombre):
    """
    Método que verifica si el nombre solo contiene letras.
    """
    # Expresión regular para verificar solo letras.
    patron = re.compile("^[a-zA-Z]+$")
    
    # Verifica si el nombre coincide con el patrón.
    if patron.match(nombre):
        return True
    else:
        return False

def validaCorreo(correo):
    """
    Método que verifica si la dirección de correo electrónico es válida.
    """
    # Expresión regular para verificar si el correo es válido.
    patron = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    # Verifica si la dirección de correo electrónico coincide con el patrón.
    if patron.match(correo):
        return True
    else:
        return False

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

def validaFechaNacimiento(fecha):
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

def manejaEmpleados():
    """
    Muestra todo el manejo de datos que se tiene para los empleados.
    """
    seguir = True
    print("\n           Base de Datos para Empleados         ")
    while seguir:
        try:
            empleados = pd.read_csv("Empleado.csv")
            print("\nEscribe que opcion quieres realizar: \n")
            print("[1] Ver Empleados")
            print("[2] Agregar empleado")
            print("[3] Editar datos de un empleado")
            print("[4] Eliminar empleado")
            print("[5] Buscar empleado mediante ID")
            print("[6] Atras")
            opcion = (int(input("\nOpcion: ")))
            if opcion == 1:
                print("\t\t\t EMPLEADOS\n")
                print(empleados)
            elif opcion == 2:
                empleados = pd.read_csv("Empleado.csv")
                agregarEmpleado()
            elif opcion == 3:
                empleados = pd.read_csv("Empleado.csv")
                editarEmpleado()
            elif opcion == 4:
                empleados = pd.read_csv("Empleado.csv")
                eliminarEmpleado()
            elif opcion == 5:
                empleados = pd.read_csv("Empleado.csv")
                buscarEmpleado()
            elif opcion == 6:
                seguir = False
            else:
                print("\nPor favor, ingresa una opcion valida.")
        except:
            print("\nPor favor, ingresa un numero.")




