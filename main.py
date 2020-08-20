import speech_recognition
import pyttsx3
import time
import wikipedia
import webbrowser
import time
import pickle
import os
import datetime
import random
import requests
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from tkinter import *
import tkinter
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import pyautogui


class AssistantSpeak(object):  # Ассистент читает voice

    def text_speak(text):
        # Инициализация
        text_to_speak = pyttsx3.init()  # Инициализация голосового движка
        text_to_speak.setProperty('voice', 'ru')  # Указываем используемый голос
        text_to_speak.setProperty('rate', 230)  # Скорость голоса'
        print(text)  # Вывод в консоль
        st1 = scrolledtext.ScrolledText(root)  # Меню текста
        st1.insert(INSERT, text.capitalize())
        st1.configure(bg='white')
        st1.place(x=0, y=75, height=250, width=275)
        text_to_speak.say(text)  # Читает текст
        text_to_speak.runAndWait()
        text_to_speak.stop()


class AssistantListens(object):

    def reply_system(recognizer, audio):

        try:

            voice = recognizer.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + voice)

            # Интерфейс
            st2 = scrolledtext.ScrolledText(root)
            st2.insert(INSERT, "Вы сказали: " + voice.capitalize())
            st2.configure(bg='white')
            st2.place(x=0, y=0, height=75, width=275)

            if voice.startswith('люба'):

                AssistantCommands.dialog(voice)
                AssistantCommands.search_in_wikipedia(voice)
                AssistantCommands.website_in_browser(voice)
                AssistantCommands.search_in_browser(voice)
                AssistantCommands.music(voice)
                AssistantCommands.clip(voice)
                AssistantCommands.windows_commands_in_cmd(voice)
                AssistantCommands.currency_transfer(voice)
                AssistantCommands.windows_program_open(voice)
                AssistantCommands.search_in_google_maps(voice)
                AssistantCommands.translate_iz_bufera_angl(voice)
                AssistantCommands.read_iz_bufera(voice)
                AssistantCommands.mouse(voice)
            else:
                pass

        except speech_recognition.UnknownValueError:
            print("Я вас не поняла")

        except speech_recognition.RequestError:
            print("Что-то с интернет соединением; {0}".format(speech_recognition.RequestError))


