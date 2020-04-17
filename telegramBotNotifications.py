
# Report Feed initiated in last 15 minutes
import feedparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime, dateutil

def parseRSS( rss_url ):
    return feedparser.parse( rss_url )

def getHeadlinesFromAUrl(rss_url):
    headlines = []
    feed = parseRSS(rss_url)
    for newsitem in feed.get('items'):
        headlines.append(newsitem.get('title'))
    return headlines

def getHeadlinesForAllDictUrls(newsurls):
    allheadlines = []
    for key, url in newsurls.items():
        allheadlines.extend(getHeadlinesFromAUrl(url))
    return allheadlines

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Hi Welcome to Nikhil Verma's Bot! You know, its going to be amazing. Lets Chat")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def sendRssFeeds(update, context):
    newsurls = {
        'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
    }
    allheadlines = getHeadlinesForAllDictUrls(newsurls)
    for i in range(len(allheadlines)):
        context.bot.send_message(chat_id = update.effective_chat.id, text= str(i) + ". "+str(allheadlines[i]))

def addHandlersToTelegramBotAndStartIt(updater, dispatcher):
    unknown_handler = MessageHandler(Filters.command, unknown)
    start_handler = CommandHandler('start', start)
    sendRssFeeds_handler = CommandHandler('sendRssFeeds', sendRssFeeds)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(sendRssFeeds_handler)
    dispatcher.add_handler(unknown_handler)
    updater.start_polling()

def sendAlways(updater):
    newsurls = {
        'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
    }
    allheadlines = getHeadlinesForAllDictUrls(newsurls)
    updater.bot.send_message(<some chat id>, text = str(allheadlines))

def main():
   token = 'BOT TOKEN'
   updater = Updater(token=token, use_context=True)
   #sendAlways(updater)
   dispatcher = updater.dispatcher
   addHandlersToTelegramBotAndStartIt(updater, dispatcher)

if __name__ == '__main__':
    main()
