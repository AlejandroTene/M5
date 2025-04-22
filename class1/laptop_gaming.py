from laptop import lapto

class Laptop_Gaming(lapto):
    def __init__(self, marca, procesador, memoria,tarj_graf , costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.tarj_graf = tarj_graf

    def __str__(self):
        return f"Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Tarjeta Gráfica: {self.tarj_graf} \n Costo: {self.costo} \n Impuestos: {self.impuestos}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico

    def realizar_diagnostico_juegos(self):
        juegos = ["FORNITE","COD","GTA"]
        resultados={}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_graf:
                fps = fps_base*3
            elif "GTX" in self.tarj_graf:
                fps = fps_base*2
            else:
                fps = fps_base
            
            resultados [juego] = f"{fps} FPS"
        return resultados
    
    def realizar_informe_uso(self):
        informe= super().realizar_informe_uso()
        informe.update({
            "Tipo":"Gaming",
            "Uso Recomendado" : "Juegos de video",
            "Horas de uso": 10,
            "Recomendaciones de software ": ["Antivirus","VPN"] 
        })
        return informe

    pass

    