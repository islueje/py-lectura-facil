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




# Importación de módulos
import py_lectura_facil as lf




#texto = "En ocasiones sin embargo se escribe etcétera o ETC. con la puntuación utilizada inapropiadaMENTE. mentecato como en los siguientes ejemplos: «Los inspectores les comunicaron a los titulares de los puestos de fruta, verduras, ropa, calzado, etc ... que tendrán que instalarse más arriba» y «Asimismo se ocuparán otros espacios del recinto, como vestuarios, zonas para camerinos etc...»."
texto = " ;Ejemplo de texto con etc., etc y también podemos usar; ... o quizás Etc. (con mayúscula). To;do sigue, etcetera;;;... ; "


puntuacion, recomendaciones = lf.ValidacionLFTexto(texto)

rango, descripcion_rango = lf.RangoLFPuntuacion(puntuacion)


print("")
print("Texto:\n\n" + texto)
print("")
print("Puntuación LF: " + str(puntuacion))
print("")
print("Rango LF: " + rango + ", " + descripcion_rango)
print("")
print("Recomendaciones:\n\n" + recomendaciones)

    
    
