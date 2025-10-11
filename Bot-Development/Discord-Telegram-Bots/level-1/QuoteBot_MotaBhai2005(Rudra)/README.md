# 💬 Telegram Quote Bot by Rudra  

A simple and fun **Telegram bot** built with Python that shares **random quotes, fun facts, jokes, and inspirational messages**.  
Perfect for adding a spark of motivation or humor to your chats!  

---

## ✨ Features

- 📝 **Random Quotes:** Receive motivational or thought-provoking quotes.  
- 📚 **Fun Facts:** Learn something interesting every day.  
- 😂 **Jokes:** Lighten the mood with a random joke.  
- 🌅 **Inspirational Messages:** Get uplifted with daily inspiration.  
- 🛠 **Command Handling:** Easy-to-use commands for quick interaction.  
- 🔒 **Secure Setup:** Environment variables keep your token safe.  

---

## ⚙️ Setup & Installation

Follow these steps to get your **Quote Bot** running locally.  

### 1️⃣ Prerequisites

- Python 3.8 or higher  
- A Telegram account  

---

### 2️⃣ Bot Registration

1. Open Telegram and search for **@BotFather**  
2. Send the command: `/newbot`  
3. Follow the prompts: give your bot a **name** and **unique username** (must end with `bot`)  
4. Copy the **API Token** provided — you’ll need it in the next step  

---

### 3️⃣ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YourUsername/QuoteBot_YourUsername.git
cd QuoteBot_YourUsername
````

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
python-telegram-bot==20.3
python-dotenv==1.0.0
```

4. **Configure Environment Variables:**

* Copy `.env.example` to `.env`
* Add your token:

```env
TELEGRAM_TOKEN="your_telegram_token_here"
```

5. **Run the bot:**

```bash
python bot.py
```

Terminal should show:

```
Rudra's Quote Bot is Running.....
```

---

## 📱 Usage

Interact with the bot using these commands:

| Command    | Description                        |
| ---------- | ---------------------------------- |
| `/start`   | Displays a welcome message         |
| `/quote`   | Sends a random quote               |
| `/fact`    | Shares an interesting fact         |
| `/joke`    | Tells a funny joke                 |
| `/inspire` | Sends an inspirational message     |
| `/help`    | Shows a list of available commands |

**Example:**

**You:** `/quote`
**Bot:** “The only way to do great work is to love what you do. — Steve Jobs”

**You:** `/joke`
**Bot:** “I have a lot of jokes about unemployed people, but none of them work.”

---

## 📝 Notes

* Works best in **private chats** or **groups** where it has access to messages.
* Keep your **Telegram token secret**. Do not share it publicly.

---

## 💖 Credits

Developed with ❤️ by **Rudra Narayan Samantaray**

> “Code with purpose, share with kindness.”

---