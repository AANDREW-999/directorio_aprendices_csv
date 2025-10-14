# 📘 Directorio de Aprendices (CSV + Pandas)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-v2.0+-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-v7.0+-009688.svg?style=for-the-badge&logo=pytest&logoColor=white)

Proyecto en **Python** que gestiona un directorio de aprendices utilizando archivos **CSV** y la librería **pandas**.

Permite **crear**, **leer** y **actualizar** registros de aprendices, implementando **buenas prácticas**, gestión de entorno virtual con **uv** y **pruebas unitarias** con **pytest**.

---

## ⚙️ Instalación

Asegúrate de tener `uv` instalado para gestionar el entorno virtual y las dependencias.

1.  **Inicializa** el entorno virtual:
    ```bash
    uv init
    ```
2.  **Instala** las dependencias necesarias (`pandas` y `pytest`):
    ```bash
    uv add pandas pytest
    ```

---

## 🚀 Uso

El módulo `directorio_aprendices_csv.py` expone las funciones principales para la gestión de datos:

```python
from directorio_aprendices_csv import crear_aprendiz, leer_aprendices, actualizar_aprendiz

# 1. Crear un nuevo registro de aprendiz
crear_aprendiz("Ana", "Gomez", "Calle 10 #5-20", "3123456789", "2567890")

# 2. Leer y mostrar todos los aprendices
print("--- Directorio Completo ---")
print(leer_aprendices())

# 3. Actualizar el número de teléfono de un aprendiz existente
actualizar_aprendiz("Ana", "Gomez", telefono="3201234567")

print("\n--- Después de la Actualización ---")
print(leer_aprendices())
```

---

## 🧪 Pruebas

Ejecuta las pruebas unitarias con:

```bash
uv run pytest -v
```

---

## 🧠 Estructura

```
directorio_aprendices_csv/
├── directorio_aprendices_csv.py
├── test/
│   └── test_directorio_aprendices_csv.py
├── pyproject.toml
└── README.md
```

---

## ✍️ Autor

Andrés Gonzalez — 2025

Proyecto educativo con uv, pandas y pytest.
