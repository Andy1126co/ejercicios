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
    
    separacion =secreto.rsplit("  ")
    for i in posicion:
        separacion[i]=letra
    return separacion
            
    
    

  
def run():
    escoger = select(read())
    while True:
        letra = input("Ingresa una letra: ")    
            
        secreto = secret(escoger)
        print(f'primer secreto: {secreto}',escoger)
        print("//////////////////////////////")
        prueba = comparar(escoger,letra)
        cambio = reemplazo(secreto,prueba,letra)
        cambio ="  ".join(cambio)
        secreto = cambio
        print(f'impresion de cambio: {cambio}')
        print(f'segundo secreto: {secreto}',escoger)
        if secreto == escoger:
            break
        
    
    #print(secreto,escoger,"--->"+str(prueba))
    #print(f'el cambio: {cambio}')
    
    
    
        

if __name__ =="__main__":
    run()