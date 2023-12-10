#en este codigo aprenderemos como sobrescribir metodos heredados

#supongamos tenmos la clase ave

class Ave:
    def volar(self):
        print("la ave esta volando")
        
#ahora cremos una clase heredando lo de ave

class Pinguino(Ave):
    def volar(self):
        #heredamos lo de super
        super().volar()
        print("el pinguino no puede volar pero se siente feliz")
        
#creamos una instancias de pinguino

pingui = Pinguino()

#utilizamos su metodo
pingui.volar()                