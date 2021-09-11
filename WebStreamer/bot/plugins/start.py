# (c) @EverythingSuckz | @AbirHasan2005

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text='𝙷𝙻𝙾 𝙱𝚄𝙳𝙳𝚈 ☻︎\n𝙸 𝙰𝙼 𝙰 𝙸𝙽𝚂𝚃𝙰𝙽𝚃 𝙵𝙸𝙻𝙴 𝚃𝙾 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙰𝚁𝙰𝚃𝙴𝚁 𝙱𝙾𝚃 𝙾𝙵 𝙳𝙼𝚇 𝙶𝚁𝙾𝚄𝙿 ..𝙽𝙾𝚆 𝙸𝙰𝙼 𝙲𝚄𝚁𝚁𝙴𝙽𝚃𝙻𝚈 𝙵𝚄𝙻𝙻𝚃 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝙲𝚁𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙰𝙻𝚂𝙾 𝚄𝚂𝙴 𝙼𝙴 \n\n𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚃 𝙵𝙸𝙻𝙴 𝙵𝙾𝚁𝙼 𝙰𝙽𝚈 𝚆𝙷𝙴𝚁𝙴 |»«| 𝙰𝙽𝙳 𝙲𝙻𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝙼𝙰𝙻𝙻 𝙴𝚈𝙴𝚂 𝙰𝙽𝙳 𝙲𝙾𝚄𝙽𝚃 𝚃𝙾 𝙾𝙽𝙴(:_-_:)',
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('𝐌𝐘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋', url='https://t.me/dmxall_2'), InlineKeyboardButton('𝐆𝐑𝐎𝐔𝐏', url='https://t.me/dmx_chating')],
                    [InlineKeyboardButton('𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑', url='https://t.me/basildmx2')]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [ONWER](https://t.me/basildmx2).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
                                                     url=f"https://t.me/AH_File2Link_Bot?start=AbirHasan2005_{usr_cmd}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [ONWER](https://t.me/basildmx2).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "Bruh! 😁\nYour Link Generated! 🤓\n\n📂 **File Name:** `{}`\n**File Size:** `{}`\n\n📥 **Download Link:** `{}`"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Now", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [ONWER](https://t.me/basildmx2).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [ONWER](https://t.me/basildmx2).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="Send me any File I will provide External Direct Download Link!\n\nAlso I am Supported in Channels. Add me to Channel as Admin to Make Me Workable!",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝐆𝐑𝐎𝐔𝐏", url="https://t.me/dmx_chating"), InlineKeyboardButton("𝐌𝐘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/dmxall_2")],
                [InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑", url="https://t.me/basildmx")]
            ]
        )
    )
