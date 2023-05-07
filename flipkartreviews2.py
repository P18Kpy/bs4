import requests
from bs4 import BeautifulSoup

# Replace <product_url> with the URL of the product you want to scrape reviews for
url = 'https://www.flipkart.com/audio-video/~cs-rhcb4z7hcr/pr?sid=0pm&collection-tab-name=Monitor+Headphones&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVcCB0byA4MCUgb2ZmIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiU3R1ZGlvIEhlYWRwaG9uZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJBQ0NHNUdVNlVUM0haU0pOIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_42738ac6-c1a6-41b9-89f4-304e2f9d8d3e_6.GPWXGD7P7DJW&ssid=8lx435w4gg0000001682261290206&otracker=hp_omu_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_2_6.dealCard.OMU_GPWXGD7P7DJW_4&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_NA_dealCard_cc_2_NA_view-all_4&cid=GPWXGD7P7DJW'

# Send a GET request to the product review page
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section containing all the reviews
reviews_section = soup.find('div', {'class': '_1YokD2 _3Mn1Gg col-9-12'})

# Find all the individual reviews within the reviews section
reviews = reviews_section.find('div', {'class': '_1AtVbE col-12-12'})

# Loop through each review and extract relevant information
for review in reviews:
    # Extract the rating
    rating = review.find('div', {'class': '_3LWZlK _1BLPMq'}).text
    
    # Extract the review title
    title = review.find('p', {'class': '_2-N8zT'}).text
    
    # Extract the review text
    text = review.find('div', {'class': 't-ZTKy'}).text
    
    # Print the extracted information
    print('Rating:', rating)
    print('Title:', title)
    print('Text:', text)
    print('\n')
