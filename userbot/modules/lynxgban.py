# by:kenzo @TeamSecret_Kz
# Lynx Userbot

from telethon.events import ChatAction
from userbot import ALIVE_NAME, CMD_HELP, bot
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Yang Mulia, Ini Tidak Mungkin Tanpa ID Pengguna`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`Terjadi Kesalahan... Mohon Lapor Ke Grup` @LordUserbot_Group", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
# Ported For Lynx-Userbot by KENZO/Axel


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"𝐘𝐚𝐧𝐠 𝐌𝐮𝐥𝐢𝐚, 𝐏𝐞𝐧𝐠𝐠𝐮𝐧𝐚 𝐆𝐁𝐚𝐧 𝐓𝐞𝐥𝐚𝐡 𝐁𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠. \n"
                                f"𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖 __:__ [{guser.id}](tg://user?id={guser.id}) \n"
                                f"𝘼𝙠𝙨𝙞 __:__ 🚫 `Banned` 🚫"
                            )
                        except BaseException:
                            return


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Awas, Yang Mulia Ingin Mengaktifkan Perintah Global Banned!`")
    else:
        dark = await dc.edit("`Memproses Global Banned Pengguna Ini ❗`")
    me = await userbot.client.get_me()
    await dark.edit(f"`𝗚𝗹𝗼𝗯𝗮𝗹 𝘽𝙖𝙣𝙣𝙚𝙙 Akan Segera Aktif, Anda Akan Dibanned Secara Global Oleh Yang Mulia.`")
    await dark.edit(f"`𝗚𝗹𝗼𝗯𝗮𝗹 𝘽𝙖𝙣𝙣𝙚𝙙 Akan Segera Aktif, Anda Akan Dibanned Secara Global Oleh Yang Mulia..`")
    await dark.edit(f"`𝗚𝗹𝗼𝗯𝗮𝗹 𝘽𝙖𝙣𝙣𝙚𝙙 Akan Segera Aktif, Anda Akan Dibanned Secara Global Oleh Yang Mulia...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Terjadi Kesalahan...`")
    if user:
        if user.id == 1448477501:
            return await dark.edit(
                f"`Anda Tidak Bisa Melakukan Global Banned Ke Lord Axel, Dia Adalah Pembuat Saya 😼`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡ 🐈`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡🐈`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛🐈`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞🐈⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩🐈𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠🐈𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼🐈𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 🐈𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙🐈𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚🐈 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣🐈𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣🐈𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖🐈𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 𝘽🐈𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡 🐈𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖𝙡🐈𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗𝙖🐈 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤𝙗🐈𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡𝙤🐈𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂𝙡🐈𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡𝙂🐈𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"`⚡🐈𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛⚡`")
                await dark.edit(f"⚡`𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝘼𝙠𝙩𝙞𝙛`⚡")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Mohon Balas Ke Pesan Pengguna`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Kesalahan!!! Pengguna Ini Sudah Terkena Perintah Global Banned 😎**")
    except BaseException:
        pass
    return await dark.edit(
        f"**⚡ 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 :** `{ALIVE_NAME}`\n**👤 𝐏𝐞𝐧𝐠𝐠𝐮𝐧𝐚 :** [{user.first_name}](tg://user?id={user.id})\n**🔥 𝐀𝐤𝐬𝐢 : **🚫 𝗚𝗹𝗼𝗯𝗮𝗹 𝘽𝙖𝙣𝙣𝙚𝙙 🚫"
    )


@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Membatalkan Perintah Global Banned Pengguna Ini 😼`")
    else:
        dark = await dc.edit("⚡`Membatalkan Perintah Global Banned`⚡")
    me = await userbot.client.get_me()
    await dark.edit(f"`Memulai Membatalkan Perintah Global Banned, Pengguna Ini Akan Dapat Bergabung Ke Grup Anda 😼`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Terjadi Kesalahan 😾`")
    if user:
        if user.id == 1448477501:
            return await dark.edit("**Mohon Maaf, Pengguna Tidak Bisa Terkena Perintah Ini, Karna Dia Pembuatku 😼**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`Membatalkan Global Banned. Sedang Memproses.`")
                await dark.edit(f"`Membatalkan Global Banned. Sedang Memproses..`")
                await dark.edit(f"`Membatalkan Global Banned. Sedang Memproses...`")
                await dark.edit(f"`😼 Berhasil Membatalkan Global Banned 😼`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Harap Reply Ke Pesan Pengguna Yang Mulia...`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Kesalahan!!! Pengguna Ini Tidak Masuk Kedalam Kategori Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**⚡ 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡 :** `{ALIVE_NAME}`\n**👤 𝐏𝐞𝐧𝐠𝐠𝐮𝐧𝐚 :** [{user.first_name}](tg://user?id={user.id})\n**😼 𝐀𝐤𝐬𝐢 : **`Membatalkan Global Banned`"
    )


CMD_HELP.update({
    "gban": "\
⚡𝘾𝙈𝘿⚡: `.gban`\
\n↳ : Melakukan Banned Secara Global Ke Semua Grup Dimana Kamu Sebagai Admin.\
\n\n⚡𝘾𝙈𝘿⚡: `.ungban`\
\n↳ : Membatalkan Global Banned"
})
