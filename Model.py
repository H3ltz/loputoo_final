import csv
from tkinter.messagebox import showinfo


class Model:
    def __init__(self):
        self.data = {} #tühi muutuja andmete salvestamiseks

    #Faili avamine
    def open_file(self, file_path, encoding='utf-8'):
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            self.data[file_path] = {'header': header, 'rows': []}
            for row in reader:
                self.data[file_path]['rows'].append(row)

        showinfo(title='Valitud fail', message=str(file_path))

    #Failist otsimine
    def search(self, file_path, search_text):
        search_results = []
        if file_path in self.data:
            header = self.data[file_path]['header']
            for row in self.data[file_path]['rows']:
                if any(search_text in str(column).lower() for column in row):
                    search_results.append(row)
        return search_results

    #Listi puhastamine
    def clear_data(self):
        self.data = {}

