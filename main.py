from ahorcado import Ahorcado 

def jugar():
    juego=Ahorcado(5)
    juego.dibujar() 
    #resp=''
    continuar=True

    while continuar :
        resp=input("Ingrese una letra (o 0 para salir):") 
        if resp=="0":
            break
        win=juego.jugar(resp)
        juego.dibujar() 
        # win=0:perdió , win=1:ganó, win=2:sigue jugando
        if win<2:
            resp=input("Desea jugar de nuevo?(s/n):")
            if resp!="s":
                continuar=False
                print("Eres demasiado malo para este juego!")
            else:
                juego=Ahorcado(5) 
                juego.dibujar() 

jugar()