from telegram import Update, Message
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from config import ADMIN_IDS
from database import get_all_user_ids

BROADCAST = range(1)

async def start_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Bu buyruq faqat adminlar uchun.")
        return ConversationHandler.END

    await update.message.reply_text("📢 Reklama postini forward qiling (yoki har qanday postni yuboring).")
    return BROADCAST

async def handle_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = get_all_user_ids()
    message: Message = update.message
    success = 0

    for uid in users:
        try:
            await message.copy(chat_id=uid)
            success += 1
        except:
            continue

    await update.message.reply_text(f"✅ Xabar {success} foydalanuvchiga yuborildi.")
    return ConversationHandler.END

async def cancel_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Bekor qilindi.")
    return ConversationHandler.END

broadcast_handler = ConversationHandler(
    entry_points=[CommandHandler("broadcast", start_broadcast)],
    states={
        BROADCAST: [MessageHandler(filters.ALL & ~filters.COMMAND, handle_broadcast)],
    },
    fallbacks=[CommandHandler("cancel", cancel_broadcast)],
)
