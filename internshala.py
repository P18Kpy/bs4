import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://internshala.com/internships/big-data,data-science,front-end-development,machine-learning,python-django,wordpress-development-internship/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

internship_listings = soup.find_all("div", {"class": "internship_meta"})

job_titles = []
company_names = []
job_locations = []
application_dates = []
application_deadlines = []
links = []
for listing in internship_listings:
    job_title = listing.find("h4").text.strip()
    company_name = listing.find("a").text.strip()
    internship_link = "https://internshala.com" + listing.find("a")["href"]
    
 
    job_location_element = listing.find("span", {"class": "location"})
    if job_location_element:
        job_location = job_location_element.text.strip()
    else:
        job_location = "Not specified"
        
    
    application_date_element = listing.find("div", {"class": "apply_by"})
    if application_date_element:
        application_date_sibling = application_date_element.find_next_sibling("div")
        if application_date_sibling:
            application_date = application_date_sibling.text.strip()
        else:
            application_date = "Not specified"
        
        application_deadline_element = application_date_element.find("div") if application_date_element is not None else None
        if application_deadline_element:
            application_deadline = application_deadline_element.text.strip()
        else:
            application_deadline = "Not specified"
        
    else:
        application_date = "Not specified"
        application_deadline = "Not specified"
    
    job_titles.append(job_title)
    company_names.append(company_name)
    job_locations.append(job_location)
    application_dates.append(application_date)
    application_deadlines.append(application_deadline)
    links.append(internship_link)


df = pd.DataFrame({
    "Job Title": job_titles,
    "Company Name": company_names,
    "Job Location": job_locations,
    "Link": links,
    
})


print(df)
df.to_csv(" internship.csv ", index=False)