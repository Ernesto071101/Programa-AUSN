import tkinter as tk
import webbrowser
from tkinter import messagebox
import subprocess

#Funcion para hacer ping:
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


#------------------------------------------------------VÍAS------------------------------------------------------#

#Dispositivos vía 101:
def via101():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.11"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.12"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.13"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana101.withdraw()
        ventana.deiconify()
    
    ventana101 = tk.Tk()
    ventana101.title("Equipos Vía 101")
    tk.Label(ventana101, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana101, text="Cámara + PoE 101", command=incidencias).pack(pady=5)
    tk.Button(ventana101, text="Cámara OCR 101", command=ocr).pack(pady=5)
    tk.Button(ventana101, text="Reader 3M 101", command=reader).pack(pady=5)
    tk.Button(ventana101, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 102:
def via102():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.21"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.22"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.23"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana102.withdraw()
        ventana.deiconify()

    ventana102 = tk.Tk()
    ventana102.title("Equipos Vía 102")
    tk.Label(ventana102, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana102, text="Cámara + PoE 102", command=incidencias).pack(pady=5)
    tk.Button(ventana102, text="Cámara OCR 102", command=ocr).pack(pady=5)
    tk.Button(ventana102, text="Reader 3M 102", command=reader).pack(pady=5)
    tk.Button(ventana102, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 103:
def via103():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.31"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.32"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.33"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana103.withdraw()
        ventana.deiconify()

    ventana103 = tk.Tk()
    ventana103.title("Equipos Vía 102")
    tk.Label(ventana103, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana103, text="Cámara + PoE 103", command=incidencias).pack(pady=5)
    tk.Button(ventana103, text="Cámara OCR 103", command=ocr).pack(pady=5)
    tk.Button(ventana103, text="Reader 3M 103", command=reader).pack(pady=5)
    tk.Button(ventana103, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 104:
def via104():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.41"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.42"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.43"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana104.withdraw()
        ventana.deiconify()

    ventana104 = tk.Tk()
    ventana104.title("Equipos Vía 104")
    tk.Label(ventana104, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana104, text="Cámara + PoE 104", command=incidencias).pack(pady=5)
    tk.Button(ventana104, text="Cámara OCR 104", command=ocr).pack(pady=5)
    tk.Button(ventana104, text="Reader 3M 104", command=reader).pack(pady=5)
    tk.Button(ventana104, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 201:
def via201():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.51"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.52"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.33"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana201.withdraw()
        ventana.deiconify()

    ventana201 = tk.Tk()
    ventana201.title("Equipos Vía 201")
    tk.Label(ventana201, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana201, text="Cámara + PoE 201", command=incidencias).pack(pady=5)
    tk.Button(ventana201, text="Cámara OCR 201", command=ocr).pack(pady=5)
    tk.Button(ventana201, text="Reader 3M 201", command=reader).pack(pady=5)
    tk.Button(ventana201, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 202:
def via202():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.61"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.62"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.63"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana202.withdraw()
        ventana.deiconify()

    ventana202 = tk.Tk()
    ventana202.title("Equipos Vía 202")
    tk.Label(ventana202, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana202, text="Cámara + PoE 202", command=incidencias).pack(pady=5)
    tk.Button(ventana202, text="Cámara OCR 202", command=ocr).pack(pady=5)
    tk.Button(ventana202, text="Reader 3M 202", command=reader).pack(pady=5)
    tk.Button(ventana202, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 301:
def via301():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.71"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.72"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.73"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana301.withdraw()
        ventana.deiconify()

    ventana301 = tk.Tk()
    ventana301.title("Equipos Vía 301")
    tk.Label(ventana301, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana301, text="Cámara + PoE 301", command=incidencias).pack(pady=5)
    tk.Button(ventana301, text="Cámara OCR 301", command=ocr).pack(pady=5)
    tk.Button(ventana301, text="Reader 3M 301", command=reader).pack(pady=5)
    tk.Button(ventana301, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 302:
def via302():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.81"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.82"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.83"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana302.withdraw()
        ventana.deiconify()

    ventana302 = tk.Tk()
    ventana302.title("Equipos Vía 301")
    tk.Label(ventana302, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana302, text="Cámara + PoE 302", command=incidencias).pack(pady=5)
    tk.Button(ventana302, text="Cámara OCR 302", command=ocr).pack(pady=5)
    tk.Button(ventana302, text="Reader 3M 302", command=reader).pack(pady=5)
    tk.Button(ventana302, text="Regresar", command=regresar).pack(pady=5)


#Dispositivos vía 401:
def via401():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.91"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.92"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.93"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana401.withdraw()
        ventana.deiconify()

    ventana401 = tk.Tk()
    ventana401.title("Equipos Vía 401")
    tk.Label(ventana401, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana401, text="Cámara + PoE 401", command=incidencias).pack(pady=5)
    tk.Button(ventana401, text="Cámara OCR 401", command=ocr).pack(pady=5)
    tk.Button(ventana401, text="Reader 3M 401", command=reader).pack(pady=5)
    tk.Button(ventana401, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 402:
def via402():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.101"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.102"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.103"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana402.withdraw()
        ventana.deiconify()

    ventana402 = tk.Tk()
    ventana402.title("Equipos Vía 402")
    tk.Label(ventana402, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana402, text="Cámara + PoE 402", command=incidencias).pack(pady=5)
    tk.Button(ventana402, text="Cámara OCR 402", command=ocr).pack(pady=5)
    tk.Button(ventana402, text="Reader 3M 402", command=reader).pack(pady=5)
    tk.Button(ventana402, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 501:
def via501():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.131"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.132"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.133"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana501.withdraw()
        ventana.deiconify()

    ventana501 = tk.Tk()
    ventana501.title("Equipos Vía 501")
    tk.Label(ventana501, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana501, text="Cámara + PoE 501", command=incidencias).pack(pady=5)
    tk.Button(ventana501, text="Cámara OCR 501", command=ocr).pack(pady=5)
    tk.Button(ventana501, text="Reader 3M 501", command=reader).pack(pady=5)
    tk.Button(ventana501, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 502:
def via502():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.141"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.142"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.143"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana502.withdraw()
        ventana.deiconify()

    ventana502 = tk.Tk()
    ventana502.title("Equipos Vía 502")
    tk.Label(ventana502, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana502, text="Cámara + PoE 502", command=incidencias).pack(pady=5)
    tk.Button(ventana502, text="Cámara OCR 502", command=ocr).pack(pady=5)
    tk.Button(ventana502, text="Reader 3M 502", command=reader).pack(pady=5)
    tk.Button(ventana502, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 601:
def via601():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.111"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.112"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.113"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana601.withdraw()
        ventana.deiconify()

    ventana601 = tk.Tk()
    ventana601.title("Equipos Vía 601")
    tk.Label(ventana601, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana601, text="Cámara + PoE 601", command=incidencias).pack(pady=5)
    tk.Button(ventana601, text="Cámara OCR 601", command=ocr).pack(pady=5)
    tk.Button(ventana601, text="Reader 3M 601", command=reader).pack(pady=5)
    tk.Button(ventana601, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos vía 602:
def via602():
    #Camara Incidencias:
    def incidencias():
        url = "http://10.17.10.121"
        webbrowser.open(url)
    #Camara OCR:
    def ocr():
        url1 = "http://10.17.10.122"
        webbrowser.open(url1)
    #READER:
    def reader():
        url2 = "http://10.17.10.123"
        webbrowser.open(url2)
    #Menu Princial -- Quitas ventana vía 101 y rregresar ventana de menu principal:
    def regresar():
        ventana602.withdraw()
        ventana.deiconify()

    ventana602 = tk.Tk()
    ventana602.title("Equipos Vía 602")
    tk.Label(ventana602, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana602, text="Cámara + PoE 602", command=incidencias).pack(pady=5)
    tk.Button(ventana602, text="Cámara OCR 602", command=ocr).pack(pady=5)
    tk.Button(ventana602, text="Reader 3M 602", command=reader).pack(pady=5)
    tk.Button(ventana602, text="Regresar", command=regresar).pack(pady=5)

#------------------------------------------------------PÓRTICOS--------------------------------------------------------#

#Dispositivos pórtico 101:
def portico101():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.11"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.11"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.12"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.12"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.13"))
        #url = "http://10.17.20.13"
        #webbrowser.open(url)
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.13"))
    #OCR 2:
    def portico_ocr2():
        #print(hacer_ping("10.17.20.14"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.14"))
        url = "http://10.17.20.14"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.15"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.15"))
     #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.16"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.16"))
    #Reader Portico 101:
    def portico_reader():
        url = "http://10.17.20.17"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.18"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.19"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.19"))
    
    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana101.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos d Portico 101:
    ventana101 = tk.Tk()
    ventana101.title("Equipos Pórtico 101")
    tk.Label(ventana101, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana101, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana101, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana101, text="Cámara OCR 1", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana101, text="Cámara OCR 2", command=portico_ocr2).pack(pady=5)
    tk.Button(ventana101, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana101, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana101, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana101, text="Camara deIncidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana101, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana101, text="Regresar", command=regresar).pack(pady=5)


#Dispositivos pórtico 102:
def portico102():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.71"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.71"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.72"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.72"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.73"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.73"))
        url = "http://10.17.20.73"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.75"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.75"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.76"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.76"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.77"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.78"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.79"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.79"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana102.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos d Portico 102:
    ventana102 = tk.Tk()
    ventana102.title("Equipos Pórtico 102")
    tk.Label(ventana102, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana102, text="RPM1", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana102, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana102, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana102, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana102, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana102, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana102, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana102, text="RPM2", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana102, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 201:
def portico201():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.21"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.21"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.22"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.22"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.23"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.23"))
        url = "http://10.17.20.23"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.25"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.25"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.26"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.26"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.27"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.28"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.29"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.29"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana201.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 201:
    ventana201 = tk.Tk()
    ventana201.title("Equipos Pórtico 201")
    tk.Label(ventana201, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana201, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana201, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana201, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana201, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana201, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana201, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana201, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana201, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana201, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 202:
def portico202():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.31"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.31"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.32"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.32"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.33"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.33"))
        url = "http://10.17.20.23"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.35"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.35"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.36"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.36"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.37"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.38"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.39"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.39"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana202.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 202:
    ventana202 = tk.Tk()
    ventana202.title("Equipos Pórtico 202")
    tk.Label(ventana202, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana202, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana202, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana202, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana202, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana202, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana202, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana202, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana202, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana202, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 301:
def portico301():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.41"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.41"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.42"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.42"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.43"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.43"))
        url = "http://10.17.20.43"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.45"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.45"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.46"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.46"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.47"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.48"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.49"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.49"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana301.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 301:
    ventana301 = tk.Tk()
    ventana301.title("Equipos Pórtico 301")
    tk.Label(ventana301, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana301, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana301, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana301, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana301, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana301, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana301, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana301, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana301, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana301, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 302:
def portico302():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.51"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.51"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.52"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.52"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.53"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.53"))
        url = "http://10.17.20.53"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.55"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.55"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.56"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.56"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.57"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.58"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.59"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.59"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana302.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 301:
    ventana302 = tk.Tk()
    ventana302.title("Equipos Pórtico 302")
    tk.Label(ventana302, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana302, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana302, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana302, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana302, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana302, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana302, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana302, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana302, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana302, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 401:
def portico401():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.61"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.61"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.62"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.62"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.63"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.63"))
        url = "http://10.17.20.63"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.65"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.65"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.66"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.66"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.67"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.68"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.69"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.69"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana401.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 301:
    ventana401 = tk.Tk()
    ventana401.title("Equipos Pórtico 401")
    tk.Label(ventana401, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana401, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana401, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana401, text="Cámara OCR", command=portico_ocr1).pack(pady=5)
    tk.Button(ventana401, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana401, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana401, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana401, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana401, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana401, text="Regresar", command=regresar).pack(pady=5)

#Dispositivos pórtico 501:
def portico501():
    #RPM:
    def portico_rpm1():
        #print(hacer_ping("10.17.20.81"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.81"))
    #UPS
    def portico_ups():
        #print(hacer_ping("10.17.20.82"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.82"))
    #OCR 1:
    def portico_ocr1():
        #print(hacer_ping("10.17.20.83"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.83"))
        url = "http://10.17.20.83"
        #webbrowser.open(url)
    #Escaner Sick 1:
    def portico_escaner1():
        #print(hacer_ping("10.17.20.85"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.85"))
    #Escaner Sick 2:
    def portico_escaner2():
        #print(hacer_ping("10.17.20.86"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.86"))
    #Reader Portico 102:
    def portico_reader():
        url = "http://10.17.20.87"
        webbrowser.open(url)
    #Camara Incidencias:
    def portico_incidencias():
        url = "http://10.17.20.88"
        webbrowser.open(url)
    #RPM:
    def portico_rpm2():
        #print(hacer_ping("10.17.20.89"))
        messagebox.showinfo("Resultado del Ping:", hacer_ping("10.17.20.89"))


    #Menu Princial -- Quitas ventana Portico 101 y solo muestras ventana de menu principal:
    def regresar():
        ventana501.withdraw()
        ventana.deiconify()
    
    #Menu Dispositivos de Portico 301:
    ventana501 = tk.Tk()
    ventana501.title("Equipos Pórtico 501")
    tk.Label(ventana501, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana501, text="RPM", command=portico_rpm1).pack(pady=5)
    tk.Button(ventana501, text="UPS", command=portico_ups).pack(pady=5)
    tk.Button(ventana501, text="Cámara OCR ", command=portico_ocr1).pack(pady=5)
    #tk.Button(ventana501, text="Cámara OCR ", command=portico_ocr2).pack(pady=5)
    tk.Button(ventana501, text="Escáner Sick 1", command=portico_escaner1).pack(pady=5)
    tk.Button(ventana501, text="Escáner Sick 2", command=portico_escaner2).pack(pady=5)
    tk.Button(ventana501, text="Reader", command=portico_reader).pack(pady=5)
    tk.Button(ventana501, text="Camara de Incidencias", command=portico_incidencias).pack(pady=5)
    tk.Button(ventana501, text="RPM", command=portico_rpm2).pack(pady=5)
    tk.Button(ventana501, text="Regresar", command=regresar).pack(pady=5)

#Funcion para salir del programa:
def salir():
    ventana.quit()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Menu Principal:
ventana = tk.Tk()
ventana.title("Equipos AUSN México")

tk.Label(ventana, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)
tk.Button(ventana, text="Vía 101", command=via101).pack(pady=5)
tk.Button(ventana, text="Pórtico 101", command=portico101).pack(pady=5)
tk.Button(ventana, text="Vía 102", command=via102).pack(pady=5)
tk.Button(ventana, text="Pórtico 102", command=portico102).pack(pady=5)
tk.Button(ventana, text="Vía 103", command=via103).pack(pady=5)
tk.Button(ventana, text="Vía 104", command=via104).pack(pady=5)
tk.Button(ventana, text="Vía 201", command=via201).pack(pady=5)
tk.Button(ventana, text="Pórtico 201", command=portico201).pack(pady=5)
tk.Button(ventana, text="Vía 202", command=via202).pack(pady=5)
tk.Button(ventana, text="Pórtico 202", command=portico202).pack(pady=5)
tk.Button(ventana, text="Vía 301", command=via301).pack(pady=5)
tk.Button(ventana, text="Pórtico 301", command=portico301).pack(pady=5)
tk.Button(ventana, text="Vía 302", command=via302).pack(pady=5)
tk.Button(ventana, text="Pórtico 302", command=portico302).pack(pady=5)
tk.Button(ventana, text="Vía 401", command=via401).pack(pady=5)
tk.Button(ventana, text="Pórtico 401", command=portico401).pack(pady=5)
tk.Button(ventana, text="Vía 402", command=via402).pack(pady=5)
tk.Button(ventana, text="Vía 501", command=via501).pack(pady=5)
tk.Button(ventana, text="Pórtico 501", command=portico501).pack(pady=5)
tk.Button(ventana, text="Vía 502", command=via502).pack(pady=5)
tk.Button(ventana, text="Vía 601", command=via601).pack(pady=5)
tk.Button(ventana, text="Vía 602", command=via602).pack(pady=5)
tk.Button(ventana, text="Salir", command=salir).pack(pady=5)

ventana.mainloop()