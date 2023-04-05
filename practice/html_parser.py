import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://spotlightenglish.com/playlists/")
soup = bs(page.text, "html.parser")

elements = soup.select('div.megaphone-show-header h3.entry-title a')

titles = []
links = []
for element in elements:
    titles.append(element.text)
    links.append(element.attrs['href'])

df = pd.DataFrame({'titles': titles, 'links': links})

df.to_excel('./spotlightenglish.xlsx', sheet_name='Sheet1')