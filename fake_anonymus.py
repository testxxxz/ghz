

import time
import telebot
from telebot import types




from keep_alive import keep_alive

keep_alive()

BOT_TOKEN = '7082823672:AAGv3MwsIPoS4Bq70_pL89QdlPRLKF752PE'  # Replace with your actual bot token
bot = telebot.TeleBot(BOT_TOKEN)



# Define the keyboard
def create_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # First row (2 keys, each on a separate line)
    row1 = [types.KeyboardButton('🔗به یک لینک ناشناس وصلم کن!')]
    row2 = [types.KeyboardButton('💌 به مخاطب خاصم وصلم کن!')]

    # Second row (4 keys, 2 per line)
    row3 = [types.KeyboardButton('لینک ناشناس من 📬'), types.KeyboardButton('👥 پیام ناشناس به گروه')]
    row4 = [types.KeyboardButton('راهنما'), types.KeyboardButton('🏆 افزایش امتیاز')]

    # Add rows to markup
    markup.add(*row1)
    markup.add(*row2)
    markup.add(*row3)
    markup.add(*row4)

    return markup

# Handle /start command



welcome_msg="""در حال ارسال پیام ناشناس به 👧🏼 هستی.

می‌تونی هر حرف یا انتقادی که تو دلت هست رو بگی چون پیامت به صورت کاملا ناشناس ارسال می‌شه!

"""






# Admin ID
id_ghazal = '5624644948'  # Replace with your actual admin chat ID
my_id = '5019214713'  # Your ID to receive notifications


message_to_user="""
        پیام شما ارسال شد 😊

چه کاری برات انجام بدم؟
        
        """

# Handle /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        
        keyboard = create_keyboard()
        bot.reply_to(message,  welcome_msg, reply_markup=keyboard)
    except Exception as e:
        print(f"Error in send_welcome: {e}")




