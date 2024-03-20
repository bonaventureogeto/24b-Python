# fetch the following data from the rick and morty API:
# - 20 characters
# - 20 locations
# - 20 episodes
# and save it in a CSV file
import requests

url = "https://rickandmortyapi.com/api/episode"

response = requests.get(url)

print(response.json())
