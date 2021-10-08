import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# find unique id
results = soup.find(id='sf-accordion')

#find related div
elems = results.find_all('div', class_='sf-accordion__panel')

data = []

for elem in elems:
    ques_elem = elem.find('div', class_='sf-accordion__trigger-panel')
    ans_elem = elem.find('div', class_='sf-accordion__content')

    if None in (ques_elem, ans_elem):
        continue
    #print(ques_elem.text.strip())
    #print(ans_elem.text.strip())
    #print()

    data.append([ques_elem.text.strip(), ans_elem.text.strip()])

with open('covid_2.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    headers = ['Question','Answer']
    writer.writerow(headers)
    
    for dat in data:
        writer.writerow(dat)
