#Purpose : To find the data from review section of wikipedia/other website and write it in a csv file
#import requests to send HTTP requests and download web pages
#import BeautifulSoup to parse HTML and extract specific data
#import time to add a pause between the requests sent to a website
#import csv to deal with file functions
import requests 
from bs4 import BeautifulSoup
import time 
import csv
#create variable to store the website link
web_url="add your wikipedia_link here "
#create a variable to store agent data
header_data={'User-agent':'EthicalScrapper/1.0'}
#create a variable to store data obtained from get() that fetches page content
web = requests.get(web_url,headers=header_data)
# add a delay between requests to a page 
time.sleep(3)
#parse the information obtained and create a variable to store it
soup = BeautifulSoup(web.text,'html.parser')
#create a starting point 
target_element = soup.find(id='Critical_response')
#create and open the csv file to store the information that is going to be extracted 
csv_file= open('dummy_file.csv','w',newline='', encoding='utf-8')
#use csv.writer to write content
csv_writer = csv.writer(csv_file)
#create a row in csv file 
csv_writer.writerow(['Paragraph'])
#create a list to store the information/paragraphs extracted
paragraphs=[]
#find the parent of the targeted portion to begin
start_point = target_element.parent
#check if a starting point exists
if start_point:
    #find the next sibling/element that comes after the target
    current_point=start_point.find_next_sibling()
    #create a loop to find a paragraph to extract 
    while current_point and current_point.text != 'h3':
        #check if the paragraph is empty
        if current_point.name == 'p' and current_point.text.strip():
            # add the paragraph to the list
            paragraphs.append(current_point.text.strip())
        #find the next element    
        current_point = current_point.find_next_sibling()
#check is the list is empty
if paragraphs:
    print('Exraction succesful')
    # add the contents from the list to the csv file using a loop
    for i, para in enumerate(paragraphs):
        csv_writer.writerow([para])
    print('Writing to file succesful')
    print(f'{len(paragraphs)} paragraphs obtained and written')
else:
    print("Extraction Unsuccesful")
#close the opened csv file
csv_file.close()

