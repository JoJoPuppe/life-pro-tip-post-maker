import requests
from bs4 import BeautifulSoup


url = "https://www.reddit.com/r/LifeProTips/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("article")
face_plates = soup.find_all("faceplate-number")
print(titles)