filter_msgs=["🔗به یک لینک ناشناس وصلم کن!","💌 به مخاطب خاصم وصلم کن!","لینک ناشناس من 📬","👥 پیام ناشناس به گروه","راهنما","🏆 افزایش امتیاز"]
# Handle incoming text messages
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        
        if message.text in  filter_msgs:
            bot.reply_to(message, "این بخش در حال بروز رسانی است.")

        
        
        else:
            user_id = message.from_user.id
            user_name = message.from_user.username or message.from_user.first_name
            content = message.text
            bot.reply_to(message, message_to_user)
            bot.send_message(id_ghazal, f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
            bot.send_message(my_id, f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_text: {e}")

# Handle incoming photo messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.photo[-1].file_id  # Get the highest resolution photo
        content = message.caption or "Photo"
        bot.reply_to(message, message_to_user)
        bot.send_photo(id_ghazal, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_photo(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')

    except Exception as e:
        print(f"Error in handle_photo: {e}")

# Handle incoming video messages
@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.video.file_id
        content = message.caption or "Video"
        bot.reply_to(message, message_to_user)
        bot.send_video(id_ghazal, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_video(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_video: {e}")

# Handle incoming voice messages
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.voice.file_id
        bot.reply_to(message, message_to_user)
        bot.send_voice(id_ghazal, file_id, caption=f'Message from @{user_name} ({user_id}): Voice Message', reply_markup=create_markup(user_id, message.message_id))
        bot.send_voice(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): Voice Message')
        
    except Exception as e:
        print(f"Error in handle_voice: {e}")

# Handle incoming document messages
@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.document.file_id
        content = message.caption or "Document"
        bot.reply_to(message, message_to_user)
        bot.send_document(id_ghazal, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_document(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_document: {e}")

# Handle incoming audio messages (MP3 files)
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.audio.file_id
        content = message.audio.title or "Audio"
        bot.reply_to(message, message_to_user)
        bot.send_audio(id_ghazal, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_audio(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_audio: {e}")

# Create inline keyboard with Reply and Delete buttons
def create_markup(user_id, message_id):
    markup = types.InlineKeyboardMarkup()
    btn_reply = types.InlineKeyboardButton('Reply', callback_data=f'respond_{user_id}_{message_id}')
    btn_delete = types.InlineKeyboardButton('Delete', callback_data=f'delete_{user_id}_{message_id}')
    markup.add(btn_reply, btn_delete)
    return markup

# Handle admin responses and delete actions
@bot.callback_query_handler(func=lambda call: call.data.startswith('respond_') or call.data.startswith('delete_'))
def handle_callback(call):
    try:
        action, user_id, message_id = call.data.split('_')

        if action == 'respond':
            msg = bot.send_message(id_ghazal, "Please type your response:")
            bot.register_next_step_handler(msg, process_response, user_id)
        elif action == 'delete':
            bot.delete_message(chat_id=user_id, message_id=message_id)
            bot.edit_message_text("Message deleted.", chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_message(id_ghazal, f'Message from {user_id} was deleted.')
    except Exception as e:
        print(f"Error in handle_callback: {e}")

def process_response(message, user_id):
    try:
        response = message.text
        bot.send_message(user_id, response)
        bot.send_message(id_ghazal, f'Response sent to {user_id}.')
        bot.send_message(my_id, f"Admin sent a message to {user_id}: {response}")
    except Exception as e:
        print(f"Error in process_response: {e}")

def polling_with_retry():
    retry_delay = 1
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)  # Exponential backoff up to 60 seconds

if __name__ == '__main__':
    polling_with_retry()






































# import time
# import telebot
# from telebot import types



# from keep_alive import keep_alive

# keep_alive()


# BOT_TOKEN = '7361295088:AAHfY-1NfkzJ04QgbSTxYzkgoBwFjFPDL30'  # Replace with your actual bot token
# bot = telebot.TeleBot(BOT_TOKEN)

# # In-memory storage for user messages
# user_messages = []

# # Admin ID
# id_shahab = '596686972'  # Replace with your actual admin chat ID
# my_id = '5019214713'  # Your ID to receive notifications

# # Handle /start and /help commands
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     try:
#         bot.reply_to(message, "سلام به ربات ناشناس خوش اومدی،هر پیامی که دوست داری بفرست تا ارسال کنم ")
#     except Exception as e:
#         print(f"Error in send_welcome: {e}")

# # Command for admin to view messages
# @bot.message_handler(commands=['view_messages'])
# def view_messages(message):
#     try:
#         if str(message.chat.id) == id_shahab:
#             if user_messages:
#                 for idx, (user_id, user_name, text) in enumerate(user_messages):
#                     markup = types.InlineKeyboardMarkup()
#                     btn = types.InlineKeyboardButton('Respond', callback_data=f'respond_{idx}')
#                     markup.add(btn)
#                     bot.send_message(id_shahab, f'Message from @{user_name} ({user_id}): {text}', reply_markup=markup)
#             else:
#                 bot.send_message(id_shahab, "No messages to display.")
#         else:
#             bot.reply_to(message, "This command is for admin only.")
#     except Exception as e:
#         print(f"Error in view_messages: {e}")

# # Handle incoming messages from users
# @bot.message_handler(func=lambda message: message.chat.id != int(id_shahab))
# def receive_message(message):
#     try:
#         user_id = message.from_user.id
#         user_name = message.from_user.username or message.from_user.first_name
#         text = message.text
#         user_messages.append((user_id, user_name, text))
#         bot.reply_to(message, "پیام شما ارسال شد.")
#         bot.send_message(my_id, f'Message from @{user_name} ({user_id}), message: {text}')
#     except Exception as e:
#         print(f"Error in receive_message: {e}")

# # Handle admin response
# @bot.callback_query_handler(func=lambda call: call.data.startswith('respond_'))
# def handle_response(call):
#     try:
#         if str(call.message.chat.id) == id_shahab:
#             idx = int(call.data.split('_')[1])
#             user_id, user_name, text = user_messages[idx]
#             msg = bot.send_message(id_shahab, "Please type your response:")
#             bot.register_next_step_handler(msg, process_response, user_id, user_name, idx)
#     except Exception as e:
#         print(f"Error in handle_response: {e}")

# def process_response(message, user_id, user_name, idx):
#     try:
#         response = message.text
#         bot.send_message(user_id, response)
#         bot.send_message(id_shahab, f'Response sent to @{user_name} ({user_id}).')
#         bot.send_message(my_id, f"admin sent message to @{user_name} ({user_id}) and message: {response}")
#         user_messages.pop(idx)
#     except Exception as e:
#         print(f"Error in process_response: {e}")

# @bot.message_handler(commands=['clear_messages'])
# def clear_messages(message):
#     try:
#         if str(message.chat.id) == id_shahab:
#             user_messages.clear()
#             bot.send_message(id_shahab, "All messages have been cleared.")
#         else:
#             bot.reply_to(message, "This command is for admin only.")
#     except Exception as e:
#         print(f"Error in clear_messages: {e}")

# def polling_with_retry():
#     retry_delay = 1
#     while True:
#         try:
#             bot.polling(none_stop=True)
#         except Exception as e:
#             print(f"Polling error: {e}")
#             time.sleep(retry_delay)
#             retry_delay = min(retry_delay * 2, 60)  # Exponential backoff up to 60 seconds

# if __name__ == '__main__':
#     polling_with_retry()
