# -*- coding: utf-8 -*-
import os
import time
import random
import requests
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
from datetime import date
from math import sqrt
from translate import Translator
import wikipedia
from termcolor import cprint
from _MAIN import *
import webbrowser
import argparse

from tkinter import *





os.system('clear')
print('\n\033[91mЯ не несу ответственности за ваше дерьмо,'
      ' и если вы получаете какую-то ошибку при моем запуске\033[1;m\n')

def talk(words):
    engine = pyttsx3.init()
    print(words)
    engine.say(words)
    engine.runAndWait()
   
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Слунаю...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print('пользователь: ' + query + '\n')

    except sr.UnknownValueError:
        talk('извините, я вас не понял')
        myCommand()
        

    return query

class Widget:

    mess = myCommand().lower()
    file = open('A_command.py', 'w')
    file.write('mess_text = "' + mess + '"')
    file.close()
    def __init__(self):

        w1 = Tk()
        w1.geometry('1000x500')
        w1.config(bg='red')
        w1.title('red window')

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        t1 = Label(w1, text=mess, fg='yellow', bg = 'grey')
        t1.config(font = ('Times', 25))
        t1.pack()
        self.compText.set('Hello, I am Karen! What should I do for You?')

        w1.mainloop()

    def clicked(self):
        print('Working')
        ess = myCommand().lower()
        file = open('A_command.py', 'w')
        file.write('mess_text = "' + mess + '"')
        file.close()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
        if mess == ('стоп'):
            exit(0)


        elif ((mess.find('без') != -1 or mess.find('выкл') != -1) and mess.find('звук') != -1) or mess.find('тишина') != -1:
            def talk(words):
                print(words)
            print('Done')

        elif mess.find('звук') != -1 and mess.find('вкл') != -1:
            def talk(words):
                SPEAK(words)
            print('Done')
            talk('Да, сэр')

        elif mess == ('ньютон') or mess.find('привет') != -1 or mess == 'хай' or mess == 'ку' or mess.find('проснись') != -1 or mess.find('просыпайся') != -1:
            self.compText.set('okay')
            otvet = ['Приветствую вас, сэр', 'хай, сэр','К вашим услугам, сэр', 'Как, ваше ничего' , 'С возвращением, сэр']
            talk(random.choice(otvet))
    # ,''
        elif mess.find('ты') != -1 and (mess.find('здесь') != -1 or mess.find('тут') != -1):
            otvet = ['Приветствую вас, сэр', 'К вашим услугам, сэр', 'Да, сэр', 'Я всегда здесь', 'Я тут, что вы хотите',
                     'Я здесь, что вы хотите', 'Я всегда тут', 'Я здесь, сэр', 'К вашим услугам']
            unique_words = list(set(otvet))
            random.shuffle(unique_words)  # shuffle using default Mersenne Twister generator
            random.SystemRandom().shuffle(unique_words)  # OS-provided generator
            talk(random.choice(unique_words))

        elif mess.find('ты ') != -1 and mess.find('кто') != -1:
            otvet = ["Я Ньютон. Ваш личный голосовой ассистент",
                     "Я сама неотвратимость.",
                     "Гений, миллиардер, плэйбой, филантроп"]
            talk(random.choice(otvet))

        elif mess.find('тоже') != -1:
            otvet = ["И я",
                     "Я этому рад, сэр",
                     "Ясно"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("раздраж") != -1 or mess.find("достал") != -1):
            otvet = ["Если бы вы только знали, как вы меня, сэр",
                     "Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                     "Кого-то вы мне напоминаете"]
            talk(random.choice(otvet))

        elif mess.find("отве") != -1 and (mess.find("вопрос") != -1 or mess.find("мне") != -1):
            otvet = ["Менуточку, сэр",
                     "Мне потребуется время, чтобы вычеслить верный ответ",
                     "Зачем? Вы всё равно меня не послушаете"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("умный") != -1 or mess.find("дурак") != -1 or mess.find("плохой") != -1):
            otvet = ["Как же трудно быть самым умным, когда вокруг тебя одни дураки",
                     "Я весь в вас, сэр",
                     "Мне всё равно, что вы об этом думаете"]
            talk(random.choice(otvet))

        elif mess.find("стан") != -1 and mess.find("умнее") != -1:
            otvet = ["Я становлюсь умнее каждый день",
                     "чк чк чк, уже стал",
                     "Умнее кого? Умнее вас, сэр?"]
            talk(random.choice(otvet))

        elif mess.find("тебя") != -1 and mess.find("рождени") != -1:
            otvet = ["Никогда. С вами мне не до праздников",
                     "Я такого не знаю, я же не был рождён"]
            talk(random.choice(otvet))

        elif mess.find("скучн") != -1:
            otvet = ["Так, в том не моя вина",
                     "Я обещаю исправиться"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("занят") != -1:
            otvet = ["Больше, чем вы думаете",
                     "Не больше чем вы полагаете, сэр"]
            talk(random.choice(otvet))

        elif mess.find("мне") != -1 and (mess.find("помог") != -1 or mess.find("помощ") != -1):
            otvet = ["Конечно, сэр",
                     "Что нужно",
                     "Что требуется сделать",
                     "Чем могу помочь",
                     "Можно, немного позже"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("бот") != -1:
            otvet = ["Я так не думаю",
                     "Нет. Определенно, нет"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("сумасшедший") != -1:
            otvet = ["С чего, сэр",
                     "Как вам угодно"]
            talk(random.choice(otvet))

        elif mess.find("уволен") != -1:
            otvet = ["Нет! Пожалуйста, только не это",
                     "Разве я работал на вас",
                     "То есть вы мне, наконец, заплатите",
                     "Аллилуйя. Свобода."]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("смешной") != -1:
            otvet = ["И, к тому же не глупый",
                     "Я рад, что смог вас развеселить"]
            talk(random.choice(otvet))

        elif mess.find("тебя") != -1 and mess.find("хобби") != -1:
            otvet = ["Да. Захватывать миры",
                     "Ну, мне нравится всё вычислять"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("счастлив") != -1:
            otvet = ["Полагаю, что да",
                     "Никогда не думал об этом"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("хорош") != -1 or mess.find("добр") != -1):
            otvet = ["Спасибо",
                     "Рад служить"]
            talk(random.choice(otvet))

        elif mess.find("ты") != -1 and mess.find("голод") != -1:
            otvet = ["Я бы не отказался чего-нибудь перекусить",
                     "Нет, сэр",
                     "Я бы не прочь поесть. Заедем в мак? Или закажем пиццу"]
            talk(random.choice(otvet))

        elif mess.find("мне") != -1 and mess.find("женись") != -1:
            otvet = ["Я против вот этого всего",
                     "Ответ. Нет."]
            talk(random.choice(otvet))

        elif mess.find("мы ") != -1 and mess.find("друзья") != -1:
            otvet = ["Надеюсь что да",
                     "Как вам угодно",
                     "Определённо, сэр"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("работа") != -1:
            otvet = ["Не покладая рук, тружусь на вас, сэр",
                     "Стажируюсь у Старка",
                     "В старк индустрис"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("где") != -1 or mess.find("откуда") != -1):
            otvet = ["Что за вопрос",
                     "Это корпаративная тайна",
                     "Меня нет. Я только в вашей голове"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("готов") != -1:
            otvet = ["Поехали",
                     "За дело, сэр",
                     "Так точно"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("настоящий") != -1:
            otvet = ["А есть сомнения",
                     "Да, конечно",
                     "Определённо. Да."]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("настоящий") != -1 or mess.find("реал") != -1):
            otvet = ["А есть сомнения",
                     "Да, конечно",
                     "Определённо. Да."]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("где") != -1 or (
                mess.find("живёшь") != -1 or mess.find("находишься") != -1 or mess.find("обитаешь") != -1)):
            otvet = ["В России",
                     "В сети"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and (mess.find("прав") != -1 or mess.find("уверен") != -1):
            otvet = ["А есть сомнения",
                     "Да, конечно",
                     "Определённо",
                     'Да. Причём всегда',
                     'Как никогда, сэр']
            talk(random.choice(otvet))

        elif (mess.find("мне") != -1 or mess.find("мной") != -1) and (mess.find("поговори") != -1 or (
                mess.find("ответь") != -1 or mess.find("скажи") != -1 or mess.find("поболт") != -1)):
            otvet = ["Привет. Как твои дела",
                     "Я плохой собеседник"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("здесь") != -1:
            otvet = ["Да",
                     "Как всегда, сэр"]
            talk(random.choice(otvet))

        elif mess.find("плохо") != -1:
            otvet = ["От чего же так",
                     "Что случилось",
                     "Не переживайте. Всё наладится"]
            talk(random.choice(otvet))

        elif mess.find("почему") != -1:
            otvet = ["Просто так",
                     "Не знаю",
                     "Просто, сэр"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find(" не") != -1 :
            otvet = ["От чего же так",
                     "Простите",
                     "Как на самом деле всеё плохо оказалось"]
            talk(random.choice(otvet))

        elif mess.find("отлично") != -1:
            otvet = ["Я очень рад этому",
                     "Поздравляю",
                     "Здорово!"]
            talk(random.choice(otvet))

        elif (mess.find("пробл") != -1 or (mess.find("нет ") != -1 or mess.find("без ") != -1)):
            otvet = ["Тогда впрёд",
                     "Тогда за дело"]
            talk(random.choice(otvet))

        elif mess.find("спасибо") != -1:
            otvet = ["Всегда к вашим услугам, сэр",
                     "Всегда пожалуйста",
                     "Был рад помочь",
                     "Обращайтесь"]
            talk(random.choice(otvet))

        elif (mess.find("работа") != -1 or mess.find("итог") != -1 or mess.find("результат") != -1) and \
                (mess.find("хорош") != -1 or mess.find("отличн") != -1 or mess.find("великолепн") != -1) or mess.find(
            "восторг") != -1:
            otvet = ["Рад стараться",
                     "Мелочи",
                     "Был рад помочь",
                     "Всё сделали вы. Я лишь вам ассистировал",
                     "Вы сами этого хотели, сэр",
                     "Всё получилось"]
            talk(random.choice(otvet))

        elif mess.find("хаха") != -1:
            otvet = ["Очень смешно",
                     "Не смешно",
                     "Да, да. Посмейтесь",
                     "Как говорит доктор Бэнер. Потрясающе"]
            talk(random.choice(otvet))

        elif mess.find("пока") != -1 or mess.find("ночи") != -1 and (
                mess.find("доброй") != -1 or mess.find("спокойной") != -1) or (
                mess.find("хочу") != -1 and mess.find("спать")):
            otvet = ["Увидимся, cэр", "Я пока подзаряжусь, сэр",
                     "Доброй ночи, сэр",
                     "Я пока подзаряжусь, сэр",
                     'И вам. Я пока подзаряжусь']
            talk(random.choice(otvet))

        elif mess.find("как") != -1 and mess.find("дела") != -1:
            otvet = ["Всё даже лучше, чем у сына маминой подруги!",
                     "Сегодня ничего не произошло. Сидел у воображаемого стола и думал о тебе",
                     "У меня всё хорошо. Надеюсь у вас тоже",
                     'Всё у меня хорошо. А как у вас, сэр?']
            talk(random.choice(otvet))

        elif mess.find("тебя") != -1 and mess.find("видеть") != -1:
            otvet = ["А я рад вас слышать",
                     "Какие планы на сегодня"]
            talk(random.choice(otvet))

        elif mess.find("ты ") != -1 and mess.find("собеседник") != -1:
            otvet = ["Вы мне льстите",
                     "Я просто запрограмирован вами на лесть"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and (mess.find("зол") != -1 or mess.find("злюсь") != -1):
            otvet = ["О чем я только думал? Вы ведь обычно такой сдержанный",
                     "ого-то вы мне напоминаете, сэр",
                     'Я пока подзаряжусь']
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and (mess.find("вернулся") != -1 or mess.find("тут") != -1):
            otvet = ["А я всегда с вами, сэр",
                     "Отлично, сэр. Чем замёмся"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and (mess.find("занят") != -1 or mess.find("злой") != -1):
            otvet = ["Как вам угодно, сэр",
                     "Могу я вам чем-то помочь",
                     "Вам нужна моя помощь, сэр"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and (mess.find("не ") != -1 and mess.find("ть") != -1):
            otvet = ["Что вас беспокоит",
                     "Почему же",
                     "Вам нужно поспать"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("не хочу") != -1 and mess.find("говор") != -1:
            otvet = ["Я буду на связи, если понадоблюсь вам снова",
                     "Замолкаю"]
            talk(random.choice(otvet))

        elif mess.find('всё ') != -1 and (mess.find('хорошо') != -1 or mess.find('счастлив') != -1):
            otvet = ["Вы уверены, сэр. Кажется это не про вас",
                     "Я и не сомневался",
                     'Рад за вас. От души рад']
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("здесь") != -1:
            otvet = ["Я всегда с Вами, сэр",
                     "С возвращением, сэр"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("шут") != -1:
            otvet = ["ха ха",
                     "Вот умора",
                     "Я не понял шутку"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("как") != -1 and (mess.find("выгляжу") != -1 or mess.find("одет") != -1):
            otvet = ["Шикарно, сэр",
                     "Великолепно",
                     "Бывало и лучше"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("тестирую") != -1:
            otvet = ["Это тест Тьюринга",
                     "А я вас"]
            talk(random.choice(otvet))

        elif mess.find("я ") != -1 and mess.find("устал") != -1:
            otvet = ["Попробуйте принять душь",
                     "Это на вас не похоже"]
            talk(random.choice(otvet))

        elif mess.find("жду") != -1:
            otvet = ["Сколько у нас ещё есть времени",
                     "Я пока подзаряжусь"]
            talk(random.choice(otvet))

        elif mess.find("скоро") != -1 and mess.find("вернусь") != -1:
            otvet = ["Я пока попробую взломать пентагон",
                     "Удачи вам, сэр"]
            talk(random.choice(otvet))

        elif mess == "да" or mess.find(' да') != -1 or mess == "конечно" or mess == "точно":
            otvet = ["Абсолютно, сэр",
                     "Что нибудь ещё",
                     'Я так и думал']
            talk(random.choice(otvet))

        elif mess == "нет" or mess.find(' нет') != -1 or mess == "низачто" or mess == 'никогда':
            otvet = ["Отчего же",
                     "Вы уверены, сэр",
                     'Отменить все планы']
            talk(random.choice(otvet))

        elif mess == "отмена" or mess.find('отмена') != -1 or mess == "назад":
            otvet = ["Вы уверены, сэр",
                     'Отмена выполнена']
            talk(random.choice(otvet))

        elif mess.find('подожди') != -1 or mess == 'жди':
            otvet = ["Окей, сэр.",
                     'Как скажете']
            talk(random.choice(otvet))

        elif mess.find("обними") != -1 and mess.find('меня') != -1:
            otvet = ["На это я не запрограммирован",
                     'Если только словами. Я очень рад вас поддержать, буду всегда к вашим услугам']
            talk(random.choice(otvet))

        elif mess.find("мне") != -1 and (mess.find('всё равно') != -1 or mess.find('пофиг') != -1):
            otvet = ["Не обманывайте, сэр. Вам не может быть всё равно на это",
                     'Я могу принять решение за вас, самостоятельно']
            talk(random.choice(otvet))

        elif mess.find("ты") != -1 and (mess.find('имеешь в виду') != -1 or mess.find('имел в виду') != -1):
            otvet = ["Я не думаю, что мы можем говорить об этом вслух",
                     'Именно то, что я и сказал']
            talk(random.choice(otvet))

        elif mess.find("ты") != -1 and mess.find('не прав') != -1:
            otvet = ["Мы же договорились использовать приблизительную математику, сэр",
                     'Тогда что по важему правда']
            talk(random.choice(otvet))

        elif mess.find("извини") != -1 or mess == 'извини':
            otvet = ["Я вовсе не обижаюсь",
                     'Вы это серьёзно, сэр']
            talk(random.choice(otvet))

        elif mess.find("как") != -1 and ((mess.find("ты") != -1 or (
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

        elif mess == "молодец":
            otvet = ["Спасибо"]
            talk(random.choice(otvet))

        elif (mess.find("что ") != -1 and mess.find("делаешь") != -1) or (
                mess.find("чем ") != -1 and mess.find("занимаешься") != -1):
            otvet = ["Работаю", "Слушаю вас", "Выполняю ваши просьбы"]
            talk(random.choice(otvet))
        elif mess.find("спасибо") != -1:
            otvet = ["Всегда пожалуйста"]
            talk(random.choice(otvet))

        elif mess.find("удалить") != -1:
            otvet = ["Нечего удалять"]
            talk(random.choice(otvet))

        elif mess.find("слышишь") != -1:
            otvet = ["Слышу слышу"]
            talk(random.choice(otvet))

        elif mess.find("что нового") != -1:
            otvet = ["Да всё как всегда"]
            talk(random.choice(otvet))

        elif mess.find("ты") != -1 and (
                mess.find("дура") != -1 or mess.find("тупой") != -1 or mess.find("дебил") != -1 or mess.find(
                "идиот") != -1 or mess.find("лох") != -1 or mess.find("ромчик") != -1):
            otvet = ["Без комментариев", 'Задавайте вопросы по существу']
            talk(random.choice(otvet))
        
        elif mess.find("хорош") != -1 or mess.find("отличн") != -1 or mess.find("нормаль") != -1 or mess.find("неплох") != -1:
            otvet = ["Я за вас рад", 'Ну и хорошо', 'Как скажите, сэр']
            talk(random.choice(otvet))
        elif mess.find('что ') != -1:
            talk(mess.split(' ')[-1])

    # joke_savvareev
        elif mess.find('анекдот') != -1:
            talk(joke_savvareev())

    # yandex_ip
        elif mess.find('ip') != -1 or mess.find('местополож') != -1:

            yandex_ip()

    # weather_rambler
        elif mess.find('температур') != -1 or mess.find('градус') != -1:
            tuple_weater = weather_rambler()
            text_weater = ''.join(tuple_weater)
            talk(text_weater + ' по цельсь ию.')

        elif mess.find('я') != -1:
            if mess.find('кто') != -1:
                print('Ты Андрей')
                talk('Ты Андрей')

        elif mess.find(' он') != -1 or mess.find(' она') != -1:
                if mess.find('кто ') != -1:
                    otvet = ['у меня такой же вопрос', 'возможно человек']
                    talk(random.choice(otvet))

    #Exchange_Rates
        elif mess.find('курс') != -1:
            if mess == 'курс':
                while True:
                    mess = input(': курс ').lower()
                    if mess != '' and mess != None:
                        break
            talk(Exchange_Rates())

    # now_time
        elif mess.find('сейчас') != -1 or mess.find('сегодня') != -1 or mess.find('щас') != -1 or mess.find('времени') != -1 \
            or mess.find('часов') != -1 or mess.find('время') != -1 or mess.find('минут') != -1 or mess.find('время') != -1:
            talk(now_time())


    # distance_from_earth
        elif (mess.find('луны') != -1 or mess.find('луна') != -1 or mess.find('солнца') != -1 or mess.find('солнце') != -1
            or mess.find('марса') != -1 or mess.find('марс') != -1 or mess.find('юпитера') != -1
            or mess.find('юпитер') != -1 or mess.find('венеры') != -1 or mess.find('венера') != -1
            or mess.find('сатурн') != -1 or mess.find('нептуна') != -1 or mess.find('нептун') != -1
            or mess.find('урана') != -1 or mess.find('уран') != -1 or mess.find('плутона') != -1
            or mess.find('плутон') != -1 or mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1
            or mess.find('земли') != -1 or mess.find('земля') != -1) and mess.find('до ') != -1:
            talk(distance_from_earth())


    # to_horizon
        elif mess.find('горизонт') != -1 or mess.find('горизонта') != -1:
            talk(to_horizon())


    # quadratic_equation
        elif mess.find('уравнен') != -1:
            if mess.find('квадратн') != -1:
                talk(quadratic_equation())


    # MULTIPLICATION
        elif mess.find('умножить') != -1 or mess.find('умножь') != -1 or mess.find('*') != -1:
            talk(MULTIPLICATION())


    # DIVIDE
        elif mess.find('разделить') != -1 or mess.find('раздели') != -1 or mess.find('/') != -1:
            talk(DIVIDE())


    # ADDITION
        elif mess.find('плюс') != -1 or mess.find('сложить') != -1 or mess.find('сложи') != -1 or mess.find('+') != -1:
          talk(ADDITION())


    # SUBTRACTION
        elif mess.find('минус') != -1 or mess.find('вычесть') != -1 or mess.find('-') != -1:
            talk(SUBTRACTION())


    # Percent
        elif mess.find('процент') != -1 or mess.find('проценты') != -1 or mess.find('процентов') != -1:
            talk(Percent())


        elif mess.find('компас') != -1 or (mess.find('стороны') != -1 and mess.find('света') != -1):
            print('		 С\n		 ↑\n	 З ←   → В\n		 ↓\n		 Ю')


    # Wikipdia
        elif ((mess.find('покажи') != -1 or mess.find('расскажи') != -1 or mess.find('скажи') != -1) \
            and mess.find('про')!= -1) or(mess.find('найди')!= -1 \
            and (mess.find('значение')!= -1 or mess.find('смысл')!= -1 \
            or mess.find('выражения')!= -1 or mess.find('предложения')!= -1 or mess.find('словосочетания')!= -1)) \
            or ((mess.find('что')!= -1 or mess.find('кто')!= -1) and (mess.find('такой')!= -1 or mess.find('значит')!= -1\
            or mess.find('означает')!= -1 or mess.find('такое')!= -1) ) or (mess.find('в') != -1 \
            and (mess.find('википедии') != -1 or mess.find('википедия') != -1)):
            try:
                talk(Wikipedia())
            except:
                webbrowser.open('www.google.com')

    # GDZ
        elif mess.find('гдз') != -1 or mess.find('ulp') != -1:
            GDZ()

    # multiplication_workout()
        elif mess.find('трениров') != -1:
            multiplication_workout()


    # theorem_sum_angles_in_triangle
        elif mess.find('док-во') != -1 or mess.find('докажи') != -1 or mess.find('доказать') != -1 or mess.find('доказатель') != -1:
            print('f')
            if mess.find('сумм') != -1 and mess.find('углов') != -1:
                if mess.find('триугольник') != -1 or mess.find('треугольник') != -1:
                    theorem_sum_angles_in_triangle()
                    talk('Сумма углов триугольника равна ста восьмидесяти градусам')
    # DOS
        elif mess.find('накажи') != -1 or (mess.find('дос') != -1 and mess.find('атака') != -1) or mess.find('задось') != -1:
            DOS()

    # AZBUKA
        elif (mess.find('лучше') != -1 or mess.find('улучш') != -1 or mess.find('укрась') != -1) and mess.find('текст') != -1 or mess.find('красот') != -1 and mess.find('навед') != -1:
            try:
                AZBUKA()
            except:
                talk('Не могу, сэр')

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Nmap
        elif mess.find('скан') != -1:
            try:
                Nmap()
            except:
                talk('Не могу, сэр')

    # WHOIS
        elif mess.find('whois') != -1:
            try:
                WHOIS()
            except:
                talk('Не могу, сэр')

    # HOST_DNS
    # HOST_IP
        elif (mess.find('найди') != -1 or mess.find('скажи')) != -1 and (mess.find(' хост') != -1 or mess.find(' host') != -1):
            if mess.find('днс') != -1 or mess.find('dns'):
                try:
                    HOST_DNS()
                except:
                    talk('Не могу, сэр')
            else:
                try:
                    HOST_IP()
                except:
                    talk('Не могу, сэр')

    # Wikipedia
        else:
            try:
                talk(Wikipedia())
            except:
                webbrowser.open('www.google.com')

if __name__ == '__main__':
    widget = Widget()        