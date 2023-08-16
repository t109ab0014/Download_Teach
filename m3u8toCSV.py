
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Function to get m3u8 URLs from a web page
def get_m3u8_urls(url):
    # Check if the URL is for 'webpro'
    if 'webpro' not in url:
        return []
    # Send a HTTP request to get the content of the web page
    response = requests.get(url)
    # Parse the web page's HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all script tags in the web page
    scripts = soup.find_all('script')
    # For each script tag, find the URLs of .m3u8 files
    m3u8_urls = []
    for script in scripts:
        if script.string:
            urls = re.findall(r'https://[^\s]*\.m3u8', script.string)
            m3u8_urls.extend(urls)
    # Remove duplicate URLs and return the first URL, if there are any
    return m3u8_urls[0] if m3u8_urls else "N/A"


webURL='/Users/ro9air/VScode/test_scratchTSMC/webURL.txt'
# Read all the URLs from 'webURL.txt'
with open(webURL, 'r') as file:
    data = [line.strip().split(',') for line in file.readlines()]

# For each row, get its m3u8 URLs (if the URL is for 'webpro') and store them in a list
rows = []
for row in data:
    url = row[-1]
    m3u8_urls = get_m3u8_urls(url)
    rows.append(row + [m3u8_urls])

# Create a DataFrame from the list of rows
df = pd.DataFrame(rows, columns=['時間', '股票', '檔名', '網址', 'm3u8_urls'])

# Write the DataFrame to 'output.csv'
df.to_csv('output.csv', index=False)
