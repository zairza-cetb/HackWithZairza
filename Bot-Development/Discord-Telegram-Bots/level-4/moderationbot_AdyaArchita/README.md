## ModerationBot by AdyaArchita
I have built a high-performance, feature-rich moderation bot for Telegram, built using the `python-telegram-bot` library. It is designed for reliability and scalability, providing group administrators with a powerful toolkit to maintain a safe, clean, and well-managed community.
From automated content filtering to a persistent warning system and a complete audit trail, ModerationBot serves as a complete solution for serious community management.

## Key Features
ModerationBot is equipped with a full suite of moderation and administrative tools.

## Core Moderation
1. *Warn System*: Issue and track user warnings with reasons stored in a persistent database.
2. *Kick & Ban*: Temporarily or permanently remove users from the group.
3. *Mute*: Temporarily or permanently restrict users from sending messages.
4. *Message Purge*: Clean up message history by deleting messages in bulk.
5. *Auto-Moderation*: Automatically delete messages containing words from a configurable blacklist.
6. *Action Logging*: Log all administrative actions to a private channel for a complete and transparent audit trail.

## Advanced System Features
1. *Permission Control*: All moderation commands are strictly limited to group administrators using a custom decorator.
2. *Temporary Sanctions*: Mute and ban commands support time durations (e.g., `30m`, `6h`, `7d`).
3. *Rate Limiting*: Protects against command spam and unintended API abuse.
4. *Automated Backups*: Periodically creates a secure backup of the warnings database to prevent data loss.
5. *Health Monitoring*: A `/health` command is included to instantly verify that the bot is online and responsive.
6. *Graceful Shutdown*: Ensures a clean shutdown process, saving state and closing connections properly.

## Installation Guide
Follow these steps to get your own instance of ModerationBot running.

# Prerequisites
1. Python 3.10 or newer
2. Git version control
3. A Telegram Bot Token obtained from [@BotFather]

1. *Clone the Repository*
First, clone the project files to your local machine or server.
```bash
git clone [https://github.com/YourGitHubUsername/ModerationBot_YourGitHubUsername.git](https://github.com/YourGitHubUsername/ModerationBot_YourGitHubUsername.git)
cd ModerationBot_YourGitHubUsername
```

2. *Install Dependencies*
It is highly recommended to use a Python virtual environment to manage dependencies and avoid conflicts.

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows: venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. *Configure the Bot*
ModerationBot is configured using two primary files:

`.env`: Stores your secret bot token. Create this file by copying the template:
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and paste your `TELEGRAM_BOT_TOKEN`.

`config.json`: Controls the bot's operational parameters. Create this file by copying the template:
    ```bash
    cp config.json.example config.json
    ```
    Open `config.json` and customize the values. See the Configuration Details section below for an explanation of each setting.

4. Run the Bot
Once configured, you can start the bot with a single command.
```bash
python bot.py
```
Your bot is now online. To stop it, press `Ctrl+C`.

## Configuration Details
All settings are managed in the `config.json` file.

       Key           Type                                      Description 
`mod_log_chat_id`   Integer    Unique ID of private channel/group where the bot will send moderation logs. Set to `0` to disable.
`banned_words`       Array     A list of case-insensitive strings. Message with one of these words will be automatically deleted. 
`super_admin_ids`    Array     A list of user IDs for bot super administrators. (This can be used for future owner-only commands).
`database_path`      String    The file path for the SQLite database. Defaults to `moderation.db`. 
`backup_directory`   String    The folder where automated database backups will be stored. Defaults to `./backups`. 

## Command Reference
Note: All moderation commands must be executed by an administrator as a *reply* to a target user's message.

 Command        Syntax                         Description 
`/warn`     `/warn [reason]`             Issues a formal warning to the user, logged to the database.
`/warnings` `/warnings`                  Retrieves and displays the full warning history for the user.
`/kick`    `/kick [reason]`              Removes the user from the group. They are permitted to rejoin.
`/mute`    `/mute [duration] [reason]`   Restricts the user from sending messages. Duration is optional (e.g., `1h`, `2d`). If omitted, the mute is permanent.
`/ban`      `/ban [duration] [reason]`  Bans the user from the group. Duration is optional. If omitted, the ban is permanent.
`/unmute`   `/unmute`                   Lifts all message-sending restrictions from a muted user.
`/purge`    `/purge`                    Deletes the entire range of messages from the replied-to message up to the command itself. Useful for cleaning up spam. 
`clean`     `/clean [number]`           Deletes that number of messages mentioned 
`/health`   `/health`                   A simple check to confirm the bot is online and responsive. 

## Production Deployment
For 24/7 uptime and automatic restarts on failure, the bot must be deployed as a service on a server. A detailed guide for deploying with `systemd` on Linux is available in the deployment documentation.

See the full guide: [DEPLOYMENT.md](DEPLOYMENT.md)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.