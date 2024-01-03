import telebot
from telebot import types
import os
import datetime
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


path_to_audio = "audio"
common_button_path = os.path.join(path_to_audio, 'COMMON')
in_the_plane_button_path = os.path.join(path_to_audio, 'IN THE PLANE')
in_the_hotel_button_path = os.path.join(path_to_audio, 'IN THE HOTEL')
in_the_cafe_button_path = os.path.join(path_to_audio, 'IN THE CAFE')
on_the_street_button_path = os.path.join(path_to_audio, 'ON THE STREET')


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Advice')
    btn2 = types.KeyboardButton(text='Basic phrases')
    btn3 = types.KeyboardButton(text='Attractions')
    btn4 = types.KeyboardButton(text='Feedback')

    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "If you’ve downloaded this app you might already have decided to visit "
                                      "Russia. Anyway, our team wants to say to you: don’t believe in all kinds of "
                                      "scary stories about our country. You would probably face some usual travelling "
                                      "troubles but no more. That’s why we do our work. We want to attract some "
                                      "tourists and make their journey easier. And enjoy your travel! ",
                     reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'MAIN MENU')
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Advice')
    btn2 = types.KeyboardButton(text='Basic phrases')
    btn3 = types.KeyboardButton(text='Attractions')
    btn4 = types.KeyboardButton(text='Feedback')

    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Select the category:", reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Advice')
def start(message):
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='GETTING STARTED')
    btn2 = types.KeyboardButton(text='TRAVEL APPS')
    btn3 = types.KeyboardButton(text='LEGAL')
    btn4 = types.KeyboardButton(text='MISC ADVICE')
    btn5 = types.KeyboardButton(text='MAIN MENU')
    kb1.add(btn1, btn2, btn3, btn4, btn5)

    bot.send_message(message.chat.id, 'Select a category: ', reply_markup=kb1)


@bot.message_handler(func=lambda message: message.text == 'GETTING STARTED')
def start(message):
    bot.send_message(message.chat.id, "  Let’s start with basic advice you might want to know.\n  First of all, you"
                                      " would need a visa to enter Russia. We highly recommend you to visit a visa "
                                      "agency for your one. There are lots of things you might not know about papers"
                                      " and visa agency would solve all the problems for moderate reward.\n  Also even"
                                      " if you are going to visit for less than 30 days, always apply for the full 30 "
                                      "days visa, and submit arrival and departure dates 29-30 days apart, this will "
                                      "avoid any issues should you need to extend your stay and provide you with a bit "
                                      "of spare time, just in case.\n  You will not require any vaccinations for "
                                      "traveling in Russia. But if you are taking prescription medication we recommend "
                                      "you to bring it with a little spare. Even if you find the same medicine in "
                                      "Russia, you will need a prescription from a Russian doctor, which you can’t get "
                                      "easily.\n  Then, be sure to learn some Cyrillic before your visit. At least "
                                      "learn the alphabet. St. Petersburg is very tourist friendly and there’s plenty "
                                      "of English – spoken and written. Moscow and rural towns are not so friendly. Or "
                                      "you really should have Internet access to use an online translator. This bot has"
                                      " a special menu with basic phrases and examples of sounding.\n  Electrical "
                                      "adapters in Russia use the two prongs round European outlets. If you are living "
                                      "in Europe, no worries. But anyways check your adapter.\n  Russia uses 220-volt "
                                      "electricity (America uses 110 volts). Most electrical devices will support both."
                                      " You can look at the back of the power adapter to find out its supported "
                                      "voltage. If it is 110-240 volts, you can bring your device with you. If it is "
                                      "110 volts, you will not be able to use it in Russia. \n  You also needn’t "
                                      "exchange much money before the trip because you can easily do it in Russia, "
                                      "sometimes even at a better rate. Just take a bit of rubles in advance. Dollars"
                                      " and euros are not accepted everywhere. \n  The culture views women as strong, "
                                      "independent and respected members of society, similar to images you might have "
                                      "seen of babushkas carrying logs in the tundra forests (that's a really dumb "
                                      "stereotype, actually). So, you will typically feel respected and safe on the "
                                      "streets.")


