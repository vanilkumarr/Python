import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.linkedin.com/jobs/search/?keywords=python%20developer'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

job_titles = []
for title in soup.find_all('h3', class_='result-card__title'):
    job_titles.append(title.text.strip())

df = pd.DataFrame({'Job Title': job_titles})
df.to_excel('job_details.xlsx', index=False)
