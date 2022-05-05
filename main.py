from ClaseRegistro import Registro
import csv

def mostrar (lista):
    for i in range (len(lista)):
        for j in range(len(lista[i])):
            print (lista[i][j])


if __name__ =="__main__":
    matriz=[] #la matriz guarda lista

    for i in range (2):
        lista=[]
        for j in range (3):
            lista.append(0)
        #print(lista)
        matriz.append(lista)

    archivo=open("Registro.csv")
    reader=csv.reader(archivo,delimiter=",")

    for fila in reader:
        indice1=int (fila[0])
        indice2=int (fila[1])
        temp=fila[2]
        hum=fila[3]
        pre=fila[4]
        unRegistro=Registro(temp,hum,pre)
        matriz[indice1-1][indice2]=unRegistro
        print(matriz[indice1-1][indice2])
    archivo.close()

    opcion=0
    def menu():
        opc=int(input("Menu principal\n"+
                      "1)Mostrar para cada variable el dia y hora de menor y mayor valor\n"+
                      "2)Indicar tempteratura promedio mensual por cada hora\n"+
                      "3)Listar los valores de las tres variables para cada hora del dia dado\n"+
                      "4)Salir\n"+
                      "Seleccione una opcion\n"))
        return opc
    while opcion!=4:
        opcion=menu()
        if opcion ==1:
            maxt="0"
            maxh="0"
            maxp="0"
            mint="1000"
            minh="1000"
            minp="1000"
            indicei=0
            indicej=0
            print("VALORES MAXIMOS")
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Gettemperatura()>maxt):
                        maxt=matriz[i][j].Gettemperatura()
                        indicei=i+1
                        indicej=j
            print("La temperatura maxima es:{}. Del dia {}, a la hora {}".format(maxt,indicei,indicej))
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Gethumedad()>maxh):
                        maxh=matriz[i][j].Gethumedad()
                        indicei=i+1
                        indicej=j
            print("La humedad maxima es:{}. Del dia {}, a la hora {}".format(maxh,indicei,indicej))
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Getpresion()>maxp):
                        maxp=matriz[i][j].Getpresion()
                        indicei=i+1
                        indicej=j
            print("La presion maxima es:{}. Del dia {}, a la hora {}".format(maxp,indicei,indicej))
            print("VALORES MINIMOS")
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Gettemperatura()<mint):
                        mint=matriz[i][j].Gettemperatura()
                        indicei=i+1
                        indicej=j
            print("La temperatura minima es:{}. Del dia {}, a la hora {}".format(mint,indicei,indicej))
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Gethumedad()<minh):
                        minh=matriz[i][j].Gethumedad()
                        indicei=i+1
                        indicej=j
            print("La humedad minima es:{}. Del dia {}, a la hora {}".format(minh,indicei,indicej))
            for i in range (2):
                for j in range (3):
                    if(matriz[i][j].Getpresion()<minp):
                        minp=matriz[i][j].Getpresion()
                        indicei=i+1
                        indicej=j
            print("La presion minima es:{}. Del dia {}, a la hora {}".format(minp,indicei,indicej))
        if opcion ==2:

            for i in range (2):
                prom=float (0)
                sum=0
                for j in range (3):
                    sum+=int (matriz[i][j].Gettemperatura())
                prom=float (sum/3)
                dia=i+1
                print("La temperatura promedio del dia  " +   str(dia) + "  es  "   + str(prom))

        if opcion ==3:

            dia=int (input("Ingrese el dia\n"))
            indice= (dia-1)
            for j in range (3):
                  print("Hora   Temperatura    Humedad   Presion")
                  print("{}   -   {}   -   {}   -   {}".format(j, matriz[indice][j].Gettemperatura(),matriz[indice][j].Gethumedad(),matriz[indice][j].Getpresion()))


