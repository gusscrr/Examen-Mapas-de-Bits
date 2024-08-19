# Actividad 04, Examen de Mapas de Bits --- 19-08-24
# Gustavo Carrasco

from PIL import Image
import os

def solicitar_datos():

    nom_img = input("Ingrese el nombre de su imagen favorita (con extensión): ")

    try:
        x_inicial = int(input("Ingrese la coordenada X inicial: "))
        y_inicial = int(input("Ingrese la coordenada Y inicial: "))
        ancho = int(input("Ingrese el ancho del recorte: "))
        alto = int(input("Ingrese la altura del recorte: "))
    except ValueError:
        print("Los valores de coordenadas y dimensiones deben ser números enteros.")
        return None, None, None, None, None

    return nom_img, x_inicial, y_inicial, ancho, alto

def validar_parametros(imagen, x_inicial, y_inicial, ancho, alto):
    ancho_imagen, alto_imagen = imagen.size

    if (x_inicial < 0 or y_inicial < 0 or 
        x_inicial + ancho > ancho_imagen or 
        y_inicial + alto > alto_imagen):
        return False
    return True

def realizar_recorte(nom_img, x_inicial, y_inicial, ancho, alto):
    try:
        imagen = Image.open(nom_img)
    except FileNotFoundError:
        print(f"No se encontró la imagen: {nom_img}")
        return

    if not validar_parametros(imagen, x_inicial, y_inicial, ancho, alto):
        print("Los parámetros de recorte exceden los límites de la imagen.")
        return

    area_recorte = (x_inicial, y_inicial, x_inicial + ancho, y_inicial + alto)
    recorte = imagen.crop(area_recorte)

    carpt_recortes = "recortes"
    if not os.path.exists(carpt_recortes):
        os.makedirs(carpt_recortes)

    numero_recortes = len([nombre for nombre in os.listdir(carpt_recortes) if nombre.startswith("recorte") and nombre.endswith(".png")])

    nombre_recorte = f"recorte{numero_recortes + 1}.png"
    ruta_guardado = os.path.join(carpt_recortes, nombre_recorte)
    recorte.save(ruta_guardado)
    
    print(f"Recorte guardado como: {ruta_guardado}")

if __name__ == "__main__":
    
    nom_img, x_inicial, y_inicial, ancho, alto = solicitar_datos()

    if nom_img and x_inicial is not None:
    
        realizar_recorte(nom_img, x_inicial, y_inicial, ancho, alto)
