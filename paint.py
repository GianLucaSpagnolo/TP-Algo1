import gamelib
import png
import pila

PIXEL = 20    # Cantidad de pixeles que componen un casillero del lienzo. Predeterminado: 20
PADDING = 20  # Margen entre el lienzo y el borde de la ventana. Predeterminado: 20

# COLORES DEL PAINT. DATOS PARA ACOMODAR LOS COLORES INGRESADOS POR EL USUARIO.
COLOR1 = "#FFFFFF"   # Blanco
COLOR2 = "#000000"   # Negro
COLOR3 = "#FF0000"   # Rojo
COLOR4 = "#00FF00"   # Verde
COLOR5 = "#FFFF00"   # Amarillo
COLOR6 = "#0000FF"   # Azul
COLOR7 = "#FF00FF"   # Violeta
COLOR8 = "#FF9300"   # Naranja
LISTA_COLORES = [COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, COLOR8]  # COLORES PREDETERMINADOS. Cantidad predeterminada: 8

MAXIMO_COLORES_INGRESADOS = 8  # Maxima cantidad de colores ingresados por el usuario. Predeterminado: 8
CANTIDAD_COLORES_FILA = 8      # Maxima cantidad de colores por fila en la paleta. Predeterminado: 8
# ACLARACION: No se pudo encontrar la logica para que, con una cantidad de colores por fila diferente a 8, los colores ingresados por el usuario se dibujen correctamente en la paleta. (Linea 134)

# ESTRUCTURA DEL PROGRAMA  -  **NO TOCAR**  -  REALIZAR MODIFICACIONES EN CONJUNTO PARA MANTENER LA UNIFORMIDAD DEL MISMO.
ANCHO_MAXIMO_PAINT = 30
ANCHO_MINIMO_PAINT = 5
ANCHO_RECOMENDADO_PAINT = 20
ALTO_MAXIMO_PAINT = 30
ALTO_MINIMO_PAINT = 5
ALTO_RECOMENDADO_PAINT = 20

MAXIMOS_PAINT = (ANCHO_MAXIMO_PAINT, ALTO_MAXIMO_PAINT)
MINIMOS_PAINT = (ANCHO_MINIMO_PAINT, ALTO_MINIMO_PAINT)
RECOMENDADOS_PAINT = (ANCHO_RECOMENDADO_PAINT, ALTO_RECOMENDADO_PAINT)

MINIMO_ANCHO_ALTO_VENTANA = 400
MINIMO_ALTO_VENTANA_EXTRA = 215
PARTE_SUPERIOR_TEXTO_VENTANA = 30
PARTE_SUPERIOR_VENTANA = 100
BOTON_AYUDA_SUPERIOR = 30

BOTONES_ARCHIVO_LONGITUD_X = 120
BOTONES_ARCHIVO_LONGITUD_Y = 30
BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI = 30
BOTONES_ARCHIVO_DISTANCIA_Y = 20

BOTONES_COLORES_LONGITUD_X_Y = 30
BOTONES_COLORES_DISTANCIA_ENTRE_SI = 20
BOTONES_GAMA_COLORES_Y = 50
BOTONES_GAMA_COLORES_X = 210
BOTONES_GAMA_COLORES_DISTANCIA_Y = 65

BOTONES_SUPERIORES_DISTANCIA_Y = 45
BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI = 20
BOTONES_SUPERIORES_LONGITUD_X_Y = 30

MAGNITUD_AUMENTO_RESOLUCION = 10

############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def dimension_ventana(dimension_ancho, dimension_alto):
    """calcula el tamaño de la ventana, de acuerdo a la dimension del tablero de dibujo"""
    ancho_ventana = max(MINIMO_ANCHO_ALTO_VENTANA, dimension_ancho * PIXEL) + PADDING * 2
    alto_ventana = max(MINIMO_ANCHO_ALTO_VENTANA, dimension_alto * PIXEL) + MINIMO_ALTO_VENTANA_EXTRA + PADDING * 2
    return ancho_ventana, alto_ventana

