import os
import asyncio
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The unexamined life is not worth living. - Socrates",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. - Ralph Waldo Emerson",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "Our greatest glory is not in never falling, but in rising every time we fall. - Confucius",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "That which does not kill us makes us stronger. - Friedrich Nietzsche",
    "The human spirit is stronger than anything that can happen to it. - C.C. Scott",
    "The best thing to hold onto in life is each other. - Audrey Hepburn",
    "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that. - Martin Luther King, Jr.",
    "To love and be loved is to feel the sun from both sides. - David Viscott",
    "If I know what love is, it is because of you. - Hermann Hesse",
    "I am so clever that sometimes I don't understand a single word of what I am saying. - Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "To be sure of hitting the target, shoot first, and call whatever you hit the target. - Ashleigh Brilliant",
    "I have a simple philosophy: Fill what's empty. Empty what's full. Scratch where it itches. - Alice Roosevelt Longworth"
]

facts = [
    "An octopus has three hearts and blue blood.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "A day on Venus is longer than a year on Venus. It takes Venus 243 Earth days to rotate once on its axis, but only 225 Earth days to orbit the Sun.",
    "Bananas are berries, but strawberries are not. In botany, berries are fruits produced from a single ovary.",
    "A group of flamingos is called a 'flamboyance.'",
    "Oxford University is older than the Aztec Empire. Teaching at Oxford started in 1096, while the Aztec city of Tenochtitlán was founded in 1325.",
    "Cleopatra lived closer in time to the first moon landing than to the construction of the Great Pyramid of Giza. The pyramid was built ~2560 BCE, Cleopatra lived ~30 BCE, and the moon landing was in 1969 CE.",
    "During World War II, the Oscar statuettes were made of painted plaster due to the metal shortage.",
    "The human brain operates on about 10-20 watts of power, which is less than a standard light bulb.",
    "It's impossible to hum while holding your nose closed. This is because humming requires you to exhale air, which you can't do if your mouth and nose are shut.",
    "Humans share about 60%' of their DNA with bananas.",
    "The inventor of the Pringles can, Fredric Baur, was so proud of his creation that his ashes were buried in one after he passed away in 2008.",
    "The word 'nerd' was first coined by Dr. Seuss in his 1950 book, 'If I Ran the Zoo.'",
    "Chainsaws were originally invented in the late 18th century for assisting in childbirth, specifically for cutting through the pelvic bone.",
    "The world's first university, Takshashila, was established in India around 700 BCE.",
    "Varanasi is one of the oldest continuously inhabited cities in the world.",
    "The landmass of India was an island over 100 million years ago before colliding with Asia to form the Himalayas.",
    "The Statue of Unity in Gujarat, at 182 meters (597 feet), is the world's tallest statue.",
    "The concept of zero as a number and its use in the decimal system was developed in India.",
    "Mathematical concepts like Algebra, Trigonometry, and Calculus have their origins in India.",
    "The ancient Indian physician Sushruta is considered the 'Father of Surgery,' performing complex operations like plastic surgery over 2,600 years ago.",
    "The word 'navigation' is derived from the Sanskrit word 'Navgatih,' originating from practices in the Indus River.",
    "Mawsynram in Meghalaya, India, is the wettest inhabited place on Earth.",
    "India has the world's only floating post office, located on Dal Lake in Srinagar.",
    "India has 22 officially recognized languages and over 19,500 dialects spoken across the country.",
    "India is the world's largest producer, consumer, and exporter of spices.",
    "The games of Chess (originally 'Chaturanga') and Snakes and Ladders were invented in India.",
    "The practice and the word 'shampoo' originated in India from the Hindi word 'chāmpo,' meaning to massage.",
    "Buttons were first used in the Indus Valley Civilization, and until 1896, India was the world's only source of diamonds."
]

jokes = [
    "My doctor told me I had a fatal illness. I told him I wanted a second opinion. He said, 'Okay, you're ugly too.'",
    "They all laughed when I said I wanted to be a comedian. Well, they're not laughing now.",
    "My grief counselor died the other day. He was so good at his job, I don't even care.",
    "What's red and bad for your teeth? A brick.",
    "I have a lot of jokes about unemployed people, but none of them work.",
    "My grandfather's last words were, 'Are you still holding the ladder?'",
    "The last thing I want to do is hurt you. But it's still on the list.",
    "My therapist told me time heals all wounds, so I stabbed him. Now we wait.",
    "I told my doctor I broke my arm in two places. He told me to stop going to those places.",
    "My favorite Baskin-Robbins flavor is Pralines and Cream. My least favorite is getting hit by a car."
]

inspirational = [
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "The journey of a thousand miles begins with a single step. - Lao Tzu",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Arise, awake, and stop not till the goal is reached. - Swami Vivekananda",
    "In the midst of winter, I found there was, within me, an invincible summer. - Albert Camus",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Fall seven times, stand up eight. - Japanese Proverb",
    "The best way to predict the future is to create it. - Peter Drucker",
    "You are the sky. Everything else – it’s just the weather. - Pema Chödrön",
    "It is not the mountain we conquer, but ourselves. - Sir Edmund Hillary"
]

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Hello! I’m your Quote Bot. Use /help to see what I can do!"
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(quotes))

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(facts))

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(jokes))

async def inspire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(inspirational))

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📘 *Available Commands:*\n\n"
        "/start - Start the bot\n"
        "/quote - Get a random quote\n"
        "/fact - Learn an interesting fact\n"
        "/joke - Hear a funny joke\n"
        "/inspire - Get inspired\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("inspire", inspire))
    app.add_handler(CommandHandler("help", help))

    print("Rudra's Quote Bot is Running.....")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())