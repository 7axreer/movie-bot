# handlers/retrieve_handler.py

from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from database import get_movie_by_code

async def retrieve_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    if not code.isdigit():
        return

    movie = get_movie_by_code(code)
    if not movie:
        await update.message.reply_text("❌ Kino topilmadi.")
        return

    caption = f"<b>{movie['title']}</b>\n\n🎥 {movie['quality']} | 🔈 {movie['audio']} | 📝 {movie['subtitle']}\n\n{'🔗 https://t.me/movfilms_robot'}"
    await update.message.reply_video(
        video=movie["file_id"],
        caption=caption,
        parse_mode="HTML"
    )

retrieve_handler = MessageHandler(filters.TEXT & filters.Regex(r'^\d+$'), retrieve_movie)
