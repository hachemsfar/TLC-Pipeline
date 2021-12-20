from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import requests



def Extract():
    url='https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html')
    filesnames_list=[]  

    i=soup.find_all("div", {"class": "faq-answers"})[0].find_all("a", {"title": "Yellow Taxi Trip Records"})[-1]
    filesnames_list.append("Yellow Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
    r = requests.get(i.get('href'), allow_redirects=True)
    open( "Yellow Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)

    
    i=soup.find_all("div", {"class": "faq-answers"})[0].find_all("a", {"title": "Green Taxi Trip Records"})[-1]
    filesnames_list.append("Green Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
    r = requests.get(i.get('href'), allow_redirects=True)
    open("Green Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
   

    i=soup.find_all("div", {"class": "faq-answers"})[0].find_all("a", {"title": "For-Hire Vehicle Trip Records"})[-1]
    filesnames_list.append("For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
    r = requests.get(i.get('href'), allow_redirects=True)
    open("For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
   

    i=soup.find_all("div", {"class": "faq-answers"})[0].find_all("a", {"title": "High Volume For-Hire Vehicle Trip Records"})[-1]
    filesnames_list.append("High Volume For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
    r = requests.get(i.get('href'), allow_redirects=True)
    open("High Volume For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
        
   
    return(filesnames_list)


def Extract_all():
    url='https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html')

   
    filesnames_list=[]  
    
    for i in soup.find_all("a", {"title": "Yellow Taxi Trip Records"})[:33]:
        filesnames_list.append("Yellow Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
        r = requests.get(i.get('href'), allow_redirects=True)
        open("Yellow Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
        

    
    for i in soup.find_all("a", {"title": "Green Taxi Trip Records"})[:33]:
        filesnames_list.append("Green Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
        r = requests.get(i.get('href'), allow_redirects=True)
        open("Green Taxi Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
  
    
    for i in soup.find_all("a", {"title": "For-Hire Vehicle Trip Records"})[:33]:
        filesnames_list.append("For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
        r = requests.get(i.get('href'), allow_redirects=True)
        open("For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)

    
    for i in soup.find_all("a", {"title": "High Volume For-Hire Vehicle Trip Records"})[:33]:
        filesnames_list.append("High Volume For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]))
        r = requests.get(i.get('href'), allow_redirects=True)
        open("High Volume For-Hire Vehicle Trip Records/raw/"+str(i.get('href').split("/trip+data/")[1]), 'wb').write(r.content)
    
    return(filesnames_list)

if __name__ == '__main__':
    filesnames_list=Extract_all()