import os
import sys
import json
import tkinter as tk


def display_data(data):
    if not data:
        print("Data is empty, cannot display in GUI.")
        return

    window = tk.Tk()
    window.title("Wikipedia Categories")
    window.geometry("600x400")

    title_label = tk.Label(window, text=f"Title: {data['title']}", font=("Arial", 14))
    title_label.pack(pady=10)

    description_label = tk.Label(
        window,
        text=f"Description: {data['description']}",
        font=("Arial", 12),
        wraplength=500,
        justify="left",
    )
    description_label.pack(pady=10)

    categories_label = tk.Label(
        window,
        text=f"Categories: {', '.join(data['categories'])}",
        font=("Arial", 12),
        wraplength=500,
        justify="left",
    )
    categories_label.pack(pady=10)

    images_label = tk.Label(
        window,
        text=f"Images: {', '.join(data['images'])}",
        font=("Arial", 12),
        wraplength=500,
        justify="left",
    )
    images_label.pack(pady=10)

    external_links_label = tk.Label(
        window,
        text=f"External Links: {', '.join(data['external_links'])}",
        font=("Arial", 12),
        wraplength=500,
        justify="left",
    )
    external_links_label.pack(pady=10)

    def close_window():
        if window.winfo_exists():
            window.destroy()

    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    data = {
        "title": "Example Title",
        "description": "Example Description",
        "categories": ["Category 1", "Category 2", "Category 3"],
        "images": ["Image 1", "Image 2", "Image 3"],
        "external_links": ["Link 1", "Link 2", "Link 3"],
    }
    display_data(data)
