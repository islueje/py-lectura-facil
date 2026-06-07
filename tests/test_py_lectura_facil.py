# -*- coding: utf-8 -*-


"""

Curso de Adaptación al Grado en Ingeniería Informática 

Trabajo de Fin de Grado 

Desarrollo de una librería Python para la validación de textos de Lectura Fácil

Iván Sánchez Lueje 

15/07/2026


Este proyecto forma parte de un trabajo de fin de estudios del Grado en Ingeniería Informática 
de la Universidad Internacional de La Rioja, UNIR.


test_py_lectura_facil.py

Pruebas unitarias del módulo py_lectura_facil.py


"""


# Pruebas incluidas:

# 
# 
# 
# 
# 
# 


# !pytest -v
# !pytest --cov=py_lectura_facil --cov-report term-missing
# módulo pytest-cov 7.1.0




import pytest # pytest-8.3.4


import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from py_lectura_facil import (
    validacion_lf_texto,
    rango_lf_texto,
)




# TESTS GENERALES


def test_texto_simple_deberia_tener_puntuacion_alta():
    texto = "Ana vive en Madrid. Ana lee libros fáciles."

    puntuacion, recomendaciones = validacion_lf_texto(texto)

    assert puntuacion == 100
    assert recomendaciones == ""


def test_puntuacion_nunca_debe_ser_negativa():
    texto = (
        "hola. esto es algo tremendísimamente complicado; "
        "etcétera... abogados/as @ usuario "
        "01/01/2025 23:59 50% 1/2 "
        "He comido. Fue realizado."
    ) * 20

    puntuacion, _ = validacion_lf_texto(texto)

    assert puntuacion == 0


def test_recomendaciones_deben_ser_string():
    texto = "Esto es algo."

    _, recomendaciones = validacion_lf_texto(texto)

    assert isinstance(recomendaciones, str)




# TESTS CRITERIOS INDIVIDUALES


@pytest.mark.parametrize(
    "texto,fragmento",
    [
        (
            "Hola. esto empieza en minúscula.",
            "mayúscula inicial"
        ),
        (
            "Texto con punto y coma;",
            "punto y coma"
        ),
        (
            "Texto con (paréntesis).",
            "paréntesis"
        ),
        (
            "Texto con etcétera...",
            "puntos suspensivos"
        ),
        (
            "electroencefalografista",
            "palabras muy largas"
        ),
        (
            "rápidamente",
            "adverbios terminados"
        ),
        (
            "buenísimo",
            "superlativos"
        ),
        (
            "Hay algo extraño.",
            "contenido indeterminado"
        ),
        (
            "Mi teléfono es 666777888",
            "teléfono"
        ),
        (
            "1.º puesto",
            "ordinales"
        ),
        (
            "El 50% aprobó",
            "fracciones y de porcentajes"
        ),
        (
            "Fecha 01/01/2025",
            "fecha con guiones o barras"
        ),
        (
            "La hora es 23:59",
            "formato 24 horas"
        ),
        (
            "He comido temprano",
            "tiempos verbales compuestos"
        ),
        (
            "Fue realizado por Ana",
            "voz pasiva"
        ),
        (
            "Estoy caminando",
            "gerundio"
        ),
        (
            "Sin embargo, seguimos",
            "conectores complejos"
        ),
        (
            "abogados/as",
            "desdoblamiento con barras"
        ),
    ]
)
def test_criterios_detectados(texto, fragmento):

    _, recomendaciones = validacion_lf_texto(texto)

    assert fragmento.lower() in recomendaciones.lower()




# TESTS FALSOS POSITIVOS


def test_demente_no_debe_detectarse_como_adverbio_mente():

    texto = "El personaje parece demente."

    puntuacion, recomendaciones = validacion_lf_texto(texto)

    assert puntuacion == 100
    assert "adverbios terminados" not in recomendaciones.lower()


def test_cuando_no_debe_detectarse_como_gerundio():

    texto = "Te aviso cuando llegue."

    puntuacion, recomendaciones = validacion_lf_texto(texto)

    assert puntuacion == 100
    assert "gerundio" not in recomendaciones.lower()




# TESTS PUNTUACIÓN


def test_punto_y_coma_resta_5_puntos():

    texto = "Texto;"

    puntuacion, _ = validacion_lf_texto(texto)

    assert puntuacion == 95


def test_dos_puntos_y_coma_restan_10_puntos():

    texto = "Uno; Dos;"

    puntuacion, _ = validacion_lf_texto(texto)

    assert puntuacion == 90


def test_varios_criterios_reducen_puntuacion():

    texto = (
        "Hola; rápidamente buenísimo "
        "01/01/2025"
    )

    puntuacion, _ = validacion_lf_texto(texto)

    assert puntuacion < 100




# TESTS RANGOS LF


@pytest.mark.parametrize(
    "puntuacion,rango",
    [
        (0, "I"),
        (19, "I"),
        (20, "II"),
        (39, "II"),
        (40, "III"),
        (59, "III"),
        (60, "IV"),
        (79, "IV"),
        (80, "V"),
        (100, "V"),
    ]
)
def test_rangos_validos(puntuacion, rango):

    resultado, descripcion = rango_lf_texto(puntuacion)

    assert resultado == rango
    assert descripcion != ""


@pytest.mark.parametrize(
    "puntuacion",
    [-1, 101, 999]
)
def test_rangos_invalidos(puntuacion):

    resultado, descripcion = rango_lf_texto(puntuacion)

    assert resultado == ""
    assert descripcion == "Puntuación no válida"




# TESTS CASOS LÍMITE


def test_texto_vacio():

    puntuacion, recomendaciones = validacion_lf_texto("")

    assert puntuacion == 100
    assert recomendaciones == ""


def test_texto_con_solo_espacios():

    puntuacion, recomendaciones = validacion_lf_texto("     ")

    assert puntuacion == 100
    assert recomendaciones == ""


def test_texto_con_multiples_ocurrencias():

    texto = "rápidamente lentamente cuidadosamente"

    puntuacion, recomendaciones = validacion_lf_texto(texto)

    assert puntuacion == 90
    assert "rápidamente" in recomendaciones.lower()


# def test_deteccion_telefonos():

#     texto = "Llama al 666777888"

#     puntuacion, recomendaciones = validacion_lf_texto(texto)

#     assert puntuacion == 99
#     assert "teléfono" in recomendaciones.lower()

    
    
    
