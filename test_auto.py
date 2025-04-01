from auto import auto



carro_Alejandro = auto("KIA","EV5",2025)
carro_Claudia = auto("Toyota","EV6",2024,20000)

#print(carro_Alejandro.mostrar_informacion())
#print(carro_Alejandro.actualizar_kilometraje(5000))
#print(carro_Alejandro.realizar_viaje(10000))
#print(carro_Alejandro.estado_auto())

for i in range(1,6):
    toyota_auto = auto.toyota_auto()
    print(toyota_auto.__dict__)

print("-------------------------------------------------------------------")
print(auto.comparar_km(carro_Alejandro,carro_Claudia))

print("-------------------------------------------------------------------")
print(auto.comparar_anio(carro_Alejandro,carro_Claudia))


print("-------------------------------------------------------------------")
for i in range(1,4):
    kia_auto = auto.KIA_auto("EV6")
    print(kia_auto.__dict__)