class AssistantCommands(AssistantSpeak, AssistantListens):
    dictionary = {
        "sites": ('люба ', 'любава ', 'любава', 'люба'),
        "action": ('включи', 'воспроизведи', 'открой', 'покажи', 'расскажи', 'в ', 'найди'),
        "who": ('как', 'где', 'кто такой'),
        "where": ('википедия', 'гугл', 'википедии', 'кто такой'),
        "all": (
            'люба ', 'любава ', 'любава', 'люба', 'включи', 'воспроизведи', 'открой', 'покажи', 'расскажи', 'в ',
            'найди', 'как', 'где', 'кто такой', 'гугл', 'википедии', 'что такое',),

        "песня": (
            'В лесу родилась елочка, '
            'В лесу она росла.'
            ' Зимой и летом стройная, '
            'Зеленая была. '

            'В лесу родилась елочка, '
            'В лесу она росла, '
            'Зимой и летом стройная, '
            'Зеленая была. '
            'Дальше не помню, ха-ха',

            'Расцветали яблони и груши,'
            ' Поплыли туманы над рекой. '
            'Выходила на берег Катюша, '
            'На высокий берег на крутой. '

            'Выходила, песню заводила '
            'Про степного сизого орла, '
            'Про того, которого любила, '
            'Про того, чьи письма берегла.',),
        "как дела": (
            'хорошо',
            'отлично',
            'замечательно'
        )

    }

    def quit(voice):
        if "конец работы" in voice:
            exit(0)


    def dialog(voice):

        if "спой мне песню" in voice:
            back_replay = random.choice(AssistantCommands.dictionary["песня"])
            AssistantSpeak.text_speak(back_replay)
        if "как дела" in voice:
            back_replay = random.choice(AssistantCommands.dictionary["как дела"])
            AssistantSpeak.text_speak(back_replay)
        if "что нового" in voice:
            back_replay = 'ничего'
            AssistantSpeak.text_speak(back_replay)
        if "что ты умеешь" in voice:
            back_replay = 'мои возможности можно просмотреть нажав кнопку О'
            AssistantSpeak.text_speak(back_replay)

    def currency_transfer(voice):
        text = voice
        try:

            b = BtcConverter()
            c = CurrencyRates()
            if 'евро в рубл' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_eur_rub = c.convert('EUR', 'RUB', value)
                perevod_eur_rub = '{:.2f}'.format(perevod_eur_rub)
                AssistantSpeak.text_speak('{} рублей'.format(perevod_eur_rub))

            elif 'долларов в рубл' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_usd_rub = c.convert('USD', 'RUB', value)
                perevod_usd_rub = '{:.2f}'.format(perevod_usd_rub)
                AssistantSpeak.text_speak('{} рублей'.format(perevod_usd_rub))

            elif 'руб. в евро' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_rub_eur = c.convert('RUB', 'EUR', value)
                perevod_rub_eur = '{:.2f}'.format(perevod_rub_eur)
                AssistantSpeak.text_speak('{} евро'.format(perevod_rub_eur))

            elif 'руб. в доллары' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_rub_usd = c.convert('RUB', 'USD', value)
                perevod_rub_usd = '{:.2f}'.format(perevod_rub_usd)
                AssistantSpeak.text_speak('{} долларов'.format(perevod_rub_usd))

            elif 'долларов в евро' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_usd_eur = c.convert('USD', 'EUR', value)
                perevod_usd_eur = '{:.2f}'.format(perevod_usd_eur)
                AssistantSpeak.text_speak('{} евро'.format(perevod_usd_eur))

            elif 'евро в доллар' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_eur_usd = c.convert('EUR', 'USD', value)
                perevod_eur_usd = '{:.2f}'.format(perevod_eur_usd)
                AssistantSpeak.text_speak('{} долларов'.format(perevod_eur_usd))

            elif 'руб. в биткоины' or 'руб. в bitcoin' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_rub_bts = b.convert_to_btc(value, 'RUB')
                AssistantSpeak.text_speak('{} биткоинов'.format(perevod_rub_bts))

            elif 'евро в биткоины' or 'евро в bitcoin' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_eur_bts = b.convert_to_btc(value, 'EUR')
                AssistantSpeak.text_speak('{} биткоинов'.format(perevod_eur_bts))

            elif 'доллар в биткоины' or 'доллар в bitcoin' in text:
                value = int(''.join(filter(lambda x: x.isdigit(), text)))
                perevod_bts_usd = b.convert_to_btc(value, 'USD')
                AssistantSpeak.text_speak('{} биткоинов'.format(perevod_bts_usd))
        except ValueError:
            pass


    def music(voice):
        if "включи музыку" in voice:
            AssistantSpeak.text_speak('Укажите директорию с музыкой')
            folder = os.listdir(os.chdir(askdirectory()))
            for files in folder:
                if files.endswith(".mp3"):
                    os.startfile(files)

    def clip(voice):
        if "включи видео" in voice:
            AssistantSpeak.text_speak('Укажите директорию с видео')
            folder = os.listdir(os.chdir(askdirectory()))
            for files in folder:
                if files.endswith(".mkv" or ".mp4"):
                    os.startfile(files)

    def search_in_wikipedia(voice):
        """Оставляем только ключевые слова для поиска в википедии.

        Остальные слова, относящиеся к словарю удаляем.

        """

        search = voice  # input
        search = search.lower()
        if 'в википедии' in search:
            for i in AssistantCommands.dictionary["all"]:
                if i in search:  # Если  ЗНАЧЕНИЕ i в КОМАНДЕ search
                    search = search.replace(i, "")  # удаляем ЗНАЧЕНИЕ i в строке

            wikipedia.set_lang("ru")  # Язык википедии
            summary = wikipedia.summary(search)  # Поиск в википедии search
            print(summary)  # Вывод найденной информации (500 символов)
            AssistantSpeak.text_speak(summary[0:350])

    def website_in_browser(voice):
        """Команда: (сайт + название) производит открытие нужного портала

        """

        sites_new = {'https://vk.com/': ["vk", "вк"],
                     'https://youtube.com/': ['youtube', 'ютуб'],
                     'https://ru.aliexpress.com/': ['алиэкспресс', 'алик'],
                     'http://google.com': ['гугл', 'google'],
                     'https://amazon.com': ['амазон', 'amazon'],
                     'https://apple.com/ru': ['apple', 'эпл'],
                     'https://yandex.ru': ['yandex', 'яндекс'],
                     'https://market.yandex.ru': ['яндекс маркет', 'yandex market', 'маркет'],
                     'http://sbmpei.ru/': ['смоленский сайт московского энергетического института', 'сф мэи']
                     }


        website = voice  # input
        website = website.lower()

        if 'открой ' in website:

            for k, v in sites_new.items():  # КЛЮЧ k, ВСЕ ЗНАЧЕНИЯ v, items возвращает (ключ, значение)
                for i in v:  # ЗНАЧЕНИЕ i перебирает из ВСЕХ ЗНАЧЕНИЙ v

                    if i in website.lower():  # Если  ЗНАЧЕНИЕ i в КОМАНДЕ SITE
                        open_tab = webbrowser.open_new_tab(k)  # Открываем сайт (КЛЮЧ)
                        time.sleep(0.1)
                        AssistantSpeak.text_speak('открываю {0}'.format(i))  # Воспроизводит ответ
                    else:
                        #  входит i)
                        open_tab = None
                        # Если сайт открылся, переходит к поиску следующего
                        if open_tab is not None:
                            #  Конец
                            break

    def search_in_browser(voice):
        """Команда: (сайт + название + ключевые слова для поиска) производит
        поиск в нужном портале

        """

        website = voice  # input
        website = website.lower()

        sites_search = {'https://vk.com/search?c%5Bq%5D=': ['vk', 'вк', 'вконтакте'],
                     'https://www.youtube.com/results?search_query=': ['youtube', 'ютуб', 'ютубе'],
                     'https://aliexpress.ru/af/%25D0%25BF%25D0%25BB%25D0%25B0%25D0%25BD%25D1%2588%25D0%25B5%25D1%25'
                     '82.html?d=y&origin=n&SearchText=': [
                         'aliexpress', 'алиэкспресс', 'алиэкспрессе', 'алик'],
                     'https://www.google.com/search?sxsrf=ALeKk0078Qq2y9sYoYIIrg8dR2BrMBJlPA%3A1589446926457&source'
                     '=hp&ei=Dgm9XomtGK2RmwXSo7joCA&q=': [
                         'гугл', 'google', 'гугле'],
                     'https://www.amazon.com/s?k=': ['амазон', 'amazon', 'амазоне'],
                     'https://market.yandex.ru/search?was_redir=1&rs=eJwzYgpgBAABcwCG&rt=10&text=': ['маркет',
                                                                                                     'яндекс маркет',
                                                                                                     'yandex market'],
                     'https://music.yandex.ru/search?text=': ['яндекс музыка', 'яндекс музыке', 'yandex music'],
                     'https://yandex.ru/search/?lr=12&text=': ['yandex', 'яндексе', 'яндекс', ],
                     }

        if 'найди в ' in website:

            for k, v in sites_search.items():  # КЛЮЧ k, ВСЕ ЗНАЧЕНИЯ v, items возвращает (ключ, значение)
                for i in v:  # ЗНАЧЕНИЕ i перебирает из ВСЕХ ЗНАЧЕНИЙ v
                    if i in website.lower():  # Если  ЗНАЧЕНИЕ i в КОМАНДЕ SITE
                        word_to_site = website.split(i)[1]  # Слово для поиска
                        k = k + word_to_site
                        open_tab = webbrowser.open_new_tab(k)  # Открываем сайт (КЛЮЧ)
                        time.sleep(0.1)
                        AssistantSpeak.text_speak('открываю в {0}{1}'.format(i, word_to_site))  # Воспроизводит ответ
                        return

    def search_in_google_maps(voice):
        """Команда: (сайт + название + ключевые слова для поиска) производит
        поиск в нужном портале

        """

        website = voice  # input
        website = website.lower()

        site_google_maps = 'https://www.google.ru/maps/dir/'

        if 'проложи мне путь ' in website:
            website = website.replace('от ', '', 1)  # Заменяем от
            website = website.replace('до ', '/', 1)  # Заменяем до
            word_to_site = website.replace('люба проложи мне путь ', '', 1)  # Заменяем кодовую фразу
            site_google_maps = site_google_maps + word_to_site  # Добавляем ключевые слова к url
            open_tab = webbrowser.open_new_tab(site_google_maps)  # Открываем сайт
            time.sleep(0.1)
            AssistantSpeak.text_speak('прокладываю путь в google maps')  # Воспроизводит ответ

    def translate_iz_bufera_angl(voice):
        """Функция предназначена для перевода выделенного текста на английский
        язык

        """

        i = "переведи выделенн"

        if i in voice:
            pyautogui.hotkey('ctrl', 'c')  # Нажатие ctrl + с
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'с')
            iz_bufera_obmena = tkinter.Tk().clipboard_get()  # Данные из буфера обмена копируем в переменную
            if re.search(r'[^а-яА-Я]', iz_bufera_obmena):

                url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
                key = 'trnsl.1.1.20200514T120743Z.32021358c1aecb82.139eb7f48700df0d93951bf04d9af318198f6a8e'
                text = iz_bufera_obmena
                lang = 'ru-en'
                reg = requests.post(url, data={'key': key, 'text': text, 'lang': lang}).json()
                AssistantSpeak.text_speak('перевод {0}'.format(reg['text']))

            else:
                pass
                """Функция предназначена для перевода выделенного текста на русский
                язык

                """
            if re.search(r'[^a-zA-Z]', iz_bufera_obmena):
                url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
                key = 'trnsl.1.1.20200514T120743Z.32021358c1aecb82.139eb7f48700df0d93951bf04d9af318198f6a8e'
                text1 = iz_bufera_obmena
                lang = 'en-ru'
                reg = requests.post(url, data={'key': key, 'text': text1, 'lang': lang}).json()
                AssistantSpeak.text_speak('перевод {0}'.format(reg['text']))
            else:
                pass

    def read_iz_bufera(voice):
        """Функция предназначена для чтения выделенного текста

        """
        i = "прочти выделенн"
        if i in voice:
            pyautogui.hotkey('ctrl', 'c', 'с')  # Нажатие ctrl + с

            iz_bufera_obmena = tkinter.Tk().clipboard_get()  # Данные из буфера обмена копируем в переменную

            AssistantSpeak.text_speak(iz_bufera_obmena)  # Читаем выделенный текст

    def mouse(voice):
        """Функция управления мышью

        """

        if "клик" in voice:
            pyautogui.click()

        if "doubleclick" in voice:
            pyautogui.doubleClick()

        if "правый клик" in voice:
            pyautogui.click(button='right')

        if "правый doubleclick" in voice:
            pyautogui.doubleClick(button='right')

        if "мышь влев" in voice:
            pyautogui.moveRel(-50, 0, 0.2)

        if "мышь прав" in voice:
            pyautogui.moveRel(50, 0, 0.2)

        if "мышь вверх" in voice:
            pyautogui.moveRel(0, -50, 0.2)

        if "мышь вниз" in voice:
            pyautogui.moveRel(0, 50, 0.2)

    def windows_program_open(voice):
        """Функция запуска приложения

        """

        w = voice  # input
        w = w.lower()
        sites = {
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Windows Media Player.lnk': ['медиа плеер',
                                                                                                          'виндовс медиа плеер'],
            'POWERPNT.EXE': ['поверпоинт', 'презентация'],
            'Wordpad.exe': ['вордпад'],
            'WINWORD.EXE': ['ворд', 'word'],
            'EXCEL.EXE': ['эксель', 'excel', 'таблицы'],
            'MSACCESS.EXE': ['аккес', 'акес', 'база данных', 'базу данных'],
            'C:\Program Files (x86)\Steam\Steam.exe': ['стим', 'steam'],
            'programopen\\Skype.lnk': ['скайп', 'skype'],
        }

        if 'открой ' in w:

            for k, v in sites.items():  # КЛЮЧ k, ВСЕ ЗНАЧЕНИЯ v, items возвращает (ключ, значение)

                for i in v:  # ЗНАЧЕНИЕ i перебирает из ВСЕХ ЗНАЧЕНИЙ v

                    if i in w.lower():  # Если  ЗНАЧЕНИЕ i в КОМАНДЕ SITE
                        open_tab = os.startfile(k)  # Открываем сайт (КЛЮЧ)
                        time.sleep(0.1)
                        AssistantSpeak.text_speak('открываю {}'.format(i))
                    else:
                        # не входит i
                        open_tab = None

                        if open_tab is not None:  # Если приложение открылось, переходит к поиску следующего
                            #  Конец
                            break

    def windows_commands_in_cmd(voice):
        """Функция запуска системного приложения

        """
        cmd = {'appwiz.cpl': ['программы и компоненты', 'программы'],
               'azman.msc': ['диспетчер авторизации'],
               'certmgr.msc': ['управление сертификатами'],
               'charmap.exe': ['таблицу символов'],
               'cleanmgr.exe': ['очистку дисков'],
               'cmd.exe': ['системную консоль'],
               'comexp.msc': ['служба компонентов', 'службы компонентов'],
               'compmgmt.msc': ['управление компьютером'],
               'ComputerDefaults': ['программы по умолчанию'],
               'control admintools': ['администрирование', 'администрирования'],
               'control color': ['управление цветом и внешним видом'],
               'control desktop': ['персонализацию', 'персонализацию компьютера'],
               'control folders': ['параметры папок'],
               'control fonts': ['управление шрифтами'],
               'control intl.cpl': ['управление языками'],
               'control keyboard': ['параметры клавиатуры', 'свойства клавиатуры'],
               'control mouse': ['свойства мыши', 'параметры мыши', 'свойства мышь'],
               'control mmsys.cpl': ['параметры звука'],
               'control netconnections': ['параметры сетевых адаптеров'],
               'control powercfg.cpl': ['параметры электропитания'],
               'control printers': ['устройства и принтеры'],
               'control schedtasks': ['планировщик заданий'],
               'control timedate.cpl': ['параметры даты и времени'],
               'control': ['панель управления'],
               'dccw.exe': ['калибровку цветов экрана'],
               'DevicePairingWizard.exe': ['добавление устройства'],
               'devmgmt.msc': ['диспетчер устройств'],
               'diskmgmt.msc': ['управление дисками'],
               'dpiscaling.exe': ['параметры экрана'],
               'eventvwr.msc': ['просмотр событий'],
               'explorer.exe': ['окно проводника', 'проводник'],
               'fsmgmt.msc': ['параметры общих папок'],
               'gpedit.msc': ['редактор локальной групповой политики'],
               'lusrmgr.msc': ['управление локальными пользователями и группами'],
               'magnify.exe': ['экранню лупу'],
               'powercfg.cpl': ['управление электропитанием'],
               'regedit.exe': ['реестр'],
               'resmon.exe': ['монитор ресурсов компьютера'],
               'shrpubw.exe': ['мастер создания общих ресурсов'],
               'sndvol.exe': ['микшер громкости'],
               'taskmgr.exe': ['диспетчер задач'],
               'utilman.exe': ['центр специальных возможностей']}


        commands_in_cmd = voice  # input
        commands_in_cmd = commands_in_cmd.lower()

        if 'открой ' in commands_in_cmd:

            for k, v in cmd.items():  # КЛЮЧ k, ВСЕ ЗНАЧЕНИЯ v, items возвращает (ключ, значение)

                for i in v:  # ЗНАЧЕНИЕ i перебирает из ВСЕХ ЗНАЧЕНИЙ v

                    if i in commands_in_cmd.lower():  # Если  ЗНАЧЕНИЕ i в КОМАНДЕ SITE
                        open_tab = os.system(k)  # Открываем сайт (КЛЮЧ)
                        time.sleep(0.1)
                        AssistantSpeak.text_speak('открываю {0}'.format(i))
                    else:

                        open_tab = None
                        # Если сайт открылся, переходим к поиску следующего
                        if open_tab is not None:
                            #  Конец
                            break


