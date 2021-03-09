import requests
from bs4 import BeautifulSoup as bs4

from constants import CORONA_URL


def remove_empty(a: list):
    return list(filter(None, a))


html = requests.get(CORONA_URL + 'tokyo')
soup = bs4(html.content, 'html.parser')

# print(soup('strong')) = print(soup.find_all('strong'))
corona_infected = [tag.text[4:] for tag in soup('strong')]
print(corona_infected)

corona_infected = [tag.text.splitlines() for tag in soup(class_='dialog')]
corona_infected = list(map(remove_empty, corona_infected))
print(corona_infected)
# print(soup(class_='today'))
# print(soup(class_='compare today'))
# print(soup(class_='compare'))

# updated_time = soup.find('p').text
# print(updated_time)

html = requests.get(CORONA_URL + 'tottori')
soup = bs4(html.content, 'html.parser')

corona_infected = [tag.text.splitlines() for tag in soup(class_='dialog')]
corona_infected = list(map(remove_empty, corona_infected))
print(corona_infected)
# print(soup(class_='today'))
# print(soup(class_='compare'))

# updated_time = soup.find('p').text
# print(updated_time)
