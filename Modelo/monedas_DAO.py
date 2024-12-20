from .conectorBD import ConectorBD

class Monedas_DAO:

    def __init__(self, conectorBD) -> None:
        self.conectorBD = conectorBD

    def recuperar_listaMonedas(self):
        # Activar la conexión a la base de datos
        estado = self.conectorBD.activarConexion()

        if estado == 66:  # Error al conectar
            del self.conectorBD
            return estado, None
        
        # Consulta para recuperar toda la tabla "moneda"
        sql = "SELECT id, nombre, simbolo FROM moneda"
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        # Crear diccionario para almacenar los datos
        listaMonedas_DTO = {}

        if estado == 0:  # Si la consulta fue exitosa
            for i in range(len(datos)):
                registro = {
                    "codigo": datos[i][0], 
                    "nombre": datos[i][1], 
                    "simbolo": datos[i][2]
                }
                listaMonedas_DTO[i] = registro

        # Cerrar la conexión
        self.conectorBD.desactivarConexion()
        del self.conectorBD

        return estado, listaMonedas_DTO
