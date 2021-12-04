from textblob import TextBlob
import difflib

def lang_detecter(text):
    ''''LAnguage detecter function'''
    language = TextBlob(text)
    return language.detect_language()

print()