from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5171126044:AAEYdIHvc6SfxXM3ErPINgKrdTsZXOqSc9g",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Olá, sou o Elevatinho, estou aqui para ajudar. Por favor responda este formulário para eu saber os grupos que irei te adicionar!https://forms.gle/uFEhsB4tUV1x1Xm28''')

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Deseja o link novamente? https://forms.gle/uFEhsB4tUV1x1Xm28")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))


updater.start_polling()
