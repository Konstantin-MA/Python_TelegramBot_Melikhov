import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import note_actions
import secrets

from asyncio import Queue

botQueue = Queue()
updater = Updater(secrets.API_TOKEN, botQueue)
#updater = Updater(token="API_TOKEN")

# Создать обработчик для создания заметок create_handler
def create_note_handler(update, context):
    try:
        # Получить текст заметки из сообщения пользователя
        note_text = update.message.text
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Создать заметку с помощью функции create_note(note_text, note_name)
        note_actions.create_note(note_text, note_name)
        # Отправить пользователю подтверждение, что заметка создана
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию create_note_handler как CommandHandler для команды /create
updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))


# Создать обработчик для чтения заметок create_handler
def read_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Открыть заметку с помощью функции read_note(note_name)
        note_actions.read_note(note_name)
        # Отправить пользователю подтверждение, что заметка открыта
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} открыта.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию read_note_handler как CommandHandler для команды /read
updater.dispatcher.add_handler(CommandHandler('read', read_note_handler))


def edit_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Получить текст заметки из сообщения пользователя
        note_new_text = update.message.text
        # Изменить заметку с помощью функции edit_note(note_name, note_new_text)
        note_actions.edit_note(note_name, note_new_text)
        # Отправить пользователю подтверждение, что заметка изменена
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} изменена.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию edit_note_handler как CommandHandler для команды /edit
updater.dispatcher.add_handler(CommandHandler('edit', edit_note_handler))


# Создать обработчик для удаления заметок create_handler
def delete_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Удалить заметку с помощью функции delete_note(note_name)
        note_actions.delete_note(note_name)
        # Отправить пользователю подтверждение, что заметка удалена
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию delete_note_handler как CommandHandler для команды /delete
updater.dispatcher.add_handler(CommandHandler('delete', delete_note_handler))


# Создать обработчик для просмотра списка заметок create_handler
def display_note_handler(update, context):
    try:
        # Открыть список заметок с помощью функции display_notes()
        note_actions.display_notes()
        # Отправить пользователю подтверждение, что список заметок открыт
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Список заметок открыт.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию display_note_handler как CommandHandler для команды /display
updater.dispatcher.add_handler(CommandHandler('display', display_note_handler))


# Создать обработчик для просмотра сортированного списка заметок create_handler
def display_sorted_note_handler(update, context):
    try:
        # Открыть сортированный список заметок с помощью функции display_notes()
        note_actions.display_sorted_notes()
        # Отправить пользователю подтверждение, что сортированный список заметок открыт
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Сортированный список заметок открыт.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию display_sorted_note_handler как CommandHandler для команды /display sorted
updater.dispatcher.add_handler(CommandHandler('display sorted', display_sorted_note_handler))

