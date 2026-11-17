import menu

CARGOS = {"1": ("Conductor", 160, 0.01044),
          "2": ("Oficios Generales", 100, 0.00522),
          "3": ("Vigilancia", 336, 0.0435)}


def pedir_texto(msg):
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Error: el campo no puede estar vacío.")


def pedir_entero(msg):
    while True:
        try:
            val = int(input(msg))
            if val >= 0:
                return val
            print("Error: ingrese un número mayor o igual a 0.")
        except ValueError:
            print("Error: ingrese un número entero válido.")


def liquidar_administrativo(nomina_db):
    nombre = pedir_texto("Nombre: ")
    cargo = pedir_texto("Cargo: ")
    ht = pedir_entero("Horas trabajadas: ")
    he = pedir_entero("Horas extras: ")
    salario, tphe = ht * 20000, he * 25000
    base = salario + tphe
    salud, pension, arl = round(base * 0.04), round(base * 0.04), round(base * 0.00522)
    emp = {"nombre": nombre, "tipo": "Administrativo", "cargo": cargo, "ht": ht,
           "salario": salario, "he": he, "tphe": tphe, "salud": salud,
           "pension": pension, "arl": arl, "total_descuentos": salud + pension,
           "total_pagar": base - (salud + pension + arl)}
    nomina_db.append(emp)
    menu.imprimir_volante(emp)


def liquidar_operativo(nomina_db):
    nombre = pedir_texto("Nombre: ")
    print("1. Conductor | 2. Oficios Generales | 3. Vigilancia")
    op = ""
    while op not in CARGOS:
        op = input("Seleccione cargo (1-3): ").strip()
    cargo, ht, tasa_arl = CARGOS[op]
    salario = ht * 40000
    ibc = salario * 0.40
    salud, pension, arl = round(ibc * 0.125), round(ibc * 0.16), round(ibc * tasa_arl)
    desc = salud + pension + arl
    emp = {"nombre": nombre, "tipo": "Operativo", "cargo": cargo, "ht": ht,
           "salario": salario, "he": 0, "tphe": 0, "salud": salud,
           "pension": pension, "arl": arl, "total_descuentos": desc,
           "total_pagar": salario - desc}
    nomina_db.append(emp)
    menu.imprimir_volante(emp)
