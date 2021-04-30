
import sys
import sqlite3
from sqlite3 import Error
import datetime
'''
try:
    with sqlite3.connect("DB_NEGOCIO.db") as conn:
        mi_cursor = conn.cursor()
        print("DB CREADA")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")'''




lista_totales = list()
conceptos = list()

while True:
    print("[1]. DAR DE ALTA EMPLEADO")
    print("[2]. REGISTRAR UNA VENTA")
    print("[3]. CONSULTAR VENTA POR FOLIO")
    print("[4]. CONSULTAR VENTA POR FECHA")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        try:
            while True:
                with sqlite3.connect("DB_NEGOCIO.db") as conn:
                    cursor = conn.cursor()

                    id_Empleado = int(input("Id del Empleado: "))
                    _id = {"id":id_Empleado}
                    cursor.execute("SELECT IdEmpleado FROM EMPLEADO WHERE IdEmpleado = :id",_id)
                    consulta = cursor.fetchall()
                    if consulta:
                        print("El id ingresado ya esta registrado, intenta con otro")
                        print("\n")
                    else:
                        nombre_empleado = input("Nombre: ")
                        apellido_paterno = input("Apellido paterno: ")
                        apellido_materno = input("Apellido materno: ")
                        estatus = input("Estatus del empleado (Vigente/Vacaciones/Suspsndido): ")

                        datos_empleado = {"IdEmpleado":id_Empleado,
                        "Nombre":nombre_empleado,
                        "ApellidoPaterno":apellido_paterno,
                        "ApellidoMaterno":apellido_materno,
                        "EStatus":estatus}

                        cursor.execute("INSERT INTO EMPLEADO values (:IdEmpleado,:Nombre,:ApellidoPaterno,:ApellidoMaterno,:EStatus)",datos_empleado)
                        print("\n")
                        print("---Datos procesados correctamente---")
                        print("\n")

        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

    elif opcion == 2:
        try:
            while True:
                with sqlite3.connect("DB_NEGOCIO.db") as conn:
                    cursor = conn.cursor()
                    print("\n")

                    NoVenta = int(input("No. de venta: "))
                    _NoVenta = {"IdVenta":NoVenta}
                    cursor.execute("SELECT IdVenta FROM VENTA WHERE IdVenta = :IdVenta",_NoVenta)
                    consulta = cursor.fetchall()
                    if consulta:
                        print("El No. de Venta ingresado ya existe. Intente con otro")
                    else:
                        cantArt = int(input("Ingrese la cantidad de articulos a registrar: "))
                        for cant in range (cantArt):

                            venta = {}
                            NombreArt = input("Nombre o descripcion del articulo: ")
                            venta['Articulo'] = NombreArt
                            cantVendida = int(input("Cantidad vendida: "))
                            venta['Cant. Comprada'] = cantVendida
                            precioVenta = int(input("Precio por pz: "))
                            venta['Precio Unitario'] = precioVenta
                            print("\n")

                            totalArt = precioVenta * cantVendida
                            lista_totales.append(totalArt)

                            conceptos.append(venta)

                        _concepto = str(conceptos)

                        totalVenta = sum(lista_totales)
                        fecha_venta = datetime.date.today()
                        while True:
                            with sqlite3.connect("DB_NEGOCIO.db") as conn:
                                cursor = conn.cursor()
                                empleado = int(input("Id del empleado que registra la venta: "))
                                _id = {"id":empleado}
                                cursor.execute("SELECT IdEmpleado FROM EMPLEADO WHERE IdEmpleado = :id",_id)
                                consulta = cursor.fetchall()
                                if consulta:
                                    datos_vennta = {"IdVetnta":NoVenta,
                                    "Fecha":fecha_venta,
                                    "Total":totalVenta,
                                    "IdEmpleado":empleado}

                                    datos_VentaDetalle = {"IdSeguimiento":NoVenta,
                                    "IdVetnta":NoVenta,
                                    "Concepto":_concepto,
                                    "ArtComprados":cantArt}

                                    print("\n")
                                    print("El total a pagar es de .... ${}".format(totalVenta))
                                    print("\n")

                                    cursor.execute("INSERT INTO VENTA values (:IdVetnta,:Fecha,:Total,:IdEmpleado)",datos_vennta)

                                    cursor.execute("INSERT INTO VENTA_DETALLE values (:IdSeguimiento,:IdVetnta,:Concepto,:ArtComprados)",datos_VentaDetalle)

                                    print("---Datos procesados correctamente---")
                                    print("\n")

                                    Base_De_Datos = []
                                    Ventas = []
                                    _base_venta = []

                                else:
                                    print("El ingresado no existe. Intente nuevamente")
                                    print("\n")

        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

    elif opcion == 3:
        try:
            while True:
                with sqlite3.connect("DB_NEGOCIO.db") as conn:
                    cursor = conn.cursor()

                    id_consultar = int(input("Id de la venta a consultar: "))
                    dato_consulta = {"Id":id_consultar}
                    cursor.execute("SELECT VENTA.IdVenta, VENTA.Fecha, VENTA_DETALLE.Concepto, VENTA.TotalVenta FROM VENTA INNER JOIN VENTA_DETALLE ON VENTA.IdVenta = VENTA_DETALLE.IdVenta WHERE VENTA.IdVenta = :Id",dato_consulta)
                    consulta = cursor.fetchall()
                    print("\n")

                    print("Folio de Venta\tFecha\t\tDetalle\t\t\t\t\t\t\t\t\t\tTotal")

                    if consulta:
                        for folio, fecha, concepto, total in consulta:
                            print (f"{folio}\t\t{fecha}\t{concepto}\t\t{total}")
                            print("\n")
                    else:
                        print("El Id de venta ingresado no existe. Intente nuevamente")
                        print("\n")

        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")