@bot.message_handler(func=lambda message: message.text == 'TRAVEL APPS')
def start(message):
    bot.send_message(message.chat.id, "Let’s finish with general tips and get to the actual guide to action. "
                                      "We want to introduce you a list of travelling apps. You’ll really want to "
                                      "download those for your trip. \n\n   -   MosMetro\n\nUnderground in Moscow "
                                      "is rather hard to navigate in especially if you catch outdated train without "
                                      "interactive screens. That’s why the MosMetro app is highly recommended because "
                                      "it provides an offline map of the underground with an in-built route building "
                                      "system. \n\n   -   Moscow Transport\n\nAnother eternal problem for residents of"
                                      " a big city is how to get into ground transportation without getting stuck in a"
                                      " traffic jam. The Moscow Transport application tries to build the best route,"
                                      " calculates the travel time, the number of transfers and the cost of trips.\n\n"
                                      "   -   WiFi Map\n\nDo you need to send a message to someone? And it is very "
                                      "important? But the thing is, you don’t have mobile network and you don’t know "
                                      "where you can find any spots with free Wi-Fi(by the way, metro in Moscow has "
                                      "free WiFi). That’s why it is crucial to have this application. Everything is "
                                      "very simple: you just need to open the Wi-Fi map – and the application will show"
                                      " you which networks are best to connect to now.\n\n   -   Velobike\n\nBicycle is"
                                      " rather convenient mean of transport, so you can use this app to find the "
                                      "nearest bike rental and obtain some information such as price of rent.\n\n"
                                      "   -   2GIS\n\nThis app can provide you offline maps which are very easy to use"
                                      " and are always willing to give you a helping hand during your trip. Application"
                                      " has a list of city maps: Moscow, Minsk, Baku, Dubai and more. \n\n   -   "
                                      "xCurrency\n\nIntuitive and easy to use app for converting currencies. It will"
                                      " definitely come in handy when traveling abroad in order to quickly navigate the"
                                      " prices.\n\n   -   Timeshifter\n\nJet lag can spoil your traveling experience,"
                                      " especially if it is a short trip. Timeshifter actually helps you avoid jet lag"
                                      " long before your flight takes off and also offers inflight and post-flight"
                                      " suggestions based on neuroscience research. But keep in mind that only your"
                                      " first plan is free, next ones are 10$ each or you can just purchase yearly"
                                      " subscription for 25$.\n\n   -   Metric Conversion\n\nMetric systems differ"
                                      " from country to country and if you don’t want to transfer pounds to kilos by"
                                      " yourself(of course, if you actually know the ratio) you should definitely make"
                                      " sure to download the app before your trip")


@bot.message_handler(func=lambda message: message.text == 'LEGAL')
def start(message):
    bot.send_message(message.chat.id, "Statement 62 p. 3 of the Constitution of the Russian Federation says that "
                                      "foreigners and people without citizenship has the same rights as citizens of "
                                      "Russia and are similarly responsible for any violations if not declared "
                                      "alternatively. \n\nThe State guarantees equality of human and civil rights and "
                                      "freedoms regardless of gender, race, nationality, language, origin, property and"
                                      " official status, place of residence, attitude to religion, beliefs, membership"
                                      " in public associations, as well as other circumstances. Any form of restriction"
                                      " of the rights of citizens on the grounds of social, racial, national, "
                                      "linguistic or religious affiliation is prohibited.\n\nArrest, and detention are"
                                      " allowed only after court’s decision otherwise person could be arrested only for"
                                      " 48 hours. \n\nRemember, in case of arrest you have a right for a single phone"
                                      " call. Use it to contact the embassy. Don’t worry if you don’t know the phone"
                                      " number: police officer must give you that information.\n\nDo not forget to"
                                      " bring your passport with you during city walks. It’s not necessary but can"
                                      " potentially save you from undesirable and not very pleasant situations. Also,"
                                      " you need your passport to buy a train ticket or a local SIM card. And you"
                                      " really want to have one because the cost of usage of your mobile data or calls"
                                      " would be really high. \n\nYou will get a migration card on the passport control"
                                      " while entering Russia. Do not ignore this small piece of paper left in your"
                                      " passport. It is an EXTREMELY important Russian travel tip.\n\nIt is illegal to"
                                      " drink alcohol and swear in public places even if you use foreign language. ")


