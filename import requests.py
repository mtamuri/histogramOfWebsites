import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def scrape_website(website_url):
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {
            'status_code': response.status_code,
            'response_time': response.elapsed.total_seconds()
        }
    except Exception as e:
        print(f"Error scraping website {website_url}: {e}")
        data = {'status_code': None, 'response_time': None}

    return data


# Get a list of the websites that you want to monitor.
website_urls = ['https://www.google.com/', 'https://www.yahoo.com/', 'https://www.bing.com/']

# Scrape the websites and store the data in a list.
website_data = []
for website_url in website_urls:
    data = scrape_website(website_url)
    website_data.append(data)

# Create a Pandas DataFrame to store the website data.
website_df = pd.DataFrame(website_data)

# Extract website name from URL
website_df['url_name'] = website_df['website_url'].apply(lambda x: x.split('//')[1].split('/')[0])

# Print the DataFrame
print(website_df)
