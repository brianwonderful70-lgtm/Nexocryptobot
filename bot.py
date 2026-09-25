import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load token from environment variables (Railway will inject this)
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *NexoCryptoBot is online!*\n\n"
        "I'm your smart crypto assistant. Currently under development.\n"
        "Try /help for available commands.",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "*Available Commands:*\n"
        "/start - Welcome message\n"
        "/help - This help message\n"
        "/price [ticker] - *Coming soon*\n"
        "/insight - *Coming soon*"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Placeholder - replace with crypto logic
    await update.message.reply_text(f"Received: {update.message.text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🚀 NexoCryptoBot starting with long polling...")
    app.run_polling()
