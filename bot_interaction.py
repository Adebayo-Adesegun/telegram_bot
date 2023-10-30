from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler


token = ''

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text='Hello and welcome to the BuiltIn Telegram bot!'
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
     chat_id=update.effective_chat.id, 
     text="""
     The BuiltIn Telegram bot supports the following commands:
      - /start: Welcoming users
      - /help: List of supported commands (you are here)
      - /first_name: Reports the user's first name
      - /last_name: Reports the user's last name
     """
    )

async def first_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await context.bot.send_message(
     chat_id=update.effective_chat.id, 
     text=f'Your first name is {update.message.from_user.first_name}'
    )


async def last_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await context.bot.send_message(
     chat_id=update.effective_chat.id, 
     text=f'Your last name is {update.message.from_user.last_name}'
    )


if __name__ == '__main__':
    application = Application.builder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    first_name_handler = CommandHandler('first_name', first_name)
    application.add_handler(first_name_handler)

    last_name_handler = CommandHandler('last_name', last_name)
    application.add_handler(last_name_handler)

    application.run_polling()