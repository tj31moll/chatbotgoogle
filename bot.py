import telegram
from telegram.ext import Updater, MessageHandler, Filters
import google.assistant.library as ga

TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
GA_DEVICE_MODEL_ID = 'YOUR_GOOGLE_ASSISTANT_DEVICE_MODEL_ID' 

def handle_telegram_message(bot, update):
  text = update.message.text
  ga_request = ga.AssistRequest(text)
  
  # Send request to Google Assistant
  response_audio = ga_assistant.assist(ga_request)
  
  # Send audio response to Telegram
  bot.send_voice(chat_id=update.message.chat_id, voice=response_audio)

if __name__ == '__main__':

  # Create Telegram bot
  bot = telegram.Bot(token=TELEGRAM_TOKEN)
  
  # Create Google Assistant instance
  ga_assistant = ga.get_assistant(GA_DEVICE_MODEL_ID)

  # Telegram bot handlers
  updater = Updater(TELEGRAM_TOKEN)
  dispatcher = updater.dispatcher
  dispatcher.add_handler(MessageHandler(Filters.text, handle_telegram_message))

  # Start polling Telegram bot
  updater.start_polling()
