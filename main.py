import os
import math
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=["start"])
def start(message):
    prikaz = (
        f'Привет, {message.from_user.first_name}, я - бот для решения квадратных уравнений '
        '\nАктивируй команду /equation для того, чтобы начать решать'
    )
    bot.send_message(message.chat.id, prikaz)


@bot.message_handler(content_types=["text"])
def k(message):
    if message.text == "/equation":
        bot.send_message(message.from_user.id, 'Введи коэффициент а')
        bot.register_next_step_handler(message, input_a)
    else:
        bot.send_message(message.from_user.id, "Напиши /equation, чтобы начать работу")


def input_a(message):
    global a
    try:
        a = float(message.text)
        bot.send_message(message.chat.id, 'Введи значение b')
        bot.register_next_step_handler(message, input_b)
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Введи число для коэффициента 'a'")



def input_b(message):
    global b
    try:
        b = float(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Введи число для коэффициента 'b'")
        return  # Вернуться, чтобы не продолжать выполнение функции после ошибки
    bot.send_message(message.chat.id, 'Введи значение c')
    bot.register_next_step_handler(message, input_c)


def input_c(message):
    global c
    try:
        c = float(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, "Некорректный ввод. Введи число для коэффициента 'c'")
        return  # Вернуться, чтобы не продолжать выполнение функции после ошибки
    D = (b * b) - (4 * a * c)
    bot.send_message(message.from_user.id, "Дискриминант (D) = %.2f" % D)

    if D < 0:
        bot.send_message(message.from_user.id, "D < 0, в уравнении нет корней")
        bot.send_message(message.from_user.id, "Напиши /start, чтобы начать сначала")
    elif D == 0:
        bot.send_message(message.from_user.id, "D = 0, в уравнении 1 корень")
        x1 = (-b + math.sqrt(D)) / (2 * a)
        bot.send_message(message.from_user.id, "Корень (x) = %.2f" % x1)
        bot.send_message(message.from_user.id, "Напиши /start, чтобы начать сначала")
    elif D > 0:
        bot.send_message(message.from_user.id, "D > 0, в уравнении 2 корня")
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        bot.send_message(message.from_user.id, "Первый корень (x1) = %.2f \nВторой корень (x2) = %.2f" % (x1, x2)
                        )
        bot.send_message(message.from_user.id, "Напиши /start, чтобы начать сначала")


def is_number(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
