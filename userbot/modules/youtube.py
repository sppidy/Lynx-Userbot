# © Copyright 2021 Lynx-Userbot LLC Company.
# GPL-3.0 License From Github
# Ported for Lynx-Userbot by @TeamSecret_Kz (KENZO)
# WARNING !! Don't Remove this hashtag if u kang it.
# Credits : @Catuserbot and @SyndicateTwenty4

import asyncio
import json
import os
import re
import shutil
import time
import qrcode
import barcode
import asyncurban
import emoji
import requests

from asyncio import sleep
from barcode.writer import ImageWriter
from re import findall
from re import match
from os import popen
from urllib.error import HTTPError
from urllib.parse import quote_plus
from random import choice
from requests import get, post, exceptions
from humanize import naturalsize

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from emoji import get_emoji_regexp
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from requests import get
from search_engine_parser import YahooSearch as GoogleSearch
from telethon.tl.types import DocumentAttributeAudio
from telethon.tl.types import MessageMediaPhoto
from urbandict import define
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from youtube_dl import YoutubeDL
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
from youtube_search import YoutubeSearch

from userbot import (
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    IMG_LIMIT,
    TEMP_DOWNLOAD_DIRECTORY,
    WOLFRAM_ID,
    CHROME_DRIVER,
    GOOGLE_CHROME_BIN,
    LOGS,
    OCR_SPACE_API_KEY,
    REM_BG_API_KEY,
    bot
)

from userbot.events import register
from userbot.utils import chrome, googleimagesdownload, progress, options


@register(outgoing=True, pattern=r"\.(ytaud|ytvid) (.*)")
 async def download_video(v_url):
     url = v_url.pattern_match.group(2)
     type = v_url.pattern_match.group(1).lower()

     await v_url.edit("`Preparing to download...`")

     if type == "ytaud":
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

     elif type == "ytvid":
         opts = {
             "format": "best",
             "addmetadata": True,
             "key": "FFmpegMetadata",
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
         with YoutubeDL(opts) as rip:
             rip_data = rip.extract_info(url)
     except DownloadError as DE:
         return await v_url.edit(f"`{str(DE)}`")
     except ContentTooShortError:
         return await v_url.edit("`The download content was too short.`")
     except GeoRestrictedError:
         return await v_url.edit(
             "`Video is not available from your geographic location "
             "due to geographic restrictions imposed by a website.`"
         )
     except MaxDownloadsReached:
         return await v_url.edit("`Max-downloads limit has been reached.`")
     except PostProcessingError:
         return await v_url.edit("`There was an error during post processing.`")
     except UnavailableVideoError:
         return await v_url.edit("`Media is not available in the requested format.`")
     except XAttrMetadataError as XAME:
         return await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
     except ExtractorError:
         return await v_url.edit("`There was an error during info extraction.`")
     except Exception as e:
         return await v_url.edit(f"{str(type(e)): {str(e)}}")
     c_time = time.time()
     if song:
         await v_url.edit(f"`Preparing to upload song:`\n**{rip_data['title']}**")
         await v_url.client.send_file(
             v_url.chat_id,
             f"{rip_data['id']}.mp3",
             supports_streaming=True,
             attributes=[
                 DocumentAttributeAudio(
                     duration=int(rip_data["duration"]),
                     title=str(rip_data["title"]),
                     performer=str(rip_data["uploader"]),
                 )
             ],
             progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                 progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp3")
             ),
         )
         os.remove(f"{rip_data['id']}.mp3")
         await v_url.delete()
     elif video:
         await v_url.edit(f"`Preparing to upload video:`\n**{rip_data['title']}**")
         await v_url.client.send_file(
             v_url.chat_id,
             f"{rip_data['id']}.mp4",
             supports_streaming=True,
             caption=rip_data["title"],
             progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                 progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp4")
             ),
         )
         os.remove(f"{rip_data['id']}.mp4")
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
