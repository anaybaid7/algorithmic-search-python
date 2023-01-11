import tkinter
import messagebox
def main():
    root = tk.Tk()
    root.title("Anay's Search Engine")

    notebook = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text='Search')
    notebook.add(tab2, text='Summary')
    notebook.pack()

    url_label = tk.Label(tab1, text="Enter the seed page's url:")
    url_label.pack()

    url_entry = tk.Entry(tab1)
    url_entry.pack()

    pages_label = tk.Label(tab1, text="Enter the maximum number of pages to crawl (enter 0 for no limit): ")
    pages_label.pack()

    pages_entry = tk.Entry(tab1)
    pages_entry.pack()

    search_button = tk.Button(tab1, text="Search", command=lambda: search(url_entry, pages_entry))
    search_button.pack()

    search_label = tk.Label(tab1)
    search_label.pack()

    listbox = tk.Listbox(tab1)
    listbox.pack()

    scrollbar = tk.Scrollbar(tab1)
    scrollbar.pack(side='right', fill='y')
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)

    progress = ttk.Progressbar(tab1, orient="horizontal", length=200, mode="determinate")
    progress.pack()

    crawled_label = tk.Label(tab2, text="Crawled Pages: ")
    crawled_label.grid(row=0, column=0, sticky="w")
    crawled_pages = tk.StringVar()
    crawled_display = tk.Label(tab2, textvariable=crawled_pages)
    crawled_display.grid(row=0, column=1, sticky="w")

    def search(url_entry, pages_entry):
        progress.config(maximum=int(pages_entry.get()), value=0)
        user_url = url_entry.get()
        num_pages = pages_entry.get()
        try:
            num_pages = int(num_pages)
        except ValueError:
            num_pages = 20
            messagebox.showerror("Invalid Input", "Invalid input. Using default value of 20 pages.")

        if num_pages > 0:
            crawl_web(user_url, num_pages)
        else:
            crawl_web(user_url)

        srch = input('Enter the key word to look up: ')
        search_label.config(text=lookup(srch))
        crawled_pages.set(len(crawled))
        for url in crawled:
            listbox.insert("end", url)
            progress.config(value=len(crawled))
            root.mainloop()

    if name == "main":
        main()


