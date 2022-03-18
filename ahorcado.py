from random import random, randrange
from re import S


def datos():
    palabra = input("Adinivina la palabra: ")
    
    
def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.lower(), b.lower())
        return s

def read():
    palabras =[]
    
    with open("./archivos/varias_a.txt","r",encoding="utf-8") as f:
        for line in f :
            
            if line !="\n":               
                palabras.append(normalize((line.replace("\n",""))))
                
                    
    return palabras
                    
def select(palabra):
    limit = len(palabra)
    capture = palabra[randrange(limit)]
    return capture
    
def secret(select):
    pista = [' ___ ']*len(select)
    one_string ="".join(pista)
    return one_string



def comparar(word,letter):
    posiciones=[]
    c = 0
    for i in word:
        c = c + 1
        if word.find(letter,c) != -1 and word.find(letter,c)not in posiciones:
            posiciones.append(word.find(letter,c))
    
    return posiciones   
        
        
def reemplazo(secreto,posicion,letra):
    #posiciones ya no entra un valor entra una lista,
    # toca recorrer la lista y hacer los reemplazos
    separacion =secreto.rsplit("  ")
    separacion[posicion]=letra
    return separacion
            
    
    

  
def run():
   
    letra = input("Ingresa una letra: ")    
    escoger = select(read())    
    secreto = secret(escoger)
    print(f'primer secreto: {secreto}',escoger)
    print("//////////////////////////////")
    prueba = comparar(escoger,letra)
    #cambio = reemplazo(secreto,prueba,letra)
    #cambio ="  ".join(cambio)
    #if prueba == "True":
     #   secreto = cambio
    
    #print(secreto,escoger,"--->"+str(prueba))
    #print(f'el cambio: {cambio}')
    print(f'impresion de reemplazo: {prueba}')
        

if __name__ =="__main__":
    run()