import telebot
from telebot import types
import random
import string
import time
import logging

# Define your bot token here
BOT_TOKEN = '7814126602:AAGzhZjU04L9n9TJQWynL-ndg8aYirmxOXw'
bot = telebot.TeleBot(BOT_TOKEN)

# Store the original order message info
order_messages = {}  # Dictionary to store message_id to user_id mapping for order tracking

# Generate a random order ID
def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Define channels for user to join
CHANNELS = [
    {"name": "Main Channel", "username": "@ModVipRM"},
    {"name": "Mod Channel", "username": "@modDirect_download"},
    {"name": "Backup Channel", "username": "@ModviprmBackup"}
]

# Sample storage for user data
user_data = {}
total_users = set()

# Channel IDs for request forwarding
CHORKI_CRACK_CHANNEL_ID = -1002113563800
HOICHOI_CRACK_CHANNEL_ID = -1002113563800
CHORKI_ON_MAIL_CHANNEL_ID = -1002113563800
HOICHOI_ON_MAIL_CHANNEL_ID = -1002113563800
GROUP_ID = -1002263161625
REVIEW_CHANNEL_ID = -1002113563800
ADMIN_USER_IDS = {7303810912,5991909954}  # Replace with actual admin user IDs

# Options for withdrawal items and points cost
options = {
    "💰 Chorki Crack": {"cost": 0, "channel_id": CHORKI_CRACK_CHANNEL_ID},
    "👥 Hoichoi Crack": {"cost": 3, "channel_id": HOICHOI_CRACK_CHANNEL_ID},
    "💲 Hoichoi 30 Days": {"cost": 15, "channel_id": CHORKI_ON_MAIL_CHANNEL_ID, "group_id": GROUP_ID},
    "📂 Hoichoi Own mail": {"cost": 30, "channel_id": HOICHOI_ON_MAIL_CHANNEL_ID, "group_id": GROUP_ID},
}

# Account storage
accounts = {
    "💰 Chorki Crack": [

    ],
    "👥 Hoichoi Crack": [
        {"username": "datta.siddhartha@rediffmail.com", "password": "chem@1980"},
        {"username": "soumik.bsp@gmail.com", "password": "bhu18042015"},
        {"username": "sunscriptysubscripty@gmail.com", "password": "Yoursubhub"},
        {"username": "bjeerupam@gmail.com", "password": "Shub00@76"}
    ],
    "💲 Hoichoi 30 Days": [
        {"username": "datta.siddhartha@rediffmail.com", "password": "chem@1980"},
        {"username": "soumik.bsp@gmail.com", "password": "bhu18042015"},
        {"username": "sunscriptysubscripty@gmail.com", "password": "Yoursubhub"},
        {"username": "bjeerupam@gmail.com", "password": "Shub00@76"}
        ]
}

