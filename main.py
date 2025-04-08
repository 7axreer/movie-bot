# main.py

from telegram.ext import ApplicationBuilder
from config import TOKEN
from handlers.add_handler import add_conv_handler
from handlers.retrieve_handler import retrieve_handler
from handlers.start_handler import start_handler
from handlers.cancel_handler import cancel_handler
from handlers.broadcast_handler import broadcast_handler
from handlers.admin_handler import admin_only_handler
from handlers.user_handler import track_user_handler
from handlers.stats_handler import stats_handler
from handlers.stats_handler import stats_handler
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(start_handler)
    app.add_handler(add_conv_handler)
    app.add_handler(retrieve_handler)
    app.add_handler(cancel_handler)
    app.add_handler(broadcast_handler)
    app.add_handler(admin_only_handler)
    app.add_handler(track_user_handler)
    app.add_handler(stats_handler) 
    app.add_handler(stats_handler)# Foydalanuvchini ro'yxatga olish

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
