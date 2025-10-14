import os
import pandas as pd
from directorio_aprendices_csv import crear_aprendiz, leer_aprendices, actualizar_aprendiz, CSV_FILE


def setup_function():
    """Crea un entorno limpio antes de cada prueba."""
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)


def test_crear_y_leer_aprendiz():
    crear_aprendiz("Juan", "Perez", "Calle 1", "3000000000", "12345")
    df = leer_aprendices()
    assert not df.empty
    assert df.iloc[0]["Nombre"] == "Juan"
    assert df.iloc[0]["Ficha"] == "12345"


def test_actualizar_aprendiz():
    crear_aprendiz("Maria", "Lopez", "Calle 2", "3111111111", "67890")
    actualizado = actualizar_aprendiz("Maria", "Lopez", telefono="3222222222")
    assert actualizado is True

    df = leer_aprendices()
    assert df.iloc[0]["Telefono"] == "3222222222"


def test_actualizar_inexistente():
    actualizado = actualizar_aprendiz("Pedro", "Torres", telefono="3111111111")
    assert actualizado is False
