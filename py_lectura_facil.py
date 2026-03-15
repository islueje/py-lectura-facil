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
# Se van revisando los n criterios y en caso de existir utilización de los mismos se van descontando puntos según una ponderación del criterio y 
# el número de ocurrencias del mismo 
# Recibe:
#   texto, String con el texto a validar 
# Se devuelve:
#   Entero con la puntuación obtenida en el rango 0..100, 0 menor LF, 100 mayor LF
#   String con las recomendaciones dictadas por cada criterio
def ValidacionLFTexto(texto):
    
    
    Criterios = [
        "UtilizacionPuntoComa",
        "UtilizacionEtcOPuntosSuspensivos"
    ]
    
    
    # Diccionario de ponderaciones de los criterios
    Ponderacion_Criterios = {
        Criterios[0]: 2,
        Criterios[1]: 5
    }


    # Se comprueba la utilización o no de un criterio en un texto
    # Recibe:
    #   criterio, String con el criterio a comprobar 
    #   texto, String con el texto a validar 
    # Se devuelve:
    #   Entero con el número de ocurrencias
    #   String con la recomendación asociada
    def Utilizacion(criterio, texto):
        
        if (criterio == Criterios[0]): # "UtilizacionPuntoComa" 6.1.7
            
            if (';' in texto):
                return texto.count(';'), "*No se debe utilizar el punto y coma (;).\n"
            else:
                return 0, "" 
            
        elif (criterio == Criterios[1]): # "UtilizacionEtcOPuntosSuspensivos" 6.1.9
            
            if ("etcétera" in texto or "etc." in texto or "..." in texto):
                ocurrencias = texto.count("etcétera") + texto.count("etc.") + texto.count("...")
                return ocurrencias, "*No se debe utilizar (etcétera) (etc.), ni los puntos suspensivos (…). Se puede sustituir por (entre otros), (y muchos más) y otras frases similares.\n"
            else:
                return 0, ""
            
        else:
            return -1, "Criterio no válido"


    # # 6.1.7
    # # Se devuelve:
    # #   XXX Booleano en función de si se utiliza (;) en el texto o no
    # #   Entero con el número de ocurrencias
    # #   String con la recomendación asociada    
    # def UtilizacionPuntoComa(texto):
        
    #     if (';' in texto):
    #         return True, texto.count(';'), "*No se debe utilizar el punto y coma (;).\n"
    #     else:
    #         return False, 0, "" 

        
    # # 6.1.9
    # # Se devuelve:
    # #   XXX Booleano en función de si se utiliza (etcétera) ó (...) en el texto o no
    # #   Entero con el número de ocurrencias
    # #   String con la recomendación asociada    
    # def UtilizacionEtcOPuntosSuspensivos(texto):
        
    #     if ("etcétera" in texto or "etc." in texto or "..." in texto):
    #         ocurrencias = texto.count("etcétera") + texto.count("etc.") + texto.count("...")
    #         return True, ocurrencias, "*No se debe utilizar (etcétera) (etc.), ni los puntos suspensivos (…). Se puede sustituir por (entre otros), (y muchos más) y otras frases similares.\n"
    #     else:
    #         return False, 0, "" 
    
    
    puntuacion = 100
    recomendaciones = ""
    
    for c in Criterios:
        ocurrencias, recomendacion = Utilizacion(c, texto)
        puntuacion = puntuacion - ocurrencias * Ponderacion_Criterios[c]
        recomendaciones = recomendaciones + recomendacion
    
    return puntuacion, recomendaciones








# Rangos de puntuación:
# 0..19 El texto NO CUMPLE CON CASI NINGUNA de las características que definen la Lectura Fácil. Rango I.
# 20..39 El texto CUMPLE CON ALGUNAS de las características que definen la Lectura Fácil. Rango II.   
# 40..59 El texto CUMPLE CON BASTANTES de las características que definen la Lectura Fácil. Rango III.
# 60..79 El texto CUMPLE CON MUCHAS de las características que definen la Lectura Fácil. Rango IV.
# 80..100 El texto CUMPLE CON CASI TODAS las características que definen la Lectura Fácil. Rango V.
# Recibe:
#   puntuacion, la devuelta por ValidacionLFTexto(texto) 
# Se devuelve:
#   String con el rango calculado
#   String con la descripción del rango    
def RangoLFPuntuacion(puntuacion):
    
    
    Rangos_Puntuacion = {
        "I": "El texto NO CUMPLE CON CASI NINGUNA de las características que definen la Lectura Fácil",
        "II": "El texto CUMPLE CON ALGUNAS de las características que definen la Lectura Fácil",
        "III": "El texto CUMPLE CON BASTANTES de las características que definen la Lectura Fácil",
        "IV": "El texto CUMPLE CON MUCHAS de las características que definen la Lectura Fácil",
        "V": "El texto CUMPLE CON CASI TODAS las características que definen la Lectura Fácil"
    }
    
    
    if (puntuacion >= 0 and puntuacion <= 19):
        return "I", Rangos_Puntuacion["I"]
    elif (puntuacion >= 20 and puntuacion <= 39):
        return "II", Rangos_Puntuacion["II"]
    elif (puntuacion >= 40 and puntuacion <= 59):
        return "III", Rangos_Puntuacion["III"]
    elif (puntuacion >= 60 and puntuacion <= 79):
        return "IV", Rangos_Puntuacion["IV"]
    elif (puntuacion >= 80 and puntuacion <= 100):
        return "V", Rangos_Puntuacion["V"]
    else:
        return "", "Puntuación LF no válida"



