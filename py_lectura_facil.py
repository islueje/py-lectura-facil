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


    

# Importación de módulos

import re # Módulo Python para el uso de expresiones regulares. 




# Este método se encarga de realizar la validación de un texto según 18 de los criterios de Lectura Fácil, LF, definidos en la norma UNE 153101:2018 EX.
# Para llevar a cabo esta validación se comprobará si el texto cumple o no con cada uno de los 18 criterios implementados.    
# Inicialmente, la validación, la puntuación de validación, parte de 100 puntos.
# Sucesivamente se van revisando los 18 criterios y en caso de existir utilización de los mismos, lo que indica que no se cumplen los criterios, 
# se van descontando puntos de validación según una ponderación del criterio y el número de ocurrencias de utilización del mismo.
#
# Este método recibe:
#   -texto, String con el texto a validar. 
#
# El método devuelve:
#   -Entero con la puntuación de validación obtenida, en el rango 0..100, 0 menor LF, 100 mayor LF.
#   -String con las recomendaciones dictadas por cada criterio no cumplido. 
#       En este String también se incluirán las ocurrencias detectadas por cada criterio no cumplido.

def validacion_lf_texto(texto):
    
    
    # Listado con los 18 criterios de Lectura Fácil a validar, definidos en la norma UNE 153101:2018 EX.
    # La utilización de lo indicado en el criterio implica el no cumplimiento del mismo.
    
    criterios = (    
        
        # 6.1.- Pautas y recomendaciones relacionadas con la ortotipografía
        "UtilizacionMinusculasInicialesDespuesPunto", # 6.1.2
        "UtilizacionPuntoComa", # 6.1.7
        "UtilizacionParentesisCorchetesOSignosOrtográficosPocoHabituales", # 6.1.8
        "UtilizacionEtceteraOPuntosSuspensivos", # 6.1.9
        
        # 6.2.- Pautas y recomendaciones relacionadas con el vocabulario y las expresiones
	    "UtilizacionPalabrasLargas", # 6.2.6
        "UtilizacionAdverbiosMente", # 6.2.7
        "UtilizacionSuperlativos", # 6.2.8
        "UtilizacionPalabrasContenidoIndeterminado", # 6.2.18
        "UtilizacionTelefonosSinBloques", # 6.2.20
        "UtilizacionCaracteresOrdinales", # 6.2.21
        "UtilizacionFraccionesOPorcentajes", # 6.2.22
        "UtilizacionFechasConGuionesOBarras", # 6.2.23
        "UtilizacionHoras24H", # 6.2.24
        
        # 6.3.- Pautas y recomendaciones relacionadas con frases y oraciones       
        "UtilizacionTiemposVerbalesCompuestos", # 6.3.3
        "UtilizacionVozPasiva", # 6.3.4
        "UtilizacionGerundio", # 6.3.8
        "UtilizacionConectoresComplejos", # 6.3.16
        
        # 6.4.- Pautas y recomendaciones relacionadas con la organización del texto y el estilo
        "UtilizacionARROBAODesdoblamientoConBarras" # 6.4.9
    )
        
    
    # Listado con las ponderaciones de los criterios. A mayor valor de ponderación mayor descuento de puntos en la validación final.
    # Para realizar esta ponderación se tiene en cuenta lo indicado en la norma UNE 153101:2018 EX para cada criterio, 
    # estableciéndose una categorización de "gravedad" según la norma indique "No se debe utilizar", "Se deben evitar", "Se debería evitar", etc.
    # Se considerará como más grave el incumplimiento de un criterio con indicación de "No se debe utilizar" 
    # y el menos grave el incumplimiento de un "Se debería evitar".
    
    ponderacion_criterios = {
        
        criterios[0]:  5, # No se debe utilizar
        criterios[1]:  5, # No se debe utilizar
        criterios[2]:  1, # Se debería evitar
        criterios[3]:  5, # No se debe utilizar
        
        criterios[4]:  1, # Se debería evitar
        criterios[5]:  3, # Se deben evitar
        criterios[6]:  3, # Se deben evitar
        criterios[7]:  1, # Se debería evitar
        criterios[8]:  1, # Se debería evitar
        criterios[9]:  1, # Se debería evitar
        criterios[10]: 1, # Se debería evitar
        criterios[11]: 1, # Se debería evitar
        criterios[12]: 1, # Se debería evitar
                
        criterios[13]: 1, # Se deberían evitar
        criterios[14]: 3, # Se debe evitar
        criterios[15]: 1, # Se debería evitar en lo posible
        criterios[16]: 1, # Se debería evitar
        
        criterios[17]: 3  # Se debe evitar
    }




    # Este método privado se encarga de comprobar la utilización o no de un criterio en un texto.
    # La utilización de lo indicado en el criterio implica el no cumplimiento del mismo.
    #
    # Este método recibe:
    #   -criterio, String con el criterio a comprobar. 
    #   -texto, String con el texto a validar. 
    #
    # El método devuelve:
    #   -Entero con el número de ocurrencias del criterio comprobado. Si el criterio comprobado se cumple se devuelve 0.
    #   -String con las recomendaciones dictadas por el criterio comprobado y que no se cumple. 
    #       En este String también se incluirán las ocurrencias detectadas para el criterio comprobado y no cumplido.
    #       Si el criterio comprobado se cumple se devuelve "".
        
    def utilizacion(criterio, texto):

        
        # "UtilizacionMinusculasInicialesDespuesPunto" 6.1.2
        if (criterio == criterios[0]): 
            
            ocurrencias = re.findall(r"\.\s*[a-záéíóúüñ]\w*\b", texto)
            
            if (len(ocurrencias) > 0):
                return len(ocurrencias), "*Se debe utilizar la mayúscula inicial al principio de un párrafo o un título, después de punto o en nombres propios. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, "" 
        
                
        # "UtilizacionPuntoComa" 6.1.7
        if (criterio == criterios[1]): 
            
            ocurrencias = re.findall(r";", texto)
            
            if (len(ocurrencias) > 0):
                return len(ocurrencias), "*No se debe utilizar el punto y coma (;). \n\t->Se han detectado " + str(len(ocurrencias)) + " ocurrencias.\n\n"
            else:
                return 0, "" 


        # "UtilizacionParentesisCorchetesOSignosOrtográficosPocoHabituales" 6.1.8
        elif (criterio == criterios[2]): 
            
            ocurrencias = re.findall(r"(\([^)]+\)|\[[^)]+\]|\%|\betc\b|\&|\/)", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar el uso de paréntesis, corchetes y signos ortográficos poco habituales (%, &, /, …, etc.). \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionEtcOPuntosSuspensivos" 6.1.9
        elif (criterio == criterios[3]): 
            
            ocurrencias = re.findall(r"(\betcétera\b|\.\.\.)", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*No se debe utilizar (etcétera), ni los puntos suspensivos (…). Se puede sustituir por (entre otros), (y muchos más) y otras frases similares. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionPalabrasLargas" 6.2.6
        elif (criterio == criterios[4]): 
            
            # Se considerarán palabras muy largas aquellas que tengan una longuitud mayor o igual a 13 letras. De acuerdo a la Real Academia Española (RAE), 
            # las palabras más largas en el idioma español tienen entre 13 y 23 letras.
            LONGITUD_MINIMA_PALABRA_LARGA = 13

            ocurrencias_palabras_largas = []
            
            palabras = re.findall(r"\b\w+\b", texto)
            for p in palabras:
                if (len(p) >= LONGITUD_MINIMA_PALABRA_LARGA):
                    ocurrencias_palabras_largas.append(p)
                    
            ocurrencias = ""
            if (len(ocurrencias_palabras_largas) > 0):
                ocurrencias = ocurrencias + str(ocurrencias_palabras_largas) + " "
            	    
            if (len(ocurrencias_palabras_largas) > 0):
                return len(ocurrencias_palabras_largas), "*Se debería evitar el uso de palabras muy largas o que contengan sílabas complejas. \n\t->\
Se han detectado las siguientes ocurrencias: " + ocurrencias + "\n\n"
            else:
                return 0, ""


        # "UtilizacionAdverbiosMente" 6.2.7    
        elif (criterio == criterios[5]): 
            
            falsos_positivos = ["demente", "DEMENTE"]
        
            ocurrencias = re.findall(r"\w+mente\b", texto, re.IGNORECASE)
            
            ocurrencias = list(set(ocurrencias) - set(falsos_positivos))
            	    
            if (len(ocurrencias) > 0):
                return len(ocurrencias), "*Se deben evitar los adverbios terminados en (–mente). \n\t->Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        #  "UtilizacionSuperlativos" 6.2.8    
        elif (criterio == criterios[6]): 
        
            ocurrencias = re.findall(r"(\w+ísimo\b|\w+ísima\b|\w+érrimo\b)", texto, re.IGNORECASE)
	    
            if (len(ocurrencias) > 0):
                return len(ocurrencias), "*Se deben evitar los superlativos. Es recomendable añadir el adverbio muy al adjetivo o al adverbio. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionPalabrasContenidoIndeterminado" 6.2.18
        elif (criterio == criterios[7]): 
            
            # cosa, algo o asunto
            ocurrencias = re.findall(r"(\bcosa\b|\balgo\b|\basunto\b)", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar el uso de palabras de contenido indeterminado como: (cosa), (algo) o (asunto). \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionTelefonosSinBloques" 6.2.20
        elif (criterio == criterios[8]): 
            
            ocurrencias = re.findall(r"\+?[1-9]\d{7,14}", texto)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Los números de teléfono se deberían separar por bloques. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionCaracteresOrdinales" 6.2.21
        elif (criterio == criterios[9]): 
            
            ocurrencias = re.findall(r"(\w+\.\º|\w+\.\ª)", texto)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar el uso de números ordinales (ej. 1.º) y sustituirlos por números cardinales (1). \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionFraccionesOPorcentajes" 6.2.22
        elif (criterio == criterios[10]): 
            
            ocurrencias = re.findall(r"(\d+/\d+|\d+%)", texto)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar el uso de fracciones y de porcentajes. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionFechasConGuionesOBarras" 6.2.23
        elif (criterio == criterios[11]): 
            
            ocurrencias = re.findall(r"(\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})", texto)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar escribir la fecha con guiones o barras. Se debería escribir la fecha completa y el nombre del día cuando aporte información adicional para la comprensión del texto. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionHoras24H" 6.2.24
        elif (criterio == criterios[12]): 
            
            ocurrencias = re.findall(r"([0-1]\d:[0-5]\d|2[0-3]:[0-5]\d)", texto)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar escribir la hora en formato 24 horas. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionTiemposVerbalesCompuestos" 6.3.3
        elif (criterio == criterios[13]): 
                    
            ocurrencias_tiempos_verbales_compuestos = re.findall(r"\b(he|has|ha|hemos|habéis|han|había|habías|habíamos|habíais|habían|hube|hubiste|hubo|hubimos|hubisteis|hubieron|habré|habrás|habrá|habremos|habréis|habrán|habría|habrías|habríamos|habríais|habrían|haya|hayas|hayamos|hayáis|hayan|hubiera|hubieras|hubiéramos|hubierais|hubieran|hubiese|hubieses|hubiésemos|hubieseis|hubiesen|hubiere|hubieres|hubiéremos|hubiereis|hubieren)\s+(\w+)(do|to|so|cho)\b", texto, re.IGNORECASE)
            	    
            if (len(ocurrencias_tiempos_verbales_compuestos) > 0):
                return len(ocurrencias_tiempos_verbales_compuestos), "*Se deberían evitar los tiempos verbales compuestos o poco frecuentes y el uso de los condicionales y subjuntivos. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias_tiempos_verbales_compuestos) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionVozPasiva" 6.3.4
        elif (criterio == criterios[14]): 
            
            ocurrencias = re.findall(r"\b(soy|eres|es|somos|sois|son|fui|fuiste|fue|fuimos|fuisteis|fueron|sido|siendo|será|serán|sería)\s+(\w+)(ado|ido|ido|ido|to|so|cho)\b", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debe evitar la voz pasiva. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionGerundio" 6.3.8
        elif (criterio == criterios[15]): 
            
            falsos_positivos = ["cuando", "CUANDO"]
            
            ocurrencias = re.findall(r"(\b\w+ando\b|\b\w+iendo\b|\b\w+yendo\b)", texto, re.IGNORECASE)
            
            ocurrencias = list(set(ocurrencias) - set(falsos_positivos))
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar en lo posible el uso de oraciones con gerundio. \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # "UtilizacionConectoresComplejos" 6.3.16
        elif (criterio == criterios[16]): 
            
            ocurrencias = re.findall(r"(\bpor lo tanto\b|\bno obstante\b|\bpor consiguiente\b|\bsin embargo\b)", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debería evitar el uso de conectores complejos entre oraciones, como (por lo tanto), (no obstante), (por consiguiente) o (sin embargo). \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        # UtilizacionARROBAODesdoblamientoConBarras"" 6.4.9
        elif (criterio == criterios[17]): 
            
            ocurrencias = re.findall(r"(\w+o/a\b|\w+os/as\b|@)", texto, re.IGNORECASE)
            
            if (len(ocurrencias) > 0):    
                return len(ocurrencias), "*Se debe evitar el uso de caracteres especiales como (@) o el desdoblamiento con barras (ej. abogados/as). \n\t->\
Se han detectado las siguientes ocurrencias: " + str(ocurrencias) + "\n\n"
            else:
                return 0, ""


        #else:
        #    return -1, "Criterio no válido"
    
    
    
    
    puntuacion = 100
    recomendaciones_ocurrencias = ""
    
    for c in criterios:
        num_ocurrencias, recomendacion_ocurrencias = utilizacion(c, texto)
        puntuacion = puntuacion - num_ocurrencias * ponderacion_criterios[c]
        recomendaciones_ocurrencias = recomendaciones_ocurrencias + recomendacion_ocurrencias
        
    if (puntuacion < 0):
        puntuacion = 0
    
    return puntuacion, recomendaciones_ocurrencias








# Este método se encarga de calcular un rango de Lectura Fácil en función de una puntuación devuelta por validacion_lf_texto(texto).
#
# Se definen los siguientes rangos de Lectura Fácil:
#   -Rango I. [0..19]. El texto NO CUMPLE CON CASI NINGUNA de las características que definen la Lectura Fácil. 
#   -Rango II. [20..39]. El texto CUMPLE CON ALGUNAS de las características que definen la Lectura Fácil.    
#   -Rango III. [40..59]. El texto CUMPLE CON BASTANTES de las características que definen la Lectura Fácil. 
#   -Rango IV. [60..79]. El texto CUMPLE CON MUCHAS de las características que definen la Lectura Fácil. 
#   -Rango V. [80..100]. El texto CUMPLE CON CASI TODAS las características que definen la Lectura Fácil. 
#
# Este método recibe:
#   -puntuacion, Entero con la puntuación devuelta por validacion_lf_texto(texto). 
#
# El método devuelve:
#   -String con el rango de Lectura Fácil calculado.
#   -String con la descripción del rango de Lectura Fácil.   
 
def rango_lf_texto(puntuacion):
    
    
    rangos_lf = {
        
        "I": "El texto NO CUMPLE CON CASI NINGUNA de las características que definen la Lectura Fácil.",
        "II": "El texto CUMPLE CON ALGUNAS de las características que definen la Lectura Fácil.",
        "III": "El texto CUMPLE CON BASTANTES de las características que definen la Lectura Fácil.",
        "IV": "El texto CUMPLE CON MUCHAS de las características que definen la Lectura Fácil.",
        "V": "El texto CUMPLE CON CASI TODAS las características que definen la Lectura Fácil."
    }
    
    
    if (puntuacion >= 0 and puntuacion <= 19):
        return "I", rangos_lf["I"]
    
    elif (puntuacion >= 20 and puntuacion <= 39):
        return "II", rangos_lf["II"]
    
    elif (puntuacion >= 40 and puntuacion <= 59):
        return "III", rangos_lf["III"]
    
    elif (puntuacion >= 60 and puntuacion <= 79):
        return "IV", rangos_lf["IV"]
    
    elif (puntuacion >= 80 and puntuacion <= 100):
        return "V", rangos_lf["V"]
    
    else:
        return "", "Puntuación no válida"