# Set up logging
logging.basicConfig(level=logging.INFO)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_") or call.data == "cancel")
def handle_confirm_or_cancel(call):
    user_id = call.from_user.id
    action = call.data.split("_")[0]
    option = call.data.split("_")[1] if action == "confirm" else None

    if action == "confirm":
        cost = options[option]["cost"]

        # Check if user has sufficient balance
        if user_data.get(user_id, {}).get("balance", 0) >= cost:
            # Deduct the balance for the withdrawal
            user_data[user_id]["balance"] -= cost
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Your withdrawal for {option} has been confirmed. {cost} points have been deducted.")
            
            # Generate and send order confirmation
            order_id = generate_order_id()
            message_text = (
                f"✅ *New Order Received*\n\n"
                f"🔰 *Service:* {option}\n"
                f"👤 *User:* {call.from_user.full_name}\n"
                f"🆔 *User ID:* {user_id}\n"
                f"📈 *Quantity:* 1\n"
                f"💰 *Order Charge:* {cost} points\n"
                f"📛 *Order ID:* \\[{order_id}\\]\n"
                f"🔗 *Profile Link:* Hidden\n\n"
                f"🚀 *Get Premium Accounts Here ➡️* @OTTFREEBOT"
            )

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("Track Order Details", url="https://t.me/OTTFREEBOT"))

            # Send order message only to the channel if it's "Hoichoi 30 Days"
            if option == "💲 Hoichoi 30 Days":
                bot.send_message(options[option]["channel_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
            else:
                # For other options, send to both the channel and group
                order_msg = bot.send_message(options[option]["channel_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
                order_messages[order_msg.message_id] = user_id  # Store message ID with user ID

                # Forward to group if not "Hoichoi 30 Days"
                if "group_id" in options[option]:
                    group_msg = bot.send_message(options[option]["group_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
                    order_messages[group_msg.message_id] = user_id  # Store message ID with user ID

            # Special handling for "📂 Hoichoi Own mail" to always forward the request
            if option == "📂 Hoichoi Own mail":
                bot.send_message(user_id, "🔹 Your request for 'Hoichoi Own Mail' has been forwarded to our team. We will notify you once it’s processed.")
            elif option in accounts and accounts[option]:  # For other options, check if accounts are available
                # Assign account if available and remove from list
                account = accounts[option].pop(0)
                account_message = f"🔹 **{option} Account**:\nUsername: {account['username']}\nPassword: {account['password']}"
                bot.send_message(user_id, account_message)
            else:
                # Notify user if no accounts available (excluding "📂 Hoichoi Own mail")
                bot.send_message(user_id, "❌ Sorry, no accounts are currently available for this service.")
        else:
            bot.answer_callback_query(call.id, "❌ You don't have enough points to make this withdrawal.")
    elif action == "cancel":
        bot.send_message(user_id, "Withdrawal request has been canceled.", reply_markup=get_main_menu_keyboard())



def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("💰 Balance", "👥 Referral")
    keyboard.row("💲 Withdraw", "👥 Submit Review")
    keyboard.row("📂 PROOFS", "📞 Support")
    return keyboard

# Inside the `start` function, update this section to store referrer info
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    referrer_id = int(message.text.split()[1]) if len(message.text.split()) > 1 else None

    if user_id not in total_users:
        total_users.add(user_id)
        user_data[user_id] = {'balance': 0, 'invited_users': 0, 'bonus_claimed': False, 'referrer_id': referrer_id}

        if referrer_id and referrer_id != user_id and referrer_id in user_data:
            user_data[referrer_id]['referrals'] = user_data[referrer_id].get('referrals', []) + [user_id]

    message_text = "🟢 Welcome In Our Premium Account Giveaway Bot\n"
    message_text += "---------------------------------------\n"
    for channel in CHANNELS:
        message_text += f"🔹 [{channel['name']}](https://t.me/{channel['username'][1:]})\n"
    message_text += "---------------------------------------\n\n"
    message_text += "✅ After completing all tasks, click on ✅ *Joined!*"

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("✅ Joined", callback_data="joined"))

    bot.send_message(
        chat_id=user_id,
        text=message_text,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# Inside the `joined_button` callback, add this section to notify referrer
@bot.callback_query_handler(func=lambda call: call.data == "joined")
def joined_button(call):
    user_id = call.from_user.id
    referrer_id = user_data.get(user_id, {}).get("referrer_id")
    all_joined = True

    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(channel["username"], user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                all_joined = False
                break
        except Exception:
            all_joined = False
            break

    if all_joined:
        bot.send_message(user_id, "Thank you for joining! You may now use the bot's premium features.", reply_markup=get_main_menu_keyboard())

        # Award points and notify referrer, if any
        if referrer_id:
            user_data[referrer_id]['balance'] += 1
            user_data[referrer_id]['invited_users'] += 1
            referrer_name = call.from_user.full_name  # Get the name of the new user
            bot.send_message(referrer_id, f"❤️ Your referral {referrer_name} joined our channel.\n➕ 1 point added.")
    else:
        bot.answer_callback_query(call.id, "❌ You are not joined! You must join all Channels!")


@bot.message_handler(func=lambda message: message.text == "💲 Withdraw")
def withdraw(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("💰 Chorki Crack", "👥 Hoichoi Crack")
    keyboard.row("💲 Hoichoi 30 Days", "📂 Hoichoi Own mail")
    keyboard.row("🔙 Back")
    bot.send_message(message.chat.id, "Please choose one of the withdrawal options below:", reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == "🔙 Back")
def go_back_to_main_menu(message):
    bot.send_message(message.chat.id, "Returning to the main menu.", reply_markup=get_main_menu_keyboard())

@bot.message_handler(func=lambda message: message.text in options.keys())
def confirm_withdrawal(message):
    option = message.text
    cost = options[option]["cost"]
    message_text = f"Would you like to withdraw {option}? This will cost {cost} points."

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Confirm", callback_data=f"confirm_{option}"))
    keyboard.add(types.InlineKeyboardButton("Cancel", callback_data="cancel"))

    bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

# Update the existing confirm_withdrawal function to store message IDs and user IDs
@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_") or call.data == "cancel")
def handle_confirm_or_cancel(call):
    user_id = call.from_user.id
    action = call.data.split("_")[0]
    option = call.data.split("_")[1] if action == "confirm" else None

    if action == "confirm":
        cost = options[option]["cost"]

        if user_data.get(user_id, {}).get("balance", 0) >= cost:
            user_data[user_id]["balance"] -= cost
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Your withdrawal for {option} has been confirmed. {cost} points have been deducted.")
            order_id = generate_order_id()
            message_text = (
                f"✅ *New Order Received*\n\n"
                f"🔰 *Service:* {option}\n"
                f"👤 *User:* {call.from_user.full_name}\n"
                f"🆔 *User ID:* {user_id}\n"
                f"📈 *Quantity:* 1\n"
                f"💰 *Order Charge:* {cost} points\n"
                f"📛 *Order ID:* \\[{order_id}\\]\n"
                f"🔗 *Profile Link:* Hidden\n\n"
                f"🚀 *Get Premium Accounts Here ➡️* @OTTFREEBOT"
            )

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("Track Order Details", url="https://t.me/OTTFREEBOT"))
            # Send message to designated channel and group, and store the message ID and user ID
            order_msg = bot.send_message(options[option]["channel_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
            order_messages[order_msg.message_id] = user_id  # Store message ID with user ID
            
            if "group_id" in options[option]:
                group_msg = bot.send_message(options[option]["group_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
                order_messages[group_msg.message_id] = user_id  # Store message ID with user ID

        else:
            bot.answer_callback_query(call.id, "❌ You don't have enough points to make this withdrawal.")
    elif action == "cancel":
        bot.send_message(user_id, "Withdrawal request has been canceled.", reply_markup=get_main_menu_keyboard())
        
# Listener to detect replies in the group or channel
@bot.message_handler(func=lambda message: message.reply_to_message and message.chat.id in [GROUP_ID, CHORKI_CRACK_CHANNEL_ID, HOICHOI_CRACK_CHANNEL_ID])
def handle_admin_reply(message):
    original_message_id = message.reply_to_message.message_id
    user_id = order_messages.get(original_message_id)

    if user_id:
        # Notify the user that their order received a reply from an admin
        reply_text = f"🔔 *Admin replied to your order:*\n\n{message.text}"
        bot.send_message(user_id, reply_text, parse_mode="Markdown")
    else:
        logging.info(f"No user found for message_id {original_message_id}. Skipping.")        

@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):
    user_id = message.from_user.id
    points = user_data.get(user_id, {}).get("balance", 0)
    bot.send_message(message.chat.id, f"💰 Balance: {points} POINTS\n\n⚜️ Refer And Earn More !!!")
# Admin command to delete user balance
@bot.message_handler(commands=['delbalance'])
def delbalance_handler(message):
    if message.from_user.id not in ADMIN_USER_IDS:
        bot.send_message(message.chat.id, "⚠️ You don't have permission to use this command.")
        return

    msg = bot.send_message(message.chat.id, "Please enter the user ID to delete balance:")
    bot.register_next_step_handler(msg, process_delbalance)

# Process delete balance input
def process_delbalance(message):
    try:
        user_id = int(message.text.strip())
        if user_id in user_data:
            user_data[user_id]['balance'] = 0
            bot.send_message(message.chat.id, f"✅ Balance for user {user_id} has been deleted.")
            bot.send_message(user_id, "⚠️ Your balance has been reset to 0 by an admin.")
        else:
            bot.send_message(message.chat.id, "⚠️ User ID not found.")
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Invalid user ID format. Please try again.")
# Admin command to add balance
@bot.message_handler(commands=['balanceadd'])
def balance_add_handler(message):
    if message.from_user.id not in ADMIN_USER_IDS:
        bot.send_message(message.chat.id, "⚠️ You don't have permission to use this command.")
        return

    # Ask for the amount and user ID to add balance
    msg = bot.send_message(message.chat.id, "Please enter the amount of points and user ID in this format:\n\n`points user_id`", parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_balance_add)

# Process the balance add input from the admin
def process_balance_add(message):
    try:
        # Split input into points and user ID
        points, user_id = map(str.strip, message.text.split())
        points = int(points)
        user_id = int(user_id)

        # Ensure the user ID exists in user_data, initialize if missing
        if user_id not in user_data:
            user_data[user_id] = {'balance': 0, 'invited_users': 0, 'bonus_claimed': False}

        # Add points to the user's balance
        user_data[user_id]['balance'] += points
        bot.send_message(message.chat.id, f"✅ Successfully added {points} points to user {user_id}'s balance.")
        bot.send_message(user_id, f"🎉 You have received {points} points! Your new balance is {user_data[user_id]['balance']} points.")

    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Invalid input format. Please use the format `points user_id` (e.g., `10 123456789`).")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ An error occurred: {e}")

# Admin command to broadcast a message
@bot.message_handler(commands=['broadcast'])
def broadcast_handler(message):
    if message.from_user.id not in ADMIN_USER_IDS:
        bot.send_message(message.chat.id, "⚠️ You don't have permission to use this command.")
        return

    # Ask for the message to broadcast
    msg = bot.send_message(message.chat.id, "Please enter the message or send the file to broadcast.")
    bot.register_next_step_handler(msg, process_broadcast)

# Process the broadcast message or file
def process_broadcast(message):
    # Broadcast the received message to all users in total_users
    for user_id in total_users:
        try:
            # Check if the message contains text, photo, document, or video to broadcast
            if message.content_type == 'text':
                bot.send_message(user_id, message.text)
            elif message.content_type == 'photo':
                bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
            elif message.content_type == 'document':
                bot.send_document(user_id, message.document.file_id, caption=message.caption)
            elif message.content_type == 'video':
                bot.send_video(user_id, message.video.file_id, caption=message.caption)
        except Exception as e:
            print(f"Could not send message to {user_id}: {e}")

    # Notify the admin that the broadcast was successful
    bot.send_message(message.chat.id, "✅ Broadcast sent to all users.")
    # Admin command to check user balance
@bot.message_handler(commands=['check'])
def check_balance_handler(message):
    if message.from_user.id not in ADMIN_USER_IDS:
        bot.send_message(message.chat.id, "⚠️ You don't have permission to use this command.")
        return

    # Ask for the user ID to check balance
    msg = bot.send_message(message.chat.id, "Please enter the user ID to check balance:")
    bot.register_next_step_handler(msg, process_check_balance)

# Process the check balance input from the admin
def process_check_balance(message):
    try:
        user_id = int(message.text.strip())
        
        # Retrieve the balance for the specified user ID
        if user_id in user_data:
            balance = user_data[user_id].get('balance', 0)
            bot.send_message(message.chat.id, f"💰 User {user_id} has a balance of {balance} points.")
        else:
            bot.send_message(message.chat.id, f"⚠️ User ID {user_id} not found.")
    
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Invalid user ID format. Please enter a valid number.")
        
@bot.message_handler(func=lambda message: message.text == "👥 Referral")
def referral(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {'balance': 0, 'invited_users': 0, 'bonus_claimed': False}

    referral_link = f"https://t.me/OTTFREEBOT?start={user_id}"
    invited_users = user_data[user_id]['invited_users']
    bot.send_message(
        message.chat.id,
        f"👬 Your invite link: {referral_link}\n💸 Per refer: 1 point\n👉 Total invited users: {invited_users}"
    )

@bot.message_handler(func=lambda message: message.text == "📂 PROOFS")
def proofs(message):
    bot.send_message(message.chat.id, "Join: @Proofchannelch To Check Proofs 🥳")

@bot.message_handler(func=lambda message: message.text == "📞 Support")
def support(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Message Admin", url="https://t.me/RealonlineTech_bot"))
    bot.send_message(message.chat.id, "If you have a major problem, you can directly contact the owner - @RealonlineTech_bot", reply_markup=keyboard)

# Review submission initiation
@bot.message_handler(func=lambda message: message.text == "👥 Submit Review")
def submit_review(message):
    user_id = message.from_user.id
    bot.send_message(
        user_id,
        "Please send your screenshot and review of our service. Failure to do so may result in a password change for the account."
    )
    user_data[user_id]["awaiting_review"] = True  # Set the user as awaiting review

# Handle incoming review submissions
@bot.message_handler(content_types=['photo', 'text'])
def handle_review_submission(message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    is_waiting_for_review = user_data.get(user_id, {}).get("awaiting_review", False)

    if is_waiting_for_review:
        # If the user sent a photo with a caption
        if message.photo:
            caption = message.caption or "No text provided."
            photo = message.photo[-1].file_id  # Get the highest resolution image
            bot.send_photo(
                REVIEW_CHANNEL_ID,
                photo=photo,
                caption=f"👤 User: {user_name} (ID: {user_id})\n\n📄 Review: {caption}",
                parse_mode="Markdown"
            )
        # If the user sent text without a photo
        elif message.text:
            bot.send_message(
                REVIEW_CHANNEL_ID,
                text=f"👤 User: {user_name} (ID: {user_id})\n\n📄 Review: {message.text}",
                parse_mode="Markdown"
            )

        # Reset user's review submission state
        user_data[user_id]["awaiting_review"] = False
        bot.send_message(user_id, "Thank you for your review!")

# Polling for updates with exception handling
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