def paint_nuevo(dimension_ancho, dimension_alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    imagen = []
    for x in range(dimension_alto): 
        imagen.append([])
        for _ in range(dimension_ancho):
            imagen[x].append(COLOR1)
    return imagen

def contorno_texto_botones_archivos(texto, x1, y1, x2, y2):
    """dibuja el contorno y el texto de los botones para guardar y cargar en el programa"""
    gamelib.draw_rectangle(x1, y1, x2, y2, outline="black", fill="white")
    gamelib.draw_text(texto, x2 - ((x2 - x1) // 2), y2 - ((y2 - y1) // 2), fill="black")

def vista_previa(referencia, ancho_ventana):
    """dibuja un rectangulo con texto indicando la vista previa cuando el cursor se apoya sobre un boton"""
    palabras_clave = ("Deshacer", "Rehacer", "Rellenar", "Ingresar Color")
    gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - 15, BOTONES_SUPERIORES_DISTANCIA_Y, (ancho_ventana // 2) + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 + 15, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y, outline="black", fill="#D1D4D5")
    gamelib.draw_text(palabras_clave[referencia], ancho_ventana // 2, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y // 2, fill="black")

def paint_mostrar(paint, color, relleno, referencia, colores_ingresados, cantidad_colores, ancho_tablero, alto_tablero, ancho_ventana, alto_ventana, copiar_color):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0, 0, ancho_ventana, alto_ventana, fill="gray")
    gamelib.draw_rectangle(0, 0, ancho_ventana, PARTE_SUPERIOR_TEXTO_VENTANA, outline='black', fill="#3E3E3E")
    gamelib.draw_text('AlgoPaint ++', ancho_ventana // 2, (PARTE_SUPERIOR_TEXTO_VENTANA // 2) + 1, fill="white")
    gamelib.draw_oval(ancho_ventana - BOTON_AYUDA_SUPERIOR + 3, 3, ancho_ventana - 3, BOTON_AYUDA_SUPERIOR - 3, outline="black", fill="white")
    gamelib.draw_text("?", ancho_ventana - BOTON_AYUDA_SUPERIOR // 2, BOTON_AYUDA_SUPERIOR // 2, fill="black", size="15")
    if copiar_color == True:
        gamelib.draw_oval(5, 5, 25, 25, outline="black", fill="red")
    elif copiar_color == False:
        gamelib.draw_oval(5, 5, 25, 25, outline="black", fill="#3E3E3E")
    gamelib.draw_rectangle(PADDING, PARTE_SUPERIOR_VENTANA, ancho_tablero + PADDING, alto_tablero + PARTE_SUPERIOR_VENTANA, outline="#7DDFFF", fill="#D1D4D5")

    gamelib.draw_rectangle(0, PARTE_SUPERIOR_TEXTO_VENTANA, ancho_ventana, PARTE_SUPERIOR_VENTANA - 10, fill="#D1D4D5", outline="black")
    if relleno == True: gamelib.draw_rectangle((ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - 5, BOTONES_SUPERIORES_DISTANCIA_Y - 5, (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y + 5, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y + 5, fill="#4D4D4D")
    # Deshacer
    gamelib.draw_rectangle((ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y * 2, BOTONES_SUPERIORES_DISTANCIA_Y, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y, outline="black", fill="#F4F4F4")
    gamelib.draw_polygon([(ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y * 2 + 5, BOTONES_SUPERIORES_DISTANCIA_Y + 15, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y - 5, BOTONES_SUPERIORES_DISTANCIA_Y + 5, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y - 5, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y - 5], fill="black")
    # Rehacer
    gamelib.draw_rectangle((ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - BOTONES_SUPERIORES_LONGITUD_X_Y, BOTONES_SUPERIORES_DISTANCIA_Y, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y, outline="black", fill="#F4F4F4")
    gamelib.draw_polygon([(ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - 5, BOTONES_SUPERIORES_DISTANCIA_Y + 15, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - BOTONES_SUPERIORES_LONGITUD_X_Y + 5, BOTONES_SUPERIORES_DISTANCIA_Y + 5, (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - BOTONES_SUPERIORES_LONGITUD_X_Y + 5, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y - 5], fill="black")
    # Rellenar
    gamelib.draw_rectangle((ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI, BOTONES_SUPERIORES_DISTANCIA_Y, (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y, outline="black", fill="#F4F4F4")
    gamelib.draw_oval((ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + 5, BOTONES_SUPERIORES_DISTANCIA_Y + 5, (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y - 5, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y - 5, fill='black')
    gamelib.draw_oval((ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + 10, BOTONES_SUPERIORES_DISTANCIA_Y + 10, (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y - 10, BOTONES_SUPERIORES_DISTANCIA_Y  + BOTONES_SUPERIORES_LONGITUD_X_Y - 10, fill='#F4F4F4')
    # Seleccionar Color
    gamelib.draw_rectangle((ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2, BOTONES_SUPERIORES_DISTANCIA_Y, (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y * 2, BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y, outline="black", fill="#F4F4F4")
    gamelib.draw_text("?", (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y + (BOTONES_SUPERIORES_LONGITUD_X_Y // 2) + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2, BOTONES_SUPERIORES_DISTANCIA_Y + (BOTONES_SUPERIORES_LONGITUD_X_Y // 2), fill="black", size=17)
    contorno_texto_botones_archivos("Guardar PPM", (ancho_ventana // 4) - BOTONES_ARCHIVO_LONGITUD_X + BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y, (ancho_ventana // 4) + BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y)
    contorno_texto_botones_archivos("Cargar PPM", (ancho_ventana // 2) - BOTONES_ARCHIVO_LONGITUD_X // 2, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y, (ancho_ventana // 2) + BOTONES_ARCHIVO_LONGITUD_X // 2, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y)
    contorno_texto_botones_archivos("Guardar PNG", (ancho_ventana // 2) + (ancho_ventana // 4) - BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y, (ancho_ventana // 2) + (ancho_ventana // 4) + BOTONES_ARCHIVO_LONGITUD_X - BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI, alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y)
    if referencia != -1: vista_previa(referencia, ancho_ventana)

    gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * cantidad_colores, (ancho_ventana // 2) + BOTONES_GAMA_COLORES_X, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y, fill="#D1D4D5", outline="black")
    color_seleccionado_indice = -1
    if color in LISTA_COLORES:
        color_seleccionado_indice = LISTA_COLORES.index(color)
    elif color in colores_ingresados:
        color_seleccionado_indice = colores_ingresados.index(color) + len(LISTA_COLORES)
    for i in range(1, cantidad_colores + 1):
        for indice in range(CANTIDAD_COLORES_FILA):
            if (indice + (i - 1) * CANTIDAD_COLORES_FILA) == color_seleccionado_indice and color != "" and color_seleccionado_indice != -1:
                gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * indice + 16, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * i + 6, (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * (indice + 1) + 24, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (i - 1) - 6, fill="#4D4D4D", outline="black")
            gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * indice + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * i + 10, (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * (indice + 1) + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (i - 1) - 10, fill="white")
            gamelib.draw_line((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * indice + 25, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * i + 25, (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * (indice + 1) + 15, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (i - 1) - 25, fill="gray", width="8")
            if (indice + (i - 1) * CANTIDAD_COLORES_FILA) < len(LISTA_COLORES):
                gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * indice + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * i + 10, (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * (indice + 1) + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (i - 1) - 10, fill=LISTA_COLORES[indice + (i - 1) * CANTIDAD_COLORES_FILA], outline="black")
            # nuevo_indice = indice + (len(LISTA_COLORES) - (CANTIDAD_COLORES_FILA * (i - 1)))
            if len(colores_ingresados) != 0 and (indice + (i - 1) * CANTIDAD_COLORES_FILA) >= len(LISTA_COLORES) and 0 <= (indice + (i - 1) * CANTIDAD_COLORES_FILA) - len(LISTA_COLORES) < len(colores_ingresados) and indice < CANTIDAD_COLORES_FILA:
                gamelib.draw_rectangle((ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * indice + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * i + 10, (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice + BOTONES_COLORES_LONGITUD_X_Y * (indice + 1) + 20, alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (i - 1) - 10, fill=colores_ingresados[(indice + (i - 1) * CANTIDAD_COLORES_FILA) - len(LISTA_COLORES)], outline="black")

    for y, _ in enumerate(paint):
        for x, _ in enumerate(paint[y]):
            gamelib.draw_rectangle(PADDING + PIXEL * x, PARTE_SUPERIOR_VENTANA + PIXEL * y, PADDING + PIXEL * (x + 1), PARTE_SUPERIOR_VENTANA + PIXEL * (y + 1), fill=paint[y][x], outline="black")
    gamelib.draw_end()

def pedir_dimension():
    """le pide al usuario que ingrese de que dimension quiere que sea su lienzo para dibujar"""
    cancelado = False
    alto_ancho_dibujo = ["", ""]
    texto = ("ANCHO", "ALTO")
    indice = 0
    intento = 0
    alto_ancho_dibujo[indice] = gamelib.input(f"INGRESE  EL  {texto[indice]}  DE  SU  LIENZO  PARA  DIBUJAR:\n\n{texto[indice]}  RECOMENDADO:  {RECOMENDADOS_PAINT[indice]}  /  MAXIMO  =  {MAXIMOS_PAINT[indice]}  /  MINIMO  =  {MINIMOS_PAINT[indice]}")
    while True:
        if alto_ancho_dibujo[indice] == None or cancelado == True: 
            cancelado = True
            break

        if indice == 1 and alto_ancho_dibujo[indice] == "" and cancelado == False and intento == 0:
            alto_ancho_dibujo[indice] = gamelib.input(f"INGRESE  EL  {texto[indice]}  DE  SU  LIENZO  PARA  DIBUJAR:\n\n{texto[indice]}  RECOMENDADO:  {RECOMENDADOS_PAINT[indice]}  /  MAXIMO  =  {MAXIMOS_PAINT[indice]}  /  MINIMO  =  {MINIMOS_PAINT[indice]}")
            intento += 1
        elif alto_ancho_dibujo[indice].isdigit() == False and cancelado == False: 
            alto_ancho_dibujo[indice] = gamelib.input(f"ESCRIBA  SOLO  NUMEROS  POR  FAVOR!\n\nINGRESE  EL  {texto[indice]}  DE  SU  LIENZO  PARA  DIBUJAR:\n\n{texto[indice]}  RECOMENDADO:  {RECOMENDADOS_PAINT[indice]}  /  MAXIMO  =  {MAXIMOS_PAINT[indice]}  /  MINIMO  =  {MINIMOS_PAINT[indice]}")
        elif alto_ancho_dibujo[indice].isdigit() == True and int(alto_ancho_dibujo[indice]) > MAXIMOS_PAINT[indice] or int(alto_ancho_dibujo[indice]) < MINIMOS_PAINT[indice] and cancelado == False: 
            alto_ancho_dibujo[indice] = gamelib.input(f"NUMERO  NO  VALIDO!\n\nINGRESE  EL  {texto[indice]}  DE  SU  LIENZO  PARA  DIBUJAR:\n\n{texto[indice]}  RECOMENDADO:  {RECOMENDADOS_PAINT[indice]}  /  MAXIMO  =  {MAXIMOS_PAINT[indice]}  /  MINIMO  =  {MINIMOS_PAINT[indice]}")
        elif alto_ancho_dibujo[indice].isdigit() == True and len(alto_ancho_dibujo[indice]) <= 2 and indice == 0 and cancelado == False: indice += 1
        elif alto_ancho_dibujo[indice].isdigit() == True and len(alto_ancho_dibujo[indice]) <= 2 and indice == 1 and cancelado == False: break
    return alto_ancho_dibujo[0], alto_ancho_dibujo[1], cancelado

def seleccionar_color(x, y, colores_ingresados, cantidad_colores_linea, ancho_ventana, alto_ventana, color):
    """selecciona el color el cual el usuario haya hecho un click, para comenzar a dibujar"""
    for indice_alto_paleta in range(1, cantidad_colores_linea + 1):
        for indice_largo_paleta in range(CANTIDAD_COLORES_FILA):
            if (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice_largo_paleta + BOTONES_COLORES_LONGITUD_X_Y * indice_largo_paleta + 20 <= x <= (ancho_ventana // 2) - BOTONES_GAMA_COLORES_X + BOTONES_COLORES_DISTANCIA_ENTRE_SI * indice_largo_paleta + BOTONES_COLORES_LONGITUD_X_Y * (indice_largo_paleta + 1) + 20 and \
            alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * indice_alto_paleta + 10 <= y <= alto_ventana - BOTONES_GAMA_COLORES_DISTANCIA_Y - BOTONES_GAMA_COLORES_Y * (indice_alto_paleta - 1) - 10:
                if (indice_largo_paleta + (indice_alto_paleta - 1) * CANTIDAD_COLORES_FILA) < len(LISTA_COLORES):
                    return LISTA_COLORES[indice_largo_paleta + (indice_alto_paleta - 1) * CANTIDAD_COLORES_FILA], True
                elif (indice_largo_paleta + (indice_alto_paleta - 1) * CANTIDAD_COLORES_FILA) >= len(LISTA_COLORES) and 0 <= (indice_largo_paleta + (indice_alto_paleta - 1) * CANTIDAD_COLORES_FILA) - len(LISTA_COLORES) < len(colores_ingresados):
                    return colores_ingresados[(indice_largo_paleta + (indice_alto_paleta - 1) * CANTIDAD_COLORES_FILA) - len(LISTA_COLORES)], True
    return color, False

def pintar_paint(x, y, paint, color, ancho_tablero, alto_tablero, relleno):
    """cuando que el usuario hace clicks en el lienzo, rellena cada pixel con el color seleccionado"""
    if x > PADDING and x < ancho_tablero + PADDING and y > PARTE_SUPERIOR_VENTANA and y < alto_tablero + PARTE_SUPERIOR_VENTANA and color != "" and relleno == False:
        coordenada_x, coordenada_y = pixeles_a_casillero(x, y)
        paint[coordenada_y][coordenada_x] = color
    return paint

def ingresar_color(colores_ingresados):
    """le pide al usuario un color para dibujar, y lo agrega a la lista de colores ingresados"""
    if len(colores_ingresados) < MAXIMO_COLORES_INGRESADOS:
        color_pedido_a_usuario = gamelib.input("INGRESE UN COLOR EN FORMA HEXADECIMAL!")
        color_valido = False
        while True:
            if color_pedido_a_usuario == None: 
                break
            elif len(color_pedido_a_usuario) == 7 and color_pedido_a_usuario[:1] == "#" and hexadecimal(color_pedido_a_usuario[1:]) == True:
                if color_valido == False:
                    if color_pedido_a_usuario in LISTA_COLORES or color_pedido_a_usuario in colores_ingresados:
                        gamelib.say("EL COLOR YA HA SIDO INGRESADO!")
                        break
                    elif color_pedido_a_usuario not in LISTA_COLORES and color_pedido_a_usuario not in colores_ingresados:
                        color_valido = True
                if color_valido == True:
                    colores_ingresados.append(color_pedido_a_usuario)
                    break
            elif len(color_pedido_a_usuario) != 7 or color_pedido_a_usuario[:1] != "#" or hexadecimal(color_pedido_a_usuario[1:]) == False:
                color_pedido_a_usuario = gamelib.input("INGRESE UN COLOR EN FORMA HEXADECIMAL!\n\nEL COLOR INGRESADO NO ES VALIDO!")
    else:
        gamelib.say(f"SE HA ALCANZADO EL MAXIMO DE {MAXIMO_COLORES_INGRESADOS} COLORES INGRESADOS!")
    return colores_ingresados

def pixeles_a_casillero(x, y):
    """transforma el valor de los pixeles donde se hizo click en el lienzo y devuelve los indices correspondientes al casillero del lienzo"""
    return (x - PADDING) // PIXEL, (y - PARTE_SUPERIOR_VENTANA) // PIXEL


def hexadecimal(cadena):
    """verifica si una cadena determinada esta escrita en hexadecimal"""
    digitos_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F"]
    for caracteres in cadena:
        if caracteres not in digitos_validos:
            return False
    return True

def pedir_nombre_archivo():
    """le pide al usuario el nombre de su archivo"""
    nombre_archivo = gamelib.input("INGRESE EL NOMBRE DEL ARCHIVO:")
    while True:
        if nombre_archivo == "":
            nombre_archivo = gamelib.input("EL NOMBRE NO ES VALIDO!\n\nINGRESE EL NOMBRE DEL ARCHIVO:")
        else:
            return nombre_archivo

def verificar_si_borrar():
    """le pregunta al usuario si de verdad quiere borrar todo su dibujo"""
    confirmacion = False
    respuesta = gamelib.input("¿DESEA BORRAR TODO SU DIBUJO?\n\n¡CUIDADO! SE PERDERÁ TODO SU PROGRESO\n\n¿DESEA CONTINUAR? Escribir: (si/no)")
    while True:
        if respuesta == None or respuesta == "No" or respuesta == "no" or respuesta == "NO":
            break
        elif respuesta == "Si" or respuesta == "si" or respuesta == "SI" or respuesta == "SIUUUU":
            confirmacion = True
            break
        else:
            respuesta = gamelib.input("¿DESEA BORRAR TODO SU DIBUJO?\n\n¡CUIDADO! SE PERDERÁ TODO SU PROGRESO\n\nRESPUESTA NO VALIDA!  Escribir: (si/no)")
    return confirmacion

def lista_decimal(paint, dimension_ancho, dimension_alto):
    """crea una lista identica a la utilizada en el paint, con la diferencia que cada componente representa los 3 componentes de un color en formato decimal"""
    lista = []
    for i in range(dimension_alto):
        lista.append([])
        for j in range(dimension_ancho):
            componente_1, componente_2, componente_3 = (decimal_code(paint[i][j]))
            lista[i].append(str(componente_1) + " " + str(componente_2) + " " + str(componente_3) + " ")
    return lista

def decimal_code(color):
    """transforma un color en formato hexadecimal a decimal"""
    lista_componentes = ["", "", ""]
    for x in range(1, 4):
        lista_componentes[x - 1] += str(int(color[- 1 + 2 * x:1 + 2 * x], 16))
    return int(lista_componentes[0]), int(lista_componentes[1]), int(lista_componentes[2])

def hexadecimal_code(caracter_1, caracter_2, caracter_3):
    """transforma un color en formato decimal a hexadecimal"""
    parte_1 = f'{caracter_1:02x}'
    parte_2 = f'{caracter_2:02x}'
    parte_3 = f'{caracter_3:02x}'
    color = "#" + parte_1 + parte_2 + parte_3
    return color

def paint_guardar_png(paint, colores_ingresados):
    """transforma la lista de listas del usuario por una cuyos colores se ven representados con numeros enteros"""
    nuevo_paint = []
    for indice_y, _ in enumerate(paint):
        nuevo_paint.append([])
        for indice_x, _ in enumerate(paint[indice_y]):
            if paint[indice_y][indice_x] in LISTA_COLORES:
                nuevo_paint[indice_y].append(LISTA_COLORES.index(paint[indice_y][indice_x]))
            elif paint[indice_y][indice_x] in colores_ingresados:
                nuevo_paint[indice_y].append(colores_ingresados.index(paint[indice_y][indice_x]) + len(LISTA_COLORES))
    return nuevo_paint

def incrementar_resolucion(paint):
    """incrementa la resolucion de la imagen a guardar, para obtener una mayor resolucion"""
    paint_a_guardar = []
    for numero_fila_chica, _ in enumerate(paint):
        fila_a_guardar = []
        for numero_columna_chica, _ in enumerate(paint[numero_fila_chica]):
            for _ in range(MAGNITUD_AUMENTO_RESOLUCION):
                fila_a_guardar.append(paint[numero_fila_chica][numero_columna_chica])
        for _ in range(MAGNITUD_AUMENTO_RESOLUCION):
            paint_a_guardar.append(fila_a_guardar)
    return paint_a_guardar


def guardar_ppm(paint, dimension_ancho, dimension_alto):
    """transforma la lista de listas del paint del usuario con colores en formato decimal, para escribir y guardar un archivo .PPM"""
    nombre_archivo = pedir_nombre_archivo()
    if nombre_archivo:
        with open(nombre_archivo + ".ppm", mode="w") as archivo:
            archivo.write("P3\n" + str(dimension_ancho) + " " + str(dimension_alto) + "\n255\n")
            nuevo_paint = lista_decimal(paint, dimension_ancho, dimension_alto)
            for numero_fila, _ in enumerate(nuevo_paint):
                for numero_columna, _ in enumerate(nuevo_paint[numero_fila]):
                    archivo.write(nuevo_paint[numero_fila][numero_columna])
                archivo.write("\n")

def cargar_ppm():
    """
    Lee el archivo .PPM cuyo nombre el usuario ingresa, para pasar toda la informacion al paint y poder seguir editandolo.
    ACLARACION: Los colores del archivo en formato decimal no pueden estar separados por mas de un espacio entre si.
    Aquel formato no es aceptado por la lectura del archivo y, por ende, no es compatible para editar.
    El programa admite el ingreso de archivos externos, pero unicamente aquellos creados en este mismo programa tienen garantia de ser compatibles.
    """
    habilitado = False
    nuevo_paint = []
    nueva_dimension_ancho = 0
    nueva_dimension_alto = 0

    nombre_archivo = pedir_nombre_archivo()
    if not nombre_archivo:
        return nuevo_paint, nueva_dimension_ancho, nueva_dimension_alto, habilitado
    try:
        with open(nombre_archivo + ".ppm", mode="r") as archivo:
            lectura = False
            for numero_linea, lineas in enumerate(archivo):
                if numero_linea == 0:
                    if lineas.rstrip("\n") == "P3":
                        lectura = True
                    else:
                        break

                if numero_linea == 1 and lectura == True:
                    if len(lineas.rstrip("\n")) < 3 or len(lineas.rstrip("\n")) > 5:
                        lectura = False
                        break
                    lista_dimensiones = lineas.rstrip("\n").split(" ")
                    nueva_dimension_ancho = int(lista_dimensiones[0])
                    nueva_dimension_alto = int(lista_dimensiones[1])

                if numero_linea == 2 and lectura == True:
                    if lineas.rstrip("\n") == "255":
                        continue
                    else:
                        lectura = False
                        break

                if numero_linea >= 3 and lectura == True:
                    nuevo_paint.append([])
                    linea_colores = lineas.rstrip("\n").split(" ")
                    if lectura == True:
                        try:
                            for indice_x in range(nueva_dimension_ancho):
                                lista_caracteres = ["", "", ""]
                                for indice_colores_decimales in range(3):
                                    lista_caracteres[indice_colores_decimales] = linea_colores[3 * indice_x + indice_colores_decimales]
                                try:
                                    nuevo_paint[numero_linea - 3].append(hexadecimal_code(int(lista_caracteres[0]), int(lista_caracteres[1]), int(lista_caracteres[2])))
                                except ValueError:
                                    lectura = False
                                    break
                        except IndexError or TypeError:
                            lectura = False

                habilitado = True
            if lectura == True:
                if numero_linea >= nueva_dimension_alto + 3 or len(nuevo_paint) != nueva_dimension_alto or len(nuevo_paint[0]) != nueva_dimension_ancho:
                    lectura = False
            if lectura == False: 
                gamelib.say("EL ARCHIVO NO ES COMPATIBLE")
                habilitado = False
            elif ANCHO_MAXIMO_PAINT < nueva_dimension_ancho or ANCHO_MINIMO_PAINT > nueva_dimension_ancho or ALTO_MAXIMO_PAINT < nueva_dimension_alto or ALTO_MINIMO_PAINT > nueva_dimension_alto:
                gamelib.say(f"LAS DIMENSIONES DEL ARCHIVO NO SON COMPATIBLES!\n\nANCHO MAXIMO = {ANCHO_MAXIMO_PAINT}  /  ANCHO MINIMO = {ANCHO_MINIMO_PAINT}\nALTO MAXIMO = {ALTO_MAXIMO_PAINT}  /  ALTO MINIMO = {ALTO_MINIMO_PAINT}")
                habilitado = False
    except FileNotFoundError: gamelib.say("""EL ARCHIVO INGRESADO NO EXISTE\n(NO HACE FALTA ESCRIBIR EL .PPM)""")
    return nuevo_paint, nueva_dimension_ancho, nueva_dimension_alto, habilitado

def guardar_png(paint, colores_ingresados):
    """transforma la lista de listas del paint del usuario con la funcion paint_guardar_png(), y la escribe y guarda en un archivo .PNG junto a una paleta de colores"""
    nombre_archivo = pedir_nombre_archivo()
    if nombre_archivo:
        nombre_archivo += ".png"
        paleta = []
        for indice_colores_predeterminados, _ in enumerate(LISTA_COLORES):
            componente_1, componente_2, componente_3 = decimal_code(LISTA_COLORES[indice_colores_predeterminados])
            color_predeterminado_decimal = (componente_1, componente_2, componente_3)
            paleta.append(color_predeterminado_decimal)
        for indice_colores_ingresado, _ in enumerate(colores_ingresados):
            c_1, c_2, c_3 = decimal_code(colores_ingresados[indice_colores_ingresado])
            color_ingresado_decimal = (c_1, c_2, c_3)
            paleta.append(color_ingresado_decimal)
        png.escribir(nombre_archivo, paleta, incrementar_resolucion(paint_guardar_png(paint, colores_ingresados)))

def rellenar_paint(x, y, paint, color, dimension_ancho, dimension_alto):
    """wrapper que llama a la funcion recursiva "_rellenar_paint()" que utiliza la funcion de balde de pintura para rellenar en el lugar que el usuario haya seleccionado"""
    return _rellenar_paint(x, y, paint, color, paint[y][x], dimension_ancho, dimension_alto)

def _rellenar_paint(x, y, paint, color_a_poner, color_a_sacar, dimension_ancho, dimension_alto):
    """funcion recursiva que identifica los pixeles de un mismo color, y les asigna el color seleccionado, aplicando asi la funcion de balde de pintura"""
    if x < 0 or x >= dimension_ancho or y < 0 or y >= dimension_alto:
        return paint
    if paint[y][x] != color_a_sacar:
        return paint
    
    paint[y][x] = color_a_poner
    paint = _rellenar_paint(x + 1, y, paint, color_a_poner, color_a_sacar, dimension_ancho, dimension_alto)
    paint = _rellenar_paint(x, y + 1, paint, color_a_poner, color_a_sacar, dimension_ancho, dimension_alto)
    paint = _rellenar_paint(x - 1, y, paint, color_a_poner, color_a_sacar, dimension_ancho, dimension_alto)
    paint = _rellenar_paint(x, y - 1, paint, color_a_poner, color_a_sacar, dimension_ancho, dimension_alto)
    return paint


def copiar_color_a_paleta(paint, x, y, colores_ingresados, ancho_tablero, alto_tablero):
    """despues de que el usuario haya cargado un archivo, copia el color de un pixel especifico el cual el usuario hizo click, y lo agrega a la paleta de colores"""
    if x > PADDING and x < ancho_tablero + PADDING and y > PARTE_SUPERIOR_VENTANA and y < alto_tablero + PARTE_SUPERIOR_VENTANA:
        coordenada_x, coordenada_y = pixeles_a_casillero(x, y)
        color_a_agregar = paint[coordenada_y][coordenada_x]
        if len(colores_ingresados) >= MAXIMO_COLORES_INGRESADOS:
            gamelib.say(f"SE HA ALCANZADO EL MAXIMO DE {MAXIMO_COLORES_INGRESADOS} COLORES INGRESADOS!")
            return colores_ingresados
        if color_a_agregar in LISTA_COLORES or color_a_agregar in colores_ingresados:
            gamelib.say("EL COLOR SELECCIONADO YA ESTA EN LA PALETA!")
            return colores_ingresados
        elif color_a_agregar not in LISTA_COLORES and color_a_agregar not in colores_ingresados:
            colores_ingresados.append(color_a_agregar)
    return colores_ingresados

def referencia_vista_previa(x, y, ancho_ventana, alto_ventana):
    """recibe la posicion donde el usuario apoya su cursor, y de ser sobre uno de los botones superiores permite que se escriba una vista previa de lo que hace el boton"""
    referencia_mouse = -1
    if (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y >= x >= (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y * 2 and BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y >= y >= BOTONES_SUPERIORES_DISTANCIA_Y:
        referencia_mouse = 0
    elif (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI >= x >= (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - BOTONES_SUPERIORES_LONGITUD_X_Y and BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y >= y >= BOTONES_SUPERIORES_DISTANCIA_Y:
        referencia_mouse = 1
    elif (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y >= x >= (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI and BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y >= y >= BOTONES_SUPERIORES_DISTANCIA_Y:
        referencia_mouse = 2
    elif (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y * 2 >= x >= (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y and BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y >= y >= BOTONES_SUPERIORES_DISTANCIA_Y:
        referencia_mouse = 3
    return referencia_mouse

def deshacer(p_d, p_r, paint, modificaciones):
    """deshace la ultima accion realizada por el usuario, que haya modificado su dibujo, y devuelve el paint como se encontraba antes"""
    if modificaciones == 0:
        gamelib.say("NO SE PUEDE DESHACER MAS")
    elif modificaciones > 0:
        p_r.apilar(p_d.desapilar())
        paint = [[columnas for columnas in fila] for fila in p_d.ver_tope()]
        modificaciones -= 1
    return paint, modificaciones

def rehacer(p_d, p_r, paint, modificaciones):
    """deshace la ultima accion deshecha por el usuario, rehaciendo su ultimo trazo y devuelve el paint como se encontraba en ese momento"""
    if not p_r.esta_vacia():
        p_d.apilar(p_r.desapilar())
        paint = [[columnas for columnas in fila] for fila in p_d.ver_tope()]
        modificaciones += 1
    else:
        gamelib.say("NO SE PUEDE REHACER MAS")
    return paint, modificaciones

def vaciar_pila(pila):
    """al cargar un archivo, o al modificar el dibujo despues de deshacer, vacia la pila utilizada para la modificacion del archivo"""
    while True:
        if pila.esta_vacia():
            break
        pila.desapilar()
    return

############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def main():
    gamelib.title("AlgoPaint ++")

    # DIMENSION: Cantidad de casilleros que componen la grilla del lienzo
    dimension_ancho, dimension_alto, cancelado = pedir_dimension()
    if cancelado == True:
        return
    dimension_ancho = int(dimension_ancho)
    dimension_alto = int(dimension_alto)
    ancho_inicial, alto_inicial = dimension_ventana(dimension_ancho, dimension_alto)
    gamelib.resize(ancho_inicial, alto_inicial)
    paint = paint_nuevo(dimension_ancho, dimension_alto)

    color = ""
    color_seleccionado = False
    colores_ingresados = []
    cantidad_colores_linea = 0
    referencia_mouse = -1
    modificaciones = 0

    relleno = False
    p_d = pila.Pila()
    p_r = pila.Pila()
    click = False
    copiar_color = False
    comenzar_dibujar = False
    no_habilitado_para_guardar = False
    while gamelib.is_alive():
        # VENTANA: Tamaño (cantidad de pixeles) de la ventana del programa
        ancho_ventana, alto_ventana = dimension_ventana(dimension_ancho, dimension_alto)
        # TABLERO: Tamaño (cantidad de pixeles) del lienzo para dibujar
        ancho_tablero = PIXEL * dimension_ancho
        alto_tablero = PIXEL * dimension_alto

        if (len(LISTA_COLORES) + len(colores_ingresados)) % CANTIDAD_COLORES_FILA == 0 and len(LISTA_COLORES) + len(colores_ingresados) != 0:
            cantidad_colores_linea = (len(LISTA_COLORES) + len(colores_ingresados)) // CANTIDAD_COLORES_FILA
        elif (len(LISTA_COLORES) + len(colores_ingresados)) % CANTIDAD_COLORES_FILA != 0 or len(LISTA_COLORES) + len(colores_ingresados) == 0:
            cantidad_colores_linea = (len(LISTA_COLORES) + len(colores_ingresados)) // CANTIDAD_COLORES_FILA + 1

        alto_ventana = alto_ventana + BOTONES_GAMA_COLORES_Y * (cantidad_colores_linea - 1)
        gamelib.resize(ancho_ventana, alto_ventana)

        paint_mostrar(paint, color, relleno, referencia_mouse, colores_ingresados, cantidad_colores_linea, ancho_tablero, alto_tablero, ancho_ventana, alto_ventana, copiar_color)
        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            click = True
            x, y = ev.x, ev.y

            if copiar_color == True:
                click = False
                color = ""
                colores_ingresados = copiar_color_a_paleta(paint, x, y, colores_ingresados, ancho_tablero, alto_tablero)
                copiar_color = False
            color_elegido, color_seleccionado = seleccionar_color(x, y, colores_ingresados, cantidad_colores_linea, ancho_ventana, alto_ventana, color)
            if color_seleccionado:
                color = color_elegido
            if comenzar_dibujar == False:
                p_d.apilar([[columnas for columnas in fila] for fila in paint])
                vaciar_pila(p_r)
                comenzar_dibujar = True
            paint = pintar_paint(x, y, paint, color, ancho_tablero, alto_tablero, relleno)

            if ancho_tablero + PADDING <= x or x <= PADDING or alto_tablero + PARTE_SUPERIOR_VENTANA <= y or y <= PARTE_SUPERIOR_VENTANA: no_habilitado_para_guardar = True
            else: no_habilitado_para_guardar = False

            # Rellenar
            if x > PADDING and x < ancho_tablero + PADDING and y > PARTE_SUPERIOR_VENTANA and y < alto_tablero + PARTE_SUPERIOR_VENTANA and color != "" and relleno == True:
                coordenada_x, coordenada_y = pixeles_a_casillero(x, y)
                paint = rellenar_paint(coordenada_x, coordenada_y, paint, color, dimension_ancho, dimension_alto)
                p_d.apilar([[columnas for columnas in fila] for fila in paint])
                vaciar_pila(p_r)
                modificaciones += 1
            # Guardar PPM
            if (ancho_ventana // 4) - BOTONES_ARCHIVO_LONGITUD_X + BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI <= x <= (ancho_ventana // 4) + BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI and alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y <= y <= alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y:
                click = False
                guardar_ppm(paint, dimension_ancho, dimension_alto)
            # Cargar PPM
            if (ancho_ventana // 2) - BOTONES_ARCHIVO_LONGITUD_X // 2 <= x <= (ancho_ventana // 2) + BOTONES_ARCHIVO_LONGITUD_X // 2 and alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y <= y <= alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y:
                click = False
                nuevo_paint, nueva_dimension_ancho, nueva_dimension_alto, habilitado = cargar_ppm()
                if habilitado == True:
                    paint = nuevo_paint
                    dimension_ancho = nueva_dimension_ancho
                    dimension_alto = nueva_dimension_alto
                    modificaciones = 0
                    vaciar_pila(p_d)
                    vaciar_pila(p_r)
            # Guardar PNG
            if (ancho_ventana // 2) + (ancho_ventana // 4) - BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI <= x <= (ancho_ventana // 2) + (ancho_ventana // 4) + BOTONES_ARCHIVO_LONGITUD_X - BOTONES_ARCHIVO_DISTANCIA_ENTRE_SI and alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y - BOTONES_ARCHIVO_LONGITUD_Y <= y <= alto_ventana - BOTONES_ARCHIVO_DISTANCIA_Y:
                click = False
                guardar_png(paint, colores_ingresados)
            # Deshacer
            if (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y * 2 <= x <= (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 - BOTONES_SUPERIORES_LONGITUD_X_Y and BOTONES_SUPERIORES_DISTANCIA_Y <= y <= BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y:
                click = False
                paint, modificaciones = deshacer(p_d, p_r, paint, modificaciones)
            # Rehacer
            if (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI - BOTONES_SUPERIORES_LONGITUD_X_Y <= x <= (ancho_ventana // 3) - BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI and BOTONES_SUPERIORES_DISTANCIA_Y <= y <= BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y:
                click = False
                paint, modificaciones = rehacer(p_d, p_r, paint, modificaciones)
            # Rellenar
            if (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI <= x <= (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI + BOTONES_SUPERIORES_LONGITUD_X_Y and BOTONES_SUPERIORES_DISTANCIA_Y <= y <= BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y:
                click = False
                if relleno == False: relleno = True
                elif relleno == True: relleno = False
            # Introducir Color
            if (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 <= x <= (ancho_ventana // 3) * 2 + BOTONES_SUPERIORES_DISTANCIA_ENTRE_SI * 2 + BOTONES_SUPERIORES_LONGITUD_X_Y * 2 and BOTONES_SUPERIORES_DISTANCIA_Y <= y <= BOTONES_SUPERIORES_DISTANCIA_Y + BOTONES_SUPERIORES_LONGITUD_X_Y:
                click = False
                colores_ingresados = ingresar_color(colores_ingresados)
            # Ayuda
            if ancho_ventana - BOTON_AYUDA_SUPERIOR + 3 <= x <= ancho_ventana - 3 and 3 <= y <= BOTON_AYUDA_SUPERIOR - 3:
                gamelib.say("""COMANDOS ESPECIALES VERSION 2.0:\n\n1- PARA SELECCIONAR UN COLOR DEL DIBUJO CARGADO,\nPRESIONAR "C" Y HACER CLICK EN EL LIENZO.\n\n2- PARA BORRAR TODO EL DIBUJO, PRESIONAR "B" Y CONFIRMAR.\n""")

        elif click == True and ev.type == gamelib.EventType.Motion and relleno == False:
            x, y = ev.x, ev.y
            if ancho_tablero + PADDING > x > PADDING and alto_tablero + PARTE_SUPERIOR_VENTANA > y > PARTE_SUPERIOR_VENTANA and color != "":
                paint = pintar_paint(x, y, paint, color, ancho_tablero, alto_tablero, relleno)
            else:
                click = False
                if no_habilitado_para_guardar == False:
                    p_d.apilar([[columnas for columnas in fila] for fila in paint])
                    vaciar_pila(p_r)
                    modificaciones += 1
        elif click == True and ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            click = False
            x, y = ev.x, ev.y
            if ancho_tablero + PADDING > x > PADDING and alto_tablero + PARTE_SUPERIOR_VENTANA > y > PARTE_SUPERIOR_VENTANA and color != "" and relleno == False:
                p_d.apilar([[columnas for columnas in fila] for fila in paint])
                vaciar_pila(p_r)
                modificaciones += 1

        if ev.type == gamelib.EventType.Motion:
            x, y = ev.x, ev.y
            referencia_mouse = referencia_vista_previa(x, y, ancho_ventana, alto_ventana)

        if ev.type == gamelib.EventType.KeyPress:
            tecla = ev.key
            if str(tecla) == "B" or str(tecla) == "b":
                if verificar_si_borrar() == True:
                    paint = paint_nuevo(dimension_ancho, dimension_alto)
            elif str(tecla) == "C" or str(tecla) == "c":
                if copiar_color == False: copiar_color = True
                elif copiar_color == True: copiar_color = False
gamelib.init(main)