import requests
from bs4 import BeautifulSoup

URL = "https://www.coindesk.com/price/bitcoin/"
reponse = requests.get(URL) 
soup = BeautifulSoup(reponse.content,'html.parser') 
divTagContent = soup.find('div',{'class':'currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt'}) 
priceTag = divTagContent.find_all('span')
print(f"Current price of Bitcoin is {priceTag[0].text}")
#<span class="">21,284.41</span>