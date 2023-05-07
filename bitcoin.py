import requests
from bs4 import BeautifulSoup
URL = "https://coinmarketcap.com/currencies/bitcoin/" 
reponse = requests.get(URL) 
soup = BeautifulSoup(reponse.content,'html.parser') 
divTagContent = soup.find('div',{'class':'priceValue'}) 
priceTag = divTagContent.select_one('span') 
print(f"Current price of Bitcoin is {priceTag.text}")