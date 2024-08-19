# Actividad 02, Examen de Mapas de Bits --- 19-08-24
# Gustavo Carrasco

from PIL import Image
import os

def rotar_imagen():
    ruta_imagen = input("Ingrese la ruta de su imagen favorita: ")
    angulo = float(input("Ingrese el ángulo de rotación (en grados): "))

    try:
        imagen = Image.open(ruta_imagen)
    except FileNotFoundError:
        print("No se encontró su imagen, segun la ruta especificada.")
        return

    imagen_rotada = imagen.rotate(angulo, expand=True)

    imagen_rotada.show()

    nom_arch, extension = os.path.splitext(os.path.basename(ruta_imagen))
    
    nuevo_nombre = f"{nom_arch}Rot{extension}"

    imagen_rotada.save(nuevo_nombre)
    print(f"Su nueva imagen rotada fue guardada como : {nuevo_nombre}")

rotar_imagen()
