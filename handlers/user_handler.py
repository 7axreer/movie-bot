# handlers/user_handler.py

from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from database import save_user

# Har bir xabar kelganda foydalanuvchini ro'yxatga olish
async def track_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_id = update.effective_user.id
        save_user(user_id)

track_user_handler = MessageHandler(filters.ALL, track_user)
