def divisors(num):
    try:
        if num < 0:
            raise TypeError("Solos debe ingresar numeros positivos")
        divisors=[]
        for i in range(1,num+1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except TypeError as te:
        print(te)
        
        
        


def run():
    while True:
        try:
            
            num = int(input("Ingresa un numero: "))
            if divisors(num) =="None":
                break
            else:
                print(divisors(num))
                print("Termino mi programa")
                return False
        except ValueError:
            print("Debes ingresar un número")
            
        

if __name__=="__main__":
    run()