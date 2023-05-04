import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("6252471050:AAFlBX-EkOPRf7re1WHZnMlNyYjkOg6c8yo", "")

    API_ID = int(os.environ.get("5806640", 23560088))

    API_HASH = os.environ.get("127f130ad3745dbcd31aa39aa0eabcb8", "999c01704d5c417749a98f4b8785fe88")

    AUTH_USERS = set(int(x) for x in os.environ.get("1375408229", "6203460103").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("https://t.me/+iR0XZIijZbwzYzdl", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = os.environ.get("mongodb+srv://bossboltebro:<password>@cluster0.jrzdzmy.mongodb.net/?retryWrites=true&w=majority", "")

    SESSION_NAME = os.environ.get("utubeup628bot", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("-1001981767301", -1001642382009))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("1375408229", "5410723702"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    BOT_USERNAME = os.environ.get("utubeup628bot", "UploadLinkToFileBot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("1375408229", "0").split()))

    PRO_USERS.append(OWNER_ID)
