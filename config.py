## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBa1twSr7GwBqVgA2cdxK4xnt8zTSoYuPvmch0HQ-KgmEbn238U6Dhv0XDubJU5YSbL9FcDRRE10J3ivyD6NBUHlIZQpBmOtrEY4iKD1qLcpyLzFEwRgaGD4ydKxZLDYqMyw6PQc69SvQl1HbYGH4s5qNY6Cp2b780mFaXXtD-NG-oG76ca5kh3tSAEA_3CibOKOgho0hR-D0vjOjZecMd71kVfj2-U3I9TG4vv0zwJHTdQwUtNF5I-qfuDQmsgZ81A8G5pqjEG9rD7WLzQUMOpatLbwHLPJ3_ELOo05AFpK-Mebg5xGq41ScsjI0Rp-eP_RJCBFLuvMwkh-_nCx3a-AAAAAUqDigcA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5667013817:AAEp9ZEBF6C2bfN9D4Om2xLrOv0dwyNMTW8")
BOT_NAME = getenv("BOT_NAME", "SUMIT x BELLY")

API_ID = int(getenv("API_ID", "14200983"))
API_HASH = getenv("API_HASH", "233ef51a2c05a3979f95d7c7730cf320")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Belly:belly55@atlascluster.ends7zl.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Sumit")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_sumit_ll")
ALIVE_NAME = getenv("ALIVE_NAME", "SUMIT x MUSIC ")
BOT_USERNAME = getenv("BOT_USERNAME", "bellyvcbot")
OWNER_ID = getenv("OWNER_ID", "2139088940")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "iMi_seno")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xd_luxclub")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ab_sumit")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2139088940").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/8eb3466b2e2fc39263665.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/8eb3466b2e2fc39263665.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
