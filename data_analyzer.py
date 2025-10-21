from textblob import TextBlob
import csv
all_polarities = []
with open ('breakingbad-positive-response.csv','r',newline='',encoding='utf-8') as data_file :
    data_reader = csv.reader(data_file)
    for para in data_reader :
        if para  and para[0].strip():
            analysis = TextBlob(para[0])
            polarity = analysis.sentiment.polarity
            all_polarities.append(polarity)
i=len(all_polarities)
if i < 80 :
    if all_polarities :
        average_polarity = sum(all_polarities)/i
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
        if average_polarity > 0.2 :
            print(f'Polarity is {average_polarity}')
            print("It is relatively positive")
        elif average_polarity < -0.2 :
            print(f'Polarity is {average_polarity}')
            print('It is relatively negative')
        else :
            print(f'Polarity is {average_polarity}')
            print('It is relatively neutral')           
       