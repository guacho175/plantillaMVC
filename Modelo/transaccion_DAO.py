from .conectorBD import ConectorBD

class Transaccion_DAO:
    
    def __init__(self):
        # Configura la conexión a la base de datos
        self.conector = ConectorBD(
            hostdb='localhost',
            userdb='root',       
            passwordb='',       
            basedatosdb='acme'
        )
    
    def moneda_mas_vendida_del_dia(self, fecha):
        """
        Obtiene la moneda más vendida del día especificado.
        :param fecha: Fecha en formato 'YYYY-MM-DD'.
        :return: Diccionario con los datos de la moneda más vendida.
        """
        self.conector.activarConexion()

        sql = """
        SELECT m.nombre, m.simbolo, SUM(t.cantidad) AS total_vendida
        FROM TRANSACCION t
        JOIN MONEDA m ON t.moneda_id = m.id
        WHERE DATE(t.fecha_transaccion) = %s
        GROUP BY m.id, m.nombre, m.simbolo
        ORDER BY total_vendida DESC
        LIMIT 1;
        """

        estado, datos = self.conector.ejecutarSelectAll(sql)

        resultado = {}

        if estado == 0 and len(datos) > 0:
            resultado = {
                "nombre": datos[0][0],
                "simbolo": datos[0][1],
                "total_vendida": datos[0][2]
            }

        print("----------------------------------------------------------------------")
        print(f"Estado: {estado}")
        print(f"Moneda Más Vendida del Día ({fecha}): {resultado}")
        print("----------------------------------------------------------------------")

        self.conector.desactivarConexion()

        return resultado
