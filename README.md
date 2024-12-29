# 📲 NF-City-Bot-Clone 🤖

Welcome to **NF-City-Bot-Clone**! This Telegram bot offers premium accounts through a referral and point-based system. Users can earn points by inviting others and redeem those points for access to premium accounts like *Chorki* and *Hoichoi*. This bot comes with a fully interactive interface and a host of features for both users and admins.

---

### 🌐 Repository Link
[GitHub Repository](https://github.com/abirxdhack/NF-City-Bot-Clone)

### 🧪 Demo Bot
You can try out a live demo of the bot here: [Demo Bot](https://t.me/OTTFREEBOT)

---

## ⚙️ Key Features

- **User Registration**: Welcomes new users and registers them with an optional referral system.
- **Referral System**: Users earn points by referring others to the bot.
- **Points & Balance Management**: Users can view their balance and redeem points for services.
- **Premium Account Redemption**: Users can redeem points for premium accounts like *Chorki* and *Hoichoi*.
- **Order Confirmation & Tracking**: Each order is assigned a unique ID, and users receive notifications for order updates.
- **Admin Control Panel**: Balance management, broadcasts, and user activity tracking for admins.
- **Channel Membership Verification**: Ensures users join required channels to access services.
- **User Review Submission**: Users can submit reviews to share feedback and screenshots.

---

## 🔐 Requirements

- Python 3.6+
- Libraries:
  - `pyTelegramBotAPI`
  - `logging`
  - `random`
  - `string`
  - `time`

## 🛠️ Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abirxdhackz/NF-City-Bot-Clone.git
   cd NF-City-Bot-Clone
   ```

2. **Install Dependencies**:
   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Configure Bot Token**:
   - Replace the `BOT_TOKEN` variable in the script with your Telegram bot token obtained from [BotFather](https://core.telegram.org/bots#botfather).
   ```python
   BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
   ```

4. **Run the Bot**:
   ```bash
   python bot_script.py
   ```

---

## 📋 Bot Commands & Options

### 📲 User Commands

- **`/start`** - Register with the bot, join channels, and receive your referral link.
- **Balance 💰** - Check your points balance.
- **Referral 👥** - Generate and share your referral link to earn points.
- **Withdraw 💲** - Redeem points for premium accounts.
- **PROOFS 📂** - Access proof links for past successful transactions.
- **Support 📞** - Contact bot support for help or issues.
- **Submit Review 📝** - Submit feedback or reviews with screenshots.

### 🔑 Admin Commands

- **`/balanceadd`** - Add points to a specific user’s balance.
  - Example: `/balanceadd 10 user_id`
- **`/delbalance`** - Reset a user's balance to zero.
- **`/broadcast`** - Send messages or files to all users.
- **`/check`** - Check a specific user’s balance.

---

## 🏆 Features in Detail

### 1. **Referral Points System** 🔗
   - Users earn points by sharing their referral link. Every new user who joins through the link adds to the referrer's points, which they can use to redeem premium accounts.

### 2. **Channel Join Verification** ✅
   - On starting the bot, users are prompted to join specific channels. Access to other bot features requires joining these channels, verified using Telegram’s `get_chat_member` function.

### 3. **Balance & Redeem System** 💸
   - Users can check their balance and redeem points for premium accounts. Available services include:
     - **Chorki Crack** - 0 Points
     - **Hoichoi Crack** - 3 Points
     - **Hoichoi 30 Days** - 15 Points
     - **Hoichoi Own Mail** - 30 Points

### 4. **Order Confirmation & Tracking** 📦
   - Each order is given a unique ID, which is shared with the user. Admins can manage orders and send notifications for updates or issues.

### 5. **Admin Control Panel** 🔧
   - **Balance Management**: Admins can manage user balances with `/balanceadd` and `/delbalance`.
   - **Broadcasts**: Use `/broadcast` to send messages or files to all users.
   - **User Balance Check**: Admins can view individual user balances with `/check`.

---

## 🔄 How It Works

1. **User Registration & Referral**: On `/start`, users can join specified channels, access their referral link, and start earning points through successful referrals.
2. **Redeeming Points**: When users have enough points, they can choose a service like *Chorki* or *Hoichoi* and redeem their points. The bot will verify their balance and deduct the points upon confirmation.
3. **Account Delivery**: Upon redemption, account details are sent directly to the user.
4. **User Review Submission**: Users can submit feedback or screenshots to showcase their experience with the bot’s services.

---

## 🌐 Code Summary

The bot is organized to handle both user-facing and admin-facing functionalities. Here's a breakdown of the main components:

- **User Data Management**: Tracks user balances, referrals, and interactions with the bot.
- **Order Tracking & Management**: Logs order IDs and manages the redemption process.
- **Admin Functions**: Admins can add points, reset balances, broadcast messages, and monitor user activity.
- **Channel Verification**: Ensures that users are members of required channels before allowing premium redemptions.

---

## 🛡️ License

This project is licensed under the MIT License and is intended for educational purposes only. Misuse or improper use of the bot may result in penalties or bans, so please adhere to Telegram’s bot policies.

---

## 📞 Support & Contact

For any issues, feedback, or support requests, please contact the bot owner via [Telegram](https://t.me/RealonlineTech_bot).

---

> 🚨 **Disclaimer**: This bot is designed for educational use to demonstrate Telegram bot functionality. Misuse may lead to penalties or bans in accordance with Telegram's policy.

---

Happy using the **NF-City-Bot-Clone**! 🎉
```

Now, the **Demo Bot** link is included right at the beginning, allowing users to interact with the bot directly through [@OTTFREEBOT](https://t.me/OTTFREEBOT).
