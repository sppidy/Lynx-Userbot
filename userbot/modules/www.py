# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__C__")
    await pong.edit("__Co__")
    await pong.edit("__Con__")
    await pong.edit("__Conn__")
    await pong.edit("__Conne__")
    await pong.edit("__Connec__")
    await pong.edit("__Connect__")
    await pong.edit("__Connecti__")
    await pong.edit("__Connectin__")
    await pong.edit("__Connecting__")
    await pong.edit("__Connecting t__")
    await pong.edit("__Connecting to__")
    await pong.edit("__Connecting to s__")
    await pong.edit("__Connecting to se__")
    await pong.edit("__Connecting to ser__")
    await pong.edit("__Connecting to serv__")
    await pong.edit("__Connecting to serve__")
    await pong.edit("__Connecting to server__")
    await pong.edit("__Connecting to server.__")
    await pong.edit("__Connecting to server..__")
    await pong.edit("__Connecting to server...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╭━━━━━━━━━━━━━━━━━╮** \n"
                    f"**          - 𝐍 𝐄 𝐓 𝐖 𝐎 𝐑 𝐊 -** \n"
                    f"**   ▰▱▰▱▰▱▰▱▰▱▰▱** \n"
                    f"**        • ꜱɪɴʏᴀʟ  :** `%sms` \n"
                    f"**        • ᴏᴡɴᴇʀ   :** `{ALIVE_NAME}` \n"
                    f"**╰━━━━━━━━━━━━━━━━━╯** \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting to server...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-ꜱɪɢɴᴀʟ- :** "
                    f"`%sms` \n"
                    f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Connecting to server...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡【⁴⁰⁴ᴜꜱᴇʀʙᴏᴛ】⚡**\n"
                    f"➾ __Signal__    __:__ "
                    f"`%sms` \n"
                    f"➾ __Uptime__ __:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**⁴**")
    await pong.edit("**⁴⁰**")
    await pong.edit("**⁴⁰⁴**")
    await pong.edit("**⁴⁰⁴ᴜ**")
    await pong.edit("**⁴⁰⁴ᴜꜱ**")
    await pong.edit("**⁴⁰⁴ᴜꜱᴇ**")
    await pong.edit("**⁴⁰⁴ᴜꜱᴇʀ**")
    await pong.edit("**⁴⁰⁴ᴜꜱᴇʀʙ**")
    await pong.edit("**⁴⁰⁴ᴜꜱᴇʀʙᴏ**")
    await pong.edit("**⁴⁰⁴ᴜꜱᴇʀʙᴏᴛ**")
    await pong.edit("**__Connecting to server...__**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡【⁴⁰⁴ᴜꜱᴇʀʙᴏᴛ】⚡**\n"
                    f"☫ - **ꜱɪɢɴᴀʟ     :** "
                    f"`%sms` \n"
                    f"☫ - **ᴜᴘᴛɪᴍᴇ    :** "
                    f"`{uptime}` \n"
                    f"☫ - **ᴘᴇᴍɪʟɪᴋ   :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...⚡`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:** `404-Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Connecting to server.....⛧`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("🤴 **ꜱɪɢɴᴀʟ ʙᴀɢɪɴᴅᴀ**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "⚡**CMD**⚡: `.ping` | `.lping` | `.xping` | `.sping`\
    \n↳ : __Untuk menunjukkan ping bot.__\
    \n\n⚡**CMD**⚡: `.speed`\
    \n↳ : __Untuk menunjukkan kecepatan jaringan.__\
    \n\n⚡**CMD**⚡: `.pong`\
    \n↳ : __Sama seperti perintah ping.__"
     })
