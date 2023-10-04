#python code

import tkinter as tk
from tkinter import ttk
import threading
import requests
from bs4 import BeautifulSoup

class RedditScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reddit Scraper")

        # Create and pack labels, entry boxes, and button
        self.product_label = ttk.Label(root, text="Product Paragraph:")
        self.product_entry = ttk.Entry(root, width=50)
        self.product_label.pack()
        self.product_entry.pack()

        self.reddit_label = ttk.Label(root, text="SubReddit URL:")
        self.reddit_entry = ttk.Entry(root, width=50)
        self.reddit_label.pack()
        self.reddit_entry.pack()

        self.progress_bar = ttk.Progressbar(root, length=300, mode='indeterminate')
        self.progress_bar.pack()

        self.result_label = ttk.Label(root, text="Comments Found:")
        self.result_label.pack()

        self.comment_list = tk.Listbox(root, width=80, height=15)
        self.comment_list.pack()

        self.scrape_button = ttk.Button(root, text="Scrape Reddit", command=self.start_scraping)
        self.scrape_button.pack()

    def start_scraping(self):
        product_paragraph = self.product_entry.get()
        subreddit_url = self.reddit_entry.get()

        # Create a thread to perform web scraping
        scraping_thread = threading.Thread(target=self.scrape_reddit, args=(product_paragraph, subreddit_url))
        scraping_thread.start()

    def scrape_reddit(self, product_paragraph, subreddit_url):
        # Disable the button and start the progress bar
        self.scrape_button["state"] = "disabled"
        self.progress_bar.start()

        try:
            # Web scraping code here (use BeautifulSoup and requests)
            # Replace the following code with your scraping logic
            comments = ["Comment 1", "Comment 2", "Comment 3"]

            # Display comments in the list
            self.comment_list.delete(0, tk.END)
            for comment in comments:
                self.comment_list.insert(tk.END, comment)

        except Exception as e:
            # Handle any exceptions here
            print(f"An error occurred: {str(e)}")

        finally:
            # Stop the progress bar and re-enable the button
            self.progress_bar.stop()
            self.scrape_button["state"] = "normal"

if __name__ == "__main__":
    root = tk.Tk()
    app = RedditScraperApp(root)
    root.mainloop()

