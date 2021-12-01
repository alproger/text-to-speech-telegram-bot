# text-to-speech-telegram-bot
Telegram bot for converting text to speech. 

<h3>It's a simple telegram bot for converting text information to audio information with format ".mp3"</h3>

<h2>installitions :</h2>
<hr>
<<<<<<< HEAD
```pip install pyTelegramBotAPI ```
```pip install gTTS```


```from gtts import gTTS 
=======
* `pip install pyTelegramBotAPI`
* `pip install gTTS`
<br>
```
from gtts import gTTS 
>>>>>>> 18a31795ae12fe14c2056011b3e33a02070e57f2
import telebot
from uuid import uuid4
bot = telebot.TeleBot("your bot token")

<<<<<<< HEAD
# hendling start or help command
=======
>>>>>>> 18a31795ae12fe14c2056011b3e33a02070e57f2
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	answer = 'Hello I can convert text to speech in russian and english languages.\nSend me text'
	bot.send_message(message.chat.id, answer)
<<<<<<< HEAD

#hendling message who sends user for convert audio	
=======
	
>>>>>>> 18a31795ae12fe14c2056011b3e33a02070e57f2
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    audio_name = uuid4()
    bot.send_message(message.chat.id, text='Audio is saving...')
    text_to_speech = gTTS(text=message.text, lang='en', slow=False)
    text_to_speech.save(f"{audio_name}.mp3")
    audio_file = open(f'/home/alproger/Documents/text-to-speech/{audio_name}.mp3', 'rb')	
	
    bot.send_audio(message.chat.id, audio = audio_file)
<<<<<<< HEAD
=======


>>>>>>> 18a31795ae12fe14c2056011b3e33a02070e57f2
print('bot running...')
bot.infinity_polling()
```

