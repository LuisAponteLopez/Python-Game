import random

num1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

a = True 
puntacion , contador , vida = 0   , 0 , 5






while a:
    randomnum1   = random.randrange(21) 
    randomnum2 = random.randrange(21)
    b = True
    while b:
        resultado = input(str(num1[randomnum1]) +" X "+ str(num2[randomnum2]))
        contador += 1
        if int(resultado) == num1[randomnum1]*num2[randomnum2]:
            b = False 
            puntacion += 1
        else:
            vida -= 1
            if vida == 0:
                print("Perdiste")
                a = False
                b = False
    
