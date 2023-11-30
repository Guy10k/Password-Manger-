from exceptions import *
from database import *
from password_generator import *
import pyperclip


def save_pass(host, user, password, note=""):

    if host == "" or password == "":
        raise InvalidDataEntries


    else:
        res = search_record(host, user)
        if not res:
            add_record(host, user, password, note)
        else:
            raise DataAlreadyExist


def search_pass(host, user):
    res = search_record(host,user)
    if res:
        return res
    else:
        raise DataNoteFound

def delete_pass(host, user):
    delete_record(host,user)


def generator_password():
    new_pass = create_password()
    pyperclip.copy(new_pass)
    return new_pass