import requests

pokemon_name = 'pikachu'
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
response = requests.get(url)

if response.ok:
    pokemon_data = response.json()
    abilities = pokemon_data['abilities']
    ability_names = [ability['ability']['name'] for ability in abilities]
    print(f"The abilities of {pokemon_name} are: {', '.join(ability_names)}")
else:
    print(f"Error fetching data for {pokemon_name}.")