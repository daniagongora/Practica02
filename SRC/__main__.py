import pandas as pd

empleados = pd.read_csv('Empleado.csv')
id = "E1007"

empleados.set_index("IdEmpleado", inplace=True)
#empleado = empleados.loc[id]
correos = empleados.loc[id,"CorreoElectronico"]
#print(type(empleado))



print(correos.split())


