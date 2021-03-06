from gtts import gTTS 
import telebot
from uuid import uuid4
from engru import lang_detecter
import difflib

questions = {
                 'answer1'  : 'Что такое распознавание речи?',
                 'answer2'  : 'Какие типовые задачи существует в распознавание речи?',
                 'answer3'  : 'Какие механизмы существует в распознавание речи?',
                 'answer4'  : 'Что такое Sonix?',
                 'answer5'  : 'Как работает программа для распознования речи?',
                 'answer6'  : 'Первая техналогия для распознования речи?',
                 'answer7'  : 'Что такое акустический модел?',
                 'answer8'  : 'Что такое IBM Speech to text?',
                 'answer9'  : 'Что такое Amazon Transcribe и как он работает?',
                 'answer10' : 'Анализ сигнала это'


}
def text_eq(text1, text2):
    result = difflib.SequenceMatcher(None,f'{text1}',f'{text2}').ratio()
    return result

bot = telebot.TeleBot("token here")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	answer = 'Hello I can convert text to speech in russian and english languages.\nSend me text'
	bot.send_message(message.chat.id, answer)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):    
    try:
        keys = [k for k, v in questions.items() if v == message.text]
        key = keys[0]
        print(key)
        audio = open(f'/home/alproger/Documents/GitHub/text-to-speech-telegram-bot/answers/{key}.wav', 'rb')
        bot.send_audio(message.chat.id, audio = audio)
    except:
        message_lang = lang_detecter(message.text[0:50])
        if message_lang == 'ru' or message_lang == 'en':
            audio_name = uuid4()
            bot.send_message(message.chat.id, text='Audio is saving...')
            text_to_speech = gTTS(text=message.text, lang=message_lang, slow=False)
            text_to_speech.save(f"./audios/{audio_name}.wav")
            audio_file = open(f'/home/alproger/Documents/GitHub/text-to-speech-telegram-bot/audios/{audio_name}.wav', 'rb')	
            bot.send_audio(message.chat.id, audio = audio_file)
        else:
            bot.send_message(message.chat.id, 'Please send me message in english or russian languages')

print('bot running...')
bot.infinity_polling()