def start():
    """Функция старта приложения

    """
    with open('indexaudio.pickle', 'rb') as f:
        index_microphone = pickle.load(f)  # загружаем объект из файла

    # Recognizer полученный голос отправляет на сервера гугл
    r = speech_recognition.Recognizer()
    # получить аудио с микрофона
    m = speech_recognition.Microphone(device_index=int(index_microphone))
    """Настройки записи микрофона
    # r.non_speaking_duration = 0.3
    # r.phrase_threshold = 0.5
    # r.phrase_threshold = 0.5
    """

    with m as source:  # Берем Micriphone в качестве источника source_voice
        r.adjust_for_ambient_noise(source)  # В течение 0.2 секунды слушает фон

    r.listen_in_background(m, AssistantListens.reply_system)  # Остановка прослушивания
    # Приветствие в зависимости от текущего времени в системе
    if datetime.datetime.now().hour >= 6 and datetime.datetime.now().hour < 12:
        AssistantSpeak.text_speak('Доброе утро, Люба слушает...')
    elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 18:
        AssistantSpeak.text_speak('Добрый день, Люба слушает...')
    elif datetime.datetime.now().hour >= 18 and datetime.datetime.now().hour < 23.59:
        AssistantSpeak.text_speak('Добрый вечер, Люба слушает...')
    else:
        AssistantSpeak.text_speak('Доброй ночи, Люба слушает...')


