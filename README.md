# Clasificador de Archivos

El Clasificador de Archivos es una herramienta sencilla para organizar automáticamente los archivos de una determinada carpeta en categorías como fotos, audio, video, documentos, programas y más. Facilita la tarea de mantener tus archivos ordenados y encontrarlos rápidamente.

## Características

- Clasificación automática: El clasificador analiza los archivos de una carpeta y los organiza en categorías específicas.
- Soporte de múltiples formatos: Puede clasificar archivos de imagen (JPG, PNG, GIF), audio (MP3, WAV, FLAC), video (MP4, MKV, FLV), documentos (TXT, CSV, XLSX, PDF), programas (PY, PHP, EXE) y más.
- Estructura de carpetas predefinida: Crea automáticamente una estructura de carpetas con categorías predefinidas para organizar los archivos.
- Personalización: Permite personalizar las rutas de las carpetas de destino para adaptarse a tus preferencias.

## Requisitos previos

- Python 3.x
- Dependencias adicionales: (ver archivo `requirements.txt` para obtener una lista completa)

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:

pip install -r requirements.txt


## Uso

1. Ejecuta el archivo `app.py` desde tu entorno de desarrollo o desde la terminal.
2. Se abrirá una interfaz de usuario donde podrás ingresar tu nombre y la ruta de la carpeta que deseas organizar.
3. Haz clic en el botón "Clasificar" para iniciar el proceso de clasificación.
4. Los archivos se moverán automáticamente a las carpetas correspondientes según su tipo.
5. Una vez finalizada la clasificación, se mostrará la hora de ejecución y se guardará un registro en el archivo `clasificador_log.txt`.

## Ejecutable para Windows

Si no deseas instalar Python y las dependencias, también puedes utilizar el archivo ejecutable `app.exe` que se encuentra en la carpeta `dist`. Simplemente ejecuta el archivo `app.exe` y sigue las instrucciones en la interfaz de usuario.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el Clasificador de Archivos, puedes realizar una bifurcación (fork) de este repositorio, hacer tus cambios y enviar una solicitud de extracción (pull request).

## Licencia

Este proyecto está bajo la [licencia Apache 2.0](LICENSE).
