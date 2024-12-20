class ListControllerTransacciones:
    
    def __init__(self, model, view):
        self.model = model  # Referencia al modelo
        self.view = view    # Referencia a la vista
        self.frame = self.view.frames["listTransacciones"]
        self._bind()

    def _bind(self):
        # Botones de acción
        self.frame.return_btn.config(command=self.retorno)
        self.frame.list_btn.config(command=self.listar_moneda_mas_vendida)

    def retorno(self):
        self.view.switch("home")

    def listar_moneda_mas_vendida(self):
        """
        Captura la fecha ingresada en la vista y pasa la consulta al modelo.
        """
        fecha = self.frame.fecha_entry.get().strip()

        if not fecha:
            print("Error: No se ingresó una fecha válida.")
            return

        print(f"Consultando la moneda más vendida para la fecha: {fecha}")
        
        # Lanza el evento de consulta
        self.model.gestor_transacciones.recuperar_datos(fecha)