def allaudio():
    os.startfile('inputaudio.exe')


def add_id():
    with open('indexaudio.pickle', 'wb') as f:
        index_microphone = id1
        pickle.dump(index_microphone, f)  # помещаем объект в файл




def root_acts():
    root_acts = Tk()
    root_acts.geometry('500x500')
    root_acts.configure(bg='gray22')
    root_acts.title('Основные возможности')

    #  Открытие сайта
    but4 = Button(root_acts,
                  text='Открой "название сайта/программы"',
                  anchor='w',
                  command=root_open)
    but4.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but4.place(x=0,
               y=0,
               height=25,
               width=500)

    #  Поиск на сайте
    but5 = Button(root_acts,
                  text='Найди в "название сайта" "поисковой запрос"',
                  anchor='w',
                  command=root_search_in_browser)
    but5.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but5.place(x=0,
               y=25,
               height=25,
               width=500)

    #  Открытие приложения
    but6 = Button(root_acts,
                  text='Перевод валют',
                  anchor='w',
                  command=root_currency_transfer)
    but6.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but6.place(x=0,
               y=50,
               height=25,
               width=500)

    #  Dialog
    but7 = Button(root_acts,
                  text='Диалог',
                  anchor='w',
                  command=root_dialog)
    but7.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but7.place(x=0,
               y=75,
               height=25,
               width=500)

    #  Music
    but8 = Button(root_acts,
                  text='Воспроизведение аудиофайла',
                  anchor='w',
                  command=root_music)
    but8.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but8.place(x=0,
               y=100,
               height=25,
               width=500)

    #  Clip
    but9 = Button(root_acts,
                  text='Воспроизведение видеофайла',
                  anchor='w',
                  command=root_clip)
    but9.configure(bd=1,
                   font=('Castellar', 12),
                   bg='white')
    but9.place(x=0,
               y=125,
               height=25,
               width=500)

    #  search_in_wikipedia
    but10 = Button(root_acts,
                   text='Поиск информации в википедии',
                   anchor='w',
                   command=root_search_in_wikipedia)
    but10.configure(bd=1,
                    font=('Castellar', 12),
                    bg='white')
    but10.place(x=0,
                y=150,
                height=25,
                width=500)

    #  search_in_google_maps
    but11 = Button(root_acts,
                   text='Прокладка пути в google maps',
                   anchor='w',
                   command=root_search_in_google_maps)
    but11.configure(bd=1,
                    font=('Castellar', 12),
                    bg='white')
    but11.place(x=0,
                y=175,
                height=25,
                width=500)

    #  translate_iz_bufera_angl
    but12 = Button(root_acts,
                   text='Перевод выделенного текста',
                   anchor='w',
                   command=root_translate_iz_bufera_angl)
    but12.configure(bd=1,
                    font=('Castellar', 12),
                    bg='white')
    but12.place(x=0,
                y=200,
                height=25,
                width=500)

    #  read_iz_bufera
    but13 = Button(root_acts,
                   text='Чтение выделенного текста',
                   anchor='w',
                   command=root_read_iz_bufera)
    but13.configure(bd=1,
                    font=('Castellar', 12),
                    bg='white')
    but13.place(x=0,
                y=225,
                height=25,
                width=500)

    #  mouse
    but14 = Button(root_acts,
                   text='Управление мышью с помощью голосовых команд',
                   anchor='w',
                   command=root_mouse)
    but14.configure(bd=1,
                    font=('Castellar', 12),
                    bg='white')
    but14.place(x=0,
                y=250,
                height=25,
                width=500)


