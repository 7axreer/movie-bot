from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    CommandHandler, MessageHandler, ConversationHandler,
    ContextTypes, filters
)
from config import ADMIN_IDS
from database import save_movie

CODE, TITLE, QUALITY, AUDIO, SUBTITLE, VIDEO = range(6)

# Tugmalar
quality_options = [["720p", "1080p"]]
audio_options = [["Uzb", "Eng", "Rus"]]
subtitle_options = [["Uzb", "Eng", "Rus", "-"]]

async def add_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❗️Faqat adminlar kino qo‘shishi mumkin.")
        return ConversationHandler.END
    await update.message.reply_text("🎬 Kino uchun kodni yuboring:\n\nBekor qilish: /cancel")
    return CODE

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    if not code.isdigit():
        await update.message.reply_text("❗️Faqat raqam yuboring:")
        return CODE
    context.user_data["code"] = code
    await update.message.reply_text("📌 Kino nomini kiriting:")
    return TITLE

async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text.strip()
    await update.message.reply_text(
        "🖥 Sifatni tanlang:",
        reply_markup=ReplyKeyboardMarkup(quality_options, resize_keyboard=True, one_time_keyboard=True)
    )
    return QUALITY

async def get_quality(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["quality"] = update.message.text.strip()
    await update.message.reply_text(
        "🔈 Audiolarni tanlang:",
        reply_markup=ReplyKeyboardMarkup(audio_options, resize_keyboard=True, one_time_keyboard=True)
    )
    return AUDIO

async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["audio"] = update.message.text.strip()
    await update.message.reply_text(
        "📝 Subtitrni tanlang:",
        reply_markup=ReplyKeyboardMarkup(subtitle_options, resize_keyboard=True, one_time_keyboard=True)
    )
    return SUBTITLE

async def get_subtitle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["subtitle"] = update.message.text.strip()
    await update.message.reply_text("🎞 Kino videosini yuboring:", reply_markup=ReplyKeyboardRemove())
    return VIDEO

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.video:
        await update.message.reply_text("❗️Faqat video yuboring.")
        return VIDEO

    file_id = update.message.video.file_id
    data = context.user_data

    save_movie(
        data["code"], data["title"], data["quality"],
        data["audio"], data["subtitle"], file_id
    )

    caption = f"<b>{data['title']}</b>\n\n🎥 {data['quality']} | 🔈 {data['audio']} | 📝 {data['subtitle']}"
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=file_id,
        caption=caption,
        parse_mode="HTML"
    )
    await update.message.reply_text("✅ Kino saqlandi!")
    return ConversationHandler.END

add_conv_handler = ConversationHandler(
    entry_points=[CommandHandler("add", add_movie)],
    states={
        CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_code)],
        TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_title)],
        QUALITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_quality)],
        AUDIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_audio)],
        SUBTITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_subtitle)],
        VIDEO: [MessageHandler(filters.VIDEO, handle_video)],
    },
    fallbacks=[]
)
