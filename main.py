import os

import telebot


bot = telebot.TeleBot('6509922141:AAHVGHERak-VcEOQ3LgR_4d_NzB3MNP8iY0')


@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Привет, <b>{message.from_user.first_name}</b>!')
    bot.send_message(message.chat.id, mess, parse_mode='html')





def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()