from bs4 import BeautifulSoup
import requests


r=requests.get("http://go4mumbai.com/Mumbai_Bus_Route.php?busno=0010&bustype=RegularRoutes&busno1=0010&busno2=notselected&busno3=notselected&busno4=notselected")

#print(r.text)

html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')
span=soup.find("table", {"class" : "train"})
for row in span.findAll("tr"):
    cells = row.findAll("a")
    for cell in cells:
        print cell.text
        print("-----")
    

    
