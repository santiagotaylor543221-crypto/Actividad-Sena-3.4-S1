import os

ARCHIVO_TXT = "registros_nomina.txt"


def guardar_txt(nomina_db):
    if not nomina_db:
        print("\nNo hay registros para guardar.")
        return

    encabezado = (
        "Nombre | Tipo | Cargo | HT | Salario | HE | TPHE | "
        "Salud | Pension | ARL | Total a pagar\n"
    )
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as archivo:
        archivo.write(encabezado)
        for emp in nomina_db:
            fila = (
                f"{emp['nombre']} | {emp['tipo']} | {emp['cargo']} | "
                f"{emp['ht']} | {emp['salario']} | {emp['he']} | "
                f"{emp['tphe']} | {emp['salud']} | {emp['pension']} | "
                f"{emp['arl']} | {emp['total_pagar']}\n"
            )
            archivo.write(fila)
    print(f"\nRegistros guardados en {ARCHIVO_TXT}.")


def leer_txt():
    if not os.path.exists(ARCHIVO_TXT):
        print(f"\nEl archivo {ARCHIVO_TXT} no existe.")
        return

    with open(ARCHIVO_TXT, "r", encoding="utf-8") as archivo:
        print("\n" + archivo.read())
