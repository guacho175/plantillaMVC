# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:15:46 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .transaccion_DAO import Transaccion_DAO


class Gestor_Transacciones(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.transaccion_DAO = Transaccion_DAO()
                        
    def recuperar_datos(self, fecha):
        """
        Recupera los datos de transacciones para la fecha proporcionada.
        """
        print(f"Recuperando datos para la fecha: {fecha}")
        # Simulamos la recuperación de datos con un diccionario
        datos = {"fecha": fecha, "transacciones": []}  # Asegúrate de que 'fecha' esté presente
        self.trigger_event("lista_transacciones", datos)
        return datos

    def moneda_mas_vendida_del_dia(self, fecha):
        """
        Procesa la consulta para encontrar la moneda más vendida en una fecha específica.
        """
        print(f"Consultando la moneda más vendida para la fecha: {fecha}")
        datos = self.recuperar_datos(fecha)
        
        # Simulamos el resultado para el evento
        self.trigger_event("moneda_mas_vendida", datos)

    def retornar(self):
        print("Retornando al menú principal...")
        self.trigger_event("home")
