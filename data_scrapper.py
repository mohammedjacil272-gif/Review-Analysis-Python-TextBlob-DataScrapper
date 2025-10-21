import requests 
from bs4 import BeautifulSoup
import time 
import csv
web_url="https://en.wikipedia.org/wiki/Thor:_The_Dark_World"
header_data={'User-agent':'EthicalScrapper/1.0'}
web = requests.get(web_url,headers=header_data)
time.sleep(3)
soup = BeautifulSoup(web.text,'html.parser')
target_element = soup.find(id='Critical_response')
csv_file= open("thor-neutral-response.csv",'w',newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Paragraph'])
paragraphs=[]
start_point = target_element.parent
if start_point:
    current_point=start_point.find_next_sibling()
    while current_point and current_point.text != 'h3':
        if current_point.name == 'p' and current_point.text.strip():
            paragraphs.append(current_point.text.strip())
        current_point = current_point.find_next_sibling()
if paragraphs:
    print('Exraction succesful')
    for i, para in enumerate(paragraphs):
        csv_writer.writerow([para])
    print('Writing to file succesful')
    print(f'{len(paragraphs)} paragraphs obtained and written')
else:
    print("Extraction Unsuccesful") 
csv_file.close()

