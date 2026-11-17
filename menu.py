def mostrar_menu():
    print("\n--- NOMINA TRANSCARIBECOL ---")
    print("1. Liquidar Administrativo")
    print("2. Liquidar Operativo")
    print("3. Ver tabla en memoria")
    print("4. Guardar en TXT")
    print("5. Leer TXT")
    print("6. Salir")


def imprimir_volante(emp):
    print("\n********************* VOLANTE DE PAGO **********************")
    print(f"Nombre: {emp['nombre']}")
    print(f"Cargo: {emp['cargo']}")
    print(f"HT: {emp['ht']}")
    print(f"Salario Bruto: ${emp['salario']:,}")
    print(f"HE: {emp['he']}")
    print(f"Total HE: ${emp['tphe']:,}")
    print("********************* DESCUENTOS DE LEY ********************")
    print(f"Salud: ${emp['salud']:,}")
    print(f"Pensión: ${emp['pension']:,}")
    print(f"ARL: ${emp['arl']:,}")
    print(f"Total Descuentos: ${emp['total_descuentos']:,}")
    print(f"Total a pagar: ${emp['total_pagar']:,}")
    print("************************************************************")


def mostrar_tabla(nomina_db):
    if not nomina_db:
        print("\nNo hay registros en memoria.")
        return

    encabezado = (
        "Nombre | Tipo | Cargo | HT | Salario | HE | TPHE | "
        "Salud | Pension | ARL | Total a pagar"
    )
    print("\n" + encabezado)
    print("-" * len(encabezado))
    for emp in nomina_db:
        fila = (
            f"{emp['nombre']} | {emp['tipo']} | {emp['cargo']} | "
            f"{emp['ht']} | {emp['salario']} | {emp['he']} | "
            f"{emp['tphe']} | {emp['salud']} | {emp['pension']} | "
            f"{emp['arl']} | {emp['total_pagar']}"
        )
        print(fila)
