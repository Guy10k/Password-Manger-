
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip
from database import *
from passwordGenerator import create_password
#convention:
# title is string



class AppWindow(Tk):
    def __init__(self, title, dimension = None):
        # main setup
        super().__init__()
        self.title(title)
        self.resizable(False,False)
        self.config(padx=5, pady=5)
        # widget
        self.add_data_frame = AddDataFrame(self)
        self.search_frame = SearchFrame(self)
        self.mainloop()




class AddDataFrame(ttk.Frame):
    def __init__(self, parent):


        self.main_win = parent
        self.frame_style = ttk.Style()
        self.frame_style.configure('TFrame', background='alt')
        self.frame_style.theme_use('aqua')
        super().__init__(parent,style='TFrame')
        self['padding'] = (10, 10)
        self['relief'] = "ridge"
        self['borderwidth'] = 4
        self.pack(expand=True, fill='both')
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.generate_button = ttk.Button(self, text="Generate Password", command=self.generator_password,
                                          style='TButton')
        self.alert_label_add = ttk.Label(master=self, text="")
        self.note_label = ttk.Label(self, text="Other Details To Note:", style='TLabel')
        self.password_label = ttk.Label(self, text="Password:", style='TLabel')
        self.user_label = ttk.Label(self, text="User Name:", style='TLabel')
        self.web_label = ttk.Label(self, text="Host:", style='TLabel')
        self.note_entry = ttk.Entry(self, style='TEntry')
        self.password_entry = ttk.Entry(self, style='TEntry')
        self.user_entry = ttk.Entry(self, style='TEntry')
        self.web_entry = ttk.Entry(self, style='TEntry')
        style_red = ttk.Style()
        style_red.configure('red.TLabel', foreground="red")
        style_green = ttk.Style()
        style_green.configure('green.TLabel',foreground='green')
        self.create_widget()

    def create_widget(self):

        self.web_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
        self.web_entry.focus()

        # email entry
        self.user_entry.grid(column=1, row=2, columnspan=2, sticky='ew')

        # password entry
        self.password_entry.grid(column=1, row=3, columnspan=2, sticky='ew')

        # other note entry
        self.note_entry.grid(column=1, row=4, columnspan=2, sticky='ew')
        # adding child widget
        # labels:
        # website label
        self.web_label.grid(column=0, row=1)

        # user label
        self.user_label.grid(column=0, row=2)

        # password label
        self.password_label.grid(column=0, row=3)

        # note label
        self.note_label.grid(column=0, row=4)

        # alert label for add

        self.alert_label_add.grid(column=1, row=5, columnspan=2)
        # buttons
        # generate pass button
        self.generate_button.grid(column=3, row=3)

        # add password button
        add_button = ttk.Button(self, text="Add New Password", command=self.save_pass, style='TButton')
        add_button.grid(column=3, row=4)

    def clear_entries(self):
        self.web_entry.delete(0, END)
        self.user_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.note_entry.delete(0, END)

    def generator_password(self):
        self.password_entry.delete(0, END)
        new_pass = create_password()
        self.password_entry.insert(0, new_pass)
        pyperclip.copy(new_pass)
        self.alert_label_add.config(text="")
        self.alert_label_add.configure(style='green.TLabel')
        self.alert_label_add.config(text="Password Copied To Clipboard")

    def clear_label(self):
        print('hi')
        self.alert_label_add.config(text="")

    def save_pass(self):
        host = self.web_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()
        note = self.note_entry.get()
        if host == "" or password == "":
            self.alert_label_add.config(text="")
            self.alert_label_add.configure(style='red.TLabel')
            self.alert_label_add.config(text="Some filed Are Required")


        else:
            res = search_record(host, user)
            if not res :
                add_record(host, user, password, note)
                self.alert_label_add.config(text="")
                self.alert_label_add.configure(style='green.TLabel')
                self.alert_label_add.config(text="Password Was successfully Added")
                # window.update()
            else:
                answer = messagebox.askyesno(title="Warning", message=f"A password for {host} whit the user: {user} is already exist,"
                                                                    f"Do you want to change it?\n")

                print(answer)
                if answer:
                    delete_record(res[0][0],res[0][1])
                    add_record(host, user, password, note)

                    self.alert_label_add.config(text="")
                    self.alert_label_add.configure(style='green.TLabel')
                    self.alert_label_add.config(text="Password Was successfully Added")



            self.clear_entries()


