import telebot 

Token = "#"

bot = telebot.TeleBot(Token) 

@bot.message_handler(['start'])
def start(message):
  bot.reply_to(message,"Welcome to Upmarket. This bot is built by Aditya Jadhav.")
  
@bot.message_handler(['about'])
def start(message):
  bot.reply_to(message,"Upmarket is a fintech startup that provides roboadvisory services to early-stage stock traders in India.")  
  
@bot.message_handler(['help'])
def start(message):
  bot.reply_to(message,"Upmarket empowers traders with AI-driven insights and personalized strategies to enhance their stock marcket success.")    

bot.polling()
