import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(884031659)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[π](https://telegra.ph/file/0f8799ec342c196e2d23c.png) **FORCE SUBSCRIBE :**\n\nπΉππππ πΊπππ’π πππππππ  ππ π½πππ π΄ ππππππππ πΆβπππππ π΅πππππ πππππππ πππ π ππππ  ππ πβπ πΊπππ’π\nπΌ ππππ ππ’π‘π πππππππ  ππ πβππ¦ πππ‘ π½πππππ πππ’π πΆβπππππ π΄ππ ππππ πβππ ππ π½πππ πβπ πΆβπππππ π΄ππ ππππ’π‘π πβπππ πππ π΅π¦ ππππ π πππ π΄ π΅π’π‘π‘ππ.",
        
        "[β](https://telegra.ph/file/cbcca74bfdd4dc3308444.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\nβ Note: Only Creator Of The Group Can Setup Me.",
        
        "[β](https://i.imgur.com/LnOEiTK.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\nβ Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[π¨βπ»](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) **DEVELOPED BY @Goku_kun**"
      ]

      START_MSG = "**Hey! [π](https://telegra.ph/file/0f8799ec342c196e2d23c.png) [{}](tg://user?id={})**\n\nβ I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\nβ Learn More At π /help"
