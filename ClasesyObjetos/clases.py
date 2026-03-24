class Celular:

    #Estos son atributos estáticos
    marca = "Motorola"
    modelo = "RZR"
    camara = "48MP"



class Telefono:
    def __init__(self, marca, modelo, camara):      #A esto se le llama metodo constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estás haciendo un llamado desde un: {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")



celular1 = Telefono("Motorola", "RZR", "48MP",)
print(celular1.marca)

celular2 = Telefono("iPhone", "16 Pro MAX", "24MP",)
print(celular2.marca)

#TODAS LAS FUNCIONES DENTRO DE UN OBJETO SON METODOS, ESTOS DEFINEN LAS ACCIONES QUE PUEDEN HACER
#LOS OBJETOS QUE LOS CONTIENEN

celular2.llamar()

'''Hola mi nombre es Rodolfo. Español '''
#Español #Español























