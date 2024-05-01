import requests

def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    pokemon = buscar_pokemon(nombre_pokemon)
    
    if pokemon:
        print("Pokémon encontrado:")
        print(f"Nombre: {pokemon['name']}")
        print(f"Imagen: {pokemon['sprites']['front_default']}")
        print("Estadísticas:")
        for stat in pokemon['stats']:
            print(f"{stat['stat']['name']}: {stat['base_stat']}")
        # Agrega el código para mostrar peso, tamaño, movimientos, habilidades y tipos
        # Guarda la información en un archivo JSON
    else:
        print("No se encontró el Pokémon.")

if __name__ == "__main__":
    main()
import os
import json

def guardar_pokemon(pokemon):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    nombre_archivo = f"pokedex/{pokemon['name']}.json"
    with open(nombre_archivo, "w") as archivo:
        json.dump(pokemon, archivo)

# Llama a esta función después de obtener los datos del Pokémon
guardar_pokemon(pokemon)
