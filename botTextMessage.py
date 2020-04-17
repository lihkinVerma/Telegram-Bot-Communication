
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = 'USER BOT TOKEN'

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    print(str( update.effective_chat.id ))
    context.bot.send_message(chat_id = update.effective_chat.id, 
            text="Hi Welcome to Nikhil Verma's First Bot! You know, its going to be amazing. Lets Chat")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)
updater.start_polling()

