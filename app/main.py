import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application, ApplicationBuilder

import secrets
from asyncio import Queue

botQueue = Queue()
updater = Updater(secrets.API_TOKEN, botQueue)

import re
import os
import os.path


# Создайте функцию, которая создает заметку по запросу пользователя
def build_note(note_text, note_name):
    # Проверьте, существует ли файл, название которого указывает пользователь.
    # Если нет, создайте новый файл. Если да, замените существующий файл на новый.
    try:
        try:
            file = open(f"{note_name}.txt", "r+", encoding="utf-8")
            print("Такой файл существует")
        except IOError:
            file = open(f"{note_name}.txt", "w+", encoding="utf-8")
            print("Файл создан")
        file.write(note_text)
        print(f"Заметка {note_name} создана.")
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая запрашивает название и текст заметки, а затем создает ее
def create_note(note_name, note_text):
    # Создайте файл с заметкой
    try:
        # Запросите название заметки и проверьте его на наличие запрещенных символов
        forbidden_symbols = "\\|/*<>?:"  # набор запрещенных символов для Windows
        pattern = "[{0}]".format(forbidden_symbols)
        if re.search(pattern, note_name):
            print(
                "Вы ввели недопустимые символы в названии файла. Переименуйте заметку."
            )
        # Запросите текст заметки и создайте заметку
        else:
            print("Название заметки создано.")
            build_note(note_text, note_name)
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая прочитает заметку и выведет ее текст
def read_note(note_name):
    # Запросите у пользователя название заметки, которую он хочет вывести на экран
    try:
        note_name_read = note_name
        path = f"{note_name_read}.txt"
        # Выведите заметку, если она существует. Если такой заметки нет, сообщите об этом пользователю
        if os.path.isfile(path):
            with open(f"{note_name_read}.txt", "r") as file:
                lines = file.read()
            print("Текст заметки: ", lines)
        else:
            print("Такой заметки не существует. Введите другой запрос.")
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая редактирует заметку
def edit_note(note_name, note_new_text):
    # Запросите у пользователя название заметки, которую он хочет отредактировать
    try:
        note_name_edit = note_name
        path = f"{note_name_edit}.txt"
        # Проверьте, есть ли такая заметка. Если да, обновите ее содержание. Если нет, сообщите об этом пользователю.
        if os.path.isfile(path):
            print("Заметка существует, вы можете ее отредактировать.")
            note_text_new = open(f"{note_name_edit}.txt", "w+")
            note_text_edit_new = note_new_text
            note_text_new.write(note_text_edit_new)
            print(f"Заметка {note_name_edit} обновлена.")
        else:
            print("Такой заметки не существует. Введите другой запрос.")
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая удаляет заметку
def delete_note(note_name):
    # Запросите у пользователя название заметки, которую он хочет удалить
    try:
        note_name_delete = note_name
        path = f"{note_name_delete}.txt"
        # Проверьте, есть ли такая заметка. Если да, удалите ее. Если нет, сообщите об этом пользователю.
        if os.path.isfile(path):
            os.remove(f"{note_name_delete}.txt")
            print("Заметка удалена!")
        else:
            print("Такой заметки не существует. Введите другой запрос.")
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая выведет все заметки пользователя в порядке от самой короткой до самой длинной
def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]
        sorted_notes = sorted(notes, key=len, reverse=True)
        print(
            "Это список всех заметок в порядке от самой короткой до самой длинной: \n",
            sorted_notes,
        )
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая выведет все заметки пользователя в порядке от самой длинной до самой короткой
def display_sorted_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]
        sorted_list = sorted(notes, key=len)
        print(
            "\nЭто список заметок в порядке от самой длинной до самой короткой: \n",
            sorted_list,
        )
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Создайте функцию, которая управляет всеми операциями с заметками
def main():
    # Создайте бесконечный цикл работы с заметками и настройте меню для пользователя
    while True:
        action = input(
            "Нажмите цифру, чтобы выбрать действие, которое хотите выполнить с заметками: "
            "\n"
            "Введите 1, чтобы создать заметку с определенным названием и текстом."
            "\n"
            "Введите 2, чтобы вывести на экран нужную вам заметку."
            "\n"
            "Введите 3, чтобы отредактировать нужную вам заметку."
            "\n"
            "Введите 4, чтобы удалить заметку."
            "\n"
            "Введите 5, чтобы вывести все заметки в порядке от самой короткой до самой длинной."
            "\n"
            "Введите 6, чтобы вывести все заметки в порядке от самой длинной до самой короткой."
            "\n"
            "Введите n, чтобы выйти из приложения."
            "\n"
            "Что вы хотите сделать?"
        ).lower()
        # Проверьте символ, который ввел пользователь. Если он некорректный, сообщите об этом.
        allowed_symbols = "123456n"
        pattern1 = "[{0}]".format(allowed_symbols)
        if re.search(pattern1, action):
            print("Вы ввели корректный запрос. Действие сейчас выполнится.")
            if action == "1":
                create_note()
            if action == "2":
                read_note()
            if action == "3":
                edit_note()
            if action == "4":
                delete_note()
            if action == "5":
                display_notes()
            if action == "6":
                display_sorted_notes()
            if action == "n":
                break
        else:
            print(
                "Вы ввели некорректный символ. Пожалуйста, введите цифры от 1 до 6 или n."
            )

        # Предложите пользователю продолжить работу с приложением
        print("Чтобы продолжить работать с заметками, нажмите y/n")
        answer = input().lower()
        if answer != "y":
            break


