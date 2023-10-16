import telebot
from telebot import types
import math

bot=telebot.TeleBot("6509922141:AAHVGHERak-VcEOQ3LgR_4d_NzB3MNP8iY0")

@bot.message_handler(commands=["start"])
def start(message):
    prikaz = f'Привет, {message.from_user.first_name}, я - бот для решения квадратных уравнений \nАктивируй команду /equation для того, чтобы начать решать'
    bot.send_message(message.chat.id, prikaz)

@bot.message_handler(content_types=["text"])
def k(message):
    if message.text == "/equation":
        bot.send_message(message.from_user.id, 'Введи коэффициент а')
        bot.register_next_step_handler(message, input_a)
    else:
        bot.send_message(message.from_user.id, "Напиши /equation, что бы начать работу")

def input_a(message):
    global a
    a = float(message.text)
    if is_number(a):
        bot.send_message(message.chat.id, 'Введи значение b')
        bot.register_next_step_handler(message, input_b)
    else:
        bot.send_message(message.from_user.id, "Попробуй еще раз")
        input_a()

def input_b(message):
    global b
    b = float(message.text)
    bot.send_message(message.chat.id, 'Введи значение c')
    bot.register_next_step_handler(message, input_c)

def input_c(message):
    global c
    c = float(message.text)
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
        bot.send_message(message.from_user.id, "Первый корень (x1) = %.2f \nВторой корень (x2) = %.2f" % (x1, x2))
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