def run():
    dicc_compre = {key: key**3 for key in range(1,101) if key % 3}
    

    dicc_raiz = {key: key**(1/2) for key in range(1,1001)}
    print(dicc_raiz)



if __name__ =="__main__":
    run()