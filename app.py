import os
import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox
from clasificador import clasificar_archivos, mover_con_nombre_unico
from datetime import datetime

class ClasificadorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Clasificador de Archivos")
        self.window.geometry("500x250")
        self.window.config(bg="#B3E5FC")

        # Crea y coloca las etiquetas y campos de entrada para el nombre del usuario y la ruta a clasificar
        tk.Label(window, text="Tu nombre:", bg="#B3E5FC").grid(row=0, column=0, sticky="e")
        self.nombre_usuario = tk.Entry(window, width=50)
        self.nombre_usuario.grid(row=0, column=1)

        tk.Label(window, text="Ruta a clasificar:", bg="#B3E5FC").grid(row=1, column=0, sticky="e")
        self.ruta_a_clasificar = tk.Entry(window, width=50)
        self.ruta_a_clasificar.grid(row=1, column=1)

        # Crea y coloca las etiquetas para la hora actual y la hora de ejecución
        self.hora_actual = tk.Label(window, text="", bg="#B3E5FC")
        self.hora_actual.grid(row=2, column=0, columnspan=2)

        self.hora_ejecucion = tk.Label(window, text="", bg="#B3E5FC")
        self.hora_ejecucion.grid(row=3, column=0, columnspan=2)

        # Crea y coloca el botón de clasificar
        self.boton_clasificar = tk.Button(window, text="Clasificar", command=self.clasificar)
        self.boton_clasificar.grid(row=4, column=0, columnspan=2)

        # Crea y coloca el botón de descargar dependencias
        self.boton_descargar_dependencias = tk.Button(window, text="Descargar dependencias", command=self.descargar_dependencias)
        self.boton_descargar_dependencias.grid(row=5, column=0, columnspan=2)

        # Actualiza la hora actual cada segundo
        self.actualizar_hora_actual()

    def actualizar_hora_actual(self):
        self.hora_actual['text'] = f"Hora actual: {datetime.now().strftime('%H:%M:%S')}"
        self.window.after(1000, self.actualizar_hora_actual)

    def clasificar(self):
        # Verifica si la ruta a clasificar existe
        if not os.path.exists(self.ruta_a_clasificar.get()):
            messagebox.showerror("Clasificador", "La ruta a clasificar no existe.")
            return

        # Crea las carpetas por defecto si no existen
        categorias = ["Fotos", "Audio", "Video", "Carpetas", "Bases", "Paquetes", "Texto", "Programas", "Otros"]
        for categoria in categorias:
            ruta_predeterminada = os.path.join("C:\\", "Organizador", categoria)
            os.makedirs(ruta_predeterminada, exist_ok=True)
            globals()[f"RUTA_{categoria.upper()}"] = ruta_predeterminada

        # Clasifica los archivos en la ruta dada y muestra la hora de ejecución
        clasificar_archivos(self.ruta_a_clasificar.get())
        self.hora_ejecucion['text'] = f"Última ejecución: {datetime.now().strftime('%H:%M:%S')}"
        messagebox.showinfo("Clasificador", f"{self.nombre_usuario.get()}, la clasificación ha terminado.")

        # Guarda la ejecución en un archivo log
        with open('clasificador_log.txt', 'a') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {self.nombre_usuario.get()} clasificó archivos en {self.ruta_a_clasificar.get()}\n")

    def descargar_dependencias(self):
        # Ejecuta el comando para descargar las dependencias desde el archivo requirements.txt
        comando = f"pip install -r requirements.txt"
        subprocess.run(comando, shell=True)

if __name__ == "__main__":
    window = tk.Tk()
    app = ClasificadorApp(window)
    window.mainloop()
