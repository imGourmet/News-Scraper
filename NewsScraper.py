import urllib.request
from bs4 import BeautifulSoup
from csv import writer





class Scraper:
    def __init__(self, site):
        self.site = site 

    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open('news.csv', 'w', encoding='utf8',newline='') as f:
            thewriter = writer(f)
            header = ['Newspaper','Headers ']
            thewriter.writerow(header)

            for tag in sp.find_all("a"):
                encab = [newspaper ,]
                url = tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    encab.append(url)
                    thewriter.writerow(encab) 

newspaper = input("Enter EXACT News URL :  ")

Scraper(newspaper).scrape() 








     