from exceptions import *
from database import *
from password_generator import *
from tkinter.filedialog import askopenfilename, askdirectory
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


def browse_for_file():
   file_path = askopenfilename(initialdir="/",
      title="Select File", filetypes=(("Text files","*.txt*"),("All Files","*.*")))
   return file_path


def browse_for_directory():
   file_path = askdirectory(initialdir="/",
      title="Save As")
   return file_path