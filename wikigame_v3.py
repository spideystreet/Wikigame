import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END, RIGHT, LEFT, Y
import time
import threading
import random

def get_random_wikipedia_page():
    response = requests.get('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    return response.url, response.text

def extract_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    content_div = soup.find(id='bodyContent')
    links = content_div.find_all('a', href=True)
    return [(link.get_text(), link['href']) for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]

def load_thematic_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

class WikiGameApp(tk.Tk):
    def __init__(self, thematic_file=None):
        super().__init__()
        self.title("WikiGame")
        self.geometry("800x600")

        self.start_url, self.start_content = get_random_wikipedia_page()
        if thematic_file:
            thematic_urls = load_thematic_urls(thematic_file)
            self.start_url = random.choice(thematic_urls)
            self.start_content = requests.get(self.start_url).text
            self.end_url = random.choice(thematic_urls)
        else:
            self.end_url, _ = get_random_wikipedia_page()

        self.current_url = self.start_url
        self.current_content = self.start_content
        self.history = []
        self.turn = 0
        self.start_index = 0
        self.start_time = time.time()

        self.create_widgets()
        self.update_links()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="WikiGame", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.current_page_label = tk.Label(self, text="Page actuelle: ", font=("Arial", 16))
        self.current_page_label.pack(pady=10)

        self.links_listbox = Listbox(self, width=80, height=20)
        self.links_listbox.pack(pady=10, side=LEFT, fill="both")
        self.links_listbox.bind('<<ListboxSelect>>', self.on_link_select)

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.links_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.links_listbox.yview)

        self.navigation_frame = tk.Frame(self)
        self.navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(self.navigation_frame, text="Page précédente", command=self.prev_page)
        self.prev_button.pack(side=LEFT, padx=5)

        self.next_button = tk.Button(self.navigation_frame, text="Page suivante", command=self.next_page)
        self.next_button.pack(side=LEFT, padx=5)

        self.timer_label = tk.Label(self, text="Temps: 0s", font=("Arial", 16))
        self.timer_label.pack(pady=10)
        self.update_timer()

    def update_links(self):
        self.links_listbox.delete(0, END)
        links = extract_links(self.current_content)
        self.links = links

        for i, (text, link) in enumerate(links[self.start_index:self.start_index+20], start=1):
            self.links_listbox.insert(END, f"{i}. {text}")

        if self.start_index > 0:
            self.links_listbox.insert(END, "Page précédente")
        if len(links) > self.start_index + 20:
            self.links_listbox.insert(END, "Page suivante")

        self.current_page_label.config(text=f"Page actuelle: {self.current_url.split('/')[-1]}")

    def on_link_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            if index == self.links_listbox.size() - 1 and len(self.links) > self.start_index + 20:
                self.next_page()
            elif index == self.links_listbox.size() - 2 and self.start_index > 0:
                self.prev_page()
            else:
                self.follow_link(index)

    def follow_link(self, index):
        link = self.links[self.start_index + index][1]
        self.current_url = 'https://fr.wikipedia.org' + link
        self.current_content = requests.get(self.current_url).text
        self.history.append(self.current_url)
        self.turn += 1
        self.update_links()

        if self.current_url == self.end_url:
            elapsed_time = time.time() - self.start_time
            messagebox.showinfo("Félicitations!", f"Vous avez atteint la cible en {self.turn} tours et en {int(elapsed_time)} secondes.")
            self.show_history()

    def prev_page(self):
        self.start_index = max(0, self.start_index - 20)
        self.update_links()

    def next_page(self):
        self.start_index += 20
        self.update_links()

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Historique des pages visitées")
        history_listbox = Listbox(history_window, width=100, height=20)
        history_listbox.pack(pady=10)

        for page in self.history:
            history_listbox.insert(END, page)

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Temps: {elapsed_time}s")
        self.after(1000, self.update_timer)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="WikiGame")
    parser.add_argument('-d', '--thematic', help="Fichier contenant les URLs thématiques")
    args = parser.parse_args()

    if args.thematic:
        app = WikiGameApp(thematic_file=args.thematic)
    else:
        app = WikiGameApp()

    app.mainloop()
