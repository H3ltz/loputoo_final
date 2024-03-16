import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as font


class View(Tk):
    def __init__(self, controller):
        super().__init__()  # Tk jaoks
        self.controller = controller  #Kontrollerite asju saab view kasutada
        self.default_font = font.Font(family="Courier", size=14)

        self.width = 700
        self.height = 500
        self.title('Info otsing')

        self.resizable(False, False)

        #Wicgets loomine
        self.create_widgets()

    def create_widgets(self):
        self.search_entry_lbl = Label(text='Sisesta otsingu sõna: ')
        self.search_entry_lbl.grid(row=0, column=0, padx=5, pady=5)

        self.file_lbl = Label(text='Valitud fail: ')
        self.file_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.search_entry = Entry(width=40)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = Button(text="Otsi sõna", state=DISABLED, command=self.search)
        self.search_button.grid(row=0, column=2, padx=5, sticky='ew')

        self.open_button = Button(text="Ava fail", command=self.controller.open_file)
        self.open_button.grid(row=1, column=2, padx=5, sticky='ew')

        self.result_text = Text(wrap="none", font=self.default_font)
        self.result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=(0,10), sticky="nsew")

        self.scrollbar_y = Scrollbar(orient="vertical", command=self.result_text.yview)
        self.scrollbar_y.grid(row=2, column=3, sticky="ns")
        self.result_text.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = tk.Scrollbar(orient="horizontal", command=self.result_text.xview)
        self.scrollbar_x.grid(row=3, column=0, columnspan=3, sticky="ew")
        self.result_text.config(xscrollcommand=self.scrollbar_x.set)

    def search(self):
        search_text = self.search_entry.get().lower()
        search_results = self.controller.search(search_text)
        if len(search_text) >= 3:
            self.display_results(search_results)
        else:
            tkinter.messagebox.showerror('Viga sisestusel', 'Palun sisesta vähemalt 3 tähemärki')

    def display_results(self, search_results):
        self.result_text.delete('1.0', tk.END)
        if search_results:
            max_lengths = [max(len(cell) for cell in column) for column in zip(*search_results)]
            for row in search_results:
                formatted_row = " | ".join(f"{cell:<{max_length}}" for cell, max_length in zip(row, max_lengths))
                self.result_text.insert(END, formatted_row + "\n")
        else:
            self.result_text.insert(END, "Otsing ei andnud tulemusi\n")

    def enable_search_button(self):
        self.search_button.config(state=NORMAL)

    def update_file_label(self, file_name):
        self.file_lbl.config(text=f'Valitud fail: {file_name}')

    def clear_results(self):
        self.result_text.delete('1.0', END)
