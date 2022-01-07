import html
from lunaBot.modules.disable import DisableAbleCommandHandler
from lunaBot import dispatcher, DRAGONS
from lunaBot.modules.helper_funcs.extraction import extract_user
from telegram.ext import CallbackContext, CallbackQueryHandler, Filters, run_async
import lunaBot.modules.sql.mod_sql as sql
from lunaBot.modules.helper_funcs.chat_status import user_admin
from lunaBot.modules.log_channel import loggable
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest


@loggable
@user_admin
@run_async
def add_mod(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    args = context.args
    user = update.effective_user
    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    try:
        member = chat.get_member(user_id)
    except BadRequest:
        return ""
    if member.status == "creator":
        message.reply_text(
            "User is already admin, How to add admin as moderator"
        )
        return ""
    if sql.is_mod(message.chat_id, user_id):
        message.reply_text(
            f"[{member.user['first_name']}](tg://user?id={member.user['id']}) is already approved in {chat_title}",
            parse_mode=ParseMode.MARKDOWN,
        )
        return ""
    sql.add_mod(message.chat_id, user_id)
    message.reply_text(
        f"[{member.user['first_name']}](tg://user?id={member.user['id']}) has been moderated in {chat_title}! They will now be As Powerful as admin.",
        parse_mode=ParseMode.MARKDOWN,
    )
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#MODERATOR\n"
        f"<b>Owner:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )

    return log_message


@loggable
@user_admin
@run_async
def dis_mod(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    args = context.args
    user = update.effective_user
    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    try:
        member = chat.get_member(user_id)
    except BadRequest:
        return ""
    if member.status == "creator":
        message.reply_text("This user is an admin, they can't be Unmoderated.")
        return ""
    if not sql.is_mod(message.chat_id, user_id):
        message.reply_text(f"{member.user['first_name']} isn't moderated yet!")
        return ""
    sql.dis_mod(message.chat_id, user_id)
    message.reply_text(
        f"{member.user['first_name']} is no longer moderator in {chat_title}."
    )
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UN-MODERATED\n"
        f"<b>Owner:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )

    return log_message


@user_admin
@run_async
def is_mod(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    msg = "The following users are moderaors.\n"
    approved_users = sql.list_approved(message.chat_id)
    for i in approved_users:
        member = chat.get_member(int(i.user_id))
        msg += f"- `{i.user_id}`: {member.user['first_name']}\n"
    if msg.endswith("approved.\n"):
        message.reply_text(f"No users are approved in {chat_title}.")
        return ""
    else:
        message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)



APPROVE = DisableAbleCommandHandler("addmod", add_mod)
DISAPPROVE = DisableAbleCommandHandler("unmod", dis_mod)
APPROVED = DisableAbleCommandHandler("mods", is_mod)

dispatcher.add_handler(ADDMOD)
dispatcher.add_handler(UNMOD)
dispatcher.add_handler(MODS)

__mod_name__ = "ᴍᴏᴅs"
__command_list__ = ["add_mod", "dis_mod", "is_mod"]
__handlers__ = [ADDMOD, UNMOD, MODS]
