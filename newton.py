# -*- coding: utf-8 -*-
import os, time, random

while True:
    from TALK import talk
    mess = input(': ').lower()

    if mess.find('стоп') != -1:
        exit(0)

    if (mess.find('без') != -1 and mess.find('звука') != -1) or mess.find('тишина') != -1:
        f = open('TALK.py', 'w')
        f.write("# -*- coding: utf-8 -*-\ndef talk(words):\n    words = None\n    pass")
        f.close()
        print('Done')

    if mess.find('звук') != -1 and mess.find('включи') != -1:
        f = open('TALK.py', 'w')
        f.write("# -*- coding: utf-8 -*-\nimport os\ndef talk(words):\n    os.system(" + '"' + 'say ' + '"' + " + words)")
        f.close()
        print('Done')

    if mess == ('ньютон') or mess.find('привет') != -1 or ((mess.find('Ньютон') != -1 or mess.find('ты') != -1) \
        and (mess.find('здесь') != -1 or mess.find('тут') != -1)):
        otvet = ['Приветствую вас, сэр', 'конечно сэр','К вашим услугам, сэр']
        talk(random.choice(otvet))

    if mess.find('температура') != -1 or mess.find('температурe') != -1 or mess.find('градусов') != -1:
        import weather

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
    #if mess.find('доллар') != -1 and ((mess.find('лей') != -1 or (mess.find('лея') != -1 and mess.find('курс') != -1))\
       # and( mess.find('молдав') != -1 or mess.find('румын') != -1)) or (mess.find('манат') != -1 or (mess.find('маната') != -1 \
        #and mess.find('курс')) and (mess.find('айзерба') != -1 or mess.find('туркмен') != -1)):
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import A


    if mess.find('сейчас') != -1 or mess.find('сегодня') != -1 or mess.find('щас') != -1 or mess.find('времени') != -1 \
        or mess.find('часов') != -1 or mess.find('время') != -1 or mess.find('минут') != -1:
        if mess.find('день') != -1 or mess.find('дата') != -1:
            import date_now
        else:
            print(time.ctime(time.time())[11:-5])
            hour_now = time.ctime(time.time())[11:-11]
            minutes_now = time.ctime(time.time())[14:-8]
            seconds_now = time.ctime(time.time())[17:-5]
            if mess.find('секунд') != -1:
                talk(hour_now + 'часов' + minutes_now + 'минут' + seconds_now + 'секунд')
            else:
                talk(hour_now + 'часов' + minutes_now + 'минут')

    if (mess.find('луны') != -1 or mess.find('луна') != -1 or mess.find('солнца') != -1 or mess.find('солнце') != -1 \
        or mess.find('марса') != -1 or mess.find('марс') != -1 or mess.find('юпитера') != -1 \
        or mess.find('юпитер') != -1 or mess.find('венеры') != -1 or mess.find('венера') != -1 \
        or mess.find('меркурия') != -1 or mess.find('меркурий') != -1 or mess.find('сатурна') != -1 \
        or mess.find('сатурн') != -1 or mess.find('нептуна') != -1 or mess.find('нептун') != -1 \
        or mess.find('урана') != -1 or mess.find('уран') != -1 or mess.find('плутона') != -1 \
        or mess.find('плутон') != -1 or mess.find('бетельгейзе') != -1 or mess.find('бетельгейза') != -1 \
        or mess.find('земли') != -1 or mess.find('земля') != -1) and mess.split('').find('до') != -1:
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import distance_of_planets


    if mess.find('горизонт') != -1 or mess.find('горизонта') != -1:
        if mess.find('земли') != -1 or mess.find('земле') != -1 or mess.find('земля') != -1:
            import lV2Rh2
        else:
            import lV2Rh


    if mess.find('уравнение') != -1:
        if mess.find('квадратное') != -1:
            import kvadratnoye_uravneniye2


    if mess.find('умножить') != -1 or mess.find('умножь') != -1 or mess.find('*') != -1:
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import multiplication_command

    if mess.find('разделить') != -1 or mess.find('раздели') != -1 or mess.find('/') != -1:
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import split_up_command

    if mess.find('плюс') != -1 or mess.find('сложить') != -1 or mess.find('сложи') != -1 or mess.find('+') != -1:
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import addition_command

    if mess.find('минус') != -1 or mess.find('вычесть') != -1 or mess.find('-') != -1:
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import subtraction_command

    if mess.find('процент') != -1 or mess.find('проценты') != -1 or mess.find('процентов') != -1:
        if mess.find('процентов') != -1 or mess.find('от') != -1:
            print('Введите еще раз число')
        import Percent

    if mess.find('компас') != -1 or (mess.find('стороны') != -1 and mess.find('света') != -1):
        print('		 С\n		 ↑\n	 З ←   → В\n		 ↓\n		 Ю')

    if ((mess.find('покажи') != -1 or mess.find('расскажи') != -1 or mess.find('скажи') != -1) \
        and mess.find('про')!= -1) or(mess.find('найди')!= -1 \
        and (mess.find('значение')!= -1 or mess.find('смысл')!= -1 \
        or mess.find('выражения')!= -1 or mess.find('предложения')!= -1 or mess.find('словосочетания')!= -1)) \
        or ((mess.find('что')!= -1 or mess.find('кто')!= -1) and (mess.find('такой')!= -1 or mess.find('значит')!= -1\
        or mess.find('означает')!= -1 or mess.find('такое')!= -1) ) or (mess.find('в') != -1 \
        and (mess.find('википедии') != -1 or mess.find('википедия') != -1)):
        file = open('A_command.py', 'w')
        file.write("# -*- coding: utf-8 -*-\nmess = '" + mess + "'")
        file.close()
        import wiki_book

    if mess.find('гдз') != -1 or mess.find('ulp') != -1:
        import gdz_russian
