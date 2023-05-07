import requests
from bs4 import BeautifulSoup
import pandas as pd

# send a GET request to the Internshala website and retrieve the HTML content
url = "https://internshala.com/internships/work-from-home-jobs"
response = requests.get(url)
html_content = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# find all the internship listings on the page
internship_listings = soup.find_all("div", {"class": "internship_meta"})

# create empty lists to store the information
job_titles = []
company_names = []
job_locations = []
application_dates = []
application_deadlines = []

# loop through each internship listing and extract the relevant information
for listing in internship_listings:
    job_title = listing.find("h4").text.strip()
    company_name = listing.find("a").text.strip()
    
    # find the job location
    job_location_element = listing.find("span", {"class": "location"})
    if job_location_element:
        job_location = job_location_element.text.strip()
    else:
        job_location = "Not specified"
        
    # find the application date
    application_date_element = listing.find("div", {"class": "apply_by"}).find_next_sibling("div")
    if application_date_element:
        application_date = application_date_element.text.strip()
    else:
        application_date = "Not specified"
    
    # find the application deadline
    application_deadline_element = listing.find("div", {"class": "apply_by"}).find("div")
    if application_deadline_element:
        application_deadline = application_deadline_element.text.strip()
    else:
        application_deadline = "Not specified"
    
    # append the information to the respective lists
    job_titles.append(job_title)
    company_names.append(company_name)
    job_locations.append(job_location)
    application_dates.append(application_date)
    application_deadlines.append(application_deadline)

# create a Pandas DataFrame to store the information
df = pd.DataFrame({
    "Job Title": job_titles,
    "Company Name": company_names,
    "Job Location": job_locations,
    "Application Date": application_dates,
    "Application Deadline": application_deadlines
})

# print the DataFrame
print(df)