@bot.message_handler(func=lambda message: message.text == 'MISC ADVICE')
def start(message):
    bot.send_message(message.chat.id, "Drinking tap water is rather ok for short periods of time. Tap water in"
                                      " Russia meet sanitary standards but there are too high percentage of some"
                                      " minerals, so you might consider using filters\n\nThere’s no exact opening"
                                      " hour for museums, galleries etc. So be sure to check it.\n\nThe Ruble goes"
                                      " a long way these days and many smaller businesses prefer cash to credit. Keep"
                                      " that in mind, especially if you’re bargaining for souvenirs. And buy those"
                                      " souvenirs from local artisans and designers. It’s good to support them and"
                                      " far less expensive (and more unique) than what you’ll find at the airports"
                                      " or big city shops.\n\nThere in no  reason to be more afraid of Russia than any"
                                      " country of Western Europe for example. Of course, you shouldn’t walk through"
                                      " dark street late, should be careful about your bag in public transport etc. But"
                                      " no specific precautions. \n\nTipping in Russia is entirely your own decision,"
                                      " however, we recommend you tip a small percentage, if you are satisfied with the"
                                      " service. If you do decide to leave a tip, they can be made in US dollars, euros"
                                      " or rubles. Last variant is recommended. A tip is usually around 5-15% of the"
                                      " price of the service at a restaurant or similar. As to guides or drivers, it is"
                                      " best to tip just a nominal amount. \n\nIf you want to eat something and there"
                                      " are only small cafes or stalls choose one where the most people are. \n\nNever"
                                      " talk about politics or sport. Just believe us. ")


@bot.message_handler(func=lambda message: message.text == 'Basic phrases')
def start(message):

    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='COMMON')
    btn2 = types.KeyboardButton(text='IN THE PLANE')
    btn3 = types.KeyboardButton(text='IN THE HOTEL')
    btn4 = types.KeyboardButton(text='IN THE CAFE')
    btn5 = types.KeyboardButton(text='ON THE STREET')
    btn6 = types.KeyboardButton(text='MAIN MENU')
    kb1.add(btn1, btn2, btn3, btn4, btn5, btn6)

    bot.send_message(message.chat.id, 'Select a category: ', reply_markup=kb1)


@bot.message_handler(func=lambda message: message.text == 'COMMON')
def start(message):
    kb = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='btn1-1')
    btn2 = types.InlineKeyboardButton(text='2', callback_data='btn1-2')
    btn3 = types.InlineKeyboardButton(text='3', callback_data='btn1-3')
    btn4 = types.InlineKeyboardButton(text='4', callback_data='btn1-4')
    btn5 = types.InlineKeyboardButton(text='5', callback_data='btn1-5')
    btn6 = types.InlineKeyboardButton(text='6', callback_data='btn1-6')
    btn7 = types.InlineKeyboardButton(text='7', callback_data='btn1-7')
    btn8 = types.InlineKeyboardButton(text='8', callback_data='btn1-8')
    btn9 = types.InlineKeyboardButton(text='9', callback_data='btn1-9')
    btn10 = types.InlineKeyboardButton(text='10', callback_data='btn1-10')

    kb.row(btn1, btn2, btn3, btn4, btn5)
    kb.row(btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, "1.	Hello\n2.	Good afternoon\n3.	Do you speak English?\n4.	I don't"
                                      " understand you\n5.	My name is …\n6.	Please / you are welcome\n7.	Thank"
                                      " you\n8.	Sorry (meaning the word you use when you want to ask about something)"
                                      "\n9.	Sorry (in the meaning of regret)\n10.	Good buy")

    bot.send_message(message.chat.id, 'Please, choose the phrase number:', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'IN THE PLANE')
