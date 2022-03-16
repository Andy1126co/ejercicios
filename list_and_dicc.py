def run():
    my_list = [1,"hello",True,4.5]
    my_dicc ={"firstname":"Daniel","lastname":"Vargas"}

    super_list =[{"firstname":"Daniel","lastname":"Vargas"},
                 {"firstname":"Andres","lastname":"Vargas"},
                 {"firstname":"Daniela","lastname":"Vargas"},
                 {"firstname":"martha","lastname":"arias"}]

    super_dicc ={
        "natural_number":[1,2,3,4,5],
        "integer_number":[-1,2,3,4,0],
        "floating_number":[1.1,2.3,4.5]
    }

    for key,value in super_dicc.items():
        print(key,"->",value)

    print("····························")

    for key in super_list:
        print(key)

 
if __name__ == "__main__":
    run()