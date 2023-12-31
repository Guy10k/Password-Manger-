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
    sub_host = f"{host_name}%"

    if user_name != "":
        sub_user = f"{user_name}%"
        cursor.execute("SELECT * FROM passwords WHERE host_site = ? AND user_name= ? "
                       "OR host_site LIKE ? AND user_name LIKE ?", (host_name,user_name,sub_host,sub_user))
    else:
        # cursor.execute("SELECT * FROM passwords WHERE  host_site LIKE ? ",(sub_host,))
        cursor.execute("SELECT * FROM passwords WHERE host_site = ? OR host_site LIKE ?", (host_name,sub_host ))
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

def fetch_to_csv():
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute("SELECT host_site, user_name, password  FROM passwords")
    res = cursor.fetchall()
    db.commit()
    db.close()
    return res

# # un comment this lines at the first time of use , run the code and than comment it again.
# # create the table database
# db = sqlite3.connect('passwords.db')
# cursor = db.cursor()
# cursor.execute("""CREATE TABLE passwords (
#
#             host_site text ,
#             user_name   text,
#             password  text,
#             other   text
#         )""")





