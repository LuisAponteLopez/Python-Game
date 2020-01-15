##Para poder jugar el juego necesita crear un documento con diferente palabras separada con coma y sin espacio y guardado con el nombre "palabras.txt" y tener el programa con dicho documento en la misma carpeta .



import time
import random

nombre = input("Como te llama: ")
print("Hola,",nombre,"es hora de jugar al ahorcado.")


a = True
while a:
    
    
    f = open ('palabras.txt','r')
    palabras = f.read()
    listapalabra= palabras.split(",")
    cantidad = len(listapalabra)
    random_index = random.randrange(cantidad)
    palabra = listapalabra[random_index]#palabra que tiene que adivinar
    
    f.close()
    time.sleep(1)
    print("Comienza a adivinar")
    time.sleep(.5)
    tupalabra = ""
    vidas = 5
        
    
    
    
    while vidas > 0:
        
        fallas = 0
        for letra  in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("*",end="")
                fallas+=1
        if fallas == 0:
            print("\nFelicidades, ganaste")
            break
        tuletra=input("\nIntroduce una letra: ")
        tupalabra += tuletra
        
        if tuletra not in palabra:
            vidas-=1
            print("Equivocadon")
            print("tu tiene ",vidas," vidas.")
    
    if vidas == 0 :
        print("Perdiste")
        print(palabra)
    else:
        print("Gracias por participar")
    
    a = input("Quieres volver a jugar (si/no): ")
    
    if a != "si" :
        a = False
    time.sleep(0)
