
import sys
import sqlite3
from sqlite3 import Error
import datetime
import os


lista_totales = list()
conceptos = list()

while True:
    print("[0]. Crear Base de Datos")
    print("[1]. Dar de alta empleado")
    print("[2]. Registrar venta")
    print("[3]. Consultar venta por folio")
    print("[4]. Consultar venta por fecha")
    print("[5]. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 0:
        try:
            with sqlite3.connect("DB_NEGOCIO.db") as conn:
                cursor = conn.cursor()

                cursor.execute("CREATE TABLE EMPLEADO (IdEmpleado INTEGER PRIMARY KEY NOT NULL,Nombre TEXT NOT NULL, APaterno TEXT NOT NULL, AMaterno TEXT NOT NULL, EStatus    VARCHAR NOT NULL);")

                cursor.execute("CREATE TABLE VENTA (IdVenta INTEGER PRIMARY KEY NOT NULL,Fecha TIMESTAMP NOT NULL, TotalVenta INTEGER NOT NULL, IdEmpleado INTEGER REFERENCES EMPLEADO (IdEmpleado) NOT NULL);")

                cursor.execute("CREATE TABLE VENTA_DETALLE (IdSeguimiento INTEGER PRIMARY KEY NOT NULL, IdVenta INTEGER REFERENCES VENTA (IdVenta) NOT NULL, Concepto VARCHAR NOT NULL, ArtComprados INTEGER NOT NULL);")

                cursor.execute("INSERT INTO EMPLEADO values ('1','Jairo Manuel','Batrez','González','Vigente')")

                cursor.execute("INSERT INTO EMPLEADO values ('2','Jennifer Lizzet','Hernández', 'Serón','Vigente')")

                cursor.execute("INSERT INTO EMPLEADO values ('3','Nemesio Esaú','López', 'Del Toro','Vigente')")

                cursor.execute("INSERT INTO EMPLEADO values ('4','Sofia Blanca','Martínez', 'Galván','Vigente')")

                cursor.execute("INSERT INTO EMPLEADO values ('5','Jorge Luis','Puente','Muñiz','Vigente')")

                print("Base de datos creada exitosamente")

        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    elif opcion == 1:
        if os.path.isfile("DB_NEGOCIO.db"):
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

        else:
            print("Debe ejecutar la opcion 0 para tener acceso a este apartado")

    elif opcion == 2:
        if os.path.isfile("DB_NEGOCIO.db"):
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

                            break

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

                            break

                        else:
                            print("El ingresado no existe. Intente nuevamente")
                            print("\n")

            except Error as e:
                print (e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

        else:
            print("Debe ejecutar la opcion 0 para tener acceso a este apartado")

    elif opcion == 3:
        if os.path.isfile("DB_NEGOCIO.db"):
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

                        break

            except Error as e:
                print (e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

        else:
            print("Debe ejecutar la opcion 0 para tener acceso a este apartado")


    elif opcion == 4:
        if os.path.isfile("DB_NEGOCIO.db"):
            try:
                while True:
                    with sqlite3.connect("DB_NEGOCIO.db") as conn:
                        cursor = conn.cursor()
                        fecha_buscar = input("Ingrese la fecha de la llamdad realizada (dd/mm/aa): ")
                        _fechaprocesada = datetime.datetime.strptime(fecha_buscar, "%d/%m/%Y").date()
                        consulta_fecha = {"Fecha":_fechaprocesada}
                        cursor.execute("SELECT VENTA.IdVenta, VENTA.Fecha, VENTA_DETALLE.Concepto, VENTA.TotalVenta FROM VENTA INNER JOIN VENTA_DETALLE ON VENTA.IdVenta = VENTA_DETALLE.IdVenta WHERE  VENTA.Fecha= :Fecha",consulta_fecha)
                        consulta = cursor.fetchall()

                        print("\n")

                        print("Folio de Venta\tFecha\t\tDetalle\t\t\t\t\t\t\t\t\t\tTotal")

                        if consulta:
                            for folio, fecha, concepto, total in consulta:
                                print (f"{folio}\t\t{fecha}\t{concepto}\t\t{total}")
                                print("\n")

                        else:
                            print("No hay una venta existente con esa fecha. Intenta con otra")
                            print("\n")

                        break

            except Error as e:
                print (e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

        else:
            print("Debe ejecutar la opcion 0 para tener acceso a este apartado")

    elif opcion == 5:
        break
