import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQALpgotGTqEIopBSeOZ4cN0F8ga7O2KsFGdezw86jjobdjSVu8sATC6VXOzA8ey1z1TDwWoUh4AhXNj_CcehJg6hCUJuH5o-J_ib7YMcH-TDyHeUoic_D6Hs0ZAChowc69TP1gLZSsVRQOmdH4i8g55AxGQyXB5dNrQrl84-WB_oyX-iauQI0LhcHUGziiVSuPXGvpu56tL8uKHpk5ACYJjewNZ3O4m4LsOlLnQS-ndpplzlENJG8NbVUdvf7_gGMfh648zIxV0Y0_RDqyv13kBfIU5_NuiDYdVfkQUCEe2xub718NnYmLL38ZN64Pmy2yyZAmhzm-xbYESnIGKfozAAAAAAHTEabsA")
BOT_TOKEN = getenv("BOT_TOKEN", "5541263341:AAFsF3h7hxORPBC-9dU8v0y6AG3srj_Dsf8")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Creator_xD")
ALIVE_NAME = getenv("ALIVE_NAME", "Creator Pavan")
BOT_USERNAME = getenv("BOT_USERNAME", "UsersCallerBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TeamCodexun")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2056407064").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fa3a902da02b1aa99d2ca.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/fa3a902da02b1aa99d2ca.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/fa3a902da02b1aa99d2ca.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/fa3a902da02b1aa99d2ca.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/fa3a902da02b1aa99d2ca.jpg")
