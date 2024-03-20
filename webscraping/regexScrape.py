import requests
import re
from bs4 import BeautifulSoup
import csv


url = "https://zinduaschool.com/2024-hackathons-to-watch-out-for/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# print(response.content)

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

urls = re.findall(url_pattern, str(soup))

with open("links.csv", 'w') as file:
    writer = csv.writer(file)
    for url in urls:
        writer.writerow(url)
