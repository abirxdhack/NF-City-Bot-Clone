import telebot
from telebot import types
import random
import string
import time
import logging

# Define your bot token here
BOT_TOKEN = 'Your Bot Token'
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

# Options for withdrawal items and points cost
options = {
    "💰 Chorki Crack": {"cost": 1, "channel_id": CHORKI_CRACK_CHANNEL_ID},
    "👥 Hoichoi Crack": {"cost": 5, "channel_id": HOICHOI_CRACK_CHANNEL_ID},
    "💲 Chorki On Mail": {"cost": 1, "channel_id": CHORKI_ON_MAIL_CHANNEL_ID, "group_id": GROUP_ID},
    "📂 Hoichoi On mail": {"cost": 30, "channel_id": HOICHOI_ON_MAIL_CHANNEL_ID, "group_id": GROUP_ID},
}

# Account storage
accounts = {
    "💰 Chorki Crack": [
        {"username": "AbdullahAlMamun", "password": "500440Ma"},
        {"username": "20/2013/0076/01", "password": "Kulchandi@123"},
        {"username": "1341025", "password": "01537298084"},
        {"username": "01531311283", "password": "sanjid1423//"},
        {"username": "Abeg Rahman", "password": "Abeg1621"},
        {"username": "7hnazmul@gmail.com", "password": "mnop890abc"},
        {"username": "A.M.Jubayer", "password": "wp06ctys"},
        {"username": "01973462394", "password": "MIF2004"},
        {"username": "7076723486", "password": "973463n"},
        {"username": "3684069200", "password": "77387"},
        {"username": "424khantanvir", "password": "chorki1997"},
        {"username": "8996nightmare@gmail.com", "password": "nightmare8996"},
        {"username": "9800460", "password": "Mobc1!36"},
        {"username": "Abir", "password": "abir&ruhu"},
        {"username": "01674894440shiblee@gmail.com", "password": "vEJbA9fwOXLK"},
        {"username": "424khantanvir@gmail.com", "password": "chorki1997"},
        {"username": "97168", "password": "807499"},
        {"username": "01751948921", "password": "2591"},
        {"username": "Abdur1986A", "password": "Abdur1986@"},
        {"username": "4575", "password": "01753211086"},
        {"username": "121522000", "password": "121522000"},
        {"username": "01622180764", "password": "Doodly007@"},
        {"username": "ABID RAHMAN", "password": "*1216Mcsk"},
        {"username": "01674894440shiblee@gmail.com", "password": "ash02010"},
        {"username": "400212217", "password": "hbsdfhbfhsdbfnksdbcfirbwuei4r487y38r43"},
        {"username": "01314011976", "password": "kothakotha990@gmail.com"},
        {"username": "01730801125", "password": "nayon359"}
    ],
    "👥 Hoichoi Crack": [
        {"username": "datta.siddhartha@rediffmail.com", "password": "chem@1980"},
        {"username": "datta.siddhartha@rediffmail.com", "password": "chem@1980"},
        {"username": "mitra_arijit04@yahoo.com", "password": "holymother_1971"},
        {"username": "soumik.bsp@gmail.com", "password": "bhu18042015"},
        {"username": "sunscriptysubscripty@gmail.com", "password": "Yoursubhub"},
        {"username": "bjeerupam@gmail.com", "password": "Shub00@76"}
    ]
}

# Set up logging
logging.basicConfig(level=logging.INFO)

# Updated function for Chorki Crack and Hoichoi Crack with account assignment
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
            # Send message to designated channel
            order_msg = bot.send_message(options[option]["channel_id"], message_text, parse_mode="MarkdownV2")
            order_messages[order_msg.message_id] = user_id  # Store message ID with user ID
            
            if "group_id" in options[option]:
                group_msg = bot.send_message(options[option]["group_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
                order_messages[group_msg.message_id] = user_id  # Store message ID with user ID
            # Provide an account to the user (only for Chorki and Hoichoi Crack)
            if option == "💰 Chorki Crack":
                account = random.choice(accounts["💰 Chorki Crack"])
                account_message = f"🔹 **Chorki Account**:\nUsername: {account['username']}\nPassword: {account['password']}"
                bot.send_message(user_id, account_message)
            elif option == "👥 Hoichoi Crack":
                account = random.choice(accounts["👥 Hoichoi Crack"])
                account_message = f"🔹 **Hoichoi Account**:\nUsername: {account['username']}\nPassword: {account['password']}"
                bot.send_message(user_id, account_message)

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

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    referrer_id = int(message.text.split()[1]) if len(message.text.split()) > 1 else None

    if user_id not in total_users:
        total_users.add(user_id)
        user_data[user_id] = {'balance': 0, 'invited_users': 0, 'bonus_claimed': False}

        if referrer_id and referrer_id != user_id and referrer_id in user_data:
            user_data[referrer_id]['invited_users'] += 1
            user_data[referrer_id]['balance'] += 1
            bot.send_message(referrer_id, "Successful referral! You earned 1 point.")

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

@bot.callback_query_handler(func=lambda call: call.data == "joined")
def joined_button(call):
    user_id = call.from_user.id
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
    else:
        bot.answer_callback_query(call.id, "❌ You are not joined! You must join all Channels!")

@bot.message_handler(func=lambda message: message.text == "💲 Withdraw")
def withdraw(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("💰 Chorki Crack", "👥 Hoichoi Crack")
    keyboard.row("💲 Chorki On Mail", "📂 Hoichoi On mail")
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

# Updated function for Chorki Crack and Hoichoi Crack with account assignment
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
            # Send message to designated channel
            order_msg = bot.send_message(options[option]["channel_id"], message_text, parse_mode="MarkdownV2")
            order_messages[order_msg.message_id] = user_id  # Store message ID with user ID
            
            if "group_id" in options[option]:
                group_msg = bot.send_message(options[option]["group_id"], message_text, reply_markup=keyboard, parse_mode="MarkdownV2")
                order_messages[group_msg.message_id] = user_id  # Store message ID with user ID
            # Provide an account to the user (only for Chorki and Hoichoi Crack)
            if option == "💰 Chorki Crack":
                account = random.choice(accounts["💰 Chorki Crack"])
                account_message = f"🔹 **Chorki Account**:\nUsername: {account['username']}\nPassword: {account['password']}"
                bot.send_message(user_id, account_message)
            elif option == "👥 Hoichoi Crack":
                account = random.choice(accounts["👥 Hoichoi Crack"])
                account_message = f"🔹 **Hoichoi Account**:\nUsername: {account['username']}\nPassword: {account['password']}"
                bot.send_message(user_id, account_message)

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
