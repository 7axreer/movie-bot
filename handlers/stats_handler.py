# handlers/stats_handler.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from config import ADMIN_IDS
from database import get_all_user_ids

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Siz bu buyruqdan foydalana olmaysiz.")
        return

    users = get_all_user_ids()
    active_users = 0

    for uid in users:
        try:
            await context.bot.send_message(chat_id=uid, text="📊 Statistika tekshirilmoqda...")
            active_users += 1
        except:
            continue

    await update.message.reply_text(f"📊 Faol foydalanuvchilar soni: {active_users} ta")

stats_handler = CommandHandler("stats", stats)
