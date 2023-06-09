import telebot
from random import shuffle
from telebot import types


bot = telebot.TeleBot('5773517270:AAGtAU5mMJ17pLBliEfP0AQnZJE6fboi4gM') # токен

@bot.message_handler(commands=['start']) # Декоратор @message_handler реагирует на входящие сообщение.
def start(message):
    mess = f'Что нового ты хочешь узнать о экологии??'
    #bot.send_message(message.chat.id, mess) # через сообщение обращается к чату, а чат к айди
    markup = types.ReplyKeyboardMarkup()
    button0 = types.KeyboardButton('ЭКОпомощь')
    button1 = types.KeyboardButton('Красная книга ПО')
    button2 = types.KeyboardButton('Пункты приема вторсырья')
    button3 = types.KeyboardButton('Это от тебя зависит')
    markup.add(button0, button1, button2, button3)
    bot.send_message(message.chat.id, mess, reply_markup=markup)




@bot.message_handler()
def get_message_from_user(message):
    if message.text == 'ЭКОпомощь':
        #table = 'abcdefghijklmnopqrsyuvwxyz'
        table = 'abcdefghij'
        note = []
        data = ['<b>В природе нет ничего бесполезного.</b> <em> Мишель Монтень </em>',
                 '<b>В природе все мудро продумано и устроено, всяк должен заниматься своим делом, и в этой мудрости — высшая справедливость жизни.</b> <em>Леонардо да Винчи</em>',
                '<b>Потому мы радуемся, попадая в природу, что тут мы приходим в себя.</b> <em>Пришвин М. М.</em>',
                '<b>Любовь к родной стране начинается с любви к природе.</b> <em> К.Г. Паустовский</em>',
                '<b>В ряду высоких эстетических наслаждений человека лежит наслаждение природой.</b> <em>И.Н. Крамской</em>',
                '<b>И как по мне, есть проблемы пострашнее мафии, например, экология.</b> <em>Микеле Плачидо</em>',
                '<b>Природа всегда права; ошибки же и заблуждения исходят от людей.</b> <em>Иоганн Вольфганг Гете</em>',
                '<b>Человек совершил огромную ошибку, когда возомнил, что может отделить себя от природы и не считаться с её законами.</b> <em>В. И. Вернадский</em>',
                '<b>Незнание природы — величайшая неблагодарность.</b> <em>Плиний Старший</em>',
                '<b>Человек может развиваться только в контакте с природой, а не вопреки ей.</b> <em>В.В. Бианки</em>']
                
        for el in table:
            note.append(f'{el}.jpg')
            
        shuffle(note)
        shuffle(data)
        photo = open(note[0], 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, data[0], parse_mode='html')

    elif message.text == 'Пункты приема вторсырья':
        bot.send_message(message.chat.id, '''<em>Адреса</em>
ул. Ульяновская,25
ул. Антонова, 11а (Восток)
ул. Ульяновская,50
ул. Луначарского, 7в
ул. Бакунина, 50(Гостиный двор)
ул. Лобачевского, 7
ул.Титова,12
ул. Попова, 18
ул. Аустрина, 141
Проспект Победы, 4
ул. Ладожская, 133
проспект Строителей, 67
проспект Строителей, 142
ул. Новоказанская, 8а
ул. Терновского, 174
ул. Онежская, 21
ул. Воронова, 2	''', parse_mode='html')
    
        
    elif message.text == 'Красная книга ПО':
        dictionary = {'''<em>Мышовка штранда(Sicista strandi)</em>
Небольшой длиннохвостый зверек. Длина тела около 6075 мм, хвоста 85100 мм (более 150 % длины тела).
 Верх тела рыжевато-коричневый, брюшко сероватое. По спине вдоль хребта проходит черная узкая полоса без светлого окаймления.
Видовая самостоятельность мышовки Штранда была доказана всего несколько лет назад ''': 'a-518.png',
 '''<em>Пеструшка степная (Lagurus lagurus)</em>
Мелкий зверек с несколько вытянутым телом и коротким хвостом. Длина тела 80-120 мм, хвоста - 7-9 мм. Уши небольшие,
едва выступают из меха. Подошвы покрыты шерстью, но бугорки на пальцах хорошо видны. Окраска верха от буровато-серой до серовато-палевой.
По хребту от носа до хвоста проходит черная полоса, ширина и интенсивность окраски которой подвержена значительной изменчивости.
От серых полевок отличается черной полоской на спине.''': 'Lagurus_lagurus.jpg',
'''<em>Выхухоль русская (Desmana moschata)</em>
Внешность животного выхухоль впечатляет своей необычностью. Это довольно крупный зверь с телом 18-22 см в длину,
таким же по длине хвостом и массой до 520 г. Хвост выхухоли покрыт слоем роговых чешуек,
а вдоль них по верху ещё и жесткими волосками, которые образуют киль.''': 'vipuhol89.png', 
'''<em>Ночница Наттерера (Myotis nattereri)</em>
Летучая мышь средних размеров. Длина тела 42-55 мм, длина предплечья 36-48 мм. Окраска верхней стороны тела серовато-бурая, нижней - светло-серая.
Мех густой и короткий, все волоски двухцветные, с темным основанием и более светлой вершинкой. Крылья широкие, тупые.
Задний край межбедренной перепонки утолщен, зазубрен и покрыт жесткими волосками. Уши большие, козелок прямой, длинный, узкий и заостренный.
Шпора S-образно изогнута.''': 'Ночница Наттерера.jpg', 
'''<em>Норка (Mustela lutreola)</em>
Размеры средние, длина тела до 43 см при весе до 800 г,
хвост немного короче половины длины тела.Между пальцами, особенно на стопе, относительно хорошо развиты плавательные перепонки. Окраска тела темно-коричневая,
с рыжеватым налетом, несколько светлее на брюшной стороне и темнее на конечностях и хвосте. На верхней и нижней губах,
на подбородке и иногда на груди располагаются белые пятна, чаще всего занимающие на морде большую площадь, чему американской норки.''': 'mustela-lutreola_02.jpg',
'''<em>Речная выдра (Lutra lutra)</em>
Выдра — крупный зверь с вытянутым гибким телом обтекаемой формы. Длина тела — 55–95 см,
хвоста — 26–55 см, масса — 6–10 кг. Лапы короткие, с плавательными перепонками.
Хвост мускулистый, не пушистый. Половой диморфизм слабо выражен: самцы крупнее самок.
Окраска меха: сверху тёмно-бурая, снизу светлая, серебристая.''': '''img2096_0.jpg'''}
        keys = list(dictionary.items())
        shuffle(keys)
        bot.send_message(message.chat.id, keys[0], parse_mode='html')
        a = keys[0]
        b = dictionary.get(a)
        photo = open(a[1], 'rb')
        bot.send_photo(message.chat.id, photo)
    
    elif  message.text == 'Это от тебя зависит':
        database = 'klmn'
        lst = []
        for el in database:
            lst.append(f'{el}.jpg')
        shuffle(lst)
        photo = open(lst[0], 'rb')
        bot.send_photo(message.chat.id, photo)
        


        



    else:
        bot.send_message(message.chat.id, 'Ты неправильно ввел, попробуй еще раз')



bot.polling(none_stop=True) # запуск, аргумент обозначает постоянство