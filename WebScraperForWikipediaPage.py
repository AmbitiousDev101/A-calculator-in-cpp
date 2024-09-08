from bs4 import BeautifulSoup
import requests

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Fetch the content of the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables with the class "wikitable"
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    # this is for the third table (index 2), you can change the index to display a different table
    if len(tables) >= 3:
        table = tables[2]

        
        headers = [header.get_text(strip=True) for header in table.find_all('th')]

        
        rows = []
        for row in table.find_all('tr')[1:]:  # Skip header row
            cols = row.find_all('td')
            cols = [col.get_text(strip=True) for col in cols]
            rows.append(cols)

        
        print("Headers:", headers)
        for row in rows:
            print("Row:", row)
    else:
        print("Less than three tables found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")