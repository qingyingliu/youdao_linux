import sqlite3
from . import config

def get_db():
    #print("connecting to database...")
    db = sqlite3.connect(config.DATABASE_URI,detect_types=sqlite3.PARSE_DECLTYPES)
    # sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
    db.row_factory = sqlite3.Row
    #print("connected to database!")
    return db


def init_db():
    try:
        db = get_db()
        with open(config.DATABASE_SCHEMA) as f:
            db.executescript(f.read())
        print("init database ok!")
    except Exception as e:
        print("init database error: ",e)


def select_word_by(by):
    try:
        db = get_db()
        cursor = db.cursor()
        result = cursor.execute(("select word,phonetic_symbol,word_attr,meanings,en_sentence1,cn_sentence1,en_sentence2,"
                                 "cn_sentence2,en_sentence3,cn_sentence3 from word where word = ?"), (by,)).fetchall()
        return result

    except:
        return None


def update_times(word):

    try:
        db = get_db()
        cursor = db.cursor()
        result = cursor.execute("select * from count where word = ?",(word,)).fetchall()

        if len(result) == 0:
            cursor.execute("insert into count(word) values (?)",(word,))
            db.commit()

        cursor.execute("update count set times = times + 1 where word = ?",(word,))
        db.commit()
        db.close()
    except Exception as e:
        print("update error: ",e)


if __name__ == "__main__":
    init_db()
