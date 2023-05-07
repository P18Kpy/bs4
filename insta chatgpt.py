import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/<username>'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the number of followers
followers = soup.select_one('[data-reactid="<react-id-of-followers-element>"]').text
print(f"Number of followers: {followers}")

# Extract the number of following
following = soup.select_one('[data-reactid="<react-id-of-following-element>"]').text
print(f"Number of following: {following}")



# Extract the profile picture URL
profile_pic_url = soup.select_one('[data-reactid="<react-id-of-profile-pic-element>"]')['src']
print(f"Profile picture URL: {profile_pic_url}")