# © Copyright 2021 Lynx-Userbot LLC Company.
# GPL-3.0 License From Github
# Ported for Lynx-Userbot by @TeamSecret_Kz (KENZO)
# WARNING !! Don't Remove this hashtag if u kang it.
# Credits : @Catuserbot and @SyndicateTwenty4

import json
import asyncio
import os
import re
import time

from re import findall
from re import match
from os import popen

from datetime import datetime
from pathlib import Path
from requests import get, post, exceptions

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_search import YoutubeSearch
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import progress


@register(outgoing=True, pattern=r"\.(ytaud|ytvid) (.*)")
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    url = v_url.pattern_match.group(2)
    if not url:
        rmsg = await v_url.get_reply_message()
        myString = rmsg.text
        url = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
    if not url:
        await edit_or_reply(v_url, "What I am Supposed to find? Give link")
        return
    ytype = v_url.pattern_match.group(1).lower()
    v_url = await edit_or_reply(v_url, "`Preparing to download...`")
    reply_to_id = await reply_id(v_url)
    if ytype == "ytaud":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        video = False
        song = True
    elif ytype == "ytvid":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        song = False
        video = True
    try:
        await v_url.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await v_url.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await v_url.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await v_url.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    catthumb = Path(f"{ytdl_data['id']}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{ytdl_data['id']}.webp")
    if not os.path.exists(catthumb):
        catthumb = None
    if song:
        await v_url.edit(
            f"`Preparing to upload song:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            thumb=catthumb,
            reply_to=reply_to_id,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp3"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp3")
    elif video:
        await v_url.edit(
            f"`Preparing to upload video:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            reply_to=reply_to_id,
            supports_streaming=True,
            caption=ytdl_data["title"],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Uploading..", f"{ytdl_data['title']}.mp4"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp4")
    if catthumb:
        os.remove(catthumb)
    await v_url.delete()


@register(outgoing=True, pattern=r"^\.ytsearch (.*)")
async def yt_search(video_q):
    query = video_q.pattern_match.group(1)
    if not query:
        await video_q.edit("`Enter query to search`")
    await video_q.edit("`Processing...`")
    try:
        results = json.loads(YoutubeSearch(query, max_results=7).to_json())
    except KeyError:
        return await video_q.edit(
            "`Youtube Search gone retard.\nCan't search this query!`"
        )
    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n"
    for i in results["videos"]:
        output += f"● `{i['title']}`\nhttps://www.youtube.com{i['url_suffix']}\n\n"
    await video_q.edit(output, link_preview=False)



CMD_HELP.update(
    {
       "youtube": 
       "⚡𝘾𝙈𝘿⚡ : `.ytaud <link yt>`\
    \n↳ : Downloads the AUDIO from the given link\
    \n\n⚡𝘾𝙈𝘿⚡ : `.ytvid <link yt>`\
    \n↳ : Downloads the VIDEO from the given link\
    \n\n⚡𝘾𝙈𝘿⚡ : `.ytsearch <search>\
    \n↳ : Does a Youtube Search."
    }
)
