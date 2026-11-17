import archivo
import calculos
import menu


def main():
    nomina_db = []
    while True:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            calculos.liquidar_administrativo(nomina_db)
        elif opcion == "2":
            calculos.liquidar_operativo(nomina_db)
        elif opcion == "3":
            menu.mostrar_tabla(nomina_db)
        elif opcion == "4":
            archivo.guardar_txt(nomina_db)
        elif opcion == "5":
            archivo.leer_txt()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
