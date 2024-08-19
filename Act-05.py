# Actividad 05, Examen de Mapas de Bits --- 19-08-24
# Gustavo Carrasco

from PIL import Image
import os

def solicitar_datos():
    ruta_img = input("Ingrese la ruta de su imagen preferida: ")
    ruta_marca_agua = input("Ingrese la ruta de la imagen de la marca de agua: ")

    print("Opciones de ubicación para la marca de agua:")
    print("1. Superior izquierda")
    print("2. Superior derecha")
    print("3. Inferior izquierda")
    print("4. Inferior derecha")

    opcion = input("Esjoca una opción (1-4): ")

    ubicaciones = {
        "1": "superior izquierda",
        "2": "superior derecha",
        "3": "inferior izquierda",
        "4": "inferior derecha"
    }

    if opcion not in ubicaciones:
        print("Opción no válida. Inténtalo de nuevo.")
        return None, None, None

    return ruta_img, ruta_marca_agua, ubicaciones[opcion]

def agregar_marca_agua(ruta_img, ruta_marca_agua, ubicacion):
    try:
        imagen = Image.open(ruta_img)
        marca_agua = Image.open(ruta_marca_agua).convert("RGBA")
    except FileNotFoundError:
        print("No se encontró su imagen o la marca de agua en la ruta especificada.")
        return
    
    if marca_agua.size[0] > imagen.size[0] or marca_agua.size[1] > imagen.size[1]:
        marca_agua.thumbnail((imagen.size[0] // 3, imagen.size[1] // 3))

    margen = 50
    if ubicacion == "superior izquierda":
        posicion = (margen, margen)
    elif ubicacion == "superior derecha":
        posicion = (imagen.size[0] - marca_agua.size[0] - margen, margen)
    elif ubicacion == "inferior izquierda":
        posicion = (margen, imagen.size[1] - marca_agua.size[1] - margen)
    elif ubicacion == "inferior derecha":
        posicion = (imagen.size[0] - marca_agua.size[0] - margen, imagen.size[1] - marca_agua.size[1] - margen)

    imagen.paste(marca_agua, posicion, marca_agua)

    nombre_guardado = f"{os.path.splitext(os.path.basename(ruta_img))[0]}_marcada.png"
    imagen.save(nombre_guardado)

    print(f"Su Imagen marcada fue guardada como: {nombre_guardado}")

if __name__ == "__main__":

    ruta_img, ruta_marca_agua, ubicacion = solicitar_datos()

    if ruta_img and ruta_marca_agua and ubicacion:
        agregar_marca_agua(ruta_img, ruta_marca_agua, ubicacion)
