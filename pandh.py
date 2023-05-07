from bs4 import BeautifulSoup
import requests

#url,req,soup
url="https://www.techieempire.tech/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.find_all('h6'))