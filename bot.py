import telebot
from googletrans import Translator, LANGUAGES

TOKEN = "7914727289:AAGUyJfA3ex2t_MTxrYGIFKqNbGYrDwN_Hs"

bot = telebot.TeleBot(TOKEN)
translator = Translator()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-переводчик. Используй команду /translate <язык> <текст>.")


@bot.message_handler(commands=['translate'])
def handle_translate(message):
    try:
        args = message.text.split(maxsplit=2)
        if len(args) < 3:
            bot.reply_to(message, "Пример: /translate en Привет мир")
            return

        language, text = args[1], args[2]

        if language not in LANGUAGES:
            bot.reply_to(message, "Ошибка: указанный язык не поддерживается.")
            return

        translated = translator.translate(text, dest=language).text
        bot.reply_to(message, f"Перевод ({language}): {translated}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


@bot.message_handler(commands=['languages'])
def handle_languages(message):
    languages_list = "\n".join([f"{key}: {value}" for key, value in LANGUAGES.items()])
    bot.reply_to(message, f"Поддерживаемые языки:\n{languages_list}")

if __name__=="__main__":
    bot.polling()