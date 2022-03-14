from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tobrot import AUTH_CHANNEL


async def start_fn(client, message):
    if message.chat.type == "private":
        name = message.from_user.first_name
        msg = f"Hey {name}!\n"
        msg += "I am a uploader bot..\n"
        msg += "If you want to use me contact now <a href='https://t.me/YourX'>Team</a>!"
        msg += "\n\nThank You😊"
        await message.reply_text(
            msg,
            parse_mode="html",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Developer", url="https://t.me/YourX"
                        )
                    ]
                ]
            ),
        )
    elif message.from_user.id in AUTH_CHANNEL:
        await message.reply_text(f"Hey {message.from_user.first_name}!\nI'm alive.")
