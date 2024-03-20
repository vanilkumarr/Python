import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_naukri_jobs(search_query, location, num_pages=1, output_format="xlsx"):
    """
    Scrapes job postings from Naukri.com for a given search query and location.

    Args:
        search_query (str): The job title to search for.
        location (str): The location to filter by.
        num_pages (int, optional): The number of pages to scrape. Defaults to 1.
        output_format (str, optional): The output format for the data. Defaults to "xlsx".

    Returns:
        pd.DataFrame: A DataFrame containing the extracted job data.
    """

    base_url = "https://www.naukri.com/"
    search_url = f"{base_url}{search_query}-jobs-in-{location}"

    job_data = []
    for page_num in range(num_pages):
        page_url = f"{search_url}?pageNo={page_num + 1}"

        try:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract job titles, company names, descriptions, and links
            job_titles = soup.find_all("a", class_="title fw500 ellipsis")
            company_names = soup.find_all("a", class_="subTitleEllipsis")
            job_descriptions = soup.find_all("div", class_="descEllipsis")
            job_links = [title["href"] for title in job_titles]

            for title, company, description, link in zip(job_titles, company_names, job_descriptions, job_links):
                job_data.append({
                    "Job Title": title.text.strip(),
                    "Company Name": company.text.strip() if company else None,
                    "Job Description": description.text.strip() if description else None,
                    "Job Link": link,
                })
        except requests.exceptions.RequestException as e:
            print(f"Error scraping page {page_num + 1}: {e}")

    df = pd.DataFrame(job_data)

    if output_format == "xlsx":
        df.to_excel("naukri_job_postings.xlsx", index=False)
    elif output_format == "csv":
        df.to_csv("naukri_job_postings.csv", index=False)
    else:
        print(f"Invalid output format: {output_format}")

# Example usage
scrape_naukri_jobs("financial-analyst", "mumbai", num_pages=2, output_format="xlsx")