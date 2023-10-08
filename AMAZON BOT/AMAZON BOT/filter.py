import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent  # fake user agent library

# random user-agent
ua = UserAgent()
user_agent = ua.random

headers = {
    'Connection': 'keep-alive',
    'rtt': '300',
    'downlink': '0.4',
    'ect': '3g',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
}


url = 'https://www.amazon.com/s?k=electronics/'
response = requests.get(url=url, headers=headers)

print(response.status_code)


# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)
# Find the filter section
filter_section = soup.select('div#filters')

print(filter_section)
# # Extract all the filters
# filters = filter_section.find_all(
#     'span', {'class': 'a-size-base a-color-base a-text-bold'})

# # Extract the filter names
# filter_names = [filter.text.strip() for filter in filters]

# # Save the filter names to a file
# with open('filters.txt', 'w', encoding='utf-8') as file:
#     for filter_name in filter_names:
#         file.write(filter_name + '\n')

# print('Filters saved to filters.txt')
