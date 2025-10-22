from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Note(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    label: str = Field(default="all")
    title: str
    content: str


notes_list: list[Note] = [
    Note(label="work", title="Q4 Project Kickoff",
         content="Finalize the project brief for the Q4 initiative. Schedule a kickoff meeting with the team for next Monday."),
    Note(label="personal", title="Dentist Appointment",
         content="Appointment with Dr. Smith on Tuesday, October 21st at 10:00 AM. Remember to bring insurance card."),
    Note(label="shopping", title="Grocery Shopping",
         content="Milk, bread, eggs, cheese, apples, bananas, chicken breast, spinach."),
    Note(label="ideas", title="New App Idea",
         content="A mobile app that helps users track their plant watering schedules with reminders and plant care tips."),
    Note(label="work", title="Weekly Sync - Oct 15",
         content="Discussed progress on the 'Phoenix' project. Action item for me: Follow up with the design team."),
    Note(label="personal", title="Book Flights for Vacation",
         content="Research and book flights to Bali for the December holiday. Check for deals on Skyscanner."),
    Note(label="all", title="Favorite Quote",
         content="'The only way to do great work is to love what you do.' - Steve Jobs"),
    Note(label="personal", title="Pasta Carbonara Recipe",
         content="Ingredients: spaghetti, eggs, Pecorino Romano cheese, guanciale, black pepper."),
    Note(label="work", title="Prepare Presentation",
         content="Create a slide deck for the monthly review meeting. Include key metrics, recent wins, and challenges."),
    Note(label="reminders", title="Pay utility bills",
         content="Electricity and water bills are due by the 25th of this month."),
    Note(label="ideas", title="Weekend Project Idea",
         content="Build a small wooden bookshelf for the living room. Look up some DIY tutorials on YouTube."),
    Note(label="shopping", title="Hardware Store List",
         content="Sandpaper (120 and 220 grit), wood stain, paint brushes, screws."),
    Note(label="work", title="Code Refactoring",
         content="Refactor the authentication module. Focus on improving readability and adding more comprehensive unit tests."),
    Note(label="personal", title="Gym Schedule",
         content="Monday: Chest/Triceps, Wednesday: Back/Biceps, Friday: Legs/Shoulders."),
    Note(label="all", title="Book Recommendations",
         content="Project Hail Mary by Andy Weir, Atomic Habits by James Clear, Sapiens by Yuval Noah Harari."),
    Note(label="reminders", title="Call Mom",
         content="Call mom this weekend to catch up."),
    Note(label="work", title="Review Pull Request #431",
         content="Review Dave's PR for the new caching feature. Check for potential race conditions."),
    Note(label="ideas", title="Blog Post Ideas",
         content="1. 'Getting Started with FastAPI'. 2. 'A Guide to Effective Note-Taking'."),
    Note(label="shopping", title="Birthday Gift for Sarah",
         content="Her birthday is next month. Ideas: a nice fountain pen, a popular novel, or a gift card."),
    Note(label="personal", title="Car Maintenance",
         content="Schedule an oil change for the car. Mileage is approaching the next service interval.")
]
