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
4. Copy the **Bot Token** — you'll need it in the next step
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
**Bot:** "🌍 Timezone set to Asia/Kolkata"

**You:** `/remind 10m Take a break`
**Bot:** "✅ Reminder set for 10m from now (Asia/Kolkata)"

**You:** `/reminders`
**Bot:** Lists all your active reminders with their scheduled times.

---

## 📝 Notes

* Works best in **private chats** or **servers** where the bot has permission to read and send messages.
* Keep your **Discord token secret**. Do not share it publicly.
* Currently, reminders are stored in memory — restarting the bot will **clear all active reminders**.

---

## 🔄 Pull Request

### 🎉 Discord Reminder Bot - Initial Release

#### 📋 Summary

This PR introduces a fully functional Discord reminder bot with timezone support, allowing users to schedule and manage reminders directly within Discord. The bot provides an intuitive command-based interface for personal productivity and task management.

#### ✨ What's New

**Core Features:**
- ⏱️ **Reminder System**: Set reminders using natural time expressions (minutes, hours, days)
- 🌍 **Timezone Support**: Per-user timezone configuration for accurate local time reminders
- 📜 **Reminder Management**: List, view, and cancel active reminders
- 🔔 **Automated Notifications**: Background task system for reliable reminder delivery
- 🛠️ **Slash Commands**: Modern Discord slash command integration

**Technical Implementation:**
- Built with `discord.py` 2.6.0 using the latest Discord API features
- Timezone handling via `pytz` for accurate global time conversions
- Environment variable configuration for secure token management
- In-memory reminder storage with user-specific reminder tracking

#### 🏗️ Architecture

**File Structure:**
```
DiscordReminderBot/
├── bot.py              # Main bot logic and command handlers
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Git ignore rules
└── README.md          # Documentation
```

**Key Components:**
1. **Command System**: Slash commands for all user interactions
2. **Timezone Manager**: Per-user timezone storage and validation
3. **Reminder Scheduler**: Background task loop for reminder delivery
4. **User Data Store**: In-memory dictionary for reminders and user settings

#### 🎯 Commands Implemented

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/settimezone` | `<timezone>` | Configure user timezone (e.g., Asia/Kolkata) |
| `/remind` | `<time> <message>` | Create reminder (supports 10m, 2h, 1d formats) |
| `/reminders` | - | Display all active reminders |
| `/cancel` | `<reminder_id>` | Remove a specific reminder |
| `/help` | - | Show available commands and usage |

#### 🧪 Testing Checklist

- [x] Bot successfully connects to Discord
- [x] Slash commands register and respond correctly
- [x] Timezone setting validates input
- [x] Reminders trigger at correct times
- [x] Multiple reminders per user work independently
- [x] Cancel command removes reminders properly
- [x] Help command displays accurate information

#### ⚠️ Known Limitations

1. **Persistence**: Reminders are stored in memory - restarting the bot clears all data
2. **Scalability**: Current architecture suitable for small to medium servers
3. **Time Formats**: Only supports `Xm`, `Xh`, `Xd` format (not natural language)

#### 🚀 Future Enhancements

- [ ] Database integration for persistent reminder storage
- [ ] Recurring reminders (daily, weekly, monthly)
- [ ] Natural language time parsing ("tomorrow at 3pm")
- [ ] Reminder editing capabilities
- [ ] DM vs channel reminder options
- [ ] Reminder history and statistics

#### 🔒 Security Considerations

- Bot token stored in environment variables (not in code)
- `.env` file excluded from version control
- `.env.example` provided as template
- No sensitive data logged or exposed

#### 💡 Design Decisions

1. **In-Memory Storage**: Chosen for simplicity in initial release; database can be added later
2. **Slash Commands**: Modern Discord best practice over prefix commands
3. **Per-User Timezones**: Provides personalized experience for global users
4. **Simple Time Format**: Easy to parse and validate, reduces edge cases

#### 📝 Type of Change

- [x] New feature
- [x] Documentation
- [ ] Bug fix
- [ ] Breaking change

#### ✅ How Has This Been Tested?

- Manual testing across multiple Discord servers
- Various timezone configurations tested
- Edge cases validated (invalid timezones, malformed time inputs)
- Multiple concurrent reminders verified

---

## 💖 Credits

Developed with ❤️ by **Rudra Narayan Samantaray**

> "Stay organized, stay productive, code with purpose."

---

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For questions or feedback, reach out via GitHub issues or Discord.

---

**⭐ If you find this bot helpful, please consider giving it a star on GitHub!**