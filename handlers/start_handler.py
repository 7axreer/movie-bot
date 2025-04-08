# handlers/start_handler.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from database import save_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    save_user(user_id)
    await update.message.reply_text("🎬 Xush kelibsiz! Kino kodini yuboring!")

start_handler = CommandHandler("start", start)
