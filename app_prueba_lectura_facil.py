# -*- coding: utf-8 -*-


"""

Curso de Adaptación al Grado en Ingeniería Informática 

Trabajo de Fin de Grado 

Desarrollo de una librería Python para la validación de textos de Lectura Fácil

Iván Sánchez Lueje 

15/07/2026


Este proyecto forma parte de un trabajo de fin de estudios del Grado en Ingeniería Informática 
de la Universidad Internacional de La Rioja, UNIR.


app_prueba_lectura_facil.py

Aplicación de prueba del módulo py_lectura_facil.py


"""




# Importación del módulo de validación de textos de Lectura Fácil.
import py_lectura_facil as lf




# Captura del texto a validar.
texto = input("\nIntroduce el texto a validar: ")


# Proceso de validación de Lectura Fácil del texto.
puntuacion, recomendaciones_ocurrencias = lf.ValidacionLFTexto(texto)


# Cálculo del rango de Lectura Fácil.
rango, descripcion_rango = lf.RangoLFTexto(puntuacion)


# Salida por pantalla de los resultados obtenidos: validación de Lectura Fácil + rango de Lectura Fácil + recomendaciones y ocurrencias encontradas, 
# en el caso de haberse detectado algún incumplimiento. 
print("\n---")
print("\nValidación LF (Puntuación): " + str(puntuacion))
print("")
print("\nRango LF: " + rango + ". " + descripcion_rango)
print("")
if (len(recomendaciones_ocurrencias) > 0): 
    print("\nRecomendaciones:\n\n" + recomendaciones_ocurrencias)
else:
    print("")



