import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai
import os

openai.api_key = "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"
TELEGRAM_TOKEN = "8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI"
WEBHOOK_URL = "https://bot-telegram-mara.onrender.com"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app_flask = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)
application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut! Je suis ton bot intelligent. Envoie-moi un message!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}],
            max_tokens=150,
            temperature=0.7
)
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Erreur OpenAI: {e}")
        reply = "Désolé, je ne peux pas répondre maintenant."
    await update.message.reply_text(reply)

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app_flask.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put(update)
    return "OK", 200

@app_flask.route("/")
def index():
    return "Bot MARA est en ligne!"

if __name__ == "__main__":
    bot.delete_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}")
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
```
if __name__ == "__main__":
    main()
