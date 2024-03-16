import tkinter
from tkinter import filedialog, messagebox
from Mudel import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            if file_path.endswith("Persons.csv") or file_path.endswith("Persons_Big.csv"):
                self.model.clear_data()
                self.model.open_file(file_path)
                self.view.enable_search_button()
                self.view.update_file_label(file_path)
                self.view.clear_results()
            else:
                tkinter.messagebox.showwarning("Palun vali õige fail", "Persons.csv or Persons_Big.csv")

    def search(self, search_text):
        if self.model.data:
            search_results = []
            for file_path in self.model.data:
                search_results += self.model.search(file_path, search_text)
            return search_results
        else:
            return []
