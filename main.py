from gtts import gTTS 
import telebot
from uuid import uuid4
bot = telebot.TeleBot("your bot token")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	answer = 'Hello I can convert text to speech in russian and english languages.\nSend me text'
	bot.send_message(message.chat.id, answer)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    audio_name = uuid4()
    bot.send_message(message.chat.id, text='Audio is saving...')
    text_to_speech = gTTS(text=message.text, lang='en', slow=False)
    text_to_speech.save(f"{audio_name}.mp3")
    audio_file = open(f'/home/alproger/Documents/GitHub/text-to-speech-telegram-bot/{audio_name}.mp3', 'rb')	
	
    bot.send_audio(message.chat.id, audio = audio_file)


print('bot running...')
bot.infinity_polling()
