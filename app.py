import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import file_search_tool as fst


def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('File Search Tool')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = SearchForm(self)
        frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)


class SearchForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=100)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=100)

        self.folder_path_label = ttk.Label(self, text='Folder path')
        self.folder_path_label.grid(row=0, column=0, sticky='nw')
        # self.folder_path_label.grid(row=0, column=0)

        self.folder_path = ttk.Entry(self, width=50)
        self.folder_path.grid(row=0, column=1, columnspan=2, sticky='wne')

        self.search_word_label = ttk.Label(self, text='Search word')
        self.search_word_label.grid(row=1, column=0, sticky='nw')

        self.search_word = ttk.Entry(self, width=50)
        self.search_word.grid(row=1, column=1, columnspan=2, sticky='wne')

        self.all_matches = ttk.Checkbutton(self, text='Show all matches', variable=False)
        self.all_matches.grid(row=2, column=0, sticky='wn')

        self.entry_btn = ttk.Button(self, text='Search', command=self.search)
        self.entry_btn.grid(row=3, column=0, sticky='wn')

        self.search_result = ScrolledText(self)
        self.search_result.grid(row=4, column=0, columnspan=3, sticky="nsew")
        # self.search_result.insert(1.0, 'test\ntest\ntest')

    def add_to_text(self, _event=None):
        text = self.search_word.get()

        self.clear_results()
        if text:
            self.search_result.insert(1.0, text + '\n')

    def clear_results(self):
        self.search_result.delete(1.0, tk.END)

    def search(self):
        results = fst.search_word_in_files(self.folder_path.get(), self.search_word.get())
        self.clear_results()
        self.search_result.insert(1.0, str(results[1]) + '\n')
        self.search_result.insert(2.0, str(results[2]) + '\n')

        line = 3.0
        for item in results[0]:
            print(type(item), item)
            self.search_result.insert(line, item + '\n')
            line += 1


if __name__ == '__main__':
    main()
