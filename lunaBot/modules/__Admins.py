__mod_name__ = "Admins"

from lunaBot.modules.language import gs
from telegram.ext import CallbackContext
from lunaBot.modules.helper_funcs.dc import kigcmd, kigcallback
from lunaBot.modules.helper_funcs.string_handling import markdown_parser
from lunaBot import (
    dispatcher, 
    OWNER_ID
) 
from telegram import (
    ParseMode,
    Update,
    Chat,
    User,
    MessageEntity,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ChatAction,
)

def fud_ban_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_rules_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_warn_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )

def fud_log_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )

def fud_purge_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_antispam_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )

def fud_approve_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_greetings_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_locks_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLOBRO", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_flood_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "Hello sis", 
        parse_mode=ParseMode.MARKDOWN,
    )



def fud_mute_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLO KIDS", 
        parse_mode=ParseMode.MARKDOWN,
    )
def fud_group_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        "HELLO KIDS", 
        parse_mode=ParseMode.MARKDOWN,
    )


@kigcallback(pattern=r"fud_help_")
def fud_help(update: Update, context: CallbackContext):
    query = update.callback_query
    bot = context.bot
    help_info = query.data.split("fud_help_")[1]
    if help_info == "flood":
        help_text = gs(update.effective_chat.id, "antiflood_help") 
    elif help_info == "ban":
        help_text = gs(update.effective_chat.id, "bans_help") 
    elif help_info == "mute":
        help_text = gs(update.effective_chat.id, "muting_help") 
    elif help_info == "warn":
        help_text = gs(update.effective_chat.id, "warns_help") 
    elif help_info == "rules":
        help_text = gs(update.effective_chat.id, "rules_help") 
    elif help_info == "purge":
        help_text = gs(update.effective_chat.id, "purge_help") 
    elif help_info == "log":
        help_text = gs(update.effective_chat.id, "log_help") 
    elif help_info == "group":
        help_text = gs(update.effective_chat.id, "group_help")
    elif help_info == "antispam":
        help_text = gs(update.effective_chat.id, "antispam_help") 
    elif help_info == "approve":
        help_text = gs(update.effective_chat.id, "approve_help") 
    elif help_info == "greetings":
        help_text = gs(update.effective_chat.id, "greetings_help") 
    elif help_info == "locks":
        help_text = gs(update.effective_chat.id, "locks_help")
    query.message.edit_text(
        text=help_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"help_module({__mod_name__.lower()})"),]]
        ),
    )
    bot.answer_callback_query(query.id)


def get_help(chat):
    return [gs(chat, "admin_help"),
    [
        InlineKeyboardButton(text="ғʟᴏᴏᴅ", callback_data="fud_help_flood"),
        InlineKeyboardButton(text="ʙᴀɴ", callback_data="fud_help_ban"), 
        InlineKeyboardButton(text="ᴍᴜᴛᴇ", callback_data="fud_help_mute"), 
    ], 
    [
        InlineKeyboardButton(text="ᴡᴀʀɴ", callback_data="fud_help_warn"), 
        InlineKeyboardButton(text="ʀᴜʟᴇs", callback_data="fud_help_rules"), 
        InlineKeyboardButton(text="ᴘᴜʀɢᴇ", callback_data="fud_help_purge"), 
    ],
    [
        InlineKeyboardButton(text="ᴀᴘᴘʀᴏᴠᴇ", callback_data="fud_help_approve"), 
        InlineKeyboardButton(text="ᴡᴇʟᴄᴏᴍᴇ", callback_data="fud_help_greetings"), 
        InlineKeyboardButton(text="ʟᴏᴄᴋs", callback_data="fud_help_locks")
    ],
    [
        InlineKeyboardButton(text="ʟᴏɢs", callback_data="fud_help_log"), 
        InlineKeyboardButton(text="ɢʀᴏᴜᴘ", callback_data="fud_help_group"),         
    ],
]
