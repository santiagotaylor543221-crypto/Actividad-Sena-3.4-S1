# Módulo de Nómina – TransCaribeCol (Actividad 3.4 SENA)

Aplicación de consola modular en Python para liquidar la nómina de **Transportes del Gran Caribe Colombiano S.C.A. (TransCaribeCol)**. Permite calcular liquidaciones para personal administrativo y operativo, imprimir volantes de pago en pantalla, consultar registros almacenados en memoria (`nomina_db`) y exportar o leer los datos desde el archivo plano `registros_nomina.txt`.

---

## Requisitos y ejecución

- **Python:** 3.x
- **Dependencias:** Ninguna externa (solo utiliza el módulo estándar `os`).

Para iniciar la aplicación desde la carpeta del proyecto:

```bash
python main.py
```

---

## Arquitectura modular

```text
3.4-s1/
├── main.py                # Orquestador del menú principal
├── menu.py                # Interfaz de consola, volantes y tabla en memoria
├── calculos.py            # Validación de entradas y cálculos de nómina
├── archivo.py             # Persistencia y lectura en texto plano
└── registros_nomina.txt   # Archivo generado al guardar los registros
```

| Módulo | Responsabilidad única |
| :--- | :--- |
| `main.py` | Inicializa la lista en memoria `nomina_db`, muestra el menú y delega cada opción al módulo correspondiente. |
| `menu.py` | Imprime el menú principal, el volante de pago individual y la tabla de registros en memoria. |
| `calculos.py` | Valida entradas por consola (`pedir_texto`, `pedir_entero`) y ejecuta la liquidación de administrativos y operativos. |
| `archivo.py` | Exporta los registros a `registros_nomina.txt` separados por `\|` y lee su contenido verificando su existencia. |

---

## Reglas de negocio implementadas

### 1. Personal Administrativo
- **Tarifas:** Hora ordinaria `$20.000` y hora extra `$25.000`.
- **Base de cálculo:** `salario + total_horas_extras`.
- **Descuentos de ley (sobre la base, redondeados con `round()`):**
  - Salud: `4%`
  - Pensión: `4%`
  - ARL (Riesgo I): `0.522%`
- **Totales en volante:** `Total Descuentos` suma Salud + Pensión; `Total a pagar` resta Salud + Pensión + ARL a la base.

### 2. Personal Operativo (Prestación de servicios, sin horas extras)
- **Tarifa:** `$40.000` por hora (`HE = 0`, `TPHE = 0`).
- **Base de cotización (IBC):** `40%` del salario bruto (`salario * 0.40`).
- **Descuentos de ley (sobre el IBC, redondeados con `round()`):**
  - Salud: `12.5%`
  - Pensión: `16%`
  - ARL según cargo:

| Opción | Cargo | Horas/mes | ARL |
| :---: | :--- | :---: | :---: |
| `1` | Conductor | 160 | `1.044%` (Riesgo II) |
| `2` | Oficios Generales | 100 | `0.522%` (Riesgo I) |
| `3` | Vigilancia | 336 | `4.350%` (Riesgo IV) |

- **Total a pagar:** Resta Salud + Pensión + ARL al salario bruto.

---

## Funcionalidades del menú y formato `.TXT`

| Opción | Acción | Función ejecutada |
| :---: | :--- | :--- |
| `1` | Liquidar Administrativo | `calculos.liquidar_administrativo(nomina_db)` |
| `2` | Liquidar Operativo | `calculos.liquidar_operativo(nomina_db)` |
| `3` | Ver tabla en memoria | `menu.mostrar_tabla(nomina_db)` |
| `4` | Guardar en TXT | `archivo.guardar_txt(nomina_db)` |
| `5` | Leer TXT | `archivo.leer_txt()` |
| `6` | Salir | Finaliza la ejecución |

### Formato de `registros_nomina.txt`
El archivo almacena un encabezado y una fila por empleado con 11 columnas separadas por `|`:

```text
Nombre | Tipo | Cargo | HT | Salario | HE | TPHE | Salud | Pension | ARL | Total a pagar
Ana Perez | Administrativo | Auxiliar | 160 | 3200000 | 10 | 250000 | 138000 | 138000 | 18009 | 3155991
Carlos Ruiz | Operativo | Conductor | 160 | 6400000 | 0 | 0 | 320000 | 409600 | 26726 | 5643674
```

---

## Autoría

- **Programa:** Formación Técnica en Programación de Software – SENA
- **Desarrollado por:** Santiago José Taylor Gómez
