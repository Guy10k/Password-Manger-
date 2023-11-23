import sqlite3

#-------------# SQLite3 Data Type #--------------
    # NULL
    # INTEGER
    # REAL
    # TEXT
    # BLOB




def add_record(host_name, user_name, password, note = None):

    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO passwords VALUES (?, ?, ?, ?)", (host_name, user_name, password, note))
    db.commit()
    db.close()

def search_record(host_name,user_name=""):

    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    if user_name != "":
        cursor.execute("SELECT * FROM passwords WHERE host_site = ? AND user_name= ?", (host_name,user_name))
    else:
        cursor.execute("SELECT * FROM passwords WHERE host_site = ? ", (host_name,))
    res = cursor.fetchall()
    db.commit()
    db.close()
    return res


def update_record(host,user, new_password):
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("""UPDATE passwords SET password = ? WHERE host_site = ? AND user_name = ?""" , (new_password, host, user))
    db.commit()
    db.close()

def delete_record(host, user):
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("DELETE from passwords WHERE host_site = ? AND user_name = ?", (host, user))
    db.commit()
    db.close()

def show_all():
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM passwords")
    res = cursor.fetchall()
    db.commit()
    db.close()
    return res

def delete_all_records():
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM passwords")
    db.commit()
    db.close()

# create the table database
# db = sqlite3.connect('passwords.db')
# cursor = db.cursor()
# cursor.execute("""CREATE TABLE passwords (
#
#             host_site text ,
#             user_name   text,
#             password  text,
#             other   text
#         )""")


# update_record('a','guy10kah@gmail.com', 12)
#print(search_record('gmail'))


