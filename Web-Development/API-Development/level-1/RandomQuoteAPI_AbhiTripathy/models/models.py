from pydantic import BaseModel

class Quote(BaseModel):
    id: int
    text: str
    author: str
    category: str
    
quotes = [
    Quote(id=1, text="The only way to do great work is to love what you do.", author="Steve Jobs", category="Inspiration"),
    Quote(id=2, text="The only true wisdom is in knowing you know nothing.", author="Socrates", category="Wisdom"),
    Quote(id=3, text="I am so clever that sometimes I don't understand a single word of what I am saying.", author="Oscar Wilde", category="Humor"),
    Quote(id=4, text="To love and be loved is to feel the sun from both sides.", author="David Viscott", category="Love"),
    Quote(id=5, text="The good thing about science is that it's true whether or not you believe in it.", author="Neil deGrasse Tyson", category="Science"),
    Quote(id=6, text="Every artist was first an amateur.", author="Ralph Waldo Emerson", category="Art"),
    Quote(id=7, text="So we beat on, boats against the current, borne back ceaselessly into the past.", author="F. Scott Fitzgerald", category="Literature"),
    Quote(id=8, text="Those who cannot remember the past are condemned to repeat it.", author="George Santayana", category="History"),
    Quote(id=9, text="Technology is a useful servant but a dangerous master.", author="Christian Lous Lange", category="Technology"),
    Quote(id=10, text="An unexamined life is not worth living.", author="Socrates", category="Philosophy"),
    Quote(id=11, text="Success is not final, failure is not fatal: it is the courage to continue that counts.", author="Winston Churchill", category="Success"),
    Quote(id=12, text="Get busy living or get busy dying.", author="Stephen King", category="Life"),
    Quote(id=13, text="Courage is grace under pressure.", author="Ernest Hemingway", category="Courage"),
    Quote(id=14, text="A friend is someone who knows all about you and still loves you.", author="Elbert Hubbard", category="Friendship"),
    Quote(id=15, text="Look deep into nature, and then you will understand everything better.", author="Albert Einstein", category="Nature"),
    Quote(id=16, text="Believe you can and you're halfway there.", author="Theodore Roosevelt", category="Inspiration"),
    Quote(id=17, text="It is the mark of an educated mind to be able to entertain a thought without accepting it.", author="Aristotle", category="Wisdom"),
    Quote(id=18, text="A day without sunshine is like, you know, night.", author="Steve Martin", category="Humor"),
    Quote(id=19, text="The best thing to hold onto in life is each other.", author="Audrey Hepburn", category="Love"),
    Quote(id=20, text="Somewhere, something incredible is waiting to be known.", author="Carl Sagan", category="Science"),
    Quote(id=21, text="The purpose of art is washing the dust of daily life off our souls.", author="Pablo Picasso", category="Art"),
    Quote(id=22, text="It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", author="Jane Austen", category="Literature"),
    Quote(id=23, text="The advance of technology is based on making it fit in so that you don't even notice it, so it's part of everyday life.", author="Bill Gates", category="Technology"),
    Quote(id=24, text="I think therefore I am.", author="René Descartes", category="Philosophy"),
    Quote(id=25, text="I have not failed. I've just found 10,000 ways that won't work.", author="Thomas A. Edison", category="Success")
]