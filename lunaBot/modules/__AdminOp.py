from telegram import (
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackQueryHandler 
from telegram.ext import CallbackContext


def fmt_md_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        HelloBro, 
        parse_mode=ParseMode.HTML,
    )


def fmt_filling_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        HelloBro, 
        parse_mode=ParseMode.HTML,
    )



@callback(pattern=r"fmt_help_")
def fmt_help(update: Update, context: CallbackContext):
    query = update.callback_query
    bot = context.bot
    help_info = query.data.split("fmt_help_")[1]
    if help_info == "md":
        help_text = donopdon
    elif help_info == "filling":
        help_text = hibro 
    query.message.edit_text(
        text=help_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data=f"help_module({__mod_name__.lower()})"),]]
        ),
    )
    bot.answer_callback_query(query.id)

__mod_name__ = 'Formatting'

def get_help(chat):
    return "Hello Bruh"
[
    [
        InlineKeyboardButton(text="Markdown", callback_data="fmt_help_md"),
        InlineKeyboardButton(text="Filling", callback_data="fmt_help_filling")
    ]
]
