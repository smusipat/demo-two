import requests
from bs4 import BeautifulSoup

# Define the URL and search value
url = 'https://egov.uscis.gov/'
search_value = 'EAC123556389'

# Send a POST request with the search value
response = requests.post(url, data={'appReceiptNum': search_value})

# Parse the response HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the status element
status_element = soup.find('div', class_='current-status-sec')

# Extract the status text
status = status_element.text.strip()

# Print the status
print('Status:', status)
