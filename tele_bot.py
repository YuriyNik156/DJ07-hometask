from telebot.types import Message
import telebot
import requests

API_URL = "http://127.0.0.1:8000/api"
BOT_TOKEN = "7681943529:AAENJPqgtCKcw_OvzPl4d3WW7kzetNFzttU"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def register_user(message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username or "Безымянный"
    }
    try:
        response = requests.post(f"{API_URL}/register/", json=data)
        if response.status_code == 201:
            bot.reply_to(message, "Ты успешно зарегистрирован!")
        elif response.status_code == 200:
            bot.reply_to(message, "Ты уже был зарегистрирован ранее!")
        elif response.status_code == 400:
            bot.reply_to(message, "Уже зарегистрирован!")
        else:
            bot.reply_to(message, "Что-то пошло не так...")
            print("Статус:", response.status_code)
            print("Ответ:", response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка подключения: {e}")

@bot.message_handler(commands=['myinfo'])
def get_user_info(message):
    try:
        response = requests.get(f"{API_URL}/user/{message.from_user.id}/")
        if response.status_code == 200:
            user_data = response.json()
            bot.reply_to(
                message,
                f"Имя пользователя: {user_data['username']}\n ID: {user_data['user_id']}"
            )
        else:
            bot.reply_to(message, "Ты ещё не зарегистрирован. Напиши /start.")
    except Exception as e:
        bot.reply_to(message, f"Ошибка подключения: {e}")

if __name__== "__main__":
    bot.polling(none_stop=True)