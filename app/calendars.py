import os
import datetime


# Создать класс Calendar
class Calendar:
    def __init__(self):
        self.events = {}

    # Создать метод create_event
    def create_event(self, event_name, event_date, event_time, event_details):
        event_id = len(self.events) + 1
        event = {
            "id": event_id,
            "name": event_name,
            "date": event_date,
            "time": event_time,
            "details": event_details
        }
        self.events[event_id] = event
        return event_id

    def read_event(self, event_id):
        # Запросите у пользователя название заметки, которую он хочет вывести на экран
        try:
            event_id_read = event_id
            path = f"{event_id_read}.txt"
            # Выведите заметку, если она существует. Если такой заметки нет, сообщите об этом пользователю
            if os.path.isfile(path):
                with open(f"{event_id_read}.txt", "r") as file:
                    lines = file.read()
                print("Текст заметки: ", lines)
            else:
                print("Такой заметки не существует. Введите другой запрос.")
        except:
            print("Что-то пошло не так. Попробуйте еще раз.")

    # Напишите функцию, которая редактирует заметку
    def edit_event(self, event_id, event_new_text):
        # Запросите у пользователя название заметки, которую он хочет отредактировать
        try:
            event_id_edit = event_id
            path = f"{event_id_edit}.txt"
            # Проверьте, есть ли такая заметка. Если да, обновите ее содержание. Если нет, сообщите об этом пользователю.
            if os.path.isfile(path):
                print("Заметка существует, вы можете ее отредактировать.")
                event_text_new = open(f"{event_id_edit}.txt", "w+")
                event_text_edit_new = event_new_text
                event_text_new.write(event_text_edit_new)
                print(f"Заметка {event_id_edit} обновлена.")
            else:
                print("Такой заметки не существует. Введите другой запрос.")
        except:
            print("Что-то пошло не так. Попробуйте еще раз.")

    # Напишите функцию, которая удаляет заметку
    def delete_event(self, event_id):
        # Запросите у пользователя название заметки, которую он хочет удалить
        try:
            event_id_delete = event_id
            path = f"{event_id_delete}.txt"
            # Проверьте, есть ли такая заметка. Если да, удалите ее. Если нет, сообщите об этом пользователю.
            if os.path.isfile(path):
                os.remove(f"{event_id_delete}.txt")
                print("Заметка удалена!")
            else:
                print("Такой заметки не существует. Введите другой запрос.")
        except:
            print("Что-то пошло не так. Попробуйте еще раз.")

    # Напишите функцию, которая выведет все заметки пользователя в порядке от самой короткой до самой длинной
    def display_events(self):
        try:
            events = [note for note in os.listdir() if note.endswith(".txt")]
            sorted_events = sorted(events, key=len, reverse=True)
            print(
                "Это список всех заметок в порядке от самой короткой до самой длинной: \n",
                sorted_events,
            )
        except:
            print("Что-то пошло не так. Попробуйте еще раз.")

    # Напишите функцию, которая выведет все заметки пользователя в порядке от самой длинной до самой короткой
    def display_sorted_events(self):
        try:
            notes = [note for note in os.listdir() if note.endswith(".txt")]
            sorted_list = sorted(notes, key=len)
            print(
                "\nЭто список заметок в порядке от самой длинной до самой короткой: \n",
                sorted_list,
            )
        except:
            print("Что-то пошло не так. Попробуйте еще раз.")

 # Зададим глобально доступный объект календаря
calendar = Calendar()

# Создать обработчик для создания событий
def event_create_handler(update, context):
    try:
        # Взять данные о событии из сообщения пользователя
        event_name = update.message.text[14:]
        event_date = "2023-03-14"
        event_time = "14:00"
        event_details = "Описание события"

        # Создать событие с помощью метода create_event класса Calendar
        event_id = calendar.create_event(event_name, event_date, event_time, event_details)

        # Отправить пользователю подтверждение
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Событие {event_name} создано и имеет номер {event_id}.")
    except:
         # Отправить пользователю сообщение об ошибке
         context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")

# Зарегистрировать обработчик, чтобы он вызывался по команде /create_event
updater.dispatcher.add_handler(CommandHandler('create_event', event_create_handler))


def event_read_handler(update, context):
    try:
        event_id = update.message.text[14:]
        calendar.read_event(event_id)

        context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"Событие {event_id} создано и имеет номер {event_id}.")