# Actividad 02, Examen de Mapas de Bits --- 19-08-24
# Gustavo Carrasco

from PIL import Image
import os

ruta_imagen = input("Ingresa la ruta completa de su imagen: ")

try:
    imagen = Image.open(ruta_imagen)

    imagen.show()

    nuevo_nombre = input("Ingresa el nuevo nombre para guardar la imagen (sin extensión): ")
    directorio = os.path.dirname(ruta_imagen)
    nueva_ruta = os.path.join(directorio, f"{nuevo_nombre}{os.path.splitext(ruta_imagen)[1]}")

    imagen.save(nueva_ruta)
    print(f"Su imagen a sido guardad Exitosamente: {nueva_ruta}")

except FileNotFoundError:
    print("Error: No se encontró el archivo, segun la ruta proporcionada.")
except Exception as e:
    print(f"Error: {e}")
