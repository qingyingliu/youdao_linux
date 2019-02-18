from . import db


def analysis():
    print("\t\t*** analysis ***")
    database = db.get_db()
    cursor = database.cursor()
    result = cursor.execute("select * from count order by times desc").fetchall()[:10]

    for line in result:
        print("\t\t",line['word'],"\t",line['times'])

