# handlers/admin_handler.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from config import ADMIN_IDS

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return

    await update.message.reply_text(
        "🔒 Admin Panel:\n\n"
        "/add - Kino qo‘shish\n"
        "/broadcast - Reklama xabari yuborish\n"
        "/stats - Foydalanuvchilar statistikasi"
    )

admin_only_handler = CommandHandler("admin", admin_panel)
