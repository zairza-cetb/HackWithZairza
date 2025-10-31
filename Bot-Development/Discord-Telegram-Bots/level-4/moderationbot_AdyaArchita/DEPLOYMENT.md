# Production Deployment Guide (systemd)

To run your ModerationBot 24/7 and ensure it automatically restarts on a crash or server reboot, you should deploy it as a `systemd` service on a Linux server.

This guide assumes you are using a modern Linux distribution like Ubuntu or Debian.

## Prerequisites

* A Linux server (e.g., a VPS) that you have `sudo` access to.
* `git`, `python3`, and `python3-venv` installed on the server.
    ```bash
    sudo apt update
    sudo apt install git python3 python3-venv -y
    ```
* You have already cloned the bot repository and set up your configuration files as described in the `README.md`.

## Deployment Steps

 **Step 1: Prepare the Bot Files**

1.  *Clone your repository* to a permanent location on your server. A common location is `/opt` or your home directory (e.g., `/home/your-user/ModerationBot`).

    ```bash
    git clone [https://github.com/YourGitHubUsername/ModerationBot_YourGitHubUsername.git](https://github.com/YourGitHubUsername/ModerationBot_YourGitHubUsername.git) /opt/ModerationBot
    cd /opt/ModerationBot
    ```

2.  *Create and activate the virtual environment:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  *Install dependencies:*
    ```bash
    pip install -r requirements.txt
    ```

4.  *Create and edit your configuration files:*
    ```bash
    cp .env.example .env
    cp config.json.example config.json
    ```
    * Edit `.env` and add your `TELEGRAM_BOT_TOKEN`.
    * Edit `config.json` to set your `mod_log_chat_id`, `banned_words`, etc.

5.  *Deactivate the virtual environment* for now.
    ```bash
    deactivate
    ```

### Step 2: Create the `systemd` Service File

1.  Create a new service file using a text editor like `nano`:
    ```bash
    sudo nano /etc/systemd/system/moderationbot.service
    ```

2.  Paste the following content into the file. You must change the `User`, `Group`, `WorkingDirectory`, and `ExecStart` paths to match your specific setup.

    ```ini
    [Unit]
    Description=Telegram ModerationBot
    After=network.target

    [Service]
    # === CHANGE THESE VALUES ===
    # Run the bot as your own user (e.g., 'ubuntu' or 'pi')
    User=your-username
    # Use your user's primary group (often the same as the username)
    Group=your-username
    # The full path to the bot's project directory
    WorkingDirectory=/opt/ModerationBot
    # The full path to the python executable in your venv
    ExecStart=/opt/ModerationBot/venv/bin/python /opt/ModerationBot/bot.py

    # Standard service settings
    Type=simple
    Restart=always
    RestartSec=5
    StandardOutput=journal
    StandardError=journal
    SyslogIdentifier=moderationbot

    [Install]
    WantedBy=multi-user.target
    ```

    **How to find your values:**
    * `User`/`Group`: Type `whoami` in your terminal.
    * `WorkingDirectory`: Run `pwd` from inside your bot's directory (e.g., `/opt/ModerationBot`).
    * `ExecStart`: This is simply `WorkingDirectory` + `/venv/bin/python` + ` ` + `WorkingDirectory` + `/bot.py`.

3.  Save the file and exit `nano` (Press `Ctrl+X`, then `Y`, then `Enter`).

### Step 3: Enable and Start the Service

1.  Reload the `systemd` daemon to make it aware of your new service file:
    ```bash
    sudo systemctl daemon-reload
    ```

2.  Enable the service to make it start automatically on server boot:
    ```bash
    sudo systemctl enable moderationbot.service
    ```

3.  Start the service immediately:
    ```bash
    sudo systemctl start moderationbot.service
    ```

## Managing Your Bot

Your bot is now running as a background service. Here are the commands to manage it.

### Check Bot Status

To see if the bot is running, check its status:
```bash
sudo systemctl status moderationbot.service
````

  * Look for `active (running)` in green.
  * You will also see the most recent log entries.
  * Press `q` to exit the status view.

### View Logs

To see the live logs from your bot (e.g., to check for errors):

```bash
sudo journalctl -u moderationbot.service -f
```

  * The `-f` flag "follows" the log, showing new lines as they appear.
  * Press `Ctrl+C` to stop viewing the logs.

### Restart the Bot

If you make changes to your `config.json` or just need to restart the bot:

```bash
sudo systemctl restart moderationbot.service
```

### Stop the Bot

To stop the bot from running:

```bash
sudo systemctl stop moderationbot.service
```

## Updating Your Bot
When you have new code to deploy from your Git repository:

1.  Navigate to your bot directory:
    ```bash
    cd /opt/ModerationBot
    ```
2.  Pull the latest changes:
    ```bash
    git pull
    ```
3.  Re-install dependencies just in case `requirements.txt` changed:
    ```bash
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    ```
4.  Restart the service to apply the changes:
    ```bash
    sudo systemctl restart moderationbot.service
    ```