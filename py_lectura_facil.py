# -*- coding: utf-8 -*-


"""

Curso de Adaptación al Grado en Ingeniería Informática 

Trabajo de Fin de Grado 

Desarrollo de una librería Python para la validación de textos de Lectura Fácil

Iván Sánchez Lueje 

15/07/2026


Este proyecto forma parte de un trabajo de fin de estudios del Grado en Ingeniería Informática 
de la Universidad Internacional de La Rioja, UNIR.


py_lectura_facil.py

Módulo para la validación de textos de Lectura Fácil


"""


    
    
# Inicialmente se parte de 100 puntos
# Se van revisando las n Utilizaciones y en caso de existir se van descontando puntos según una ponderación del criterio y 
# el número de ocurrencias del mismo  
# Se devuelve:
#   Entero con la puntuación obtenida en el rango 0..100, 0 menor LF, 100 mayor LF
#   String con las recomendaciones dictadas por las Utilizaciones
def ValidacionLFTexto(texto):
    
    
    # Diccionario de Utilizaciones. Para cada una de ellas se define su ponderación a la hora de descontar puntos de valoración
    Ponderacion_Utilizaciones = {
        "UtilizacionPuntoComa": 2,
        "UtilizacionEtcOPuntosSuspensivos": 10
    }


    # 6.1.7
    # Se devuelve:
    #   Booleano en función de si se utiliza (;) en el texto o no
    #   Entero con el número de ocurrencias
    #   String con la recomendación asociada    
    def UtilizacionPuntoComa(texto):
        
        if (';' in texto):
            return True, texto.count(';'), "*No se debe utilizar el punto y coma (;).\n"
        else:
            return False, 0, "" 

        
    # 6.1.9
    # Se devuelve:
    #   Booleano en función de si se utiliza (etcétera) ó (...) en el texto o no
    #   Entero con el número de ocurrencias
    #   String con la recomendación asociada    
    def UtilizacionEtcOPuntosSuspensivos(texto):
        
        if ("etcétera" in texto or "etc." in texto or "..." in texto):
            ocurrencias = texto.count("etcétera") + texto.count("etc.") + texto.count("...")
            return True, ocurrencias, "*No se debe utilizar (etcétera) (etc.), ni los puntos suspensivos (…). Se puede sustituir por (entre otros), (y muchos más) y otras frases similares.\n"
        else:
            return False, 0, "" 
    
    
    puntuacion = 100
    recomendaciones = ""
    
    _, ocurrencias, recomendacion = UtilizacionPuntoComa(texto)
    puntuacion = puntuacion - ocurrencias * Ponderacion_Utilizaciones["UtilizacionPuntoComa"]
    recomendaciones = recomendaciones + recomendacion
    
    _, ocurrencias, recomendacion = UtilizacionEtcOPuntosSuspensivos(texto)
    puntuacion = puntuacion - ocurrencias * Ponderacion_Utilizaciones["UtilizacionEtcOPuntosSuspensivos"]
    recomendaciones = recomendaciones + recomendacion
    
    return puntuacion, recomendaciones




# Rangos de puntuación:
# 0..19
# 20..39

# 60..79
# 80..100
# def RangoLF(puntuacion):
    
    
    
    