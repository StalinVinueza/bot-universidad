from dotenv import load_dotenv
import os

load_dotenv()

MOODLE_URL = os.getenv("MOODLE_URL")
MOODLE_USERNAME = os.getenv("MOODLE_USERNAME")
MOODLE_PASSWORD = os.getenv("MOODLE_PASSWORD")

HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"