# Создать обработчик для создания заметок create_handler
def create_note_handler(update, context):
    try:
        # Получить текст заметки из сообщения пользователя
        note_text = update.message.text
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Создать заметку с помощью функции create_note(note_text, note_name)
        create_note(note_text, note_name)
        # Отправить пользователю подтверждение, что заметка создана
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


# Создать обработчик для чтения заметок create_handler
def read_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Открыть заметку с помощью функции read_note(note_name)
        read_note(note_name)
        # Отправить пользователю подтверждение, что заметка открыта
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} открыта.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def edit_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Получить текст заметки из сообщения пользователя
        note_new_text = update.message.text
        # Изменить заметку с помощью функции edit_note(note_name, note_new_text)
        edit_note(note_name, note_new_text)
        # Отправить пользователю подтверждение, что заметка изменена
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} изменена.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


# Создать обработчик для удаления заметок create_handler
def delete_note_handler(update, context):
    try:
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Удалить заметку с помощью функции delete_note(note_name)
        delete_note(note_name)
        # Отправить пользователю подтверждение, что заметка удалена
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


# Создать обработчик для просмотра списка заметок create_handler
def display_note_handler(update, context):
    try:
        # Открыть список заметок с помощью функции display_notes()
        display_notes()
        # Отправить пользователю подтверждение, что список заметок открыт
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Список заметок открыт.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


# Создать обработчик для просмотра сортированного списка заметок create_handler
def display_sorted_note_handler(update, context):
    try:
        # Открыть сортированный список заметок с помощью функции display_notes()
        display_sorted_notes()
        # Отправить пользователю подтверждение, что сортированный список заметок открыт
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Сортированный список заметок открыт.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


app = Application.builder().token("TOKEN").build()



# Добавить функцию create_note_handler как CommandHandler для команды /create
app.add_handler(CommandHandler('create', create_note_handler))

# Добавить функцию read_note_handler как CommandHandler для команды /read
app.add_handler(CommandHandler('read', read_note_handler))

# Добавить функцию edit_note_handler как CommandHandler для команды /edit
app.add_handler(CommandHandler('edit', edit_note_handler))

# Добавить функцию delete_note_handler как CommandHandler для команды /delete
app.add_handler(CommandHandler('delete', delete_note_handler))

# Добавить функцию display_note_handler как CommandHandler для команды /display
app.add_handler(CommandHandler('display', display_note_handler))

# Добавить функцию display_sorted_note_handler как CommandHandler для команды /display sorted
app.add_handler(CommandHandler('display sorted', display_sorted_note_handler))


updater.start_polling()