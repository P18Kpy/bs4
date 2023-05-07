import requests
from bs4 import BeautifulSoup
import instaloader
url="https://www.instagram.com/{}/"
def parse_data(s):
    data={}
    s=s.split("-")[0]
    s=s.split("-p")
    data['Followers']=s[0]
    data['Following']=s[2]
    data['Posts']=s[4]
    return data

def scrape_data(username):
    r=requests.get(url.format(username))
    s=BeautifulSoup(r.text,"html.parser")
    meta=s.find("meta",property="og:description")
    z=meta.attr['content']
    return parse_data(z)

if __name__=="__main__":
    print(30*"=","instagram",30*"=")
    username=input("enter the id:")
    data=scrape_data(username)
    print()
    print(username,"having",data['Followers'],"followers")
    print(username,"having",data['Following'],"following")
    print(username,"having",data['Posts'],"posts")
    print(65*"=")
instag=instaloader.Instaloader()
instag.download_profile(username,profile_pic_only=True)