import telebot

token = "6774607208:AAGgFOdUL1XLXCpWAo3PHGHtB1XSIN6EmKQ"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["bial"])
def bial(msg):
    bot.send_message(msg.chat.id, """Bial: -Oi
                                     Você: -Olá
                                     Você: Não posso controlar minhas falas?
                                     Bial: Não
                                     Você: Qual a graça disso então?
                                     Bial: Sei la, você que escolheu isso
                                     Você: Vai se ferrar então, tchau
                                     Bial: Volte sempre!""")

@bot.message_handler(commands=["anao"])
def anao(msg):
    bot.send_message(msg.chat.id, "A caminho, mas vai demorar estão vindo de um centro escravista oculto na África.")

@bot.message_handler(commands=["submarino"])
def submarino(msg):
    bot.send_message(msg.chat.id, "Ops... Afundou.")


@bot.message_handler(commands=["opcao1"])
def opc1(msg):
    bot.send_message(msg.chat.id, """Escolha uma opção:
                                        /bial 30 seg de conversa com bial
                                        /anao Encomenda de anão
                                        /submarino Pedir um submarino uber
                                    """)


@bot.message_handler(commands=["opcao2"])
def opc2(msg):
    bot.send_message(msg.chat.id, "Manda um mensagem pro email: @naoadiantareclamar")


@bot.message_handler(commands=["opcao3"])
def opc3(msg):
    print(msg)
    bot.send_message(msg.chat.id, "Vai funcionar não, desiste")








def verificar(mensagem):
    return True

@bot.message_handler(func=verificar) # diz quando a função vai ser executada
def responder(msg):
    texto = """Escolha uma opção para continuar (Clique no item):
                /opcao1 Fazer um pedido
                /opcao2 Reclamar de um pedido
                /opcao3 Parar o bot
            """
    bot.reply_to(msg, texto)


bot.polling() # loop infinito do bot