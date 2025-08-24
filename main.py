import requests
from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = "8369899594:AAGAFiK8rXMABUMKTaeyuO9EGlwzOGFSoiI"
HF_API_KEY = "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"
HF_MODEL = "mistralai/Mistral-7B-Instruct"

def query_huggingface(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(
        f"https://api-inference.huggingface.co/models/{HF_MODEL}",
        headers=headers,
        json=payload
)
    return response.json()[0]["generated_text"]

def handle_message(update, context):
    user_input = update.message.text
    ai_response = query_huggingface(user_input)
    update.message.reply_text(ai_response)

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
