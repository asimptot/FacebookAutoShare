import pyautogui as pg
import time
import sys

sys.path.append(r'D:\\Projects\\Sosyal\\Facebook')

from init import *

kaunas = ["1430412867205426", "2825610674352955", "148605668543143", "1825794714335734", "731045517043874",
          "kilkennybitsandshits", "1587632794804215", "140111069525242", "301199310059406", "631488383595071",
          "350691288286807", "257652580976751", "teqsportskilkenny"]


def tab_at():
    for i in range(1, 10, 2):
        pg.press('tab')
    pg.press('enter')


def kaunas_yaz():
    pg.typewrite('Dear friends,\n'
                 'Kaunas City app is now on our mobile phone. About: \n\n'
                 '-News\n'
                 '-Sports\n'
                 '-Job Applications\n'
                 '-Concerts\n'
                 '-Exhibitions\n'
                 '-Opera\n'
                 '-Restaurants\n'
                 '-Weather Forecast\n'
                 '-Activities\n'
                 '-Hotels\n\n'
                 'You will now have easy access to information about :) To download it, just click the link below: \n\n'
                 'https://play.google.com/store/apps/details?id=kilkenny.city')


for i in range(len(kaunas)):
    open_browser()
    pg.typewrite('https://www.facebook.com/search/groups/?q=kaunas')
    pg.press('enter')
    time.sleep(10)
    pg.click(573, 317)
    time.sleep(2)
    tab_at()