import serial
import tkinter as tk

# Configurar el puerto serial
arduino_port = '/dev/ttyACM0'  # ajustar según el puerto utilizado por Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
# Esperar a que se establezca la conexión
ser.timeout = 2

# Función para actualizar el estado de los LEDs en la interfaz gráfica
def actualizar_estado():
    # Leer datos desde Arduino
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        # Actualizar el estado de los LEDs en la interfaz
        estado_leds = data.split(",")
        estado_verde.set("Encendido" if estado_leds[0] == '1' else "Apagado")
        estado_rojo.set("Encendido" if estado_leds[1] == '1' else "Apagado")
        estado_amarillo.set("Encendido" if estado_leds[2] == '1' else "Apagado")
    
    # Llamar a esta función nuevamente después de 100ms
    root.after(100, actualizar_estado)

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Estado de LEDs")

estado_verde = tk.StringVar()
estado_rojo = tk.StringVar()
estado_amarillo = tk.StringVar()

tk.Label(root, text="LED Verde:").grid(row=0, column=0)
tk.Label(root, textvariable=estado_verde).grid(row=0, column=1)
tk.Label(root, text="LED Rojo:").grid(row=1, column=0)
tk.Label(root, textvariable=estado_rojo).grid(row=1, column=1)
tk.Label(root, text="LED Amarillo:").grid(row=2, column=0)
tk.Label(root, textvariable=estado_amarillo).grid(row=2, column=1)

# Iniciar la función para actualizar el estado de los LEDs
actualizar_estado()

root.mainloop()
