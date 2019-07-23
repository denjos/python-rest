class Alumno:
    def __init__(self,nombre,nota):
        self.__nombre=input("Nombre del alumno: ")
        self.__nota=nota
    def imprimir(self):
        print("Alumno nombre: "+self.__nombre)
        print("Alumno nota: "+str(self.__nota))
        self.resultado()
    def resultado(self):
        if self.__nota>10:
            print("El alumno aprobo")
        else:
            print("El alumno no ha aprobado")

alumno1=Alumno("oscar",15)
alumno1.imprimir()