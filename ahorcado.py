from random import random, randrange
from re import S
import collections


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
    
    with open("./archivos/palabras.txt","r",encoding="utf-8") as f:
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
        
        if word.find(letter,c) != -1 and word.find(letter,c)not in posiciones:
            posiciones.append(word.find(letter,c))
        c = c + 1
    
    return posiciones  


    
    return posiciones 
        
        
def reemplazo(secreto,posicion,letra):
    
    separacion =secreto.rsplit("  ")
    for i in posicion:
        separacion[i]=letra
    return separacion
            

    

  
def run():
    escoger = select(read())
    secreto = secret(escoger)
    cont = 0
    while True:
        letra = input("Ingresa una letra: ") 
                
        
        print("//////////////////////////////")
        prueba = comparar(escoger,letra)
        cambio = reemplazo(secreto,prueba,letra)
        cambio ="  ".join(cambio)                  
        secreto = cambio
        literal ="_"
                    
        print(f'palabra secreta: {secreto}')
        if cambio.find(literal,cont)==-1:
            print("*****************************************")
            print(f'Lo lograste')
            break
        if cont == len(escoger):
            cont = 0
        cont = cont + 1
        
           
         
    
        

if __name__ =="__main__":
    run()