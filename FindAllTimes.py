import requests
from bs4 import BeautifulSoup
find = 'RECTANGULAR","audioQuality":"AUDIO_QUALITY_MEDIUM","approxDurationMs'       #68

url = ['https://www.youtube.com/watch?v=Q1lILNGAKwU',
'https://www.youtube.com/watch?v=L0AGrHOtbj4',
'https://www.youtube.com/watch?v=dFOCdTokhzw',
'https://www.youtube.com/watch?v=oa25s_6Sfn0',
'https://www.youtube.com/watch?v=7ilKdOrFJtE',
'https://www.youtube.com/watch?v=HCCqG-t9Mt0',
'https://www.youtube.com/watch?v=9hJo_fx_STs',
'https://www.youtube.com/watch?v=AocY41hgNd4',
'https://www.youtube.com/watch?v=2I7jXfd8og0',
'https://www.youtube.com/watch?v=cy038IV1A1M',
'https://www.youtube.com/watch?v=IIJVmmNa-ZE',
'https://www.youtube.com/watch?v=KIOr2TrH3RI',
'https://www.youtube.com/watch?v=AtBDdYjGuzk',
'https://www.youtube.com/watch?v=IOaE-GI5ntU',
'https://www.youtube.com/watch?v=xD5sbSjAY-Q',
'https://www.youtube.com/watch?v=1rL1XlS7oK4',
'https://www.youtube.com/watch?v=5MtogrlCKAI',
'https://www.youtube.com/watch?v=4zusy4IH-8U',
'https://www.youtube.com/watch?v=ZaiaLztaYW4',
'https://www.youtube.com/watch?v=FKVpai2DVXs']
times = []
for j in range(0,len(url)):
    response = requests.get(url[j])
    soup = BeautifulSoup(response.text, 'lxml')
    soup_string = str(soup)
    #print(soup_string)
    print(j)
    print(url[j])
    times.append(str(soup_string[soup_string.index(find)+71:soup_string.index(find)+71+17]))
    times[j] = int(''.join(x for x in times[j] if x.isdigit()))//1000

print (times)
print(len(times))
