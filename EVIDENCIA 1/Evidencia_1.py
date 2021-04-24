import pandas as pd
import numpy as np

Base_De_Datos = {}
venta = list()
lista_ventas = list()
lista_totales = list()
_opcion = 1
switch = True


while switch:
    print("[1].Registrar una venta")
    print("[2].Consultar una venta")
    print("[3].Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        while _opcion == 1:
            if Base_De_Datos:
                NoDeVenta = len(Base_De_Datos) + 1
                print("\n")
                cant_datos = int(input("Cuanto articulos se van a registrar en la venta?: "))
                print("\n")
                for dato in range(cant_datos):
                    articulo = input("Descripcion o nombre del articulo: ")
                    cantidad  = int(input("Cantidad: " ))
                    precio = float(input("Precio x ud: "))
                    print("\n")

                    total = precio * cantidad
                    lista_totales.append(total)

                    venta = [articulo,cantidad,precio]
                    lista_ventas.append(venta)

                total_venta = sum(lista_totales)
                Base_De_Datos[NoDeVenta] = [lista_ventas]

                print("Total a pagar......... {}".format(total_venta))
                print("\n")

                _opcion = int(input("Desea agrgar otra venta? (1-SI / 2-NO): "))
                lista_totales = []
                lista_ventas = []

            else:

                NoDeVenta = 1
                print("\n")
                cant_datos = int(input("Cuanto articulos se van a registrar en la venta?: "))
                print("\n")
                for dato in range(cant_datos):
                    articulo = input("Descripcion o nombre del articulo: ")
                    cantidad  = int(input("Cantidad: " ))
                    precio = float(input("Precio x ud: "))
                    print("\n")
                    total = precio * cantidad
                    lista_totales.append(total)

                    venta = [articulo,cantidad,precio]
                    lista_ventas.append(venta)

                total_venta = sum(lista_totales)
                Base_De_Datos[NoDeVenta] = [lista_ventas]


                print("Total a pagar......... {}".format(total_venta))
                print("\n")

                _opcion = int(input("Desea agrgar otra venta? (1-SI / 2-NO): "))
                lista_totales = []
                lista_ventas = []

    elif opcion == 2:
        while True:
            ID = int(input("Ingresa el No. de venta a consultar: "))
            print("\n")
            if ID in Base_De_Datos.keys():
                _lista =Base_De_Datos[ID][0]
                df = pd.DataFrame(_lista, columns=['[Articulo/Detalle]','[Cantidad Comprado]','[Precio Unitario]'])
                print("Venta No.{}".format(ID))
                print(df)
                print("\n")
                break
            else:
                print("El No. de Venta no existe")
                print("\n")

    elif opcion == 3:
        switch = False
