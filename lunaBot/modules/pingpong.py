from lunaBot.events import register
from pyrogram import filters
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import *

PM_TEXT = "HEY THERE ME MINI MANAGERBOT CREATED BY [TEAM-RAICHU](T.ME/XRAICHU_OFFICIAL) FOR BETTER MANAGEMENT OF GROUP AND ALSO TO MAKE BOT SMALL AND ATTRACTIVE"
START_BUTTON = [
      [
        InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="t.me/RaichuxManagerbot?startgroup=true") 
      ], 
      [           
        InlineKeyboardButton("Gʀᴏᴜᴘ", url="t.me/xraichu_official"),
        InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="t.me/xraichunews")
      ], 
# ADD COLLBACK TO HELP THEN PUBLIC
      [ 
        InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs❔", callback_data="help")
      ]
    ]
HELP_BUTTON = [
      [
        InlineKeyboardButton("Admin", callback_data="admin"), 
        InlineKeyboardButton("Approval", callback_data="approval"),
        InlineKeyboardButton("Backup", callback_data="backup"),
      ],
      [
        InlineKeyboardButton("Chatbot", callback_data="chatbot"), 
        InlineKeyboardButton("connection", callback_data="connection"),
        InlineKeyboardButton("disable", callback_data="disable"),
      ],
      [
        InlineKeyboardButton("Extra", callback_data="extras"), 
        InlineKeyboardButton("Feds", callback_data="feds"),
        InlineKeyboardButton("F-sub", callback_data="forcesb"),
      ],
      [
        InlineKeyboardButton("Locks", callback_data="locks"), 
        InlineKeyboardButton("Feds", callback_data="notes"),
        InlineKeyboardButton("Rules", callback_data="rules"),
      ],
      [
        InlineKeyboardButton("Tagalrt", callback_data="tagalrt"), 
        InlineKeyboardButton("Welcome", callback_data="welcome"),
      ], 
      [
        InlineKeyboardButton("Back", callback_data="backhome"), 
      ]
    ]     
@Client.on_callback_query(filters.regex("help"))
async def cbstart(_, query: CallbackQuery):
    
    await query.edit_message_text(
        f"""HERE IS THE HELP MENU FOR THIS MANAGEMENBOT""", 
    reply_markup = InlineKeyboardMarkup(HELP_BUTTON), 
    disable_web_page_preview=True                        
  )
@register(pattern="^/blazeop?(.*)")
def start(bot, message):
    await message.Reply_text(
    text=PM_TEXT
    reply_markup=reply_markup,
    disable_web_page_preview=True                        
  )
