from laptop import lapto
import random

class Laptop_Business(lapto):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.almacenamiento = almacenamiento
        self. duracion_bateria = duracion_bateria
    
    def __str__(self):
        return f"Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Almacenamiento: {self.almacenamiento} \n Duración de bateria: {self.duracion_bateria} \n Costo: {self.costo} \n Impuestos: {self.impuestos}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_conectividad = self.verificar_conectividad()
        resultado_diagnostico["Resultado conectividad"] = resultado_conectividad
        return resultado_diagnostico

    def verificar_conectividad(self):
        datos = {
            "WIFI": "True" if random.choice([True, False]) else "False",
            "Acceso_Servidores": "False" if random.choice([True, False]) else "False",
            "Latencia_baja": "True" if random.choice([True, False]) else "False"
        }
        return datos

    pass