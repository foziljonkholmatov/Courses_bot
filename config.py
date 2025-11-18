import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path='.env'
)
BOT_TOKEN = os.getenv('BOT_TOKEN')

USERS_FILE = 'data/users.csv'
COURSES_FILE = 'data/courses.csv'

COURSES = [
    'Python',
    'HTML',
    'CSS'
]
