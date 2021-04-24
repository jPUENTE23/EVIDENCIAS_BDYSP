import os
import csv
import datetime
import pandas as pd


Ventas = list()
_base_venta = list()
lista_ventas = list()
lista_totales = list()
_opcion = 1
switch = True
nombre_archivo = 'base_De_datos.csv'

while switch:
    # Creamos un menu que se mostrara hasta que el usurio desida salir
    print("[1].Registrar una venta")
    print("[2].Consultar una venta")
    print("[3].Obtener un reporte de ventas para una fecha en específico")
    print("[4].Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        # si el archivo .csv con elnombre "base_De_datos.csv" existe, se ejecutaran las siguientes lineas de codigo
        # de lo contrario, brincara hasta la linea 61 para ejecutarse
        if bool(os.path.isfile(nombre_archivo)) == True:
            NoVenta = int(input("No. de venta: "))
            cantArt = int(input("Ingrese la cantidad de articulos a registrar: "))
            # iniciara el siguiente ciclo deacuerdo a la cantidad de articulo comprados
            for cantidad in range(cantArt):

                # iniciamos un diccionario para ir guardando los detalles del articulo
                venta = {}

                # Commo detalles del articulo, registraremos el Nombre, Cantidad vendida,
                # Y el precio de venta por pieza
                NombreArt = input("Nombre o descripcion del articulo: ")
                venta['Articulo'] = NombreArt
                cantVendida = int(input("Cantidad vendida: "))
                venta['Cant. Comprada'] = cantVendida
                precioVenta = float(input("Precio por pz: "))
                venta['Precio Unitario'] = precioVenta

                # las siguientes dos lineaa de codigo lo que haran es...
                # Calcular el precio por pieza, por la cantidad comprada
                # La lista_totales almacenara el total de cada articulo comprado
                totalArt = precioVenta * cantVendida
                lista_totales.append(totalArt)

                _base_venta.append(venta)

            # Obtenemos el total que el cliente tendra que pagar por su compra
            totalVenta = sum(lista_totales)
            # Capturamos la fecha en que se registro la venta
            fecha_venta = datetime.date.today()
            Base_De_Datos = [NoVenta,fecha_venta,_base_venta,totalVenta]
            Ventas.append(Base_De_Datos)
            print("\n")
            print("El total a pagar es de .... ${}".format(totalVenta))
            print("\n")

            # Registramos nuestra venta en un archivo con fromato .csv 
            # Que la utilizaremos como nuetrsa vase de datos
            with open (nombre_archivo,'a+',newline='') as archivo:
                registros = csv.writer(archivo)
                registros.writerows(Ventas)

            # Limpiaremos todas nuestras listas que usamos anteriormente
            # Para que al momento de que el usuario quiera registrar otra venta
            # No se agrupen con los anteriores
            Base_De_Datos = []
            Ventas = []
            _base_venta = []

        else:

            # Las siguientes lineas de codigo se ejecutaron solo si no se cumplio con...
            # nuestra condicion anyerior
            # Cabe recalcar que esta parte del codigo solo se ejecutara una vez, ya que...
            # una vez que se cree el archivo, se cumplira con la condicion anterior
            NoVenta = int(input("No. de venta: "))
            cantArt = int(input("Ingrese la cantidad de articulos a registrar: "))
            for cantidad in range(cantArt):
                venta = {}
                NombreArt = input("Nombre o descripcion del articulo: ")
                venta['Articulo'] = NombreArt
                cantVendida = int(input("Cantidad vendida: "))
                venta['Cant. Comprada'] = cantVendida
                precioVenta = float(input("Precio por pz: "))
                venta['Precio Unitario'] = precioVenta

                totalArt = precioVenta * cantVendida
                lista_totales.append(totalArt)

                _base_venta.append(venta)

            totalVenta = sum(lista_totales)
            fecha_venta = datetime.date.today()
            Base_De_Datos = [NoVenta,fecha_venta,_base_venta,totalVenta]
            Ventas.append(Base_De_Datos)
            print("\n")
            print("El total a pagar es de .... ${}".format(totalVenta))
            print("\n")

            columnas = ('Folio de Venta','FechaVenta','Detalles/Conceptos','Total pagado')
            with open (nombre_archivo,'w',newline='') as archivo:
                registros = csv.writer(archivo)
                registros.writerow(columnas)
                registros.writerows(Ventas)

            Base_De_Datos = []
            Ventas = []
            _base_venta = []

    elif opcion == 2:
        # para obtener los datos de nuestro archivo csv trabajaremos con pandas
        data = pd.read_csv(nombre_archivo)
        # Convertimos nuestro csv en un dataframe
        consulta = pd.DataFrame(data)
        # Pedimos al usuario el id de venta que desea consultar
        folio_buscar = int(input("Folio o No. de venta a buscar: "))
        print("\n")
        print("Folio de Venta\tFecha\t\tDetalle")

        # El siguiente ciclo lo que hara es que iterara cada linea de nuestro dataframe...
        # y nos devolvera los valores de la columna que le mandemos a llamar
        for i in consulta.index:

            # Si nuestra condicion cumple con el folio que el usuario desea buscar...
            # nos mostara los detalles de la venta que esta ligado con el id de venta solicitado
            if consulta['Folio de Venta'][i] == folio_buscar:

                # Convertimos los valores de nuestra consulta, para que sea mas facil...
                # imprimirlos en pantalla
                _folio = consulta['Folio de Venta'][i]
                _fecha = consulta['FechaVenta'][i]
                _detalle = consulta['Detalles/Conceptos'][i]
                print (f"{_folio}\t\t{_fecha}\t{_detalle}")
                print("\n")
        else:

            # Si el id que ingreso el usuario no existe en nuestra base de...
            # registros, mostraremos el siguiente mensaje
            print("El id o folio de venta ingresado, no existe en los registros")

    elif opcion == 3:
        # La siguiente consulta hace practicamente lo mismo que la anterior...
        # solo que en este caso, el usuario solicitara ver una venta  o mas mediente...
        # una fecha en espesifica
        data = pd.read_csv(nombre_archivo)
        consulta = pd.DataFrame(data)
        fecha_capturada = input("Ingresa la fecha a consultar (aaaa-mm-dd): ")
        print("\n")
        print("Folio de Venta\tFecha\t\tDetalle\t\t\t\t\t\t\t\t\t\t\tTotal")
        print("\n")
        for i in consulta.index:
            if consulta['FechaVenta'][i] == fecha_capturada:
                _folio = consulta['Folio de Venta'][i]
                _fecha = consulta['FechaVenta'][i]
                _detalle = consulta['Detalles/Conceptos'][i]
                _total = consulta['Total pagado'][i]
                print (f"{_folio}\t\t{_fecha}\t{_detalle}\t\t{_total}")
                print("\n")
        else:

            # si no hay una venta con la fehca que el usuario ingreso...
            # mostraremos el siguiente mensaje
            print("No existe una venta con esa fehca")
            print("\n")

    elif opcion == 4:
        break