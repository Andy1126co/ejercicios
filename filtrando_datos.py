
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workes = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    all_old_devs = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], all_old_devs))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    language_dev = list(map(lambda worker : worker["language"],DATA))
    
    
    filter_language=[]
    for i in language_dev:
        if i not in  filter_language and i != "":
            filter_language.append(i)
      
    #archivo = open("prueba.txt","w")
    #archivo.write(str(filter_language))
    #archivo.close()
    
    

    for worker in filter_language:
       print(worker)

DATA2 =[
    {'name': 'Facundo', 'age': 72, 'organization': 'Platzi', 'position': 'Technical Coach', 'language': 'python'},
    {'name': 'Luisana', 'age': 33, 'organization': 'Globant', 'position': 'UX Designer', 'language': 'javascript'},
    {'name': 'Héctor', 'age': 19, 'organization': 'Platzi', 'position': 'Associate', 'language': 'ruby'},
    {'name': 'Gabriel', 'age': 20, 'organization': 'Platzi', 'position': 'Associate', 'language': 'javascript'},
    {'name': 'Isabella', 'age': 30, 'organization': 'Platzi', 'position': 'QA Manager', 'language': 'java'}, 
    {'name': 'Karo', 'age': 23, 'organization': 'Everis', 'position': 'Backend Developer', 'language': 'python'},
    {'name': 'Juan', 'age': 17, 'organization': '', 'position': 'Student', 'language': 'go'},
    {'name': 'Pablo', 'age': 32, 'organization': 'Master', 'position': 'Human Resources Manager', 'language': 'python'},
    {'name': 'Lorena', 'age': 56, 'organization': 'Python Organization', 'position': 'Language Maker', 'language': 'python'}
    ]

    

    


if __name__ == "__main__":
    run()
