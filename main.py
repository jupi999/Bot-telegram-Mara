from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot MARA démarré ✅")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tu as dit: {update.message.text}")

app = ApplicationBuilder().token("8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.run_polling()    return "🟢 MARA est en ligne", 200

def run_flask():
    app_flask.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_telegram_bot).start()
threading.Thread(target=run_flask).start()
