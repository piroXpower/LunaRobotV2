import threading

from sqlalchemy import Column, String, UnicodeText, BigInteger, func, distinct

from lunaBot.modules.sql import BASE, SESSION


class Moderators(BASE):
    __tablename__ = "approval"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)  # ensure string
        self.user_id = user_id

    def __repr__(self):
        return "<add_mod %s>" % self.user_id


Moderators.__table__.create(checkfirst=True)

MODS_INSERTION_LOCK = threading.RLock()


def add_mod(chat_id, user_id):
    with MODS_INSERTION_LOCK:
        add_mod_user = Moderators(str(chat_id), user_id)
        SESSION.add(add_mod_user)
        SESSION.commit()


def is_add_modd(chat_id, user_id):
    try:
        return SESSION.query(Moderators).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def dis_mod(chat_id, user_id):
    with MODS_INSERTION_LOCK:
        disadd_mod_user = SESSION.query(Moderators).get((str(chat_id), user_id))
        if disadd_mod_user:
            SESSION.delete(disadd_mod_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_moderators(chat_id):
    try:
        return (
            SESSION.query(Moderators)
            .filter(Moderators.chat_id == str(chat_id))
            .order_by(Moderators.user_id.asc())
            .all()
        )
    finally:
        SESSION.close()
