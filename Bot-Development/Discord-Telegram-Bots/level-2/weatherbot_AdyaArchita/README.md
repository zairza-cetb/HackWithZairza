# Telegram Weather Bot by Adya

Ever wanted a personal weather assistant right in your Telegram chat? Now you have one.
I have built a versatile bot that gives you up-to-date weather information, forecasts, and a few neat tricks, all powered by Python and the OpenWeatherMap API.

## Features

 1. *Real-Time Weather:* Instantly pull up the current conditions for any city around the globe.
 2. *Look Ahead:* Get a simple 5-day forecast to help you plan your week.
 3. *Set & Forget:* Save your hometown as a default location, so you don't have to type it in every time.
 4. *Quick Conversions:* A handy utility to switch temperatures between Celsius and Fahrenheit on the fly.
 5. *Fast & Efficient:* Built with modern asynchronous code (`asyncio` and `aiohttp`) to make it speedy and responsive.
 6. *Clean & Clear:* Bot responses are nicely formatted with emojis, making them easy to read at a glance.

## Getting Started

# 1. API Key Provisioning
To enable full functionality, the application requires two distinct API keys. Follow the procedures below to obtain them.

i.  *Telegram Bot Token*
This token is required to authorize the script to interact with the Telegram Bot API on your behalf.

1.  Initiate a chat with the official `@BotFather` bot on Telegram.
2.  Issue the `/newbot` command to begin the bot creation process.
3.  Follow the sequential prompts to define a name and a unique username for your bot.
4.  Upon completion, BotFather will provide a unique API token. Securely store this token for the environment setup.

ii. *OpenWeatherMap API Key*
This key provides access to the OpenWeatherMap data endpoints for fetching current weather and forecast information.

1.  Navigate to the [OpenWeatherMap website](https://openweathermap.org/) and register for a new account.
2.  Once logged in, proceed to the "API keys" section within your user dashboard.
3.  A default API key will be automatically generated for your account. Copy this key for later use.
4.  Please note that a newly generated API key may require a brief activation period before it can be used.

# 2. Installation and Configuration
Follow these steps to configure the project environment and prepare the bot for execution.

i.  *Clone the Repository:* Begin by cloning the source code to your local machine.
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

ii.  *Environment Variable Configuration:* Create a file named `.env` in the root directory of the project. This file is used for the secure management of API credentials. Populate the `.env` file with the previously acquired API keys using the following format:
    ```
    TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    WEATHER_API_KEY=YOUR_OPENWEATHERMAP_API_KEY
    ```

iii.  *Dependency Installation:* Install the required Python packages by executing the following command from the project's root directory:
    ```bash
    pip install -r requirements.txt
    ```

# 3. Running the Bot
Once the configuration and dependency installation are complete, launch the bot using the following command:
```bash
python weather_bot.py
```
A successful initialization will be indicated by a "Bot is starting..." message in your terminal. At this point, the bot is active and will respond to commands on Telegram.

## How to Use It 
Here's a quick rundown of what tasks the bot can perform.

  * `/start` - Kicks things off with a friendly welcome and a list of commands.
  * `/help` - Shows you the command list again if you forget.
  * `/weather [city]` - Grabs the current weather. If you leave out the city, it'll use your saved default.
  * `/forecast [city]` - Gives you the 5-day forecast. This also uses your default city if you don't specify one.
  * `/setlocation [city]` - Sets or updates your default city.
  * `/temperature <value> [C or F]` - Converts a temperature for you. Example: `/temperature 100 F` will convert 100°F to Celsius.