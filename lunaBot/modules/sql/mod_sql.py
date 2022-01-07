import threading

from sqlalchemy import Column, String, UnicodeText, BigInteger, func, distinct

from lunaBot.modules.sql import BASE, SESSION


class Approoals(BASE):
    __tablename__ = "approoal"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)  # ensure string
        self.user_id = user_id

    def __repr__(self):
        return "<Approoe %s>" % self.user_id


Approoals.__table__.create(checkfirst=True)

APPROOE_INSERTION_LOCK = threading.RLock()


def approoe(chat_id, user_id):
    with APPROOE_INSERTION_LOCK:
        approoe_user = Approoals(str(chat_id), user_id)
        SESSION.add(approoe_user)
        SESSION.commit()


def is_approoed(chat_id, user_id):
    try:
        return SESSION.query(Approoals).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def disapprooe(chat_id, user_id):
    with APPROOE_INSERTION_LOCK:
        disapprooe_user = SESSION.query(Approoals).get((str(chat_id), user_id))
        if disapprooe_user:
            SESSION.delete(disapprooe_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_approoed(chat_id):
    try:
        return (
            SESSION.query(Approoals)
            .filter(Approoals.chat_id == str(chat_id))
            .order_by(Approoals.user_id.asc())
            .all()
        )
    finally:
        SESSION.close()
