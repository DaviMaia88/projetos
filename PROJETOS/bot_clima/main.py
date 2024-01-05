import telebot
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

token = "6933779136:AAGUq3rJD5IaCMpOsaD3XTMVubwgfqLOKiw"

bot = telebot.TeleBot(token)
print(cotacoes)

def verificar(msg):
    return True

@bot.message_handler(commands=['dolar'])
def dolar(msg):
    txt = f"""Aqui estão informações atualizadas do Dolár:
                Valor de compra:         R${cotacoes['USDBRL']['bid']}
                Valor de venda:            R${cotacoes['USDBRL']['ask']}
                Variação:                        R${cotacoes['USDBRL']['varBid']}
                Porcentagem de variação: {cotacoes['USDBRL']['pctChange']}%
                Valor maxímo:              R${cotacoes['USDBRL']['high']}
                Valor mínimo:              R${cotacoes['USDBRL']['low']}
    Digite qualquer coisa para ver de outra moeda
           """
    bot.send_message(msg.chat.id, txt)


@bot.message_handler(commands=['euro'])
def euro(msg):
    txt = f"""Aqui estão informações atualizadas do Euro:
                Valor de compra:         R${cotacoes['EURBRL']['bid']}
                Valor de venda:            R${cotacoes['EURBRL']['ask']}
                Variação:                        R${cotacoes['EURBRL']['varBid']}
                Porcentagem de variação: {cotacoes['EURBRL']['pctChange']}%
                Valor maxímo:              R${cotacoes['EURBRL']['high']}
                Valor mínimo:              R${cotacoes['EURBRL']['low']}
    Digite qualquer coisa para ver de outra moeda
           """
    bot.send_message(msg.chat.id, txt)

@bot.message_handler(commands=['bitcoin'])
def btc(msg):
    txt = f"""Aqui estão informações atualizadas do BitCoin:
                Valor de compra:         R${cotacoes['BTCBRL']['bid']}
                Valor de venda:            R${cotacoes['BTCBRL']['ask']}
                Variação:                        R${cotacoes['BTCBRL']['varBid']}
                Porcentagem de variação: {cotacoes['BTCBRL']['pctChange']}%
                Valor maxímo:              R${cotacoes['BTCBRL']['high']}
                Valor mínimo:              R${cotacoes['BTCBRL']['low']}
    Digite qualquer coisa para ver de outra moeda
           """
    bot.send_message(msg.chat.id, txt)


@bot.message_handler(func=verificar)
def responder(msg):
    txt = """Olá, clique em qual moeda deseja ver algumas informações:
                /dolar - Ver informações do Dolar
                /euro  - Ver informações do Euro
                /bitcoin - Ver informações do Bitcoin
          """
    bot.reply_to(msg,txt)

bot.polling()