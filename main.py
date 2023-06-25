from tkinter import *
from tkinter import ttk
from numer_imaginario import Imaginario

class CalculadoraImaginaria:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de Números Imaginarios")

        self.label_real1 = ttk.Label(self.__ventana, text="Parte Real:")
        self.entry_real1 = ttk.Entry(self.__ventana)
        self.label_imaginario1 = ttk.Label(self.__ventana, text="Parte Imaginaria:")
        self.entry_imaginario1 = ttk.Entry(self.__ventana)

        self.label_operacion = ttk.Label(self.__ventana, text="Operación:")
        self.combo_operacion = ttk.Combobox(self.__ventana, values=["+", "-", "*", "/"])

        self.label_real2 = ttk.Label(self.__ventana, text="Parte Real:")
        self.entry_real2 = ttk.Entry(self.__ventana)
        self.label_imaginario2 = ttk.Label(self.__ventana, text="Parte Imaginaria:")
        self.entry_imaginario2 = ttk.Entry(self.__ventana)

        self.button_calcular = ttk.Button(self.__ventana, text="Calcular", command=self.calcular)

        self.label_resultado = ttk.Label(self.__ventana, text="Resultado:")

        self.configure_layout()

    def configure_layout(self):
        self.label_real1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_real1.grid(row=0, column=1, padx=5, pady=5)
        self.label_imaginario1.grid(row=1, column=0, padx=5, pady=5)
        self.entry_imaginario1.grid(row=1, column=1, padx=5, pady=5)

        self.label_operacion.grid(row=2, column=0, padx=5, pady=5)
        self.combo_operacion.grid(row=2, column=1, padx=5, pady=5)

        self.label_real2.grid(row=3, column=0, padx=5, pady=5)
        self.entry_real2.grid(row=3, column=1, padx=5, pady=5)
        self.label_imaginario2.grid(row=4, column=0, padx=5, pady=5)
        self.entry_imaginario2.grid(row=4, column=1, padx=5, pady=5)

        self.button_calcular.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.label_resultado.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def calcular(self):
        num1 = Imaginario(float(self.entry_real1.get()), float(self.entry_imaginario1.get()))
        num2 = Imaginario(float(self.entry_real2.get()), float(self.entry_imaginario2.get()))

        if self.combo_operacion.get() == '+':
            resultado = num1 + num2
        elif self.combo_operacion.get() == '-':
            resultado = num1 - num2
        elif self.combo_operacion.get() == '*':
            resultado = num1 * num2
        elif self.combo_operacion.get() == '/':
            resultado = num1 / num2

        self.label_resultado.config(text=f'Resultado: {resultado.real} + {resultado.imaginario}i')

    def run(self):
        self.__ventana.mainloop()


def main():
    calculadora = CalculadoraImaginaria()
    calculadora.run()

if __name__ == '__main__':
    main()
