from gtts import gTTS 
import telebot
from uuid import uuid4
from engru import lang_detecter
import difflib

queestions = {
                 'question1'  : 'Что такое распознавание речи?',
                 'question2' : ''
}


bot = telebot.TeleBot("2129516170:AAGAjo7Pui79YBCIc-SyWBbMEU14q35qWx4")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	answer = 'Hello I can convert text to speech in russian and english languages.\nSend me text'
	bot.send_message(message.chat.id, answer)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    message_lang = lang_detecter(message.text[0:50])
   
    if message.text == queestions['question1']:
        audio_file = open(f'/home/alproger/Documents/GitHub/text-to-speech-telegram-bot/answer1.wav', 'rb')
        bot.send_audio(message.chat.id, audio = audio_file)
    
    else :
        if message_lang == 'ru' or message_lang == 'en':
            audio_name = uuid4()
            bot.send_message(message.chat.id, text='Audio is saving...')
            text_to_speech = gTTS(text=message.text, lang=message_lang, slow=False)
            text_to_speech.save(f"{audio_name}.wav")
            audio_file = open(f'/home/alproger/Documents/GitHub/text-to-speech-telegram-bot/{audio_name}.wav', 'rb')	
            bot.send_audio(message.chat.id, audio = audio_file)
        else:
            bot.send_message(message.chat.id, 'Please send me message in english or russian languages')
    


print('bot running...')
bot.infinity_polling()
