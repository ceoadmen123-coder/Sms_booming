import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get("8221867248:AAHTLnOqVUbn-FiP92jZldYoKikzLnezbzYN")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Your bot is working ✅")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://your-app-url/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
