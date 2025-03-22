import telebot
    
bot = telebot.TeleBot("7663125275:AAEOh5TO84wldZCSM71hX2bs-ZvZO-I31l8")
    
    # Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'Я принял нового пользователя!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "команды которые я имею: /help, /start, /bye, /hello")
    
    # Запуск бота
bot.polling()
