from pyrogram import filters
from pyrogram.types import Message

from KanhaMusic import kanha
from KanhaMusic.core.call import Kanha

welcome = 20
close = 30


@kanha.on_message(filters.video_chat_started, group=welcome)
@kanha.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Kanha.stop_stream_force(message.chat.id)