def root_open():
    root_open = Tk()
    root_open.geometry('500x500')
    root_open.configure(bg='gray22')
    root_open.title('Возможности "открой"')

    st = scrolledtext.ScrolledText(root_open)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Перечень вариантов использования для команды "открой" : \n'
                      '\n'
                      'Сайты: \n'
                      '\n'
                      'вк \n'
                      'ютуб \n'
                      'алиэкспресс \n'
                      'гугл \n'
                      'амазон \n'
                      'яндекс \n'
                      'яндекс маркет \n'
                      'сф мэи \n'
                      '\n'
                      'Системные программы:\n'
                      '\n'
                      'программы и компоненты\n'
                      'диспетчер авторизации\n'
                      'управление сертификатами\n'
                      'таблицу символов\n'
                      'очистку дисков''системную консоль\n'
                      'служба компонентов\n'
                      'управление компьютером\n'
                      'программы по умолчанию\n'
                      'администрирование\n'
                      'администрирования\n'
                      'управление цветом и внешним видом\n'
                      'персонализацию компьютера\n'
                      'параметры папок\n'
                      'управление шрифтами\n'
                      'управление языками\n'
                      'свойства клавиатуры\n'
                      'свойства мыши\n'
                      'параметры звука\n'
                      'параметры сетевых адаптеров\n'
                      'параметры электропитания\n'
                      'устройства и принтеры\n'
                      'планировщик заданий\n'
                      'параметры даты и времени\n'
                      'панель управления\n'
                      'калибровку цветов экрана\n'
                      'добавление устройства\n'
                      'диспетчер устройств\n'
                      'управление дисками\n'
                      'параметры экрана\n'
                      'просмотр событий\n'
                      'проводник\n'
                      'параметры общих папок\n'
                      'редактор локальной групповой политики\n'
                      'управление локальными пользователями и группами\n'
                      'экранню лупу\n'
                      'управление электропитанием\n'
                      'реестр\n'
                      'монитор ресурсов компьютера\n'
                      'мастер создания общих ресурсов\n'
                      'микшер громкости\n'
                      'диспетчер задач\n'
                      'центр специальных возможностей\n'
                      '\n'
                      'Программы:\n'
                      '\n'
                      'PowerPoint\n'
                      'Word\n'
                      'Wordpad\n'
                      'Excel\n'
                      'Steam\n'
                      'Skype\n'
                      'Media Player\n'
              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_search_in_browser():
    root_serch_in_browser = Tk()
    root_serch_in_browser.geometry('500x500')
    root_serch_in_browser.configure(bg='gray22')
    root_serch_in_browser.title('Возможности "найди в"')

    st = scrolledtext.ScrolledText(root_serch_in_browser)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Перечень вариантов использования для команды "найди в" : \n'
                      '\n'
                      'вк + "запрос" \n'
                      'ютуб + "запрос" \n'
                      'алиэкспресс + "запрос" \n'
                      'гугл + "запрос"\n'
                      'амазон + "запрос"\n'
                      'яндекс + "запрос"\n'
                      'яндекс маркет + "запрос"\n'
                      'яндекс музыка + "запрос"\n'
                      '\n'
                      'Пример:\n'
                      'Любава, найди в ютуб музыку.\n'
                      'Любава, найди в яндексе новости.\n'
                      'Любава, найди в яндекс музыке популярное.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_currency_transfer():
    root_translate = Tk()
    root_translate.geometry('500x500')
    root_translate.configure(bg='gray22')
    root_translate.title('Обмен валют')

    st = scrolledtext.ScrolledText(root_translate)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Обмен валют : \n'
                      '\n'
                      'рубли в евро \n'
                      'рубли в доллары \n'
                      'рубли в биткоины \n'
                      '\n'
                      'евро в рубли \n'
                      'евро в доллары \n'
                      'евро в биткоины \n'
                      '\n'
                      'доллары в рубли'
                      'доллары в евро'
                      'доллары в биткоин'
                      '\n'
                      'Пример:\n'
                      'Любава, переведи 10000 долларов в рубли\n'
                      'Любава, 100 евро в доллары.\n'
                      'Любава, 50000 рублей в биткоины.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_dialog():
    root_dialog = Tk()
    root_dialog.geometry('500x500')
    root_dialog.configure(bg='gray22')
    root_dialog.title('Возможности при разговоре')

    st = scrolledtext.ScrolledText(root_dialog)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Голосовые команды в диалоге с системой : \n'
                      '\n'
                      'Пример:\n'
                      'спой мне песню\n'
                      'как дела\n'
                      'что нового\n'
                      'что ты умеешь\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_music():
    root_music = Tk()
    root_music.geometry('500x500')
    root_music.configure(bg='gray22')
    root_music.title('Воспроизведение аудиофайлов')

    st = scrolledtext.ScrolledText(root_music)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'При использовании голосовой команды "включи музыку": \n'
                      '1. Запускается диалоговое окно выбора директории.\n'
                      '2. Воспроизводятся все аудиофайлы формата mp3 в выбранной директории.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_clip():
    root_clip = Tk()
    root_clip.geometry('500x500')
    root_clip.configure(bg='gray22')
    root_clip.title('Воспроизведение видеофайлов')

    st = scrolledtext.ScrolledText(root_clip)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'При использовании голосовой команды "включи видео": \n'
                      '1. Запускается диалоговое окно выбора директории.\n'
                      '2. Воспроизводятся все видеофайлы формата mp4 и mkv в выбранной директории.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_search_in_wikipedia():
    root_serch_in_browser = Tk()
    root_serch_in_browser.geometry('500x500')
    root_serch_in_browser.configure(bg='gray22')
    root_serch_in_browser.title('Поиск информации в википедии')

    st = scrolledtext.ScrolledText(root_serch_in_browser)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Перечень вариантов использования для поиска "в википедии" : \n'
                      '\n'
                      'Пример:\n'
                      'Любава, найди в википедии кто такой Илон Маск\n'
                      'Любава, покажи в википедии бурый медведь\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_search_in_google_maps():
    root_search_in_google_maps = Tk()
    root_search_in_google_maps.geometry('500x500')
    root_search_in_google_maps.configure(bg='gray22')
    root_search_in_google_maps.title('Поиск пути в google maps')

    st = scrolledtext.ScrolledText(root_search_in_google_maps)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Построение пути осуществляется с помощью ключевой фразы "проложи мне путь": \n'
                      '\n'
                      'Пример:\n'
                      'Любава, проложи мне путь от переулка Марины Расковой до улицы Попова\n'
                      'Любава, проложи мне путь от Казани до Смоленска\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_translate_iz_bufera_angl():
    root_translate_iz_bufera_angl = Tk()
    root_translate_iz_bufera_angl.geometry('500x500')
    root_translate_iz_bufera_angl.configure(bg='gray22')
    root_translate_iz_bufera_angl.title('Перевод выделенного текста на английский или русский язык')

    st = scrolledtext.ScrolledText(root_translate_iz_bufera_angl)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Перевод выделенного текста осуществляется с помощью ключевой фразы "переведи выделенное": \n'
                      '\n'
                      'Пример:\n'
                      'Выделяем необходимый текст для перевода. Произносим: Люба, переведи выделенный текст.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_read_iz_bufera():
    root_read_iz_bufera = Tk()
    root_read_iz_bufera.geometry('500x500')
    root_read_iz_bufera.configure(bg='gray22')
    root_read_iz_bufera.title('Чтение выделенного текста системой')

    st = scrolledtext.ScrolledText(root_read_iz_bufera)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Чтение выделенного текста происходит с помощью ключевой фразы "прочти выделенное": \n'
                      '\n'
                      'Пример:\n'
                      'Выделяем необходимый текст для чтения.\n'
                      'Произносим: Люба, прочти выделенный текст.\n'
                      'Люба, прочти выделенное.\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


