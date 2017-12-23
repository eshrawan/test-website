from bs4 import BeautifulSoup
import requests


r=requests.get("http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/larsentoubro/LT")
#print(r.text)

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')
span=soup.find_all("span", { "id" : "Bse_Prc_tick"})
print(span[0].text)

    
