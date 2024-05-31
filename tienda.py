from os import system
system("cls")
import uuid
#muestra la informacion  de la tienda
print("BIENVENIDO A LA TIENDA DE VIDEOJUEGOS ")
print("Usted acabo de ingresar a la tienda virtual de videojuegos ZONA GAMER ")

#registro de datos de el usuario
nombre=input("ingrese Su nombre:")
edad=input("ingrese su edad: ")

#desicion de usuario
#mostrara el catalogo de juegos disponibles
print("quiere ver el catalogo de juego disponible: ")
des1=int(input("dijite 1(si) O 2(no) :"))


#muestra de catalogo de juegos 
#muestra de categoria
#muetra de su alquiler
terminar = False
menu1 = False
menu2 = False
clearConsole = lambda: print('\n' * 79)
while( terminar == False):
    if des1==1:
        print("este es nuestro catalogo de juegos disponibles de el lanzamiento 2022")
        print("este es nuestra categoria de juegos")
        print("1:CATEGORIA DE DEPORTE")
        print("2:CATEGORIA DE ACCION")
        print("3:CATEGORIA DE AVENTURA")
        print("4:CATEGORIA DE CARRERA")
        print("5:CATEGORIA DE TERROR")
        
        #juegos que entran en la categoria
        #año de su edicion
        clearConsole = lambda: print('\n' * 79)
        des2=int(input("ingrese a una de nuestras categorias:"))
        if des2==1:
            print("categoria deporte")
            print("1: FiFa - 2022")
            print("2: FiFa - 2021")
            print("3: FiFa - 2020")
            print("4: PES  - 2022")
            print("5: PES  - 2021")
            print("6: PES  - 2020")
            #INTERVENCION CON EL USUARIO POR SI QUIERE COMPRAR UN JUEGO
            alquiler = int(input("¿Desea alquilar alguno de estos juegos?: 1(si)  2(no) "))
            if  alquiler == 1:
                juego=input("ingrese el nombre del juego: ")
                año=2022
                añolanza=float(input("ingrese el año de lanzamiento del juego:"))
                canticop=float(input("ingrese la cantidad de copias a comprar:"))
                edadjuego = año - añolanza 
                if edadjuego == 0:
                    print("el video juego es un estreno:")
                    print("el alquiler se a realizado  y es de 1 dia de su video juego")
                    print("el codigo de alquiler es : ")
                    print(uuid.uuid4) 
                elif (edadjuego >1) and (edadjuego <5):
                    print("el video juego es normal")
                    if canticop >=5 :
                        print("el alquiler del juego es de 3 dia")
                        print("el codigo de alquiler es : ")
                        print(uuid.uuid4)
                        
                    elif canticop <5 :
                        print("el alquiler es de 2 dias")
                        print("el codigo de alquiler es : ")
                        print(uuid.uuid4)
                elif edadjuego>5:
                    print(" es un clasico el video juego: ", juego)
                    if canticop >5:
                        print("el alquiler del juego es mayor a 5 dias")
                        print("el codigo de alquiler es : ")
                        print(uuid.uuid4)
                    elif canticop <5:
                        print("el alquiler es de 3 dias")
                        print("el codigo de alquiler es : ")
                        print(uuid.uuid4)
            elif  alquiler==2:
                print("vuelva a la eleccion de categorias")
                menu1 = False
                terminar=True
            clearConsole()  
        elif des2==2:
            print("categoria accion")
            print("1:call of duty: black ops 1-2-3-4,ghost,MWW")
            print("2:BATTLEFIED 3-4")
            print("3:UNCHARTERD-1-2-3(LA TRAICION DE DRAKE)-4")
            
        elif des2==3:
            print("AVENTURA")
            print("1:GOD OF WAR")
            print("2:ASSESIN CREED")
            alquiler=int(input("¿Desea alquilar alguno de estos juegos?: 1(si)  2(no) "))
            
        elif des2==4:
            print("categoria CARRERA")
            print("1:NEED FOR SPEED")
            print("2:Blur")
            print("3:NASCAR")
            
        elif des2==5:
            print("categoria terror")
            print("1:resident evil")
            print("2:five nigths an freddys")
            print("3:Ultimate Custom Night")
            
    elif des1==2:
        print("gracias por visitar nuestra pagina")
        terminar=True  
        clearConsole()  








    


