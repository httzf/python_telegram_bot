from telegram import Update, ParseMode
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Dispatcher
from telegram.ext import MessageHandler, CommandHandler, CallbackQueryHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters

import logging
import datetime

from key import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text, do_echo)
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    keyboard_handler = CommandHandler('keyboard', do_keyboard)
    inline_keyboard_handler = CommandHandler('inline_keyboard', do_inline_keyboard)
    set_timer_handler = CommandHandler('set', set_timer)
    stop_timer_handler = CommandHandler('stop', stop_timer)
    start_timer_handler = MessageHandler(Filters.text('Start Timer'), set_timer)
    timer_stop_handler = MessageHandler(Filters.text('Stop Timer'), stop_timer)
    callback_handler = CallbackQueryHandler(keyboard_react)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(inline_keyboard_handler)
    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(set_timer_handler)
    dispatcher.add_handler(start_timer_handler)
    dispatcher.add_handler(timer_stop_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    logger.info(updater.bot.getMe())
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text = update.message.text

    logger.info(f'{username}{user_id} вызвал функцию "do_echo"')
    answer = [
        f'А чего команду не вызываешь?\n'
        f'Ну ладно!\n'
        f'Вот твои данные: {username}, {user_id}',
        f'\nТы написал(а): \n{text}',
        f'Вот какие знаю команды!:',
        f'/start, /help, /keyboard, /inline_keyboard'
    ]
    answer = '\n'.join(answer)
    update.message.reply_text(answer, reply_markup=ReplyKeyboardRemove())


def do_start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    logger.info(f'{username}{user_id} вызвал функцию')
    text = [
        f'<i>Привет, {username}!</i>',
        f'\nЯ обычный бот в телеграме с небольшим спектром возможностей\n'
        f'Чтобы ознакомиться с моими командами нажмите /help\n'
        f'\n '
        f'Удачного пользования!',
    ]
    text = '\n'.join(text)
    update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def do_help(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    logger.info(f'{username}{user_id} вызвал функцию')
    text = [
        f'<i>Привет, {username}!</i>'
        f' '
        f'\nВот что я <u>умею:</u>',
        f'/start'
        f'\n/help'
        f'\n/keyboard - клавиатурка в поле ввода текста'
        f'\n/inline_keyboard - клавиатурка от бота'
        f'\n '
        f'\nУдачного пользования!',
    ]
    text = '\n'.join(text)
    update.message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def do_keyboard(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    logger.info(f'{user_id=} вызвал функцию do_keyboard')
    buttons = [
        ['Start Timer', 'Stop Timer'],
    ]
    logger.info(f'Созданы кнопочки!{buttons}')
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    logger.info(f'Создана клава {keyboard}')
    text = 'Попробуй запустить секундомер!'

    update.message.reply_text(
        text,
        reply_markup=keyboard
    )
    logger.info(f'Ответ улетел')


def do_inline_keyboard(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    logger.info(f'{user_id=} вызвал функцию do_inline_keyboard')
    buttons = [
        [('Плейлист 1', 'https://youtu.be/uTuuz__8gUM?si=a4YM8IC-WM15LO6c'), ('Плейлист 2', 'https://youtu.be/pnP3UQQLiaw?si=M6wRbUkeNbKIb8EL')],
        [('Плейлист 3', 'https://youtu.be/Ium7_28Hams?si=CZ_lekTRCTfFcJjD'), ('Плейлист 4', 'https://youtu.be/hAK61XcBFGs?si=uxVOIkmKWdygdxN_')],
        [('Плейлист 5', 'https://youtu.be/grBFMP3HDZA?si=n199vFCF-SwyfGwI')]
    ]
    keyboard_buttons = [[InlineKeyboardButton(text=text[0], callback_data=text[0], url=text[1]) for text in row] for row in buttons]
    logger.info(f'Созданы кнопочки!{buttons}')
    keyboard = InlineKeyboardMarkup(keyboard_buttons)
    logger.info(f'Создана клава {keyboard}')
    text = 'Выбери себе плейлист для учебы!!'
    update.message.reply_text(
        text,
        reply_markup=keyboard
    )
    logger.info(f'Ответ улетел')


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


def set_timer(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    context.bot_data['user_id'] = user_id
    context.bot_data['timer'] = datetime.datetime.now()
    context.bot_data['timer_job'] = context.job_queue.run_repeating(show_seconds, 1)


def show_seconds(context: CallbackContext):
    logger.info(f'{context.job_queue.jobs()}')
    message_id = context.bot_data.get('message_id', None)
    user_id = context.bot_data['user_id']
    timer = datetime.datetime.now() - context.bot_data['timer']
    timer = timer.seconds
    text = f'прошло {timer} секунд'
    text += '\nнажмите Stop Timer на клавиатурке чтобы остановить таймер'
    if not message_id:
        message = context.bot.send_message(user_id, text)
        context.bot_data['message_id'] = message.message_id
    else:
        context.bot.edit_message_text(text, chat_id=user_id, message_id=message_id)


def stop_timer(update: Update, context: CallbackContext):
    logger.info(f'Запущена функция delete_timer')
    timer = datetime.datetime.now() - context.bot_data['timer']
    context.bot_data['timer_job'].schedule_removal()
    update.message.reply_text(f'Таймер остановлен. Прошло {timer} секунд')
    context.bot_data.clear()

if __name__ == '__main__':
    main()
