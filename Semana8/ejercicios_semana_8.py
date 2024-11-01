import csv
import json
# 1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def order_names(my_file):
    names = []
    try:
        with open(my_file) as file:
            for line in file.readlines():
                names.append(line.strip("\n")) #Investigando topé con el método strip que elimina los caracteres indicados, lo cual es útil para remover el salto de linea.
            ordered_names = sorted(names)

        with open("Semana8/ordered_names.txt", "w") as ordered_file:
            for name in ordered_names:
                ordered_file.write(f"{name}\n")
        print(ordered_file)
    except Exception:
        print("El archivo no existe")

order_names('Semana8/names.txt')

#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    # 1. Debe incluir:
    #     1. Nombre
    #     2. Género
    #     3. Desarrollador
    #     4. Clasificación ESRB
    # 2. Ejemplo de archivo final:
        
    #     ```
    #     nombre,genero,desarrollador,clasificacion
    #     Grand Theft Auto IV,Accion,Rockstar Games,M
    #     The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
    #     Tony Hawk's Pro Skater 2,Deportes,Activision,T


def games_saver():
    try:
        game_name = input("Ingrese el nombre del juego: ")
        game_gender = input("Ingrese el genero: ")
        game_dev = input("Ingrese el desarrollador: ")
        game_esrb = input("Ingrese la clasificacion ESRB (E, T, M, A, RP)")

        game_data = [game_name, game_gender, game_dev, game_esrb]

        try:
            with open("Semana8/games_tabulated.csv","a") as games_file:
                csv.writer(games_file, delimiter=str("\t")).writerow(game_data) #Se utiliza delimiter para indicar el separador en los elementos a guardar en el archivo y se usa str() para encerrarlo y evitar el error de delimitador de mas un caracter.

        except Exception as error:
            print(error) 
    except Exception:
        print("Hubo un error")
    init_games_saver()

def init_games_saver():
    user_input = input("¿Desea agregar otro juego? (SI, NO)")

    try:
        if(user_input.upper() == "SI"):
            games_saver()
        elif(user_input.upper() == "NO"):
            print("¡Adios!")
        else: raise ValueError()
    except Exception:
        print("Debe ingresar SI o NO")
    
games_saver()

#2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
    #1. Debe leer el archivo para importar los Pokémones existentes.
    #2. Luego debe pedir la información del Pokémon a agregar.
    #3. Finalmente debe guardar el nuevo Pokémon en el archivo.

def insert_pokemon():
    
    with open('Semana8/pokemons.json') as poke_file:
        poke_json = json.load(poke_file)
        pokemon_name = input("Ingrese el nombre del pokemon: ")
        pokemon_type = input("Cual es el tipo del pokemon: ")
        pokemon_base_specs = input("Ingresa las specs base (HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed)").split(',')
        data = {
            "name": {
                "english": f"{pokemon_name}"
            },
            "type": [
                f"{pokemon_type}"
            ],
            "base": {
                "HP": int(pokemon_base_specs[0]),
                "Attack": int(pokemon_base_specs[1]),
                "Defense": int(pokemon_base_specs[2]),
                "Sp. Attack": int(pokemon_base_specs[3]),
                "Sp. Defense": int(pokemon_base_specs[4]),
                "Speed": int(pokemon_base_specs[5])
            }
        }
        poke_json.append(data)
    
    with open('Semana8/pokemons.json', 'w') as poke_save:
        poke_save.write(str(poke_json))

insert_pokemon()