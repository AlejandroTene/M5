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

carro_Alejandro = auto("KIA","EV5",2025)

print(carro_Alejandro.mostrar_informacion())
print(carro_Alejandro.actualizar_kilometraje(5000))
print(carro_Alejandro.realizar_viaje(10000))
print(carro_Alejandro.estado_auto())