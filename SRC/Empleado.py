import pandas as pd

class Empleado:

    """
        Clase empleado
    """
    
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
        Método que verifica si existe ya un empleado 
        """
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                return True

        return False
    
    def renglonEmpleado(id):
        """
        Método que devuelve el numero de reglon donde se encuentra el empleado
        """
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                return i
        return -1
    
    def sucursalEmpleado(id):
        """
        Metodo que regresa la sucursal a la que pertenece un empleado.
        """
        renglon = 0
        empleados = pd.read_csv("Empleado.csv")
        for i in range(0, len(empleados)):
            if(empleados.iloc[i,0] == id):
                renglon = i
        #sucursal = sucursal+1
        return empleados.iloc[renglon,8]
    
    def infoEmpleado(id):
        """
        Metodo que filtra la informacion del empleado
        por los atributos y los regresa. 

        Args:
            id: id del empleado
        """
        # Cargamos el archivo csv de empleados
        empleados = pd.read_csv("Empleado.csv") 

        # Busca por IdEmpleado
        empleados.set_index("IdEmpleado",inplace=True)

        menu ="""

            [1] Nombre
            [2] Correo
            [3] Telefono
            [4] Direccion
            [5] Salario
            [6] Fecha de nacimiento
            [7] Puesto
            [8] Sucursal
            [9] Salir

        """

        resultado = None

        while True:
            
            print(menu)

            opcion = int(input("Elige una opcion: "))

            if opcion == 1:
                nombre = empleados.loc[id,"Nombre"]
                resultado = nombre
            elif opcion == 2:
                correo = empleados.loc[id,"CorreoElectronico"]
                if not(correo == None):
                    resultado = correo.split()
            elif opcion == 3:
                telefono = empleados.loc[id,"Telefono"]
                if not(telefono == None):
                    resultado = str(telefono).split()
            elif opcion == 4:
                direccion = empleados.loc[id,"Direccion"]
                resultado = direccion
            elif opcion == 5:
                salario = empleados.loc[id,"Salario"]
                resultado = salario
            elif opcion == 6:
                fecha_nacimiento = empleados.loc[id,"FechaNacim"]
                resultado = fecha_nacimiento
            elif opcion == 7:
                puesto = empleados.loc[id,"PuestoTrabajo"]
                resultado = puesto
            elif opcion == 8:
                sucursal = empleados.loc[id,"Sucursal"]
                resultado = sucursal
            elif opcion == 9:
                    break
            else:
                print("Esa no es una opcion valida")

            return resultado

def buscarEmpleado():
    """
    Método que nos permite buscar un empleado por su ID 
    """
    empleados = pd.read_csv("Empleado.csv") 
    id = input("Pon el ID del empleado que quieres buscar ")
    if(Empleado.existeEmpleado(id) == True):
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
                print(empleados.loc[[Empleado.renglonEmpleado(id)]])
            elif opcion == 2:
                resultado = Empleado.infoEmpleado(id=id)
                print(f"Resultado: {resultado}")
            elif opcion == 3:
                break
            else:
                print("Esa no es una opcion valida")
    else:
        print("Ese empleado no existe")

def eliminarEmpleado():
    
    """
    Método para eliminar un empleado
    """
    empleados = pd.read_csv("Empleado.csv") 
    id = input("ID del empleado a eliminar")
    if(Empleado.existeEmpleado(id) == True):
        resultado = empleados.drop(empleados.index[Empleado.renglonEmpleado(id)])
        print("Se borro al empleado")
        resultado.to_csv("Empleado.csv", index=False)
    else:
        print("No existe ese empleado")

def agregarEmpleado():
    """
    Método para agregar un empleado
    """
    empleados = pd.read_csv("Empleado.csv") 
    id = Empleado.IDEmpleado()
    nombre = input("\n- Escribe nombre del empleado: ")
    correo = input(" Escribe el correo del empleado (Si necesitas poner varios agregalos con espacios): ")
    telefono = input(" Escribe el número de telefono del empleado (Si necesitas poner varios agregalos con espacios): ")
    direccion = input(" Escribe la direccion del empleado ")
    salario = input(" Escribe el salario del empleado ")
    fechaNac = input(" Escribe la fecha de nacimiento del empleado (Formato DD-MM-AAAA): ")
    puesto = input(" Escribe el puesto del empleado ")
    sucursal = input("Escribe la sucursal a la que pertence el empleado, recuerda que solo puede pertenecer a una ")
    nuevoEmpleado = pd.Series([id, nombre, correo, telefono, direccion, salario, fechaNac, puesto, sucursal], index=["IdEmpleado","Nombre","CorreoElectronico","Telefono","Direccion","Salario","FechaNacim","PuestoTrabajo","Sucursal"])
    resultado = pd.concat([empleados, nuevoEmpleado.to_frame().T], ignore_index=False)
    print(resultado)
    resultado.to_csv("Empleado.csv", index=False)
    print("Empleado agregado al archivo.")

def editarEmpleado():
    """
    Método para modificar los datos de un empleado
    """
    empleados = pd.read_csv("Empleado.csv") 
    id = input("\n-> Escribe el ID del empleado que quieres editar: ")
    if(Empleado.existeEmpleado(id)):
        seguir = True
        while seguir:
            try:
                
                print("\n- Escribe el número del dato que quieras editar ")
                print("1.- Nombre")
                print("2.- Correo Electronico")
                print("3.- Telefono")
                print("4.- Direccion")
                print("5.- Salario")
                print("6.- Fecha de Nacimiento")
                print("7.- Puesto de Trabajo")
                print("8.- Sucursal donde trabaja")
                print("Escogiste la opcion: ")
                opcion = (int(input()))
                
                if opcion == 1:
                    nuevo = input(" Escribe el nuevo nombre del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),1] = nuevo
                    seguir = False
                elif opcion == 2:
                    nuevo = input(" Escribe el (los) nuevo(s) correo(s) del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),2] = nuevo
                    seguir = False
                elif opcion == 3:
                    nuevo = input(" Escribe el (los) nuevo(s) telefono(s) del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),3] = nuevo
                    seguir = False
                elif opcion == 4:
                    nuevo = input(" Escribe la nueva dirección del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),4] = nuevo
                    seguir = False
                elif opcion == 5:
                    nuevo = input(" Escribe el nuevo salario del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),5] = nuevo
                    seguir = False
                elif opcion == 6:
                    nuevo = input(" Escribe la nueva fecha de nacimiento del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),6] = nuevo
                    seguir = False
                elif opcion == 7:
                    nuevo = input(" Escribe el nuevo puesto de trabajo del empleado: ")
                    empleados.iloc[Empleado.renglonEmpleado(id),7] = nuevo
                    seguir = False
                elif opcion == 8:
                    nuevo = input(" Escribe la nueva sucursal donde trabajara el empleado: ")
                    nuevo = "'" + nuevo + "'"
                    empleados.iloc[Empleado.renglonEmpleado(id),8] = nuevo
                else:
                    print("Escribe una opcion valida")
            except:
                print("Escribe un numero")
        empleados.to_csv("Empleado.csv", index=False)
    else:
        print("No existe ese empleado, intenta de nuevo")
    
def manejaEmpleados():
    """
    Muestra todo el manejo de datos que se tiene para los empleados
    """
    seguir = True
    print("           Base de Datos para Empleados         ")
    while seguir:
        try:
            empleados = pd.read_csv("Empleado.csv")
            print("\n-> Escribe que opcion quieres realizar")
            print("1. Ver Empleados")
            print("2. Agregar un empleado")
            print("3. Editar datos de un empleados")
            print("4. Eliminar a un empleado")
            print("5. Buscar a un empleado mediante su ID")
            print("6. Atras")
            opcion = (int(input()))
            if opcion == 1:
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
                print("Introduce una opcion valida")
        except:
            print("Introduce un numero.")




