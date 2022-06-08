from urllib.request import urlopen,Request
import bs4
from bs4 import BeautifulSoup as bs
header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/malaysia", headers = header)
html = urlopen(req)
obj = bs(html,'html.parser')
new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
new_deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
print(new_cases)
