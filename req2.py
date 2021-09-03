import requests
import random
import time
import json
from cities import cities
from data import data
from words import words
from essential_generators import DocumentGenerator

url = 'https://prolifewhistleblower.com/anonymous-form/'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

gen = DocumentGenerator()

i=0
while (i < 1000):
    # populate payload
    payload = {}
    for key in data.keys():
        info = 'Placeholder'
        if key == 'txtarea':
            info = gen.paragraph()
        if key == 'txt1':
            info = gen.sentence()
        if key == 'txt6':
            info = 'Dr. ' + gen.name()
        if key == 'txt2':
            info = random.choice(list(cities.items()))[0]
        if key == 'txt3':
            info = 'Texas'
        if key == 'txt4':
            info = random.randint(10000, 99999)
        if key == 'txt5':
            info = random.choice(list(cities.items()))[1]
        payload[key] = info

    print(payload)

    response = requests.post(url, data=json.dumps(payload), headers=header)

    if response.status_code == 200:
        print('Success!')
    else:
        print('Fail.')
    
    i+=1
    time.sleep(5)

