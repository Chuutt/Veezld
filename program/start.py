from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**ʜᴇᴍʟᴏ  {message.from_user.mention()}\n\n**𝗧𝗵𝗶𝘀 𝗶𝘀 𝘁𝗵𝗲 𝗕𝗿𝗼𝗸𝗲𝗻 𝟮.𝟬**\n\n┏━━━━━━━━━━━━━━━━━┓
┣★ **ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ.** 
┣★ **ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜꜱɪᴄ.**
┣★ **ᴠɪᴅᴇᴏ ᴘʟᴀʏ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.**
┣★ **ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.**
┣★ **ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.**
┗━━━━━━━━━━━━━━━━━┛
\n
**ᴅᴇꜱɪɢɴᴇᴅ ʙʏ :** [𝗖𝗿𝗲𝗮𝘁𝗼𝗿 𝗣𝗮𝘃𝗮𝗻](https://t.me/CreatorPavan)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😀  𝗔𝗗𝗗 𝗠𝗘  😀",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/CreatorPavanSupport"),
                InlineKeyboardButton(
                    "ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/CreatorPavanUpdates"
                ),
            ],[
                InlineKeyboardButton("ᴀʟʟ ɪɴꜰᴏ ʜᴇʀᴇ", url=f"https://t.me/CreatorPavan"),
            ]
        ]
    )

    alive = f"**ʜᴇᴍʟᴏ {message.from_user.mention()}, ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʙʀᴏᴋᴇɴ.**\n\n» ᴡᴏʀᴋɪɴɢ ɴᴏʀᴍᴀʟʟʏ\n» ᴏᴘ ᴍᴀꜱᴛᴇʀ : [𝗖𝗿𝗲𝗮𝘁𝗼𝗿 𝗣𝗮𝘃𝗮𝗻](https://t.me/Creator_Pavan)\n» ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ : `v{__version__}`\n» ᴘʏʀᴏ ᴠᴇʀꜱɪᴏɴ : `{pyrover}`\n» ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ : `{__python_version__}`\n» ᴘʏᴛɢᴄᴀʟʟꜱ : `{pytover.__version__}`\n» ᴜᴘᴛɪᴍᴇ : `{uptime}`\n\n**ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴅᴇꜱɪɢɴᴇᴅ ᴀɴᴅ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ, ᴛʜᴀɴᴋᴜ ᴠᴇʀʏ ᴍᴜᴄʜ ꜰᴏʀ ᴀᴅᴅɪɴɢ ʜᴇʀᴇ..**"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**» ʙʀᴏᴋᴇɴ ᴘᴏɴɢ ꜰʀᴏᴍ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ꜱᴇʀᴠᴇʀ..**\n\n💞 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🏷️ **ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ᴏᴘ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.**\n\n"
        f"• **ᴜᴘᴛɪᴍᴇ :** `{uptime}`\n"
        f"• **ꜱᴛᴀʀᴛ ᴀᴛ :** `{START_TIME_ISO}`"
    )

@Client.on_message(filters.command("pavan") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʙʀᴏᴋᴇɴ ᴡʜɪᴄʜ ɪꜱ ꜱᴘᴇᴄɪꜰɪᴄᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗔𝗯𝗼𝘂𝘁", url="https://t.me/itsCrePavan")
                ]
            ]
        )
   )
