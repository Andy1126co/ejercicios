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
        
def run():
    print(secret(select(read())))
    

if __name__ =="__main__":
    run()