def start(message):
    kb = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='btn2-1')
    btn2 = types.InlineKeyboardButton(text='2', callback_data='btn2-2')
    btn3 = types.InlineKeyboardButton(text='3', callback_data='btn2-3')
    btn4 = types.InlineKeyboardButton(text='4', callback_data='btn2-4')
    btn5 = types.InlineKeyboardButton(text='5', callback_data='btn2-5')
    btn6 = types.InlineKeyboardButton(text='6', callback_data='btn2-6')
    btn7 = types.InlineKeyboardButton(text='7', callback_data='btn2-7')
    btn8 = types.InlineKeyboardButton(text='8', callback_data='btn2-8')
    btn9 = types.InlineKeyboardButton(text='9', callback_data='btn2-9')

    kb.row(btn1, btn2, btn3)
    kb.row(btn4, btn5, btn6)
    kb.row(btn7, btn8, btn9)
    bot.send_message(message.chat.id, "1. I would like to buy a ticket\n2. How much does the ticket cost?\n3. "
                                      "Please call the stewardess\n4. Can I change places with you?\n5. When do we "
                                      "arrive?\n6. Where is the help desk?\n7. Where can I get my luggage?\n8. Where "
                                      "is the waiting room?\n9. What time is boarding?")

    bot.send_message(message.chat.id, 'Please, choose the phrase number:', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'IN THE HOTEL')
def start(message):
    kb = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='btn3-1')
    btn2 = types.InlineKeyboardButton(text='2', callback_data='btn3-2')
    btn3 = types.InlineKeyboardButton(text='3', callback_data='btn3-3')
    btn4 = types.InlineKeyboardButton(text='4', callback_data='btn3-4')
    btn5 = types.InlineKeyboardButton(text='5', callback_data='btn3-5')
    btn6 = types.InlineKeyboardButton(text='6', callback_data='btn3-6')
    btn7 = types.InlineKeyboardButton(text='7', callback_data='btn3-7')
    btn8 = types.InlineKeyboardButton(text='8', callback_data='btn3-8')
    btn9 = types.InlineKeyboardButton(text='9', callback_data='btn3-9')

    kb.row(btn1, btn2, btn3)
    kb.row(btn4, btn5, btn6)
    kb.row(btn7, btn8, btn9)

    bot.send_message(message.chat.id, "1. I want to rent a room in your hotel\n2. I would like to have my room "
                                      "cleaned\n3. I would like to vacate the room\n4. I will pay in cash\n5. I will "
                                      "pay by credit card \n6. Can I stay with you for a few more days?\n7. I need a "
                                      "room for one\n8. What is the cost of this room per day?\n9. Where is the "
                                      "nearest hotel?")

    bot.send_message(message.chat.id, 'Please, choose the phrase number:', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'IN THE CAFE')
def start(message):
    kb = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='btn4-1')
    btn2 = types.InlineKeyboardButton(text='2', callback_data='btn4-2')
    btn3 = types.InlineKeyboardButton(text='3', callback_data='btn4-3')
    btn4 = types.InlineKeyboardButton(text='4', callback_data='btn4-4')
    btn5 = types.InlineKeyboardButton(text='5', callback_data='btn4-5')
    btn6 = types.InlineKeyboardButton(text='6', callback_data='btn4-6')
    btn7 = types.InlineKeyboardButton(text='7', callback_data='btn4-7')
    btn8 = types.InlineKeyboardButton(text='8', callback_data='btn4-8')

    kb.row(btn1, btn2, btn3, btn4)
    kb.row(btn5, btn6, btn7, btn8)

    bot.send_message(message.chat.id, "1. Do you have any tables available?\n2. Can I have a menu?\n3. What can "
                                      "you advise?\n4. What is your signature dish?\n5. I want to order this\n6. How "
                                      "much does this dish cost?\n7. Please bill\n8. Thank you, it was very tasty")

    bot.send_message(message.chat.id, 'Please, choose the phrase number:', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'ON THE STREET')
