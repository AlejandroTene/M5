class auto:
    def __init__(self,marca,modelo,anio,kilometraje =0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje
    
    def mostrar_informacion(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Año:{self.anio}"
    
    def actualizar_kilometraje(self,kilometrajeN):
        if kilometrajeN > self.kilometraje:
            self.kilometraje=kilometrajeN
            return "Kilometraje Actualizado"
        else:
            return "No se puede reducir el kilometraje"

    def realizar_viaje(self,kilometrosRecorridos):
        if kilometrosRecorridos>0:
            self.kilometraje +=kilometrosRecorridos
            return "Información guardada"
        else:
            return "Los kilometros deben ser positivos"
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo"
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            return "Ya estoy usado"
        else:
            return "¡Ya déjame descansar por favor!"
    
    @staticmethod
    def comparar_km(auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        else:
            return "Tienen diferente Kilometraje"
        
    @staticmethod
    def comparar_anio(auto1,auto2):
        if auto1.anio == auto2.anio:
            return "Son del mismo año"
        else:
            return "Son de distindo año"


    @classmethod
    def toyota_auto (cls):
        marca = "Toyota"
        modelo = "RAV4"
        anio = 2025
        return cls(marca,modelo,anio)
    
    @classmethod
    def KIA_auto (cls, modelo):
        marca = "KIA"
        anio = 2026
        return cls(marca,modelo,anio)


