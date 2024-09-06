import telebot
import random
import json
import datetime
import tokennnn

information = {}
komentus = {}

bot = telebot.TeleBot(tokennnn.token)
@bot.message_handler(["start"])
def start(polso):
    bot.send_message(polso.chat.id, "Привет")

@bot.message_handler(["sapisatsa"])
def sapisatsa(polso):
    knopi = genor_knop()
    bot.send_message(polso.chat.id, "На какое число желаете записаться?", reply_markup=knopi)

@bot.message_handler(["komentar"])
def komentar(polso):
    bot.send_message(polso.chat.id, "На чъё имя хотите оставить коментарий?")
    bot.register_next_step_handler_by_chat_id(polso.chat.id, komentar_name_obrab)

def ozen_obrab(polso):
    komentus[polso.chat.id].append(polso.text)
    bot.send_message(polso.chat.id, "Комментарий?")
    bot.register_next_step_handler_by_chat_id(polso.chat.id, komentar_obrab)

def komentar_name_obrab(polso):
    komentus[polso.chat.id] = [polso.text]
    bot.send_message(polso.chat.id, "Какая оценка?")
    bot.register_next_step_handler_by_chat_id(polso.chat.id, ozen_obrab)

def komentar_obrab(polso):
    komentus[polso.chat.id].append(polso.text)
    komentarii = komentus[polso.chat.id]
    bot.send_message(polso.chat.id, f"Вы {komentarii[0]}, поставили оценку - {komentarii[1]} и оставили коментарий - {komentarii[2]}")
    dobaw_komentar(komentarii[0], komentarii[1], komentarii[2])
    
def dobaw_sap(data, time, client, procedura):
    new_sap = {"data": data, "time": time, "client": client, "procedura": procedura}
    xxx = open("warianti.json", "r", encoding="UTF-8")
    slowar = json.load(xxx)
    xxx.close()
    zapisi = slowar["записи"]
    zapisi.append(new_sap)
    xxx = open("warianti.json", "w", encoding="UTF-8")
    json.dump(slowar, xxx, ensure_ascii=False, indent=4)
    xxx.close()

def dobaw_komentar(name, ozen, komentar):
    new_komentar = {"client": name, "ozenka": ozen, "tekst": komentar}
    xxx = open("warianti.json", "r", encoding="UTF-8")
    slowar = json.load(xxx)
    xxx.close()
    zapisi = slowar["отзывы"]
    zapisi.append(new_komentar)
    xxx = open("warianti.json", "w", encoding="UTF-8")
    json.dump(slowar, xxx, ensure_ascii=False, indent=4)
    xxx.close()

def genor_knop():
    a = 1
    dat = datetime.date
    swobod_dayi = []
    while a <= 5:
        nin_day = dat.today()
        delta_day = datetime.timedelta(a)
        swobod_day = nin_day + delta_day
        swobod_dayi.append(swobod_day)
        a += 1
    knopki = telebot.types.InlineKeyboardMarkup()
    dlinspis = len(swobod_dayi)
    a = 0
    while a < dlinspis:
        element = swobod_dayi[a]
        elem = element.strftime("%d/%m/%Y")
        knop_1 = telebot.types.InlineKeyboardButton(text=elem, callback_data = "data " + elem)
        knopki.add(knop_1)
        a += 1
    return knopki

def genor_knop_time(polso):
    b = 9
    time = datetime.time
    swobod_time = []
    while b <= 17:
        swobod_Uhr = time(b, 0, 0)
        swobod_time.append(swobod_Uhr)
        b += 1
    knopkici = telebot.types.InlineKeyboardMarkup()
    dlinspisi = len(swobod_time)
    b = 0
    print(information)
    informatia = information[polso.chat.id]
    musornie_wremena = zanat_wremen(informatia[0])
    while b < dlinspisi:
        element = swobod_time[b]
        # elem = element.strftime("%h:%m:%s")
        if str(element) not in musornie_wremena:
            knop_1 = telebot.types.InlineKeyboardButton(text=str(element), callback_data = "time " + str(element))
            knopkici.add(knop_1)
        b += 1
    return knopkici

def zanat_wremen(date):
    timen = []
    ogran = open("warianti.json", "r", encoding="UTF-8")
    slowarr = json.load(ogran)
    wse_wrim = slowarr["записи"]
    for kast_sap in wse_wrim:
        old_data = kast_sap["data"]
        if old_data == date:
            old_time = kast_sap["time"]
            timen.append(old_time)
    return timen

def woswrat(polso):
    return True
def prozedur_obrab(polso):
    information[polso.chat.id].append(polso.text)
    informatia = information[polso.chat.id]
    bot.send_message(polso.chat.id, f"Запись на имя {informatia[2]} на процедуру {informatia[3]} {informatia[0]} числа в {informatia[1]} успешно создана")
    dobaw_sap(informatia[0], informatia[1], informatia[2], informatia[3])
def name_obrab(polso):
    information[polso.chat.id].append(polso.text)
    bot.send_message(polso.chat.id, "Интересующаявас процедура")
    bot.register_next_step_handler_by_chat_id(polso.chat.id, prozedur_obrab)
@bot.callback_query_handler(woswrat)
def klik_knop(polso):
    if "time" in polso.data:
        delit = polso.data.split(" ")
        information[polso.message.chat.id].append(delit[1])
        print(information)
        bot.send_message(polso.message.chat.id, "Вы выбрали:" + " " + delit[1])
        bot.send_message(polso.message.chat.id, "Введите ваше имя")
        bot.register_next_step_handler_by_chat_id(polso.message.chat.id, name_obrab)
    elif "data" in polso.data:
        delit = polso.data.split(" ")
        bot.send_message(polso.message.chat.id, "Вы выбрали:" + " " + delit[1])
        information[polso.message.chat.id] = [delit[1]]
        knopi = genor_knop_time(polso.message)
        bot.send_message(polso.message.chat.id, "Выберите время", reply_markup=knopi)

bot.polling()