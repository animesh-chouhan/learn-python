import requests
import time

start_time = time.time()

with requests.Session() as s:
    for number in range(1, 151):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = s.get(url)
        pokemon = resp.json()
        print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))
