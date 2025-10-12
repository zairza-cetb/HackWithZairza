# ⏰ Discord Reminder Bot by Rudra

A simple and useful **Discord bot** built with Python that lets users **set reminders with timezone support**.
Perfect for keeping track of tasks, deadlines, and personal reminders directly in Discord!

---

## ✨ Features

* ⏱️ **Set Reminders:** Schedule reminders in minutes, hours, or days.
* 🌍 **Timezone Support:** Set your timezone so reminders are sent at your local time.
* 📜 **List Active Reminders:** View all your upcoming reminders.
* ❌ **Cancel Reminders:** Cancel any reminder you no longer need.
* 🔔 **Automated Alerts:** Bot sends reminders automatically in the correct channel.
* 🛠 **Easy Commands:** Simple commands for quick setup and usage.
* 🔒 **Secure Setup:** Environment variables keep your bot token safe.

---

## ⚙️ Setup & Installation

Follow these steps to get your **Discord Reminder Bot** running locally.

### 1️⃣ Prerequisites

* Python 3.9 or higher
* A Discord account
* A Discord server where you have permission to add bots

---

### 2️⃣ Bot Registration

1. Open Discord and go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** → give it a name → **Create**
3. Navigate to **Bot** → **Add Bot** → **Yes, do it!**
4. Copy the **Bot Token** — you’ll need it in the next step
5. Invite the bot to your server using the OAuth2 URL Generator with **bot** and **applications.commands** permissions

---

### 3️⃣ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YourUsername/DiscordReminderBot.git
cd DiscordReminderBot
```

2. **Create and activate a virtual environment:**

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

Your `requirements.txt`:

```
discord.py==2.6.0
python-dotenv==1.0.1
pytz==2025.7
tzdata==2025.7
```

4. **Configure Environment Variables:**

* Copy `.env.example` to `.env`
* Add your Discord token:

```env
DISCORD_TOKEN="your_discord_token_here"
```

5. **Run the bot:**

```bash
python bot.py
```

Terminal should show:

```
✅ YourBotName is online!
```

---

## 📱 Usage

Interact with the bot using these commands:

| Command                | Description                           |
| ---------------------- | ------------------------------------- |
| `/settimezone <zone>`  | Set your timezone (e.g. Asia/Kolkata) |
| `/remind <time> <msg>` | Set a reminder (10m, 2h, 1d)          |
| `/reminders`           | List all your active reminders        |
| `/cancel <ID>`         | Cancel a reminder by its ID           |
| `/help`                | Shows a list of available commands    |

**Example:**

**You:** `/settimezone Asia/Kolkata`
**Bot:** “🌍 Timezone set to Asia/Kolkata”

**You:** `/remind 10m Take a break`
**Bot:** “✅ Reminder set for 10m from now (Asia/Kolkata)”

**You:** `/reminders`
**Bot:** Lists all your active reminders with their scheduled times.

---

## 📝 Notes

* Works best in **private chats** or **servers** where the bot has permission to read and send messages.
* Keep your **Discord token secret**. Do not share it publicly.
* Currently, reminders are stored in memory — restarting the bot will **clear all active reminders**.

---

## 💖 Credits

Developed with ❤️ by **Rudra Narayan Samantaray**

> “Stay organized, stay productive, code with purpose.”
