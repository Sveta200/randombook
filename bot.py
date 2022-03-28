from telebot import TeleBot as tb
from telebot import types
from book import getbook

#Переменные для получения случайной книги 
link = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\link.txt"
#По жанрам
detektivy = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\detektivy.txt"
priklyucheniya = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\priklyucheniya.txt"
uzhasy = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\uzhasy.txt"
fentezi = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\fentezi.txt"
mistika = "C:\\Users\\PC-5\\Desktop\\svetlana\\bot\\book\\mistika.txt"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 7.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

#Переменная ключа для работы бота
token = "5135744177:AAG_YhY-RxYBmRvu5JO2n28SAuyhLgXgl3c"
# Создаем экземпляр класса TeleBot (BotBook)
botBook = tb(token)
# Декоратор функцмм отлова сообщения от пользователя "start"
@botBook.message_handler(commands=["start"])
#Дописываем задекорированую функцию добавляя в нее свою функцию "start"
def start(message):
    #Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Добавляем в клавиатуру кнопки
    keyboard.add(types.KeyboardButton("Получить книгу"))
    keyboard.add(types.KeyboardButton("Выбрать жанр"))
    # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
    mes = botBook.send_message(message.chat.id, "Здравствуйте, я Бот, который рекомендует случайную книгу к чтению.", reply_markup=keyboard)
    # Определяем следующий шаг (Функцию) при срабатывание данной функции
    nextStep = botBook.register_next_step_handler(mes, sendBook)
# Следующий шаг (Функция которая сработает полсе) "sendBook"
def sendBook(message):
    if message.text == "Выбрать жанр":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Детективы"))
        keyboard.add(types.KeyboardButton("Привключения"))
        keyboard.add(types.KeyboardButton("Ужасы"))
        keyboard.add(types.KeyboardButton("Фэнтези"))
        keyboard.add(types.KeyboardButton("Мистика"))

        mes = botBook.send_message(message.chat.id, "Выберите жанр:", reply_markup=keyboard)
        nextStep = botBook.register_next_step_handler(mes, getjanrbook)
    else:
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(link, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)

def getjanrbook(message):
    if message.text == "Детективы":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(detektivy, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)
    elif message.text == "Привключения":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(priklyucheniya, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)
    elif message.text == "Ужасы":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(uzhasy, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)
    elif message.text == "Фэнтези":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(fentezi, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)
    elif message.text == "Мистика":
        #Создаем клавиатуру
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Добавляем в клавиатуру кнопки
        keyboard.add(types.KeyboardButton("Попробовать еще раз"))
        # Записываем в переменную book результат работы нашего модуля getbook который вытаскивает название и описание книги с сайта
        book = getbook.randomBook(mistika, header)
        # Отправляем ответ пользователю с чат id, сообщением, клавиатурой
        mes = botBook.send_photo(message.chat.id, photo=book["img"], caption=book["text"][0:100]+book["url"], reply_markup=keyboard, parse_mode="HTML")
        # Определяем следующий шаг (Функцию) при срабатывание данной функции
        nextStep = botBook.register_next_step_handler(mes, start)


botBook.polling()   



