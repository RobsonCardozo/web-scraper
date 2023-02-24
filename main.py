import json
import tkinter as tk

def display_categories():
    with open("data.json") as f:
        data = json.load(f)
    
    # Create a Tkinter window to display the categories
    window = tk.Tk()
    window.title("Wikipedia Categories")
    window.geometry("800x600")
    
    # Create labels to display the data
    title_label = tk.Label(window, text=f"Title: {data['title']}", font=("Arial", 14))
    title_label.pack(pady=10)
    
    description_label = tk.Label(window, text=f"Description: {data['description']}", font=("Arial", 12), wraplength=750, justify="left")
    description_label.pack(pady=10)
    
    categories_label = tk.Label(window, text=f"Categories: {', '.join(data['categories'])}", font=("Arial", 12), wraplength=750, justify="left")
    categories_label.pack(pady=10)
    
    images_label = tk.Label(window, text=f"Images: {', '.join(data['images'])}", font=("Arial", 12), wraplength=750, justify="left")
    images_label.pack(pady=10)
    
    external_links_label = tk.Label(window, text=f"External Links: {', '.join(data['external_links'])}", font=("Arial", 12), wraplength=750, justify="left")
    external_links_label.pack(pady=10)

    # Create a button to close the window
    close_button = tk.Button(window, text="Close", font=("Arial", 12), command=window.destroy)
    close_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    display_categories()
