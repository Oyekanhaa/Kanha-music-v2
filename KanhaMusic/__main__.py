import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from KanhaMusic import LOGGER, kanha, userbot
from KanhaMusic.core.call import Kanha
from KanhaMusic.misc import sudo
from KanhaMusic.plugins import ALL_MODULES
from KanhaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await kanha.start()
    for all_module in ALL_MODULES:
        importlib.import_module("KanhaMusic.plugins" + all_module)
    LOGGER("KanhaMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Kanha.start()
    try:
        await Kanha.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("KanhaMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Kanha.decorators()
    LOGGER("KanhaMusic").info(
    "\x4b\x61\x6e\x68\x61\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x61\x62\x6f\x75\x74\x6b\x61\x6e\x68\x61"
)
    await idle()
    await kanha.stop()
    await userbot.stop()
    LOGGER("KanhaMusic").info("Stopping KanhaMusic Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
