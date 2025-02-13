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
def approoe(update, context):
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
    if member.status == "administrator" or member.status == "creator":
        message.reply_text(
            "User is already admin - Can't Set Admins As Moderator."
        )
        return ""
    if sql.is_approoed(message.chat_id, user_id):
        message.reply_text(
            f"[{member.user['first_name']}](tg://user?id={member.user['id']}) is already Moderator in {chat_title}",
            parse_mode=ParseMode.MARKDOWN,
        )
        return ""
    sql.approoe(message.chat_id, user_id)
    message.reply_text(
        f"[{member.user['first_name']}](tg://user?id={member.user['id']}) has been Promoted To Moderator in {chat_title}! They can now use All Admin rights except promote User.",
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
def disapprooe(update, context):
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
    if member.status == "administrator" or member.status == "creator":
        message.reply_text("This user is an admin, they can't be Promoted To Moderator.")
        return ""
    if not sql.is_approoed(message.chat_id, user_id):
        message.reply_text(f"{member.user['first_name']} isn't Moderator yet!")
        return ""
    sql.disapprooe(message.chat_id, user_id)
    message.reply_text(
        f"{member.user['first_name']} is no longer Moderator in {chat_title}."
    )
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#RM-MODERATOR\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )

    return log_message


@user_admin
@run_async
def approoed(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    msg = "The following users are Moderators.\n"
    approoed_users = sql.list_approoed(message.chat_id)
    for i in approoed_users:
        member = chat.get_member(int(i.user_id))
        msg += f"- `{i.user_id}`: {member.user['first_name']}\n"
    if msg.endswith("approoed.\n"):
        message.reply_text(f"No users are moderator in {chat_title}.")
        return ""
    else:
        message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)


@user_admin
@run_async
def approoal(update, context):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    user_id = extract_user(message, args)
    member = chat.get_member(int(user_id))
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    if sql.is_approoed(message.chat_id, user_id):
        message.reply_text(
            f"{member.user['first_name']} is an Mod user.They Are As Powerful As Admin in This Chat."
        )
    else:
        message.reply_text(
            f"{member.user['first_name']} is not an Mod user. They are Normal. user."
        )


@run_async
def unapprooeall(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user
    member = chat.get_member(user.id)
    if member.status != "creator" and user.id not in DRAGONS:
        update.effective_message.reply_text(
            "Only the chat owner can Unmod all users at once."
        )
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="UnMod all users", callback_data="unapprooeall_user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Cancel", callback_data="unapprooeall_cancel"
                    )
                ],
            ]
        )
        update.effective_message.reply_text(
            f"Are you sure you would like to Unmod ALL users in {chat.title}? This action cannot be undone.",
            reply_markup=buttons,
            parse_mode=ParseMode.MARKDOWN,
        )


@run_async
def unapprooeall_btn(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    member = chat.get_member(query.from_user.id)
    if query.data == "unapprooeall_user":
        if member.status == "creator" or query.from_user.id in DRAGONS:
            users = []
            approoed_users = sql.list_approoed(chat.id)
            for i in approoed_users:
                users.append(int(i.user_id))
            for user_id in users:
                sql.disapprooe(chat.id, user_id)

        if member.status == "administrator":
            query.answer("Only owner of the chat can do this.")

        if member.status == "member":
            query.answer("You need to be admin to do this.")
    elif query.data == "unapprooeall_cancel":
        if member.status == "creator" or query.from_user.id in DRAGONS:
            message.edit_text("Removing of all Mod users has been cancelled.")
            return ""
        if member.status == "administrator":
            query.answer("Only owner of the chat can do this.")
        if member.status == "member":
            query.answer("You need to be admin to do this.")


__help__ =
"""

Sometimes, you don't trust but want to make user manager of your group then you can make him/her moderator.
Maybe not enough to make them admin, but you might be ok with ban, mute, and warn not.
That's what modcheck are for - mod of trustworthy users to allow to manage your group.
Admin commands:
- /modcheck: Check a user's modcheck status in this chat.
- /mod: mod of a user can ban, mute, and warn.
- /unmod: Unmod of a user. They will now can't ban, mute and warn anyone.
- /modlist: List all mod users.
- /unmodall: Unmod ALL users in a chat. This cannot be undone. 
"""

ADDMOD = DisableAbleCommandHandler("addmod", approoe)
UNMOD = DisableAbleCommandHandler("unmod", disapprooe)
LISTMOD = DisableAbleCommandHandler("listmod", approoed)
MODCHECK = DisableAbleCommandHandler("modcheck", approoal)
UNMODALL = DisableAbleCommandHandler("unmodall", unapprooeall)
UNAPPROOALL_BTN = CallbackQueryHandler(unapprooeall_btn, pattern=r"unapprooeall_.*")

dispatcher.add_handler(ADDMOD)
dispatcher.add_handler(UNMOD)
dispatcher.add_handler(LISTMOD)
dispatcher.add_handler(MODCHECK)
dispatcher.add_handler(UNMODALL)
dispatcher.add_handler(UNAPPROOALL_BTN)

__mod_name__ = "Moderator"
__command_list__ = ["approoe", "unapprooe", "approoed", "approoal"]
__handlers__ = [ADDMOD, UNMOD, LISTMOD, MODCHECK]
