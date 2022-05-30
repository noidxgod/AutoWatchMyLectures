import requests
from bs4 import BeautifulSoup
import time
import keyboard
import mouse
import random
url = 'https://www.youtube.com/playlist?list=PLVjnc1hF4kNOr27lO-zGGbFD5YsMgiI1I'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
soup_string = str(soup)
letters = ['Круто','Классно','Интересно','Полезно','Привет','Хорошо','Замечательно','Невероятно','Потрясающе','Красиво','Интригующе','Занимательно']
times = []
links = []
n = 13
time.sleep(10)
for i in range(0,len(times)):
    keyboard.press_and_release('F1')
    time.sleep(1)
    keyboard.press_and_release('F6')
    time.sleep(1)
    keyboard.write(str(links[i]))
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(6)
    keyboard.press_and_release('space')
    time.sleep(2)
    keyboard.press_and_release('home')
    time.sleep(2)
    keyboard.press_and_release('page_down')
    time.sleep(1)
    keyboard.press_and_release('page_down')
    time.sleep(1)
    keyboard.press_and_release('page_up')
    time.sleep(1)
    keyboard.press_and_release('page_up')
    time.sleep(0.5)
    keyboard.press_and_release('page_up')
    time.sleep(1)
    keyboard.press_and_release('page_up')
    time.sleep(0.5)



    keyboard.press_and_release('page_down')
    time.sleep(1)
    mouse.move(445, 445) #500 390
    time.sleep(1)
    mouse.click()
    time.sleep(1)

    keyboard.write(letters[n%12])
    n = n + 1
    time.sleep(1)
    keyboard.press_and_release('ctrl+enter')
    time.sleep(1)

    keyboard.press_and_release('space')
    time.sleep(0.5)

    for j in range(0, int(times[i])-10):
        time.sleep(1)

    keyboard.press_and_release('space')
    time.sleep(0.5)
    mouse.move(1315, 525) #986 465
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.move(1360, 570) #1021 512
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    keyboard.write('!!!')
    time.sleep(1)
    keyboard.press_and_release('ctrl+enter')
    time.sleep(random.randint(10, 20))
    keyboard.press_and_release('ctrl+w')
