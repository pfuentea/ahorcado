import random

from palabras import palabras

from motivacional import mensajes

#palabras=['casa','telefono','planta','perro']

class Ahorcado:
    def __init__(self,vidas=5) -> None:
        self.vidas=vidas
        palabra=palabras[random.randint(0,len(palabras)-1)]
        estado=[]
        for letra in palabra:
            estado.append({
                'letra':letra,
                'lista':False
                })
        self.palabra=palabra
        #print(palabra)
        self.estado=estado
        self.letras_dichas=[]

    def dibujar(self):
        palabra_mostrar=''
        personaje=['/','\\','/','\\','|','O']
        #print(5-self.vidas)
        for i in range (0,5-self.vidas):
            personaje[i]=' '
            
        for elem in self.estado:
            if elem['lista']== True:
                palabra_mostrar+=elem['letra']+ ' '
            else:
                palabra_mostrar+='* '
        
        lines=[
            f"===Ahorcado===",
            f"_____  Vidas:{self.vidas}",
            f"|   |  Letras dichas: {'-'.join(self.letras_dichas)}",
            f"|   {personaje[5]}",
            f"|  {personaje[2]}{personaje[4]}{personaje[3]}" ,
            f"|  {personaje[0]} {personaje[1]}",
            f"|            {palabra_mostrar}"  

        ]
        for lin in lines:
            print(lin)

    def jugar(self,letra):
        if letra in self.letras_dichas:
            print("Ya dijo esta letra")
            return 2
        mensaje=mensajes[random.randint(0,len(mensajes)-1)]
        for elem in self.estado:
            if elem['letra']==letra:
                elem['lista']=True
                
        self.letras_dichas.append(letra)

        letras_ganadoras =[elem for elem in self.estado if elem['lista']==True]
        if len(letras_ganadoras) == len(self.palabra):
            print('Felicidades por ganar!!!!')
            return 1
        if letra not in self.palabra:
            self.vidas -= 1
            print(f"\n{mensaje}")
            
        if self.vidas == 0:
            print('Felicidades por perder!!!!')
            return 0
        return 2


