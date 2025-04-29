import subprocess
from tkinter import messagebox
import tkinter as tk

def hacer_ping(direccion):
    try:
        # Ejecuta el ping en Windows (-n 1 envía un solo paquete)
        resultado = subprocess.run(["ping", "-n", "1", direccion], capture_output=True, text=True, timeout=5)

        # Verifica si la respuesta fue exitosa
        if "Tiempo de espera agotado" in resultado.stdout or "Host de destino inaccesible" in resultado.stdout:
            return f"❌ No se pudo alcanzar la dirección {direccion}."
        elif resultado.returncode == 0:
            return f"✅ La dirección {direccion} está accesible."
        else:
            return f"⚠️ Error desconocido al hacer ping a {direccion}."
    except Exception as e:
        return f"⚠️ Error al ejecutar el ping: {e}"

# Prueba con una dirección IP o dominio
#print(hacer_ping("10.17.20.11"))

# Crear la ventana principal
ventana = tk.Tk()
ventana.withdraw()  # Oculta la ventana principal (solo mostrará el messagebox)

# Realizar el ping
direccion = "10.17.20.11"
resultado_ping = hacer_ping(direccion)

# Mostrar el resultado en una ventana emergente
messagebox.showinfo("Resultado del Ping", resultado_ping)
