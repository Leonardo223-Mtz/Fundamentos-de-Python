class Perro:

    especie = "mamífero"
    nombre = ""
    raza = ""
    def __init__(self,nombre,raza):
        print(f"Creando perro {nombre},{raza}")
        self.nombre = nombre
        self.raza = raza

mi_Perro = Perro("Brisa","Chihuahua")
'''print(mi_Perro.especie)
print(mi_Perro.nombre)
print(mi_Perro.raza)'''


mi_Perro2 = Perro("Mila","Pug")
'''print(mi_Perro2.especie)
print(mi_Perro2.nombre)
print(mi_Perro2.raza)'''

lista= []

lista.append(mi_Perro)
lista.append(mi_Perro2)
lista.append("Cadena")
lista.append(1)
lista.append(Perro("Candas","Labrador"))
print(lista[2].nombre)