import tkinter as tk
from tkinter import messagebox
import os

class AutoArrancadorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guía para Arrancar un Auto")

        # Fijar el tamaño de la ventana
        window_width = 700  # Aumentar el ancho para el historial
        window_height = 350  # Disminuir alto
        self.window_width = window_width #Guardar width
        self.window_height = window_height #Guardar Height
        master.geometry(f"{window_width}x{window_height}")
        master.resizable(False, False)  # Deshabilitar la capacidad de cambiar el tamaño

        # Centrar la ventana
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)
        master.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

        # Historial
        self.historial_frame = tk.Frame(master, bd=2, relief=tk.GROOVE)  # Marco con borde
        self.historial_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.historial_label = tk.Label(self.historial_frame, text="Historial", font=("Arial", 12, "bold"), anchor="center")
        self.historial_label.pack(side=tk.TOP, padx=10, pady=(0, 0), anchor="n")
        self.historial_text = tk.Text(self.historial_frame, width=30, height=15, state=tk.DISABLED, font=("Arial", 10))
        self.historial_text.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        # Paso Actual - Marco con borde
        self.paso_frame = tk.Frame(master, bd=2, relief=tk.GROOVE)
        self.paso_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

        self.paso_actual = 1
        self.label_paso = tk.Label(self.paso_frame, text="", wraplength=400, font=("Arial", 14))
        self.label_paso.pack(side=tk.TOP, pady=20)

        # Botones
        button_font = ("Arial", 12)
        self.boton_si = tk.Button(self.paso_frame, text="Sí", command=self.responder_si, font=button_font)
        self.boton_no = tk.Button(self.paso_frame, text="No", command=self.responder_no, font=button_font)
        self.boton_siguiente = tk.Button(self.paso_frame, text="Siguiente", command=self.siguiente_paso, font=button_font)

        # Ruta al directorio del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path_tranquilo = os.path.join(script_dir, "Recursos", "Tranquilo Toreto.png")
        self.image_path_calmao = os.path.join(script_dir, "Recursos", "Calmao.png")

        self.pasos = { #Nuevo dict.
            1: "Entrar al auto (Por la puerta del conductor)",
            2: "Ponerse el cinturón de seguridad",
            3: "Ajustar el asiento del piloto",
            4: "Ajustar los espejos retrovisores",
            5: "Insertar la llave del auto en la ranura de encendido",
            6: "Girar la llave en sentido horario",
            7: "¿Arranca el motor?",
            8: "Mantener presionado el pedál de clutch mientras se gira la llave.",
            9: "Presiona Clutch y posicionar la palanca de velocidades en neutro.",
            10: "Soltar el clutch y dejar calentar el motor de 3min a 5min",
            11: "¿El freno de mano está puesto?",
            12: "Mientras se mantiene presionado el clutch cambiar palanca a primera velocidad.",
            13: "Presionar el acelerador mientras se va soltando el clutch, ambos progresivamente",
            14: "¿Se apagó el auto?",
            15: "¡FELICIDADES!\nSe está conduciendo.\nAhora procurar no matar a nadie."
        }

        self.historial_count = 1
        self.actualizar_paso()

    def agregar_al_historial(self, texto):
        historial_entry = f"{self.historial_count}. {texto}\n"
        self.historial_text.config(state=tk.NORMAL)
        self.historial_text.insert(tk.END, historial_entry)
        self.historial_text.config(state=tk.DISABLED)
        self.historial_text.see(tk.END)
        self.historial_count += 1

    def centrar_ventana(self, ventana, width, height):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        ventana.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def mostrar_imagen_toreto(self):
        try:
            self.ventana_toreto = tk.Toplevel(self.master)
            self.ventana_toreto.title("Toretto se enojó")
            self.centrar_ventana(self.ventana_toreto, 400, 350)

            self.toreto_photo = tk.PhotoImage(file=self.image_path_tranquilo, master=self.ventana_toreto)
            self.label_imagen = tk.Label(self.ventana_toreto, image=self.toreto_photo)
            self.label_imagen.image = self.toreto_photo
            self.label_imagen.pack(padx=10, pady=10)

            self.boton_calmar = tk.Button(self.ventana_toreto, text="Calmar a Toretto", command=self.calmar_toreto)
            self.boton_calmar.pack(pady=10)
        except Exception as e:
            print(f"Error al mostrar la imagen: {e}")
            messagebox.showinfo("Error", "No se pudo mostrar la imagen. Revisa la consola.")

    def calmar_toreto(self):
        try:
            self.calmao_photo = tk.PhotoImage(file=self.image_path_calmao, master=self.ventana_toreto)
            self.label_imagen.config(image=self.calmao_photo)
            self.label_imagen.image = self.calmao_photo

            self.boton_calmar.destroy()

            self.boton_continuar = tk.Button(self.ventana_toreto, text="Continuar", command=self.volver_al_proceso)
            self.boton_continuar.pack(pady=10)

        except Exception as e:
            print(f"Error al mostrar la imagen: {e}")
            messagebox.showinfo("Error", "No se pudo mostrar la imagen. Revisa la consola.")

    def volver_al_proceso(self):
        self.ventana_toreto.destroy()
        self.paso_actual = 6
        self.actualizar_paso()

    def actualizar_paso(self):
        texto_paso = self.pasos.get(self.paso_actual, "Paso desconocido")
        self.label_paso.config(text=texto_paso)

        tipo_botones = "siguiente" if self.paso_actual not in (7, 11, 14) else "si_no"
        self.mostrar_botones(tipo_botones)

    def responder_si(self):
        if self.paso_actual == 7:
            self.agregar_al_historial("Arrancó el motor: Sí")
            self.paso_actual = 8
        elif self.paso_actual == 11:
            self.agregar_al_historial("Freno de mano está puesto: Sí")
            messagebox.showinfo("Freno", "Quitar el freno de mano")
            self.paso_actual = 12
        elif self.paso_actual == 14:
            self.agregar_al_historial("Se apagó el auto: Sí")
            self.mostrar_imagen_toreto()
        self.actualizar_paso()

    def responder_no(self):
        if self.paso_actual == 7:
            self.agregar_al_historial("Arrancó el motor: No")
            self.preguntar_bateria()
        elif self.paso_actual == 11:
            self.agregar_al_historial("Freno de mano está puesto: No")
            self.paso_actual = 12
        elif self.paso_actual == 14:
            self.agregar_al_historial("Se apagó el auto: No")
            self.paso_actual = 15

        self.actualizar_paso()

    def mostrar_botones(self, tipo):
        if tipo == "si_no":
            self.boton_si.pack(side=tk.LEFT, padx=20)
            self.boton_no.pack(side=tk.RIGHT, padx=20)
            self.boton_siguiente.pack_forget()
        elif tipo == "siguiente":
            self.boton_si.pack_forget()
            self.boton_no.pack_forget()
            self.boton_siguiente.pack(pady=20)
        elif tipo == "none":
            self.boton_si.pack_forget()
            self.boton_no.pack_forget()
            self.boton_siguiente.pack_forget()

    def siguiente_paso(self):
        if self.paso_actual < 15: #No sobrepasar el paso 15
                self.agregar_al_historial(self.pasos.get(self.paso_actual, "Paso Desconocido"))
                self.paso_actual += 1 #Cambiar El valor
                self.actualizar_paso()

    def preguntar_bateria(self):
        respuesta = messagebox.askyesno("Batería", "¿La batería se encuentra en buenas condiciones?")
        if respuesta:
            self.agregar_al_historial("¿Batería en buenas condiciones?: Sí")
            self.preguntar_gasolina()
        else:
            self.agregar_al_historial("¿Batería en buenas condiciones?: No")
            messagebox.showinfo("Batería", "Cargar o reemplazar la batería")
            self.paso_actual = 6
            self.actualizar_paso()

    def preguntar_gasolina(self):
        respuesta = messagebox.askyesno("Gasolina", "¿El tanque de gasolina está lleno?")
        if respuesta:
            self.agregar_al_historial("¿Tanque de gasolina lleno?: Sí")
            self.paso_actual = 9
            self.actualizar_paso()
        else:
            self.agregar_al_historial("¿Tanque de gasolina lleno?: No")
            messagebox.showinfo("Gasolina", "Llenar el tanque de gasolina")
            self.paso_actual = 6
            self.actualizar_paso()

root = tk.Tk()
gui = AutoArrancadorGUI(root)
root.mainloop()