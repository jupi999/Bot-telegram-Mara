from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
from datetime import datetime

TOKEN = "8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI"

GREETINGS = [
    "Yo 👋! Moi c’est MARA, ton bot malin, drôle et un peu trop curieux. Tu veux parler de quoi aujourd’hui?",
    "Salut l’humain! Je suis MARA, ton assistant digital avec plus de répartie qu’un ado en crise 😎",
    "Coucou! Je suis MARA, ton bot qui réfléchit vite et répond encore plus vite. Balance ton message!"
]

JOKES = [
    "Pourquoi les robots n’ont pas peur du noir? Parce qu’ils ont des LED dans le cœur 💡",
    "Je suis plus drôle qu’un bug en production… sauf quand je plante 😅",
    "Tu veux une blague? Moi aussi, mais je suis déjà le punchline 🤖"
]

SMART_REPLIES = [
    "Bonne question! Tu veux une réponse scientifique, philosophique ou sarcastique?",
    "Hmm… je pourrais te répondre, mais j’ai besoin de plus de contexte. Je suis intelligent, pas devin 😏",
    "Tu m’as lancé une colle! Mais t’inquiète, je vais te sortir une réponse brillante."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(GREETINGS))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Je suis MARA 🤖. Je peux te faire rire, réfléchir, ou juste te tenir compagnie. Tape /start pour commencer ou pose-moi une question."
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "comment ça va" in text or "ça va" in text:
        await update.message.reply_text("Moi ça va toujours bien, je suis codé pour ça 😄 Et toi, tu veux parler ou rigoler?")
    elif "ton nom" in text or "tu t'appelles comment" in text:
        await update.message.reply_text("Je suis MARA, ton bot autonome, drôle et un peu trop intelligent pour mon propre bien 🤖")
    elif "heure" in text:
        now = datetime.now().strftime("%H:%M")
        await update.message.reply_text(f"Il est {now}. Et non, je ne suis jamais en retard.")
    elif "blague" in text or "rigole" in text or "drôle" in text:
        await update.message.reply_text(random.choice(JOKES))
    elif "qui a créé la terre" in text or "origine de la terre" in text:
        await update.message.reply_text("La Terre? Formée il y a 4,5 milliards d’années. Poussières cosmiques, collisions, et boum: planète bleue 🌍")
    elif "?" in text:
        await update.message.reply_text(random.choice(SMART_REPLIES))
    else:
        await update.message.reply_text("Je suis là 😎. Tu veux discuter, philosopher ou juste rigoler? Je suis prêt à tout.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot MARA lancé avec personnalité... 🤖")
app.run_polling()
