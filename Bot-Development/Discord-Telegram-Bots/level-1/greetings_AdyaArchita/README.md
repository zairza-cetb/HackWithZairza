# Telegram Greeting Bot by Adya 

I have built a simple, friendly Telegram bot with Python that greets users, handles basic commands, and manages group member events. This project acts as my first in the domain of Bot development. Hope it is functional as intended . 

##  Features

-   *Welcome Messages:* Greets new members when they join a group.
-   *Goodbye Messages:* Says goodbye to members who leave.
-   *Conversational Replies:* Responds to greetings (e.g., "hi / hello @botusername").
-   *Command Handling:* A full suite of basic commands.
-   *Admin Ready:* Works best with admin privileges to access all messages.

##  Setup and Installation

Follow these steps to get your own instance of the Greeting Bot running.

   1. Prerequisites
-   Python 3.8 or higher
-   A Telegram account

   2. Bot Registration
1.  Open Telegram and search for the **@BotFather**.
2.  Send the `/newbot` command and follow the on-screen instructions.
3.  Give your bot a name and a unique username.
4.  BotFather will provide you with a unique **API Token**. Copy this token and keep it safe.

    3. Installation Steps
       
1.  *Clone the repository:*
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
2.  Create and activate a virtual environment:
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configure Environment Variables:
    -   Find the `.env.example` file in the project.
    -   Create a copy of it and name it `.env`.
    -   Open the new `.env` file and paste your Telegram API Token.
    ```env
    TELEGRAM_TOKEN="your_telegram_token_here"
    ```
5.  Run the bot:
    ```bash
    python bot.py
    ```
    Your bot should now be running and connected to the Telegram API.

   4. Bot Permissions (Important!)
For the bot to read all messages and function as intended in a group :
1.  *Make it an Admin:* In your group settings, promote the bot to an administrator.
2.  *Disable Group Privacy:* In your chat with **@BotFather**, use the `/mybots` command, select your bot, go to `Bot Settings` -> `Group Privacy`, and click `Turn off`.

##  Usage

Interact with the bot using the following commands.

 Command                  Description                                        
 
 `/start`                Displays the initial welcome message.
 `/hello`                Get a friendly greeting from the bot.
 `/info`                 Displays detailed information about the bot.
 `/time`                 Shows the bot's current server time.
 `/echo <text>`          The bot will repeat your message back to you.      
 `/help`                 Shows the list of available commands.      

The bot will also automatically welcome new users, say goodbye, and respond to conversational greetings that mention it (e.g., `hi @greetingsadya_bot` or `hello @greetingsadya_bot` ).
