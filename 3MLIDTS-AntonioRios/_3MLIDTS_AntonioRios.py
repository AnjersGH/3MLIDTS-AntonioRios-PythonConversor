import tkinter as tk
from tkinter import messagebox

def radioButton_selected():
    sel = rbSeleccion.get()

    if sel == "Celcius":

        tbCelcius.config(state="normal")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="disabled") 

    elif sel == "Kelvin":

        tbCelcius.config(state="disabled")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="normal") 
    
    elif sel == "Fahrenheit":

       tbCelcius.config(state="disabled")
       tbFahrenheit.config(state="normal")
       tbKelvin.config(state="disabled") 
  
def btnCalcular_Click():
    try:
        if rbSeleccion.get() == "Celcius":
           tbCelcius.config(state="normal")
           tbFahrenheit.config(state="normal")
           tbKelvin.config(state="normal")
           celcius = float (tbCelcius.get())
           print(celcius)
           fahrenheit = (celcius * 9.0 /5.0) + 32.0
           print(fahrenheit)
           tbFahrenheit.insert(0,str(round(fahrenheit,2)))
           kelvin = celcius + 273.0
           print(kelvin)
           tbKelvin.insert(0,str(round(kelvin,2)))

        elif  rbSeleccion.get() == "kelvin":
            tbCelcius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            kelvin = float(tbKelvin.get())
            celcius = kelvin - 273.0
            tbCelcius.insert(o,str(round(tbCelcius,2)))
            print(celcius)
            fahrenheit = (celcius * 9.0 % 5.0) +32.0
            print(fahrenheit)
            tbFahrenheit.insert(0,str(round(fahrenheit)))

        elif rbSeleccion.get() == "fahrenheit":
            tbCelcius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")

            print(fahrenheit)
            celsius = (fahrenheit - 32.0) * 5.0 / 9.0
            print(celsius)
            kelvin = celsius + 273.0
            print(kelvin)
            tbCelcius.insert(0, str(round(celsius, 2)))
            tbKelvin.insert(0, str(round(kelvin, 2)))
        else:
            messagebox.showwarning(
                "Temperatura Seleccionada, Seleccione una temperatura de entrada (Kelvin/ Fahrenheit/Celsius)."
            )
    except ValueError:
        messagebox.showerror("Error", "ingresa un numero valido en el campo habilitado")

def btnLimpiar_Click():
    tbKelvin.delete(0, tk.END)
    tbCelcius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)


ventana=tk.Tk()
ventana.title("actividad 03-conversor de temperatura")
ventana.geometry("450x450")
ventana.config(bg="pink")


rbSeleccion=tk.StringVar(value="")
tk.Label(ventana, text="Temp. Celcius", font=("Segoe UI",12,"bold")).pack()
tbCelcius=tk.Entry(ventana, width=20, justify="center")
tbCelcius.pack()

tk.Label(ventana, text="Temp. Fahrenheit", font=("Segoe UI",12,"bold")).pack()
tbFahrenheit=tk.Entry(ventana, width=20, justify="center")
tbFahrenheit.pack()

tk.Label(ventana, text="Temp. Kelvin", font=("Segoe UI",12,"bold")).pack()
tbKelvin=tk.Entry(ventana, width=20, justify="center")
tbKelvin.pack()

gb=tk.LabelFrame(ventana, text="seleccione Temperatura de Entrada: ", padx=12, pady=10)
gb.pack()

rbCelcius=tk.Radiobutton(gb, text="Celcius", value="Celcius", variable=rbSeleccion, command=radioButton_selected)
rbCelcius.grid(row=0, column=0)

rbKelvin=tk.Radiobutton(gb, text="kelvin", value="Kelvin", variable=rbSeleccion, command=radioButton_selected)
rbKelvin.grid(row=0, column=1)

rbFahrenheit=tk.Radiobutton(gb, text="Fahrenheit", value="Fahrenheit", variable=rbSeleccion, command=radioButton_selected)
rbFahrenheit.grid(row=0, column=2)

btnCalcular=tk.Button(ventana, text="calcular", command=btnCalcular_Click)
btnCalcular.pack()

btnLimpiar=tk.Button(ventana, text="Limpiar", command=btnLimpiar_Click)
btnLimpiar.pack()


ventana.mainloop()