import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

openai.api_key = "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"
TELEGRAM_TOKEN = "8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Je suis ton bot intelligent. Envoie-moi un message !")

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
    except Exception:reply = "Désolé, je ne peux pas répondre maintenant."
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
