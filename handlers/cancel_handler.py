# handlers/cancel_handler.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Bekor qilindi.")
    return ConversationHandler.END

cancel_handler = CommandHandler("cancel", cancel)
