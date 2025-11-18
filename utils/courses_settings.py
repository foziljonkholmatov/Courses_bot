from config import COURSES_FILE
from utils.csv_files import read_file, append_csv


def is_member(user_id, course):
    rows = read_file(COURSES_FILE)
    for r in rows:
        if r[0] == str(user_id) and r[1] == course:
            return True
    return False


def save_course(user_id, course):
    append_csv(COURSES_FILE, {
        'user_id': user_id,
        'course': course
    })
