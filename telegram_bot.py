from telegram.ext import Updater

from telegram.ext import CommandHandler

import logging




# all code before the main function stays as it is



def main():

    # setting to appropriate values

    TOKEN = "934772110:AAEZlF71gtR_jBL2V4kEjdOy09QJHYWqC2A"

    APPNAME = "ttbot001"

    

    # set PORT to be used with Heroku

    PORT = os.environ.get('PORT')



    # set up updater

    updater = Updater(token=TOKEN, use_context=True)

    # set   dispatcher = updater.dispatcher

    # a print message to log successful initiation of the bot

    # this is for self

    print("Bot started")

    

    # ConversationHandler

    .

    .

    

    # add conversation handler to dispatcher

    dispatcher.add_handler(conv_handler)

    

    # starting webhook and setting it up with heroku app

    updater.start_webhook(listen="0.0.0.0",

                            port=(PORT),

                            url_path=TOKEN)

    

    updater.bot.setWebhook(

      "https://{}.herokuapp.com/{}".format(APPNAME, TOKEN)

      )



    # start the bot

    # updater.start_polling()



    # run the bot until 

























dispatcher=updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                     level=logging.INFO)



def start(update,context):

    chat_id=update.effective_chat.id

    context.bot.send_message(chat_id, text="Happy Mangolina")



start_command=CommandHandler("start" , start)

dispatcher.add_handler(start_command)



updater.start_polling()

