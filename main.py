import openai
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Sélection de la clé API selon l'environnement
env = os.getenv("ENV", "dev")  # Par défaut: "dev"
if env == "prod":
    openai.api_key = os.getenv("OPENAI_API_KEY_PROD")
else:
    openai.api_key = os.getenv("OPENAI_API_KEY_DEV")

# Fonction pour interroger l'IA
async def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
)
    return response.choices[0].message.content

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, je suis MARA 🤖. Pose-moi une question, je te réponds avec mon cerveau IA.")

# Gestion des messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    gpt_response = await ask_gpt(user_message)
    await update.message.reply_text(gpt_response)

# Lancement du bot
app = ApplicationBuilder().token("8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
