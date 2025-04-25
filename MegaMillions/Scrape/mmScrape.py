#imports, scrape, and gather the data
import requests
from bs4 import BeautifulSoup
import os

url = "https://catalog.data.gov/dataset/lottery-mega-millions-winning-numbers-beginning-2002"
response = requests.get(url)

if response.status_code == 200:    
    soup = BeautifulSoup(response.content, 'html.parser')       
    csv_link = None
    for link in soup.find_all('a', href=True):
        if 'csv' in link['href']:
            csv_link = link['href']
            break
    
    if csv_link:       
        if not csv_link.startswith('http'):
            csv_link = requests.compat.urljoin(url, csv_link)        
        
        csv_response = requests.get(csv_link)       
        filename = os.path.join(os.getcwd(), 'mega_winning_numbers.csv')
        with open(filename, 'wb') as file:
            file.write(csv_response.content)
        
        print(f"CSV file downloaded: {filename}")
    else:
        print("CSV link not found.")
else:
    print("Failed to retrieve the page.")    

