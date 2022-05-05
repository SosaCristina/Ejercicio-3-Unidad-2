class Registro:
    __temperatura:""
    __humedad:""
    __presion:""


    def __init__(self, temp, hum, pre):
        self.__temperatura=temp
        self.__humedad=hum
        self.__presion=pre

    def __str__ (self):
        return "%s %s %s"% (self.__temperatura, self.__humedad, self.__presion)

    def Gettemperatura (self):
        return self.__temperatura

    def Gethumedad (self):
        return self.__humedad

    def Getpresion (self):
        return self.__presion





