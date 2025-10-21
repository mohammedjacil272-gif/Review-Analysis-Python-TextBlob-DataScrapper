# Purpose Of this program is to arrive to a side of review(positive, negative or neutral) based on the csv file given as input  
#import TextBlob to for NLP and sentiment scoring
#import csv to deal with file functions 
from textblob import TextBlob
import csv 
#create a list to store all polarity scores
all_polarities = []
#open csv file to read its content
with open ('breakingbad-positive-response.csv','r',newline='',encoding='utf-8') as data_file :
    #this is used to reading data off the csv file 
    data_reader = csv.reader(data_file)
    #read content and add polarity score to all_polarity list
    for para in data_reader :
        #checks if para exists and skips empty para
        if para  and para[0].strip():
            analysis = TextBlob(para[0])
            polarity = analysis.sentiment.polarity
            all_polarities.append(polarity)
i=len(all_polarities)
#based on size of sample choose parameter to evaluate sentiment of text/review and also print result based on average polarity
if i < 80 :
    if all_polarities :
        average_polarity = sum(all_polarities)/i
        #parameter is 0.05 due to relatively small sample size
        if average_polarity > 0.05 :
            print(f'Polarity is {average_polarity}')
            print("It is relatively positive")
        elif average_polarity < -0.05 :
            print(f'Polarity is {average_polarity}')
            print('It is relatively negative')
        else :
            print(f'Polarity is {average_polarity}')
            print('It is relatively neutral')
if i >= 80 :
    if all_polarities :
        average_polarity = sum(all_polarities)/i
        #parameter is 0.2 due to relatively large sample size
        if average_polarity > 0.2 :
            print(f'Polarity is {average_polarity}')
            print("It is relatively positive")
        elif average_polarity < -0.2 :
            print(f'Polarity is {average_polarity}')
            print('It is relatively negative')
        else :
            print(f'Polarity is {average_polarity}')
            print('It is relatively neutral')           
       