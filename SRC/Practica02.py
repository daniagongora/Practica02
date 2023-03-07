from Sucursal import *
import Empleado
import Producto
import Sucursal

def menuPrincipal():
    """
    Menu principal.
    """
    seguir = True
    print("\n\n********** Bienvenido a la Base de Datos **********")
    while seguir:
        try:
            print("\nSelecciona la entidad que quieres administrar:\n")
            print("[1] Empleados")
            print("[2] Productos")
            print("[3] Sucursales")
            print("[4] Salir")
            opcion = (int(input("\nOpcion: ")))
            if opcion == 1:
                Empleado.manejaEmpleados()
            elif opcion == 2:
                Producto.manejaProductos()
            elif opcion == 3:
                Sucursal.manejaSucursales()
            elif opcion == 4:
                print("\nGracias por ingresar a la base de datos!\n")
                seguir = False
            else:
                print("\nPor favor, introduce una opcion valida.\n")
        except:
            print("\nPor favor, introduce un numero.\n")

def main():
	"""
	Ejecuta el menu principal que corre la base de datos.
	"""
	menuPrincipal()
	
if __name__=="__main__":
	main()