def start(message):
    kb = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='btn5-1')
    btn2 = types.InlineKeyboardButton(text='2', callback_data='btn5-2')
    btn3 = types.InlineKeyboardButton(text='3', callback_data='btn5-3')
    btn4 = types.InlineKeyboardButton(text='4', callback_data='btn5-4')
    btn5 = types.InlineKeyboardButton(text='5', callback_data='btn5-5')
    btn6 = types.InlineKeyboardButton(text='6', callback_data='btn5-6')
    btn7 = types.InlineKeyboardButton(text='7', callback_data='btn5-7')
    btn8 = types.InlineKeyboardButton(text='8', callback_data='btn5-8')
    btn9 = types.InlineKeyboardButton(text='9', callback_data='btn5-9')
    kb.row(btn1, btn2, btn3)
    kb.row(btn4, btn5, btn6)
    kb.row(btn7, btn8, btn9)
    bot.send_message(message.chat.id,
                     "1. Excuse me, how to get to…\n2. What street is this?\n3. Is it far from here?\n4. Please, "
                     "show it on the map\n5. I need to go to…\n6. What stop is it?\n7. Where can I buy a ticket?\n8. "
                     "Where is the nearest metro station?\n9.	How can I get to the train station?")

    bot.send_message(message.chat.id, 'Please, choose the phrase number:', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1-1':
        tempo_path = os.path.join(common_button_path, 'привет.wav')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-2':
        tempo_path = os.path.join(common_button_path, 'добрый день.wav')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-3':
        tempo_path = os.path.join(common_button_path, 'вы говорите на английском языке.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-4':
        tempo_path = os.path.join(common_button_path, 'я не понимаю вас.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-5':
        tempo_path = os.path.join(common_button_path, 'меня зовут.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-6':
        tempo_path = os.path.join(common_button_path, 'пожалуйста.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-7':
        tempo_path = os.path.join(common_button_path, 'спасибо.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-8':
        tempo_path = os.path.join(common_button_path, 'простите.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-9':
        tempo_path = os.path.join(common_button_path, 'простите.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn1-10':
        tempo_path = os.path.join(common_button_path, 'до свидания.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-1':
        tempo_path = os.path.join(in_the_plane_button_path, 'я бы хотел купить билет.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-2':
        tempo_path = os.path.join(in_the_plane_button_path, 'сколько стоит билет.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-3':
        tempo_path = os.path.join(in_the_plane_button_path, 'позовите пожалуйста стюардессу.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-4':
        tempo_path = os.path.join(in_the_plane_button_path, 'можно поменяться с вами местами.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-5':
        tempo_path = os.path.join(in_the_plane_button_path, 'когда мы прилетаем.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-6':
        tempo_path = os.path.join(in_the_plane_button_path, 'где справочная.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-7':
        tempo_path = os.path.join(in_the_plane_button_path, 'где получить багаж.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-8':
        tempo_path = os.path.join(in_the_plane_button_path, 'где зал ожидания.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn2-9':
        tempo_path = os.path.join(in_the_plane_button_path, 'во сколько посадка.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-1':
        tempo_path = os.path.join(in_the_hotel_button_path, 'я хочу снять номер в вашем отеле.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-2':
        tempo_path = os.path.join(in_the_hotel_button_path, 'я хотел бы чтобы в моём номере провели уборку.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn3-3':
        tempo_path = os.path.join(in_the_hotel_button_path, 'я бы хотел освободить номер.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn3-4':
        tempo_path = os.path.join(in_the_hotel_button_path, 'я буду платить наличными.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-5':
        tempo_path = os.path.join(in_the_hotel_button_path, 'я буду платить кредитной картой .mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-6':
        tempo_path = os.path.join(in_the_hotel_button_path, 'могу ли я остаться у вас ещё на несколько дней.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-7':
        tempo_path = os.path.join(in_the_hotel_button_path, 'мне нужен номер на одного.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-8':
        tempo_path = os.path.join(in_the_hotel_button_path, 'какая стоимость этого номера в сутки.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-9':
        tempo_path = os.path.join(in_the_hotel_button_path, 'где находится ближайший отель.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn3-9':
        tempo_path = os.path.join(in_the_hotel_button_path, 'где находится ближайший отель.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-1':
        tempo_path = os.path.join(in_the_cafe_button_path, 'у вас есть свободные столики.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-2':
        tempo_path = os.path.join(in_the_cafe_button_path, 'можно мне меню.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-3':
        tempo_path = os.path.join(in_the_cafe_button_path, 'что вы можете посоветовать.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-4':
        tempo_path = os.path.join(in_the_cafe_button_path, 'какое у вас фирменное блюдо.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-5':
        tempo_path = os.path.join(in_the_cafe_button_path, 'я хочу заказать это.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-6':
        tempo_path = os.path.join(in_the_cafe_button_path, 'сколько стоит это блюдо.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-7':
        tempo_path = os.path.join(in_the_cafe_button_path, 'будьте добры счёт.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn4-8':
        tempo_path = os.path.join(in_the_cafe_button_path, 'спасибо было очень вкусно.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()

    if callback.data == 'btn5-1':
        tempo_path = os.path.join(on_the_street_button_path, 'извините как пройти.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-2':
        tempo_path = os.path.join(on_the_street_button_path, 'какая это улица.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-3':
        tempo_path = os.path.join(on_the_street_button_path, 'это далеко отсюда.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-4':
        tempo_path = os.path.join(on_the_street_button_path, 'покажите пожалуйста это на карте.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-5':
        tempo_path = os.path.join(on_the_street_button_path, 'мне нужно на.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-6':
        tempo_path = os.path.join(on_the_street_button_path, 'какая это остановка.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-7':
        tempo_path = os.path.join(on_the_street_button_path, 'где можно купить билет.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-8':
        tempo_path = os.path.join(on_the_street_button_path, 'где ближайшая станция метро.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()
    if callback.data == 'btn5-9':
        tempo_path = os.path.join(on_the_street_button_path, 'как я могу добраться до железнодорожного вокзала.mp3')
        file = open(tempo_path, 'rb')
        bot.send_voice(callback.message.chat.id, file)
        file.close()


@bot.message_handler(func=lambda message: message.text == 'Attractions')
def start(message):
    file = open("att.docx", 'rb')
    bot.send_message(message.chat.id, "So you’ve reached your hotel. What’s next? You will definitely want to visit"
                                      " some interesting places. But which? Red Square? Kremlin? Bo-o-oring. That’s why"
                                      " you are reading this now: you want something extraordinary. X marks the spot:"
                                      " here is our list of unusual places of interest and tourist attractions. And"
                                      " enjoy your time!")
    bot.send_document(message.chat.id, file)
    file.close()


@bot.message_handler(func=lambda message: message.text == 'Feedback')
def start(message):
    sent = bot.send_message(message.chat.id, 'Please, leave feedback')

    bot.register_next_step_handler(sent, review)


def review(message):
    file = open("feedback.txt", 'a', encoding='utf-8')
    message_to_save = str(message.text)
    file.write(f'{datetime.datetime.now()}, {message_to_save}')
    file.write('\n')
    file.close()
    bot.send_message(message.chat.id, 'Thank you for your feedback! It´s very important for our company')


bot.polling()
