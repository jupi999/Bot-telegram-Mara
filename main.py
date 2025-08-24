import openai
import os
from flask import Flask, request
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

env = os.getenv("ENV", "dev")
if env == "prod":
    openai.api_key = os.getenv("OPENAI_API_KEY_PROD")
else:
    openai.api_key = os.getenv("OPENAI_API_KEY_DEV")

async def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
)
    return response.choices[0].message.content

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, je suis MARA 🤖. Pose-moi une question, je te réponds avec mon cerveau IA.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    gpt_response = await ask_gpt(user_message)
    await update.message.reply_text(gpt_response)

def run_telegram_bot():
    app = ApplicationBuilder().token("8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

app_flask = Flask(__name__)

@app_flask.route("/", methods=["GET"])
def keep_alive():
    if request.args.get("ping") == "keepAlice":
        return "✅ MARA réveillé par keep Alice", 200
    return "🟢 MARA est en ligne", 200

def run_flask():
    app_flask.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_telegram_bot).start()
threading.Thread(target=run_flask).start()
