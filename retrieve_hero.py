from bs4 import BeautifulSoup
import re
import string
import requests

url = 'www.dota2.com/hero/rubick/'

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, 'html.parser')

mydivs = soup.findAll("div", { "class" : "abilitiesInsetBoxContent" })

t = mydivs[0].findAll("div", { "class" : "abilityFooterBoxLeft"})

text = t[0].get_text(strip=True)

print(text + "\n")

print(text.translate(string.ascii_lowercase))