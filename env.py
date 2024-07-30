import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "28795512")
API_HASH = os.getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7439140731:AAHk4e5ZmzdPiRt3LJ5p7rUt1nD2xwbF2UQ")
SUDOERS = list(map(int, os.getenv("SUDOERS", "5959548791").split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1001970127211")
MUST_JOIN = os.getenv("MUST_JOIN", "all_sanatani_bot")
DISABLED = os.getenv("DISABLED", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
