import os
import shutil

# Define las rutas donde se moverán los diferentes tipos de archivos
# Las carpetas se crearán automáticamente en "C:\Organizador\" si no existen
ORGANIZADOR_PATH = r'C:\Organizador'
RUTA_FOTOS = os.path.join(ORGANIZADOR_PATH, 'Fotos')
RUTA_AUDIO = os.path.join(ORGANIZADOR_PATH, 'Audio')
RUTA_VIDEO = os.path.join(ORGANIZADOR_PATH, 'Videos')
RUTA_CARPETAS = os.path.join(ORGANIZADOR_PATH, 'Carpetas')
RUTA_BASES = os.path.join(ORGANIZADOR_PATH, 'Bases')
RUTA_PAQUETES = os.path.join(ORGANIZADOR_PATH, 'Paquetes')
RUTA_TEXTO = os.path.join(ORGANIZADOR_PATH, 'Texto')
RUTA_PROGRAMA = os.path.join(ORGANIZADOR_PATH, 'Programas')
RUTA_OTROS = os.path.join(ORGANIZADOR_PATH, 'Otros')

# Si no existen, crea las carpetas
os.makedirs(RUTA_FOTOS, exist_ok=True)
os.makedirs(RUTA_AUDIO, exist_ok=True)
os.makedirs(RUTA_VIDEO, exist_ok=True)
os.makedirs(RUTA_CARPETAS, exist_ok=True)
os.makedirs(RUTA_BASES, exist_ok=True)
os.makedirs(RUTA_PAQUETES, exist_ok=True)
os.makedirs(RUTA_TEXTO, exist_ok=True)
os.makedirs(RUTA_PROGRAMA, exist_ok=True)
os.makedirs(RUTA_OTROS, exist_ok=True)

# El resto del código sigue igual...
def mover_con_nombre_unico(origen, destino):
    if os.path.exists(os.path.join(destino, os.path.basename(origen))):
        base, extension = os.path.splitext(origen)
        i = 1
        while os.path.exists(os.path.join(destino, f"{os.path.basename(base)}_{i}{extension}")):
            i += 1
        os.rename(origen, os.path.join(destino, f"{os.path.basename(base)}_{i}{extension}"))
    else:
        shutil.move(origen, destino)

def clasificar_archivos(ruta):
    for root, dirs, files in os.walk(ruta):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file_path)[1]
            if extension.lower() in ['.jpg', '.png', '.jpeg', '.gif']:
                mover_con_nombre_unico(file_path, RUTA_FOTOS)
            elif extension.lower() in ['.mp3', '.wav', '.flac', '.aac','.svg']:
                mover_con_nombre_unico(file_path, RUTA_AUDIO)
            elif extension.lower() in ['.mp4', '.mkv', '.flv']:
                mover_con_nombre_unico(file_path, RUTA_VIDEO)
            elif extension.lower() in ['.txt', '.csv', '.xlsx', '.xls', '.xlsm', '.db', '.sql', '.xltx']:
                mover_con_nombre_unico(file_path, RUTA_BASES)
            elif extension.lower() in ['.docx', '.pdf', '.pptx']:
                mover_con_nombre_unico(file_path, RUTA_TEXTO)
            elif extension.lower() in ['.py','.php']:
                mover_con_nombre_unico(file_path, RUTA_PROGRAMA)
            elif extension.lower() in ['.zip', '.rar', '.msi','.exe','.gz','.html','.jar','.7z','.iso']:
                mover_con_nombre_unico(file_path, RUTA_PAQUETES)
            else:
                mover_con_nombre_unico(file_path, RUTA_OTROS)
        for dir in dirs:
            mover_con_nombre_unico(os.path.join(root, dir), RUTA_CARPETAS)

# Inicia el programa
if __name__ == "__main__":
    ruta = input(r"Por favor, introduce la ruta a clasificar: ")
    clasificar_archivos(ruta)