def root_mouse():
    root_mouse = Tk()
    root_mouse.geometry('500x500')
    root_mouse.configure(bg='gray22')
    root_mouse.title('Управление мышью с помощью голосовых команд')

    st = scrolledtext.ScrolledText(root_mouse)
    st.configure(font=('Castellar', 12))
    st.insert(INSERT, 'Управление мышью осуществляется с помощью следующих голосовых команд: \n'
                      '"клик" - воспроизводит левый клик мышью.\n'
                      '"даблклик" - воспроизводит двойной левый клик мышью.\n'
                      '"правый клик" - воспроизводит правый клик мышью.\n'
                      '"правый даблклик" - воспроизводит двойной правый клик мышью.\n'
                      '"мышь влево" - воспроизводит движение мыши влево.\n'
                      '"мышь вправо" - воспроизводит движение мыши вправо.\n'
                      '"мышь вверх" - воспроизводит движение мыши вверх.\n'
                      '"мышь вниз" - воспроизводит движение мыши вниз.\n'
                      '\n'
                      'Пример:\n'
                      'Люба, мышь вверх. "мышь перемещается вверх"\n'
                      'Люба, даблклик. "мышь воспроизводит левый даблклик"\n'

              )
    st.configure(bg='white')
    st.place(x=0, y=0, height=500, width=500)


root = Tk()
root.geometry('250x350')
root.configure(bg='gray22')
root.title('Люба')
# root.resizable(False, False)

but1 = Button(root, text='Прослушать', command=start)
but1.configure(bd=1, font=('Castellar', 12), bg='white')
but1.place(x=25, y=325, height=25, width=200)

but2 = Button(root, text='X', command=allaudio)
but2.configure(bd=1, font=('Castellar', 16), bg='white')
but2.place(x=225, y=325, height=25, width=25)

but3 = Button(root, text='O', command=root_acts)
but3.configure(bd=1, font=('Castellar', 16), bg='white')
but3.place(x=0, y=325, height=25, width=25)

root.mainloop()
# Бесконечный цикл работы
