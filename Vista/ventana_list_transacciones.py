from tkinter import Frame, Label, Button, Entry, Listbox, END

class ListViewTransacciones(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Encabezado
        self.header = Label(self, text="Moneda Más Vendida del Día")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo de entrada para la fecha
        self.fecha_label = Label(self, text="Fecha (YYYY-MM-DD):")
        self.fecha_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.fecha_entry = Entry(self, width=20)
        self.fecha_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Listbox para mostrar resultados
        self.listaDatos = Listbox(self, width=100)
        self.listaDatos.grid(row=2, column=0, columnspan=2, padx=30, pady=10)

        # Botón para listar la moneda más vendida
        self.list_btn = Button(self, text="Consultar")
        self.list_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Botón para retornar al menú
        self.return_btn = Button(self, text="Volver al Menú")
        self.return_btn.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        
    def listar_datos(self, moneda):
        """
        Actualiza la vista con los datos de la moneda más vendida.
        """
        self.listaDatos.delete(0, END)
        if moneda:
            self.listaDatos.insert(0, f"Nombre: {moneda['nombre']}")
            self.listaDatos.insert(1, f"Símbolo: {moneda['simbolo']}")
            self.listaDatos.insert(2, f"Cantidad Vendida: {moneda['total_vendida']}")
        else:
            self.listaDatos.insert(0, "No se encontraron datos para la fecha especificada.")
