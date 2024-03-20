import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='css-xdandi')

# data = []

for article in articles[:10]:
    title = article.find('p', class_='indicate-hover').text.strip()

    print(title)
    # description = article.find('p', class_='css-1echdzn').text.strip()
    # data.append({'title': title, 'description': description})

# with open('nytimes.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['title', 'description'])
#     writer.writeheader()
#     writer.writerows(data)
