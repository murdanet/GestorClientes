import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("==========================")
        print("   Bienvenido al Gestor   ")
        print("==========================")
        print("[1] Listar los clientes   ")
        print("[2] Buscar un cliente     ")
        print("[3] Añadir un cliente    ")
        print("[4] Modificar un cliente  ")
        print("[5] Borrar un cliente    ")
        print("[6] Cerrar el gestor      ")
        print("==========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == '2':
            print("Buscando los clientes...\n")
            dni = helpers.leer_texto(3,3,"DNI(2 int y un char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print ("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo al clientes...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI(2 int y un char)").upper()
                if helpers.dni_valido(dni,db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2,30,"Nombre (de 2 a 30 chars )").capitalize()
            apellido = helpers.leer_texto(2,30,"Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni,nombre,apellido)
            print("Cliente añadido correctamente")


        elif opcion == '4':
            print("Modificando el cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI(2 int y un char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars )[{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars)[{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni,nombre,apellido)
                print("Cliente modificado correctamente")
            else:
                print("Cliente no encontrado.")


        elif opcion == '5':

            print("Borrando el cliente...\n")

            dni = helpers.leer_texto(3, 3, "DNI(2 int y un char)").upper()

            print("Cliente borrado correctamente." if db.Clientes.borrar(dni) else "Cliente no encontrado.")

        elif opcion == '6':
            print("Cerrando el gestor...\n")
            break

        input("\nPresiona ENTER para continuar...")


