from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram.ext import Dispatcher
from telegram.ext import CommandHandler
import logging

from key import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    start_handler = CommandHandler(['start', 'help'], do_start)
    echo_handler = MessageHandler(Filters.text, do_echo)
    keyboard_handler = CommandHandler('keyboard', do_keyboard)
    inline_keyboard_handler = CommandHandler('inline_keyboard', do_inline_keyboard)
    callback_handler = CallbackQueryHandler(keyboard_react)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(inline_keyboard_handler)
    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    logger.info(updater.bot.getMe())
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text = update.message.text

    logger.info(f'{username}{user_id} вызвал функцию "do_echo"')
    logger.info(f'{username}{user_id} вызвал функцию "start"')
    answer = f'Твои данные: {username}, {user_id}\nТы написал(а): {text}\nЯ знаю команды:\n/start\n/help\n/keyboard\n/inline_keyboard'
    update.message.reply_text(answer, reply_markup=ReplyKeyboardRemove())


def do_start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text = update.message.text

    logger.info(f'{username}{user_id} вызвал функцию')
    answer = [
        f'Твой ID: {user_id}',
        f'Твой юзер: {username}',
        f'Ты написал(а): {text}\n'
        f'Вот еще мои команды!:\n'
        f'/start\n/help\n/keyboard\n/inline_keyboard'
    ]
    answer = '\n'.join(answer)
    update.message.reply_text(answer)


def do_keyboard(update: Update, context: CallbackContext):
    buttons = [
        ['Раз', 'Два'],
        ['Три', 'Четыре'],
        ['Калькулетор']
    ]
    logger.info(f'Созданы кнопочки!{buttons}')
    keyboard = ReplyKeyboardMarkup(buttons)
    logger.info(f'Создана клава {keyboard}')
    text = 'Выбери кнопочку!'

    update.message.reply_text(
        text,
        reply_markup=keyboard
    )


def do_inline_keyboard(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    logger.info(f'{user_id=} вызвал функцию do_inline_keyboard')
    buttons = [
        ['Раз', 'Два'],
        ['Три', 'Четыре'],
        ['Калькулетор']
    ]
    keyboard_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]
    logger.info(f'Созданы кнопочки!{buttons}')
    keyboard = InlineKeyboardMarkup(keyboard_buttons)
    logger.info(f'Создана клава {keyboard}')
    text = 'Выбери кнопочку!'
    update.message.reply_text(
        text,
        reply_markup=keyboard
    )


def keyboard_react(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user.id
    logger.info(f'{user_id=} вызвал функцию keyboard_react')
    buttons = [
        ['Раз', 'Два'],
        ['Три', 'Четыре'],
        ['Калькулетор']
    ]
    for row in buttons:
        if query.data in row:
            row.pop(row.index(query.data))
    keyboard_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]
    logger.info(f'Созданы кнопочки!{buttons}')
    keyboard = InlineKeyboardMarkup(keyboard_buttons)
    text = 'Пока кнопочка!'
    query.edit_message_text(
        text,
        reply_markup=keyboard
    )



if __name__ == '__main__':
    main()
