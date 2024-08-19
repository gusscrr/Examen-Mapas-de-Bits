# Examen de Mapas de Bits --- 19-08-24
# Gustavo Carrasco

from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta completa de su imagen: ")

try:
    imagen = Image.open(ruta_imagen)
    imagen.show()

    nom_arch = os.path.basename(ruta_imagen)  
    nombre, extension = os.path.splitext(nom_arch) 
    resolucion = imagen.size 
    cantidad_pixel = resolucion[0] * resolucion[1]  

    print("\nInformación de la imagen:")
    print(f"Nombre: {nombre}")
    print(f"Extensión: {extension}")
    print(f"Resolución: {resolucion[0]} x {resolucion[1]}")
    print(f"Cantidad de píxeles: {cantidad_pixel}")
    print(f"Ubicación de la imagen: {ruta_imagen}")

except FileNotFoundError:
    print("Error: No se encontró el archivo, segun la ruta proporcionada.")
except Exception as e:
    print(f"Error: {e}")