class SearchFrame(ttk.Frame):
    def __init__(self, parent):

        self.frame_style = ttk.Style()
        self.frame_style.configure('TFrame', background='alt')
        self.frame_style.theme_use('aqua')
        super().__init__(parent, style='TFrame')
        self.pack(side='bottom' ,expand=True, fill='both')
        self['padding'] = (10, 10)
        self['relief'] = "ridge"
        self['borderwidth'] = 4
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.table = Table(self)

        self.show_all_button = ttk.Button(self, text="Show All Passwords", command=self.show_all_Passwords,
                                          style='TButton')
        self.search_button = ttk.Button(self, text="Search For Passwords", command=self.search_password, style='TButton')
        self.user_search_entry = ttk.Entry(self, style='TEntry')
        self.host_search_entry = ttk.Entry(self, style='TEntry')
        self.user_search_label = ttk.Label(self, text="User Name:", style='TLabel')
        style_red = ttk.Style()
        style_red.configure('red.TLabel', foreground="red")
        style_green = ttk.Style()
        style_green.configure('green.TLabel',foreground='green')
        self.alert_label_search = ttk.Label(self, text="", style='red.TLabel')

        self.create_widget()


    def create_widget(self):
        # labels
        # alert label for search

        self.alert_label_search.grid(column=1, row=2)

        # host search label
        host_search_label = ttk.Label(self, text="Host:", style='TLabel')
        host_search_label.grid(column=0, row=0)

        # user search label
        self.user_search_label.grid(column=0, row=1)
        # entries
        # host search entry
        self.host_search_entry.grid(column=1, row=0, sticky='ew')

        # user search entry
        self.user_search_entry.grid(column=1, row=1, sticky='ew')
        # button
        # search button
        self.search_button.grid(column=2, row=0, sticky='ew')

        # show all_button
        self.show_all_button.grid(column=2, row=1, sticky='ew')

        # clear button
        clear_button = ttk.Button(self, text="Clear Result", command=self.clear_table, style='TButton')
        clear_button.grid(column=2, row=2, sticky='ew')
        #delete button
        delete_button = ttk.Button(self, text="Delete Selected Row", command=self.delete_item, style='TButton')
        delete_button.grid(column=0, row=3, sticky='ew', pady=4)


        #table crete
        self.table.heading('site', text='Site')
        self.table.heading('user name', text='User Name')
        self.table.heading('password', text='Password')
        self.table.heading('other notes', text='Other Notes')
        self.table.column('site', anchor='center' )
        self.table.column('user name', anchor='center' )
        self.table.column('password', anchor='center' )
        self.table.column('other notes', anchor='center' )

        self.table.grid(column=0, row=10, columnspan=4)


    def show_all_Passwords(self):
        self.alert_label_search.config(text="")
        self.update_table(show_all())


    def search_password(self):
        self.alert_label_search.config(text="")
        host_to_search = self.host_search_entry.get()
        user_to_search = self.user_search_entry.get()

        res = search_record(host_to_search, user_to_search)
        print(res)
        if res:

            self.update_table(res)


        else:
            self.alert_label_search.config(text="Site Not Found")

    def update_table(self,data):
        self.clear_table()
        for row in data:
            self.table.insert('', END, value=list(row))

    def clear_table(self):
        self.alert_label_search.config(text="")
        for item in self.table.get_children():

            self.table.delete(item)





    def delete_item(self):
        for i in self.table.selection():
            host = self.table.item(i)['values'][0]
            user = self.table.item(i)['values'][1]
            #password = self.item(i)['values'][2]
            answer = messagebox.askquestion(title='Warning', message=f"You are about to delete data,\n\n"
                                                                     f"Are you sure about that?\n")


            if answer == 'yes':

                delete_record(host, user )
                self.update_table(show_all())




class Table(ttk.Treeview):
    def __init__(self,parent):
        super().__init__(parent, column=('site', 'user name', 'password', 'other notes'),
                     show='headings', selectmode="browse")


        self.bind('<<TreeviewSelect>>', self.item_select)

    def item_select(self,_):
        for i in self.selection():
            print(self.item(i)['values'][2])
            pyperclip.copy(self.item(i)['values'][2])


if __name__ == "__main__":

    AppWindow('Mister Password Manager')
