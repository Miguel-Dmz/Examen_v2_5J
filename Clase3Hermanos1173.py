print("**** EXAMEN V2 MIGUEL DOMINGUEZ 1173 **** \n")
class zapateria:
    ## EMPLEADO
    def diccionario_empleado_1173(self):
        print("***** EMPLEADO ***** \n")
        Empleado = {
        "Id_Empleado..56965\n": "Nombre..Jose Luis",
        "Email..Jose_luis@gmail.com\n":"N_Celular..656-458-1236",
        "CURP..JOSD65636SHD12\n":"Fecha de nacimiento.. 12 agosto de 1976",
        "RFC..JOS121544": 7
        } 
        print(Empleado)
        print("\n")
        for b, z in Empleado.items():
            print(b,z)
        print("\n")
    
    ## CALZADO
    def diccionario_calzado_1173(self):
        print("***** CLAZADO ***** \n")
        Calzado = {
        "Id_Calzado..45862\n": "Nombre_C..Jordan 1",
        "Material..Cuero\n":"Talla..9.5 MX",
        "Precio..3,500 MX\n":"Color..Azul celeste con blanco",
        "Tipo_C..Tenis": 7
        } 
        print(Calzado)
        print("\n")
        for b, z in Calzado.items():
            print(b,z)
        print("\n")
        
    ## SUCURSALES
    def diccionario_sucursales_1173(self):
        print("***** SUCURSALES ***** \n")
        Sucursales = {
        "Id_Sucursal..45852\n": "NumeroC_S..656-125-7895",
        "Direccion_S..C.Plutarco elias calles #4585\n":"Encargado_S..Manuel Molina",
        "C_Empleados_S.. 45 empleados\n":"Materiales_S.. Tenis",
        "Promociones_S.. 15 anuales": 7
        } 
        print(Sucursales)
        print("\n")
        for b, z in Sucursales.items():
            print(b,z)
        print("\n")
        
    ## Proveedores
    def diccionario_proveedores_1173(self):
        print("***** PROVEEDORES ***** \n")
        Proveedores = {
        "Id_Proveedores..45852\n": "Empresa..Nike",
        "NumeroC_P..656-158-9505\n":"Email..Nike@gmail.com",
        "Foto.. *foto del proveedor*\n":"PrecioPorEncargo..50,000 MX",
        "C_Trailers.. 2 mensuales": 7
        } 
        print(Proveedores)
        print("\n")
        for b, z in Proveedores.items():
            print(b,z)
        print("\n")
        
# utilizacion del objeto
x = zapateria ()
x.diccionario_empleado_1173()
x.diccionario_calzado_1173()
x.diccionario_sucursales_1173()
x.diccionario_proveedores_1173()
